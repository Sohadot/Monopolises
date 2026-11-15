"""Checks for the candidate Monopolises Strategic Intelligence research files.

Run with: python3 -m unittest discover -s tests -v
No third-party packages or network connection required.

Passing tests show provenance and governance hygiene only. They do not
establish research validity or forecasting accuracy.
"""

from pathlib import Path
import copy
import importlib.util
import json
import re
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]
SI = ROOT / "research" / "strategic-intelligence"
CASE = SI / "cases" / "MON-SI-001"
ROUTES = ("index.html", "thesis/index.html", "methodology/index.html",
          "sources/index.html", "research/index.html", "about/index.html")

spec = importlib.util.spec_from_file_location("check_registers", SI / "tools" / "check_registers.py")
check_registers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check_registers)


def load(name):
    return json.loads((CASE / name).read_text(encoding="utf-8"))


class RegisterIntegrityTests(unittest.TestCase):
    def test_all_checks_pass(self):
        self.assertEqual(check_registers.run(), [])

    def test_pre_event_admitted_sources_precede_cutoff(self):
        reg = load("register.pre-event.json")
        cutoff = reg["cutoff_utc"]
        self.assertEqual(cutoff, "2026-05-12T23:59:00Z")
        admitted = [s for s in reg["sources"] if s["status"] == "admitted"]
        self.assertGreaterEqual(len(admitted), 10)
        for s in admitted:
            with self.subTest(source=s["source_id"]):
                self.assertLessEqual(s["availability_utc"], cutoff)

    def test_outcome_report_never_a_pre_event_source(self):
        text = (CASE / "register.pre-event.json").read_text(encoding="utf-8").lower()
        self.assertNotIn("culper", text)

    def test_s2_cannot_carry_s0_claims(self):
        reg = load("register.pre-event.json")
        classes = {s["source_id"]: s["source_class"] for s in reg["sources"]}
        for c in reg["claims"]:
            if c["evidence_class"] in ("S0", "S1"):
                for sid in c["source_ids"]:
                    self.assertNotIn(classes[sid], {"secondary_lead", "short_seller_report"})


class ContaminationDetectorTests(unittest.TestCase):
    """The checker must actually catch the failures it claims to catch."""

    def run_register(self, mutate, period="pre_event"):
        name = "register.pre-event.json" if period == "pre_event" else "register.post-event.json"
        reg = copy.deepcopy(load(name))
        mutate(reg)
        errors = []
        check_registers.check_register(reg, period, errors, "mutant")
        return errors

    def test_detects_post_cutoff_source(self):
        def mutate(reg):
            reg["sources"][0]["availability_utc"] = "2026-05-20T20:35:52Z"
        self.assertTrue(any("after cutoff" in e for e in self.run_register(mutate)))

    def test_detects_claim_citing_excluded_source(self):
        def mutate(reg):
            reg["claims"][0]["source_ids"] = ["SI1-SRC-010"]
        self.assertTrue(any("excluded source" in e for e in self.run_register(mutate)))

    def test_detects_cross_period_reference(self):
        def mutate(reg):
            reg["claims"][0]["source_ids"] = ["SI1-PST-001"]
        self.assertTrue(any("out-of-period" in e for e in self.run_register(mutate)))

    def test_detects_scoring_keys(self):
        def mutate(reg):
            reg["claims"][0]["score"] = 0.8
        self.assertTrue(any("forbidden classification" in e for e in self.run_register(mutate)))

    def test_detects_missing_excluded_implications(self):
        def mutate(reg):
            reg["claims"][0]["excluded_implications"] = []
        self.assertTrue(any("excluded implication" in e for e in self.run_register(mutate)))

    def test_detects_post_event_term_in_analysis_body(self):
        body = (CASE / "PRE_EVENT_ANALYSIS.md").read_text(encoding="utf-8")
        stripped = check_registers.DISCLOSURE.sub("", body)
        self.assertNotIn("culper", stripped.lower())
        self.assertIn("Culper", body)  # disclosed, but only inside the hindsight block


