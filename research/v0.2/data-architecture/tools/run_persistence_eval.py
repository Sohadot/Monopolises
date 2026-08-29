#!/usr/bin/env python3
"""
MON-G4-DA Step 3 — persistence/retrieval fidelity runner.

Pipeline (fixed):
  1. Load ontology instance
  2. Logical write (candidate architecture)
  3. Generic retrieval → canonical SystemRecord
  4. Semantic canonicalization (case-independent)
  5. Full-content compare to locked ground truth (after case id mapping only)
  6. Interface composability (retrieved → interface grammar render)
  7. Structural: ambiguity fixture, history A/B, W1/W2 write-integrity (outside 8/8)
"""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # data-architecture
V02 = ROOT.parent
ONTOLOGY = V02 / "ontology"
INSTANCES_DIR = ONTOLOGY / "instances"
GROUND_TRUTH_PATH = ONTOLOGY / "ground-truth" / "normalized-fields.json"
AMBIGUITY_FIXTURE = V02 / "interface" / "fixtures" / "ambiguous_layer_structural.json"
HISTORY_A = ROOT / "fixtures" / "history_payload_a.json"
HISTORY_B = ROOT / "fixtures" / "history_payload_b.json"
HISTORY_LINEAGE_KEY = "mon-g4-da-history-lineage-001"
REPORT_PATH = ROOT / "persistence-report.json"

