#!/usr/bin/env python3
"""
MON-G2-OF Step 3 round-trip runner (full-content compare).

Pipeline (fixed order):
  1. Validate instance against candidate-schema.json
  2. Generic extract (no case-id branching; filename never read by extractor)
  3. After extract, map path stem → ground truth for comparison only
  4. Field-by-field full-content compare; record loss / inflation / distortion / tautology

Ground truth is an authored artifact derived from MON-G1-LI case records
(research/v0.2/cases/), not regenerated from instances at runtime.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
except ImportError:
    print("ERROR: jsonschema package required", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "candidate-schema.json"
INSTANCES_DIR = ROOT / "instances"
GROUND_TRUTH_PATH = ROOT / "ground-truth" / "normalized-fields.json"
REPORT_PATH = ROOT / "roundtrip-report.json"

# Audit mapping only — used AFTER extract to select ground truth, never during extract.
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


def load_json(path: Path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def norm_date(date_obj: dict | None) -> dict | None:
    if date_obj is None:
        return None
    return {k: date_obj[k] for k in ("as_of", "start", "end", "label") if k in date_obj}


def extract_binding(b: dict) -> dict:
    out = {
        "claim": b["claim"],
        "evidence_class": b["evidence_class"],
        "source": b["source"],
        "fact": b["fact"],
    }
    if b["evidence_class"] == "S1":
        out["derivation"] = b["derivation"]
    return out


def collect_refusal_references(system: dict) -> list[dict]:
    refs = []
    if "refusal_assessment" in system:
        refs.extend(system["refusal_assessment"].get("refusal_references", []))
    if "negative_assessment" in system:
        refs.extend(system["negative_assessment"].get("refusal_references", []))
    if "ambiguity_assessment" in system:
        refs.extend(system["ambiguity_assessment"].get("refusal_references", []))
    return [
        {
            "candidate_label": r["candidate_label"],
            "status": r["status"],
            "reason": r["reason"],
        }
        for r in refs
    ]


def extract_normalized(instance: dict) -> dict:
    """Generic structural extract. Must not receive or use a case id."""
    system = instance["system"]
    layers = []
    for rec in system["evidenced_layer_records"]:
        holders = sorted(h["label"] for h in rec.get("holders", []))
        layers.append(
            {
                "layer_type": rec["layer_type"],
                "mechanism": rec["control_mechanism"]["statement"],
                "locus": rec["locus"]["statement"],
                "holders": holders,
                "scope": rec.get("scope"),
                "date": norm_date(rec.get("date")),
                "jurisdiction": (
                    rec["jurisdiction"]["statement"] if "jurisdiction" in rec else None
                ),
                "evidence_bindings": [extract_binding(b) for b in rec["evidence_bindings"]],
                "claim_boundary": {
                    "admissible": rec["claim_boundary"]["admissible"],
                    "excluded": list(rec["claim_boundary"]["excluded"]),
                },
            }
        )

    negative = None
    if "negative_assessment" in system:
        na = system["negative_assessment"]
        negative = {
            "examined": na["examined"],
            "claim_boundary": {
                "admissible": na["claim_boundary"]["admissible"],
                "excluded": list(na["claim_boundary"]["excluded"]),
            },
        }

    ambiguity = None
    if "ambiguity_assessment" in system:
        aa = system["ambiguity_assessment"]
        ambiguity = {
            "separation_gap": aa["separation_gap"],
            "competing_interpretations": [
                {
                    "interpretation": c["interpretation"],
                    "active_layer_type_considered": c.get("active_layer_type_considered"),
                }
                for c in aa["competing_interpretations"]
            ],
            "claim_boundary": {
                "admissible": aa["claim_boundary"]["admissible"],
                "excluded": list(aa["claim_boundary"]["excluded"]),
            },
        }

    return {
        "outcome": system["outcome"],
        "evidenced_layer_count": len(system["evidenced_layer_records"]),
        "scope": system["scope"],
        "date": norm_date(system["date"]),
        "layers": layers,
        "refusal_references": sorted(
            collect_refusal_references(system),
            key=lambda r: (r["candidate_label"], r["status"], r["reason"]),
        ),
        "negative_assessment": negative,
        "ambiguity_assessment": ambiguity,
        "refusal_assessment_present": "refusal_assessment" in system,
    }


def note_diff(diffs: list, counters: dict, kind: str, field: str, detail: str) -> None:
    diffs.append({"kind": kind, "field": field, "detail": detail})
    counters[kind] = True


def compare_value(diffs, counters, field, got, exp) -> None:
    if got == exp:
        return
    if got in (None, [], "", {}) and exp not in (None, [], "", {}):
        note_diff(diffs, counters, "loss", field, f"missing; expected {exp!r}")
    elif exp in (None, [], "", {}) and got not in (None, [], "", {}):
        note_diff(diffs, counters, "inflation", field, f"unexpected {got!r}")
    else:
        note_diff(diffs, counters, "distortion", field, f"{got!r} != {exp!r}")


def compare_bindings(diffs, counters, prefix: str, got_list: list, exp_list: list) -> None:
    if len(got_list) != len(exp_list):
        note_diff(
            diffs,
            counters,
            "distortion",
            f"{prefix}.evidence_bindings.length",
            f"{len(got_list)} != {len(exp_list)}",
        )
        return
    for i, (got, exp) in enumerate(zip(got_list, exp_list)):
        p = f"{prefix}.evidence_bindings[{i}]"
        for key in ("claim", "evidence_class", "source", "fact"):
            compare_value(diffs, counters, f"{p}.{key}", got.get(key), exp.get(key))
        if exp.get("evidence_class") == "S1" or got.get("evidence_class") == "S1":
            compare_value(
                diffs, counters, f"{p}.derivation", got.get("derivation"), exp.get("derivation")
            )
        elif "derivation" in got:
            note_diff(
                diffs,
                counters,
                "inflation",
                f"{p}.derivation",
                "S0 binding must not carry derivation",
            )


def compare_claim_boundary(diffs, counters, prefix: str, got: dict, exp: dict) -> None:
    compare_value(
        diffs, counters, f"{prefix}.admissible", got.get("admissible"), exp.get("admissible")
    )
    g_ex = list(got.get("excluded", []))
    e_ex = list(exp.get("excluded", []))
    if g_ex != e_ex:
        missing = [x for x in e_ex if x not in g_ex]
        extra = [x for x in g_ex if x not in e_ex]
        if missing:
            note_diff(diffs, counters, "loss", f"{prefix}.excluded", f"missing {missing!r}")
        if extra:
            note_diff(diffs, counters, "inflation", f"{prefix}.excluded", f"extra {extra!r}")
        if not missing and not extra:
            # same multiset but different order — still distortion for exact fidelity
            note_diff(
                diffs,
                counters,
                "distortion",
                f"{prefix}.excluded",
                f"order/content mismatch {g_ex!r} != {e_ex!r}",
            )


def compare(extracted: dict, expected: dict) -> dict:
    diffs = []
    counters = {"loss": False, "inflation": False, "distortion": False}

    compare_value(diffs, counters, "outcome", extracted["outcome"], expected["outcome"])
    compare_value(
        diffs,
        counters,
        "evidenced_layer_count",
        extracted["evidenced_layer_count"],
        expected["evidenced_layer_count"],
    )
    compare_value(diffs, counters, "scope", extracted["scope"], expected["scope"])
    compare_value(diffs, counters, "date", extracted["date"], expected["date"])

    # Refusals: full label + status + reason
    exp_refs = sorted(
        expected["refusal_references"],
        key=lambda r: (r["candidate_label"], r["status"], r["reason"]),
    )
    got_refs = extracted["refusal_references"]
    if got_refs != exp_refs:
        exp_keys = {(r["candidate_label"], r["status"], r["reason"]) for r in exp_refs}
        got_keys = {(r["candidate_label"], r["status"], r["reason"]) for r in got_refs}
        if exp_keys - got_keys:
            note_diff(
                diffs, counters, "loss", "refusal_references", f"missing {sorted(exp_keys - got_keys)}"
            )
        if got_keys - exp_keys:
            note_diff(
                diffs,
                counters,
                "inflation",
                "refusal_references",
                f"extra {sorted(got_keys - exp_keys)}",
            )

    # Negative assessment full content
    exp_neg = expected.get("negative_assessment")
    got_neg = extracted.get("negative_assessment")
    if (exp_neg is None) != (got_neg is None):
        note_diff(
            diffs,
            counters,
            "distortion",
            "negative_assessment",
            f"present={got_neg is not None} expected={exp_neg is not None}",
        )
    elif exp_neg is not None:
        compare_value(
            diffs, counters, "negative_assessment.examined", got_neg["examined"], exp_neg["examined"]
        )
        compare_claim_boundary(
            diffs,
            counters,
            "negative_assessment.claim_boundary",
            got_neg["claim_boundary"],
            exp_neg["claim_boundary"],
        )

    exp_amb = expected.get("ambiguity_assessment")
    got_amb = extracted.get("ambiguity_assessment")
    if (exp_amb is None) != (got_amb is None):
        note_diff(
            diffs,
            counters,
            "distortion",
            "ambiguity_assessment",
            f"present={got_amb is not None} expected={exp_amb is not None}",
        )
    elif exp_amb is not None:
        compare_value(
            diffs,
            counters,
            "ambiguity_assessment.separation_gap",
            got_amb["separation_gap"],
            exp_amb["separation_gap"],
        )
        compare_value(
            diffs,
            counters,
            "ambiguity_assessment.competing_interpretations",
            got_amb["competing_interpretations"],
            exp_amb["competing_interpretations"],
        )
        compare_claim_boundary(
            diffs,
            counters,
            "ambiguity_assessment.claim_boundary",
            got_amb["claim_boundary"],
            exp_amb["claim_boundary"],
        )

    if len(extracted["layers"]) != len(expected["layers"]):
        note_diff(
            diffs,
            counters,
            "distortion",
            "layers.length",
            f"{len(extracted['layers'])} != {len(expected['layers'])}",
        )
    else:
        for i, (got, exp) in enumerate(zip(extracted["layers"], expected["layers"])):
            prefix = f"layers[{i}]"
            for key in ("layer_type", "mechanism", "locus", "holders", "scope", "date", "jurisdiction"):
                compare_value(diffs, counters, f"{prefix}.{key}", got.get(key), exp.get(key))
            compare_bindings(
                diffs, counters, prefix, got["evidence_bindings"], exp["evidence_bindings"]
            )
            compare_claim_boundary(
                diffs, counters, f"{prefix}.claim_boundary", got["claim_boundary"], exp["claim_boundary"]
            )

    return {
        "loss": counters["loss"],
        "inflation": counters["inflation"],
        "distortion": counters["distortion"],
        "diffs": diffs,
    }


def check_tautology_controls(extractor_source: str) -> list[str]:
    """Static checks that the extractor does not branch on case identity."""
    flags = []
    forbidden = [
        "MON-G1-S",
        "case_id",
        "expected_outcome",
        "expected_layer",
        "ground_truth",
        "EVALUATION_ORDER",
    ]
    start = extractor_source.find("def extract_normalized")
    end = extractor_source.find("\ndef note_diff")
    if end == -1:
        end = extractor_source.find("\ndef compare")
    body = extractor_source[start:end] if start != -1 and end != -1 else ""
    for token in forbidden:
        if token in body:
            flags.append(f"extractor contains forbidden token {token!r}")
    return flags


def main() -> int:
    schema = load_json(SCHEMA_PATH)
    validator = Draft202012Validator(schema)
    ground = load_json(GROUND_TRUTH_PATH)["cases"]
    self_source = Path(__file__).read_text(encoding="utf-8")
    tautology_flags = check_tautology_controls(self_source)

    results = []
    any_blocker = False

    for case_id in EVALUATION_ORDER:
        path = INSTANCES_DIR / f"{case_id}.json"
        row = {
            "case_id": case_id,
            "instance_path": str(path.relative_to(ROOT.parent.parent.parent)),
            "schema_validation": None,
            "structural_round_trip": None,
            "gate_falsifiers_triggered": [],
            "blocker": False,
        }

        if not path.exists():
            row["schema_validation"] = "FAIL"
            row["structural_round_trip"] = "FAIL"
            row["blocker"] = True
            row["error"] = "instance file missing"
            any_blocker = True
            results.append(row)
            continue

        instance = load_json(path)
        errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))
        if errors:
            row["schema_validation"] = "FAIL"
            row["validation_errors"] = [
                {"path": "/" + "/".join(str(p) for p in e.path), "message": e.message}
                for e in errors
            ]
            row["structural_round_trip"] = "FAIL"
            row["blocker"] = True
            row["gate_falsifiers_triggered"].append(
                "Cannot encode under accepted schema without workaround (schema validation fail)"
            )
            any_blocker = True
            results.append(row)
            continue

        row["schema_validation"] = "PASS"

        # Extract WITHOUT passing case_id into the extractor.
        extracted = extract_normalized(instance)

        # Case identity used only here — to select ground truth for comparison.
        expected = ground[case_id]
        cmp = compare(extracted, expected)

        tautology = bool(tautology_flags)
        diffs = list(cmp["diffs"])
        if tautology:
            diffs.append(
                {
                    "kind": "tautology",
                    "field": "extractor",
                    "detail": "; ".join(tautology_flags),
                }
            )

        content_ok = not cmp["loss"] and not cmp["inflation"] and not cmp["distortion"]
        structural_pass = content_ok and not tautology

        row["structural_round_trip"] = "PASS" if structural_pass else "FAIL"
        row["loss"] = cmp["loss"]
        row["inflation"] = cmp["inflation"]
        row["distortion"] = cmp["distortion"]
        row["tautology"] = tautology
        row["diffs"] = diffs
        row["extracted"] = extracted

        if not structural_pass:
            row["blocker"] = True
            any_blocker = True
            if cmp["loss"]:
                row["gate_falsifiers_triggered"].append("Falsifier 2 — Loss on round-trip")
            if cmp["inflation"]:
                row["gate_falsifiers_triggered"].append("Falsifier 3 — Inflation on round-trip")
            if cmp["distortion"]:
                row["gate_falsifiers_triggered"].append(
                    "Falsifier 2/3 — Distortion on round-trip"
                )
            if tautology:
                row["gate_falsifiers_triggered"].append(
                    "Falsifier 15 — Tautological round-trip / extraction escape hatch"
                )

        if extracted["outcome"] == "no_evidenced_control_layer":
            if extracted["evidenced_layer_count"] != 0 or extracted["negative_assessment"] is None:
                row["gate_falsifiers_triggered"].append("Falsifier 7 — Cannot represent negatives")
                row["blocker"] = True
                row["structural_round_trip"] = "FAIL"
                any_blocker = True
        if (
            extracted["outcome"] == "multiple_evidenced_layers"
            and extracted["evidenced_layer_count"] < 2
        ):
            row["gate_falsifiers_triggered"].append("Falsifier 9 — Cannot represent multiples")
            row["blocker"] = True
            row["structural_round_trip"] = "FAIL"
            any_blocker = True

        results.append(row)

    summary = {
        "schema_validation_pass_count": sum(1 for r in results if r["schema_validation"] == "PASS"),
        "structural_round_trip_pass_count": sum(
            1 for r in results if r["structural_round_trip"] == "PASS"
        ),
        "total_cases": len(results),
        "any_blocker": any_blocker,
        "extractor_tautology_flags": tautology_flags,
        "compare_mode": "full_content",
        "gate_verdict_candidate": (
            "PASS"
            if (
                not any_blocker
                and not tautology_flags
                and all(r["schema_validation"] == "PASS" for r in results)
                and all(r["structural_round_trip"] == "PASS" for r in results)
            )
            else "FAIL — do not close gate; return to Step 2 if schema is the cause"
        ),
    }

    report = {"summary": summary, "cases": results}
    REPORT_PATH.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(json.dumps(summary, indent=2))
    for r in results:
        print(
            f"{r['case_id']}: schema={r['schema_validation']} "
            f"roundtrip={r['structural_round_trip']} blocker={r['blocker']}"
        )
        if r.get("diffs"):
            for d in r["diffs"][:12]:
                print(f"  - {d['kind']}: {d['field']}: {d['detail'][:200]}")
            if len(r["diffs"]) > 12:
                print(f"  ... {len(r['diffs']) - 12} more diffs")
        if r.get("validation_errors"):
            for e in r["validation_errors"]:
                print(f"  - validation: {e['path']}: {e['message']}")

    return 1 if any_blocker or tautology_flags else 0


if __name__ == "__main__":
    sys.exit(main())