class FreezeAndProvenanceTests(unittest.TestCase):
    """Second-pass regressions: frozen pre-event state, availability, errata."""

    def test_freeze_manifest_matches_frozen_content(self):
        manifest = json.loads((CASE / "FREEZE_MANIFEST.json").read_text(encoding="utf-8"))
        errors = []
        check_registers.check_freeze(CASE, manifest, load("register.pre-event.json"),
                                     (CASE / "PRE_EVENT_ANALYSIS.md").read_text(encoding="utf-8"),
                                     errors, "MON-SI-001")
        self.assertEqual(errors, [])

    def test_editing_frozen_claim_is_detected(self):
        manifest = json.loads((CASE / "FREEZE_MANIFEST.json").read_text(encoding="utf-8"))
        reg = copy.deepcopy(load("register.pre-event.json"))
        reg["claims"][0]["assertion"] += " (strengthened with hindsight)"
        errors = []
        check_registers.check_freeze(CASE, manifest, reg,
                                     (CASE / "PRE_EVENT_ANALYSIS.md").read_text(encoding="utf-8"),
                                     errors, "MON-SI-001")
        self.assertTrue(any("register.pre-event.json changed" in e for e in errors))

    def test_editing_frozen_analysis_is_detected(self):
        manifest = json.loads((CASE / "FREEZE_MANIFEST.json").read_text(encoding="utf-8"))
        text = (CASE / "PRE_EVENT_ANALYSIS.md").read_text(encoding="utf-8")
        errors = []
        check_registers.check_freeze(CASE, manifest, load("register.pre-event.json"),
                                     text.replace("could not", "could", 1), errors, "MON-SI-001")
        self.assertTrue(any("PRE_EVENT_ANALYSIS.md changed" in e for e in errors))

    def test_post_event_sources_absent_from_pre_event_findings(self):
        # The frozen sources/claims must carry no post-event material. Errata may
        # *mention* where a document was later found, but cannot add sources or claims.
        pre = load("register.pre-event.json")
        core = check_registers.canonical_core(pre).decode("utf-8")
        for marker in ("SI1-PST-", "MEDIA_STATEMENT_13112026", "megaspeed-international-pte-ltd"):
            self.assertNotIn(marker, core)
        self.assertEqual(set(pre["addenda"]), {"note", "availability_review", "errata", "p1_assessment"})
        for e in pre["addenda"]["errata"]:
            self.assertNotIn("sources", e)
            self.assertNotIn("claims", e)

    def test_post_hoc_pre_cutoff_document_stays_excluded_pre_event(self):
        pre = load("register.pre-event.json")
        src = {s["source_id"]: s for s in pre["sources"]}
        self.assertEqual(src["SI1-SRC-014"]["status"], "excluded")
        post = {s["source_id"]: s for s in load("register.post-event.json")["sources"]}
        self.assertTrue(post["SI1-PST-015"]["pre_cutoff_document_located_post_hoc"])

    def test_insufficient_availability_cannot_carry_s0(self):
        def mutate(reg):
            for c in reg["claims"]:
                if c["claim_id"] == "SI1-C-19":
                    c["evidence_class"] = "S0"
        reg = copy.deepcopy(load("register.pre-event.json"))
        mutate(reg)
        errors = []
        check_registers.check_register(reg, "pre_event", errors, "mutant")
        self.assertTrue(any("insufficiently demonstrated" in e for e in errors))

    def test_allegation_cannot_be_promoted_to_primary_fact(self):
        reg = copy.deepcopy(load("register.post-event.json"))
        for c in reg["claims"]:
            if c["claim_id"] == "SI1-V-14":
                c["evidence_class"] = "S0"
        errors = []
        check_registers.check_register(reg, "post_event", errors, "mutant")
        self.assertTrue(any("non-primary source" in e or "allegations must stay S2" in e
                            for e in errors))

    def test_short_seller_report_not_marked_examined(self):
        post = {s["source_id"]: s for s in load("register.post-event.json")["sources"]}
        self.assertEqual(post["SI1-PST-008"]["status"], "excluded")
        self.assertIn("NOT directly examined", post["SI1-PST-008"]["exclusion_reason"])

    def test_errata_are_dated_and_complete(self):
        for name in ("register.pre-event.json", "register.post-event.json"):
            for e in load(name)["addenda"]["errata"]:
                with self.subTest(erratum=e["erratum_id"]):
                    for field in check_registers.ERRATA_FIELDS:
                        self.assertIn(field, e)


def _git_available():
    return check_registers.git_show(check_registers.FREEZE_ANCHORS["MON-SI-001"],
                                    "research/strategic-intelligence/cases/MON-SI-001/register.pre-event.json") is not None


