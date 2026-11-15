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