EVALUATION_ORDER = [
    "MON-G1-S8",
    "MON-G1-S1",
    "MON-G1-S2",
    "MON-G1-S6",
    "MON-G1-S4",
    "MON-G1-S5",
    "MON-G1-S3",
    "MON-G1-S7",
]


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def load_json(path: Path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def _binding_key(b: dict) -> tuple:
    return (
        b["claim"],
        b["evidence_class"],
        b["source"],
        b["fact"],
        b.get("derivation", ""),
    )


def _layer_content_key(rec: dict) -> tuple:
    holders_key = ()
    if "holders" in rec:
        holders_key = tuple(sorted(h["label"] for h in rec["holders"]))
    bindings_key = tuple(sorted(_binding_key(b) for b in rec["evidence_bindings"]))
    excluded_key = tuple(sorted(rec["claim_boundary"]["excluded"]))
    return (
        rec["layer_type"],
        rec["control_mechanism"]["statement"],
        rec["locus"]["statement"],
        holders_key,
        "holders" in rec,
        rec.get("scope"),
        json.dumps(rec.get("date"), sort_keys=True) if rec.get("date") else None,
        rec.get("jurisdiction", {}).get("statement") if "jurisdiction" in rec else None,
        rec["claim_boundary"]["admissible"],
        excluded_key,
        bindings_key,
    )


def _refusal_key(r: dict) -> tuple:
    return (r["candidate_label"], r["status"], r["reason"])


def _competing_key(c: dict) -> tuple:
    return (c["interpretation"], c.get("active_layer_type_considered"))


def canonicalize_system(system: dict) -> dict:
    """Case-independent semantic canonicalization for unordered collections."""
    s = copy.deepcopy(system)
    s["evidenced_layer_records"] = sorted(
        s.get("evidenced_layer_records", []), key=_layer_content_key
    )
    for rec in s["evidenced_layer_records"]:
        if "holders" in rec:
            rec["holders"] = sorted(rec["holders"], key=lambda h: h["label"])
        rec["evidence_bindings"] = sorted(rec["evidence_bindings"], key=_binding_key)
        rec["claim_boundary"]["excluded"] = sorted(rec["claim_boundary"]["excluded"])

    if "negative_assessment" in s:
        na = s["negative_assessment"]
        if "refusal_references" in na:
            na["refusal_references"] = sorted(na["refusal_references"], key=_refusal_key)
        na["claim_boundary"]["excluded"] = sorted(na["claim_boundary"]["excluded"])

    if "ambiguity_assessment" in s:
        aa = s["ambiguity_assessment"]
        aa["competing_interpretations"] = sorted(
            aa["competing_interpretations"], key=_competing_key
        )
        if "refusal_references" in aa:
            aa["refusal_references"] = sorted(aa["refusal_references"], key=_refusal_key)
        aa["claim_boundary"]["excluded"] = sorted(aa["claim_boundary"]["excluded"])

    if "refusal_assessment" in s:
        ra = s["refusal_assessment"]
        ra["refusal_references"] = sorted(ra["refusal_references"], key=_refusal_key)

    return s


def canonicalize_normalized(extracted: dict) -> dict:
    """Canonicalize normalized extract for order-independent full-content compare."""
    e = copy.deepcopy(extracted)

    def layer_key(L: dict) -> tuple:
        bindings_key = tuple(
            sorted(
                (
                    b["claim"],
                    b["evidence_class"],
                    b["source"],
                    b["fact"],
                    b.get("derivation", ""),
                )
                for b in L["evidence_bindings"]
            )
        )
        return (
            L["layer_type"],
            L["mechanism"],
            L["locus"],
            tuple(sorted(L["holders"])),
            L.get("scope"),
            json.dumps(L.get("date"), sort_keys=True) if L.get("date") else None,
            L.get("jurisdiction"),
            L["claim_boundary"]["admissible"],
            tuple(sorted(L["claim_boundary"]["excluded"])),
            bindings_key,
        )

    e["layers"] = sorted(e["layers"], key=layer_key)
    for L in e["layers"]:
        L["holders"] = sorted(L["holders"])
        L["evidence_bindings"] = sorted(
            L["evidence_bindings"],
            key=lambda b: (
                b["claim"],
                b["evidence_class"],
                b["source"],
                b["fact"],
                b.get("derivation", ""),
            ),
        )
        L["claim_boundary"]["excluded"] = sorted(L["claim_boundary"]["excluded"])

    e["refusal_references"] = sorted(e["refusal_references"], key=_refusal_key)

    if e.get("negative_assessment"):
        e["negative_assessment"]["claim_boundary"]["excluded"] = sorted(
            e["negative_assessment"]["claim_boundary"]["excluded"]
        )
    if e.get("ambiguity_assessment"):
        aa = e["ambiguity_assessment"]
        aa["competing_interpretations"] = sorted(
            aa["competing_interpretations"], key=_competing_key
        )
        aa["claim_boundary"]["excluded"] = sorted(aa["claim_boundary"]["excluded"])

    return e


def check_tautology_controls(source: str) -> list[str]:
    flags = []
    forbidden = [
        "MON-G1-S",
        "case_id",
        "expected_outcome",
        "expected_layer",
        "ground_truth",
        "EVALUATION_ORDER",
    ]
    for fn in ("def write", "def read"):
        start = source.find(fn)
        end = source.find("\n  def ", start + 1)
        if end == -1:
            end = source.find("\ndef ", start + 1)
        body = source[start:end] if start != -1 else ""
        for token in forbidden:
            if token in body:
                flags.append(f"{fn} contains forbidden token {token!r}")
    return flags


def systems_semantically_equal(a: dict, b: dict) -> bool:
    return canonicalize_system(a) == canonicalize_system(b)


def build_w1_probe(base: dict) -> dict:
    inst = copy.deepcopy(base)
    b = inst["system"]["evidenced_layer_records"][0]["evidence_bindings"][0]
    b["evidence_class"] = "S0"
    b["derivation"] = "invalid probe"
    return inst


def build_w2_probe() -> dict:
    inst = copy.deepcopy(load_json(INSTANCES_DIR / "MON-G1-S3.json"))
    inst["system"]["evidenced_layer_records"] = [
        {
            "layer_type": "capacity_control",
            "control_mechanism": {"statement": "W2 probe layer"},
            "locus": {"statement": "W2 probe locus"},
            "holders": [],
            "evidence_bindings": [
                {
                    "claim": "W2 probe",
                    "evidence_class": "S0",
                    "source": "W2 probe",
                    "fact": "W2 probe",
                }
            ],
            "claim_boundary": {"admissible": "W2 probe", "excluded": ["W2 probe"]},
        }
    ]
    return inst


def main() -> int:
    store_mod = _load_module("logical_store", ROOT / "tools" / "logical_store.py")
    rt_mod = _load_module("run_roundtrip", ONTOLOGY / "tools" / "run_roundtrip.py")
    iface_mod = _load_module(
        "run_interface_readback", V02 / "interface" / "tools" / "run_interface_readback.py"
    )

    LogicalStore = store_mod.LogicalStore
    WriteRejected = store_mod.WriteRejected
    extract_normalized = rt_mod.extract_normalized
    compare = rt_mod.compare
    render_representation = iface_mod.render_representation

    ground = load_json(GROUND_TRUTH_PATH)["cases"]
    store_source = (ROOT / "tools" / "logical_store.py").read_text(encoding="utf-8")
    tautology_flags = check_tautology_controls(store_source)

    results = []
    any_blocker = False

    for case_id in EVALUATION_ORDER:
        path = INSTANCES_DIR / f"{case_id}.json"
        row = {
            "case_id": case_id,
            "persistence_round_trip": None,
            "interface_composability": None,
            "gate_falsifiers_triggered": [],
            "blocker": False,
        }

        instance = load_json(path)
        store = LogicalStore()
        try:
            sid = store.write(instance)
            retrieved = store.read(sid)
        except WriteRejected as e:
            row["persistence_round_trip"] = "FAIL"
            row["blocker"] = True
            row["error"] = str(e)
            any_blocker = True
            results.append(row)
            continue

        canon = canonicalize_system(retrieved)
        extracted = canonicalize_normalized(
            extract_normalized({"system": canon})
        )
        expected = canonicalize_normalized(ground[case_id])
        cmp = compare(extracted, expected)

        try:
            render_representation(
                {
                    "schema_version": "mon-g2-of-candidate-v0.2",
                    "system": retrieved,
                }
            )
            row["interface_composability"] = "PASS"
        except Exception as e:
            row["interface_composability"] = "FAIL"
            row["gate_falsifiers_triggered"].append(
                f"Interface non-composability: {e}"
            )

        tautology = bool(tautology_flags)
        content_ok = not cmp["loss"] and not cmp["inflation"] and not cmp["distortion"]
        iface_ok = row["interface_composability"] == "PASS"
        passed = content_ok and iface_ok and not tautology

        row["persistence_round_trip"] = "PASS" if passed else "FAIL"
        row["loss"] = cmp["loss"]
        row["inflation"] = cmp["inflation"]
        row["distortion"] = cmp["distortion"]
        row["tautology"] = tautology
        row["diffs"] = cmp["diffs"]
        row["snapshot_id"] = sid

        if not passed:
            row["blocker"] = True
            any_blocker = True
            if cmp["loss"]:
                row["gate_falsifiers_triggered"].append("Loss on persistence round-trip")
            if cmp["inflation"]:
                row["gate_falsifiers_triggered"].append("Inflation on persistence round-trip")
            if cmp["distortion"]:
                row["gate_falsifiers_triggered"].append("Distortion on persistence round-trip")
            if not iface_ok:
                pass  # already recorded
            if tautology:
                row["gate_falsifiers_triggered"].append("Falsifier 15 — tautological write/read")

        results.append(row)

    # --- structural: ambiguity (MON-G3-IT fixture unchanged) ---
    ambiguity_row = {"verdict": "FAIL", "outside_8_of_8": True, "failures": []}
    try:
        amb_inst = load_json(AMBIGUITY_FIXTURE)
        amb_expected = copy.deepcopy(amb_inst["system"])
        store = LogicalStore()
        sid = store.write(amb_inst)
        retrieved = store.read(sid)
        if not systems_semantically_equal(retrieved, amb_expected):
            ambiguity_row["failures"].append("retrieved system != fixture system")
        if retrieved.get("evidenced_layer_records") != []:
            ambiguity_row["failures"].append("evidenced_layer_records not []")
        if "ambiguity_assessment" not in retrieved:
            ambiguity_row["failures"].append("missing ambiguity_assessment")
        comps = retrieved.get("ambiguity_assessment", {}).get("competing_interpretations", [])
        if len(comps) < 2:
            ambiguity_row["failures"].append("fewer than 2 competing interpretations")
        if "=== LAYER PANEL ===" in render_representation(amb_inst):
            ambiguity_row["failures"].append("unexpected layer panels in render")
        if not ambiguity_row["failures"]:
            ambiguity_row["verdict"] = "PASS"
    except Exception as e:
        ambiguity_row["failures"].append(str(e))

    # --- structural: history A/B ---
    history_row = {"verdict": "FAIL", "outside_8_of_8": True, "failures": []}
    try:
        store = LogicalStore()
        inst_a = load_json(HISTORY_A)
        inst_b = load_json(HISTORY_B)
        sid_a = store.write(inst_a, lineage_key=HISTORY_LINEAGE_KEY)
        sid_b = store.write(inst_b, lineage_key=HISTORY_LINEAGE_KEY)
        got_a = store.read(sid_a)
        got_b = store.read(sid_b)
        if not systems_semantically_equal(got_a, inst_a["system"]):
            history_row["failures"].append("snapshot A mismatch")
        if not systems_semantically_equal(got_b, inst_b["system"]):
            history_row["failures"].append("snapshot B mismatch")
        if store.lineage_latest(HISTORY_LINEAGE_KEY) != sid_b:
            history_row["failures"].append("latest pointer != B")
        if sid_a not in store.lineage_snapshots(HISTORY_LINEAGE_KEY):
            history_row["failures"].append("A missing from lineage")
        if HISTORY_LINEAGE_KEY in json.dumps(got_a) or HISTORY_LINEAGE_KEY in json.dumps(got_b):
            history_row["failures"].append("lineage key leaked into SystemRecord")
        if not history_row["failures"]:
            history_row["verdict"] = "PASS"
    except Exception as e:
        history_row["failures"].append(str(e))

    # --- structural: W1/W2 write-integrity ---
    write_integrity = {"verdict": "FAIL", "outside_8_of_8": True, "probes": {}, "failures": []}
    try:
        base = load_json(INSTANCES_DIR / "MON-G1-S1.json")
        store = LogicalStore()
        w1 = build_w1_probe(base)
        w2 = build_w2_probe()
        for name, probe in (("W1", w1), ("W2", w2)):
            try:
                store.write(probe)
                write_integrity["probes"][name] = "FAIL — accepted invalid write"
                write_integrity["failures"].append(f"{name} not rejected")
            except WriteRejected:
                write_integrity["probes"][name] = "PASS — rejected"
            except Exception as e:
                write_integrity["probes"][name] = f"FAIL — {e}"
                write_integrity["failures"].append(f"{name}: {e}")
        if not write_integrity["failures"]:
            write_integrity["verdict"] = "PASS"
    except Exception as e:
        write_integrity["failures"].append(str(e))

    pass_count = sum(1 for r in results if r["persistence_round_trip"] == "PASS")
    structural_ok = (
        ambiguity_row["verdict"] == "PASS"
        and history_row["verdict"] == "PASS"
        and write_integrity["verdict"] == "PASS"
    )

    summary = {
        "persistence_round_trip_pass_count": pass_count,
        "total_cases": len(results),
        "denominator": 8,
        "any_blocker": any_blocker or not structural_ok,
        "write_read_tautology_flags": tautology_flags,
        "ambiguous_layer_structural": ambiguity_row["verdict"],
        "history_preservation_structural": history_row["verdict"],
        "write_integrity_structural": write_integrity["verdict"],
        "compare_mode": "full_content_after_semantic_canonicalization",
        "gate_verdict_candidate": (
            "PASS"
            if (
                not any_blocker
                and not tautology_flags
                and pass_count == 8
                and structural_ok
            )
            else "FAIL — do not close gate; if architecture contract is the cause, return to Step 2"
        ),
    }

    report = {
        "summary": summary,
        "cases": results,
        "ambiguous_layer_structural": ambiguity_row,
        "history_preservation_structural": history_row,
        "write_integrity_structural": write_integrity,
    }
    REPORT_PATH.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(json.dumps(summary, indent=2))
    for r in results:
        print(
            f"{r['case_id']}: roundtrip={r['persistence_round_trip']} "
            f"iface={r['interface_composability']} blocker={r['blocker']}"
        )
    print(f"ambiguity: {ambiguity_row['verdict']} (outside 8/8)")
    print(f"history: {history_row['verdict']} (outside 8/8)")
    print(f"write-integrity: {write_integrity['verdict']} (outside 8/8)")

    return 1 if summary["any_blocker"] or tautology_flags else 0


if __name__ == "__main__":
    sys.exit(main())