@unittest.skipUnless(_git_available(), "freeze anchor commit not in local git history")
class GitAnchoredFreezeTests(unittest.TestCase):
    """Freeze verification anchored to the original Git objects at 5b3b756."""

    def setUp(self):
        self.analysis = (CASE / "PRE_EVENT_ANALYSIS.md").read_text(encoding="utf-8")
        self.pre = load("register.pre-event.json")
        self.event = (CASE / "event-study-pre-event.json").read_bytes()
        self.manifest = json.loads((CASE / "FREEZE_MANIFEST.json").read_text(encoding="utf-8"))

    def verify(self, analysis=None, pre=None, event=None, manifest=None):
        errors = []
        check_registers.verify_freeze_against_git(
            "MON-SI-001", self.analysis if analysis is None else analysis,
            self.pre if pre is None else pre, self.event if event is None else event,
            self.manifest if manifest is None else manifest, errors)
        return errors

    def test_current_state_matches_anchor(self):
        self.assertEqual(self.verify(), [])

    def test_anchor_is_pinned_in_code_and_matches_manifest(self):
        self.assertEqual(check_registers.FREEZE_ANCHORS["MON-SI-001"],
                         "5b3b756caaf1b084752981528ec1aceea3bb05c4")
        self.assertTrue(check_registers.FREEZE_ANCHORS["MON-SI-001"].startswith(
            self.manifest["frozen_commit"]))

    def test_editing_frozen_content_alone_is_detected(self):
        errors = self.verify(analysis=self.analysis.replace("could not", "could", 1))
        self.assertTrue(any("differs from anchor" in e for e in errors))

    def test_editing_content_and_manifest_together_is_detected(self):
        pre = copy.deepcopy(self.pre)
        pre["claims"][0]["assertion"] += " (rewritten)"
        manifest = copy.deepcopy(self.manifest)
        import hashlib
        manifest["files"]["register.pre-event.json"]["sha256"] = hashlib.sha256(
            check_registers.canonical_core(pre)).hexdigest()
        errors = []
        check_registers.check_freeze(CASE, manifest, pre, self.analysis, errors, "MON-SI-001")
        self.assertEqual(errors, [])  # the manifest alone would be fooled ...
        errors = self.verify(pre=pre, manifest=manifest)
        self.assertTrue(any("differ from anchor" in e for e in errors))  # ... the Git anchor is not
        self.assertTrue(any("does not match the anchor Git object" in e for e in errors))

    def test_moving_the_manifest_anchor_is_detected(self):
        manifest = copy.deepcopy(self.manifest)
        manifest["frozen_commit"] = "e8bd4ff"
        self.assertTrue(any("differs from pinned anchor" in e for e in self.verify(manifest=manifest)))

    def test_legitimate_dated_errata_remain_permitted(self):
        pre = copy.deepcopy(self.pre)
        pre["addenda"]["errata"].append({"erratum_id": "SI1-E-99", "date": "2026-12-01",
                                         "affects": ["SI1-C-01"], "correction": "test",
                                         "interpretation_changed": False, "reason": "test"})
        analysis = self.analysis + "\nAdditional dated pointer text.\n"
        self.assertEqual(self.verify(pre=pre, analysis=analysis), [])

    def test_post_event_source_cannot_enter_frozen_findings(self):
        pre = copy.deepcopy(self.pre)
        post_src = load("register.post-event.json")["sources"][0]
        pre["sources"].append(dict(post_src, source_id="SI1-SRC-099"))
        pre["claims"][0]["source_ids"].append("SI1-SRC-099")
        self.assertTrue(any("differ from anchor" in e for e in self.verify(pre=pre)))

    def test_cutoff_cannot_change_silently(self):
        pre = copy.deepcopy(self.pre)
        pre["cutoff_utc"] = "2026-05-14T23:59:00Z"
        self.assertTrue(any("cutoff changed" in e for e in self.verify(pre=pre)))
        post = load("register.post-event.json")
        self.assertEqual(post["cutoff_utc"], check_registers.FROZEN_CUTOFFS["MON-SI-001"])

    def test_frozen_event_study_cannot_be_regenerated(self):
        self.assertTrue(any("event-study-pre-event.json differs" in e
                            for e in self.verify(event=self.event + b" ")))


