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
        self.assertEqual(set(pre["addenda"]), {"note", "availability_review", "errata"})
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