class StatisticalInferenceTests(unittest.TestCase):
    """Third pass: consistent Student-t inference with Bonferroni control."""

    @classmethod
    def setUpClass(cls):
        spec_i = importlib.util.spec_from_file_location("inference_correction",
                                                        SI / "tools" / "inference_correction.py")
        cls.inf = importlib.util.module_from_spec(spec_i)
        spec_i.loader.exec_module(cls.inf)
        cls.report = load("event-study-inference-correction.json")

    def test_student_t_quantiles_match_reference_tables(self):
        for alpha, df, expected in ((0.05, 10, 2.2281), (0.05, 30, 2.0423), (0.01, 20, 2.8453)):
            self.assertAlmostEqual(self.inf.t_crit(alpha, df), expected, places=3)

    def test_bonferroni_thresholds(self):
        self.assertAlmostEqual(self.inf.t_crit(0.05 / 24, 118), 3.148, places=3)
        self.assertAlmostEqual(self.inf.t_crit(0.05 / 8, 118), 2.784, places=3)
        pre, post = self.report["pre_event_family"], self.report["post_event_family"]
        self.assertEqual((pre["tests"], pre["df"], pre["critical_student_t"]), (24, 118, 3.1478))
        self.assertEqual((post["tests"], post["df"], post["critical_student_t"]), (8, 118, 2.7843))

    def test_no_result_significant_after_correction(self):
        for fam in ("pre_event_family", "post_event_family"):
            F = self.report[fam]
            self.assertFalse(F["any_significant"])
            for row in F["rows"]:
                self.assertLess(abs(row["t_corrected"]), F["critical_student_t"])
                self.assertLess(abs(row["t_original_method"]), F["critical_student_t"])

    def test_original_method_reproduces_frozen_statistics(self):
        frozen = load("event-study-pre-event.json")["runs"]
        rows = {(r["event_day0_input"], r["benchmark"], r["window"]): r
                for r in self.report["pre_event_family"]["rows"]}
        for run in frozen:
            for bench, cars in run["car"].items():
                for window, v in cars.items():
                    with self.subTest(day0=run["day0"], bench=bench, window=window):
                        row = rows[(run["day0"], bench, window)]
                        self.assertAlmostEqual(row["t_original_method"], v["t"], places=2)
                        self.assertAlmostEqual(row["car"], v["car"], places=5)

    def test_documents_use_consistent_thresholds(self):
        protocol = (SI / "EVIDENCE_PROTOCOL.md").read_text(encoding="utf-8")
        validation = (CASE / "POST_EVENT_VALIDATION.md").read_text(encoding="utf-8")
        self.assertIn("3.148", protocol)
        self.assertIn("2.784", protocol)
        self.assertIn("2.784", validation)
        self.assertNotIn("|t| > 2.73.", validation)
        errata = {e["erratum_id"]: e for e in load("register.pre-event.json")["addenda"]["errata"]}
        self.assertEqual(errata["SI1-E-05"]["supersedes"], "SI1-E-01")
        self.assertIn("NO pre-event window is statistically significant", errata["SI1-E-05"]["correction"])
        post_errata = {e["erratum_id"]: e for e in load("register.post-event.json")["addenda"]["errata"]}
        self.assertEqual(post_errata["SI1-PE-03"]["supersedes"], "SI1-PE-02")


class ProvenanceP1Tests(unittest.TestCase):
    def test_p1_not_established_while_availability_unresolved(self):
        st = check_registers.p1_status(load("register.pre-event.json"))
        self.assertFalse(st["established"])
        self.assertEqual(st["demonstrated"], 8)
        self.assertEqual(st["unresolved"]["SI1-SRC-013"], "insufficiently_demonstrated")

    def test_gate_cannot_claim_p1_while_unresolved(self):
        gate = (SI / "GATE_MON-SI-G0.md").read_text(encoding="utf-8")
        state = gate.split("## Current evaluation state", 1)[1]
        self.assertRegex(state, r"\| P1 \| \*\*NOT ESTABLISHED\*\*")
        original = gate
        mutated = original.replace("| P1 | **NOT ESTABLISHED**", "| P1 | MON-SI-001 passes P1", 1)
        path = SI / "GATE_MON-SI-G0.md"
        try:
            path.write_text(mutated, encoding="utf-8")
            errors = []
            check_registers.check_gate(errors)
            self.assertTrue(any("P1 as NOT ESTABLISHED" in e for e in errors))
        finally:
            path.write_text(original, encoding="utf-8")

    def test_p1_would_be_established_only_when_all_demonstrated(self):
        pre = copy.deepcopy(load("register.pre-event.json"))
        for r in pre["addenda"]["availability_review"]:
            r["demonstrated_public_availability"] = "demonstrated"
        self.assertTrue(check_registers.p1_status(pre)["established"])

    def test_p1_assessment_recorded_append_only(self):
        a = load("register.pre-event.json")["addenda"]["p1_assessment"]
        self.assertEqual(a["status"], "NOT_ESTABLISHED")
        self.assertEqual(a["insufficient"], ["SI1-SRC-013"])


class NoProspectiveCreditTests(unittest.TestCase):
    def test_validation_awards_no_prospective_credit(self):
        text = (CASE / "POST_EVENT_VALIDATION.md").read_text(encoding="utf-8")
        self.assertIn("**Prospective credit:** **none.", text)
        table = re.search(r"^## 2\..*?(?=^## 3\.)", text, re.M | re.S).group(0)
        self.assertNotIn("Independently anticipated", table)

    def test_checker_rejects_anticipated_label(self):
        text = (CASE / "POST_EVENT_VALIDATION.md").read_text(encoding="utf-8")
        mutated = text.replace("| **Confirmed** | Retrospectively consistent — no prospective credit |",
                               "| **Confirmed** | Independently anticipated |", 1)
        self.assertNotEqual(text, mutated)
        tmp = CASE.parent / "_tmp_mutant_case"
        try:
            tmp.mkdir()
            for f in CASE.iterdir():
                (tmp / f.name).write_bytes(f.read_bytes())
            (tmp / "POST_EVENT_VALIDATION.md").write_text(mutated, encoding="utf-8")
            errors = []
            check_registers.check_case(tmp, errors)
            self.assertTrue(any("retrospective relation" in e or "prospective-credit" in e
                                for e in errors))
        finally:
            for f in tmp.glob("*"):
                f.unlink()
            if tmp.exists():
                tmp.rmdir()

    def test_gate_excludes_retrospective_case_from_p5(self):
        gate = (SI / "GATE_MON-SI-G0.md").read_text(encoding="utf-8")
        self.assertIn("permanently excluded from P5", gate)
        self.assertIn("MON-SI-001 contributes nothing to P5", gate)

    def test_no_probability_or_signal_keys(self):
        for name in ("register.pre-event.json", "register.post-event.json",
                     "event-study-pre-event.json", "event-study-post-event.json"):
            keys = set(check_registers.walk_keys(load(name)))
            self.assertFalse(keys & check_registers.FORBIDDEN_KEYS, name)


class ChangeScopeTests(unittest.TestCase):
    """Binding governance files, v0.2 artifacts and public pages must be untouched."""

    ALLOWED_PREFIXES = ("research/strategic-intelligence/", "tests/test_strategic_intelligence.py",
                        ".github/workflows/research-checks.yml")

    def changed_files(self):
        try:
            base = subprocess.run(["git", "merge-base", "HEAD", "origin/main"], cwd=ROOT,
                                  capture_output=True, text=True, check=True).stdout.strip()
            out = subprocess.run(["git", "diff", "--name-only", base], cwd=ROOT,
                                 capture_output=True, text=True, check=True).stdout
        except (OSError, subprocess.CalledProcessError):
            self.skipTest("git history with origin/main not available")
        return [line for line in out.splitlines() if line]

    def test_only_allowed_paths_changed(self):
        changed = self.changed_files()
        outside = [p for p in changed if not p.startswith(self.ALLOWED_PREFIXES)]
        self.assertEqual(outside, [])

    def test_specific_protected_files_untouched(self):
        changed = set(self.changed_files())
        protected = {"DECISION_LOG.md", "README.md", "FOUNDATION_THESIS.md", "INTERFACE_THESIS.md",
                     "research/v0.2/cases/MON-G1-S3.md",
                     "research/v0.2/ontology/candidate-schema.json", "sitemap.xml", "llms.txt",
                     "styles.css", "index.html"}
        self.assertFalse(changed & protected)
        self.assertFalse([p for p in changed if p.startswith(("research/v0.2/", "thesis/",
                          "methodology/", "sources/", "about/")) or p == "research/index.html"])


class GovernanceBoundaryTests(unittest.TestCase):
    def test_no_binding_decision_inserted(self):
        log = (ROOT / "DECISION_LOG.md").read_text(encoding="utf-8")
        self.assertNotIn("MON-SI", log)
        self.assertNotIn("Strategic Intelligence", log)

    def test_gate_not_passed(self):
        gate = (SI / "GATE_MON-SI-G0.md").read_text(encoding="utf-8")
        self.assertIn("**Status:** PROPOSED", gate)
        self.assertNotRegex(gate, r"\*\*Verdict:\*\*\s*(PASS|FAIL)")

    def test_public_routes_do_not_publish_case(self):
        for route in ROUTES + ("sitemap.xml", "llms.txt"):
            with self.subTest(route=route):
                text = (ROOT / route).read_text(encoding="utf-8")
                self.assertNotIn("MON-SI", text)
                self.assertNotIn("strategic-intelligence", text)

    def test_adopted_taxonomy_unchanged(self):
        schema = (ROOT / "research" / "v0.2" / "ontology" / "candidate-schema.json").read_text(encoding="utf-8")
        for layer in ("legal_exclusivity", "capacity_control", "access_gatekeeping", "switching_dependency"):
            self.assertIn(layer, schema)
        self.assertNotIn("strategic_intelligence", schema)


if __name__ == "__main__":
    unittest.main()
