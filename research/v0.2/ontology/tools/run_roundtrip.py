#!/usr/bin/env python3
"""
MON-G2-OF Step 3 round-trip runner.

Pipeline (fixed order):
  1. Validate instance against candidate-schema.json
  2. Generic extract (no case-id branching; filename never read by extractor)
  3. After extract, map path stem → ground truth for comparison only
  4. Field-by-field compare; record loss/inflation/distortion/tautology flags

Extraction is intentionally dumb: it reads only schema-defined structural fields
from the instance object it is given.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    import jsonschema
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


def collect_refusal_references(system: dict) -> list[dict]:
    refs = []
    if "refusal_assessment" in system:
        refs.extend(system["refusal_assessment"].get("refusal_references", []))
    if "negative_assessment" in system:
        refs.extend(system["negative_assessment"].get("refusal_references", []))
    if "ambiguity_assessment" in system:
        refs.extend(system["ambiguity_assessment"].get("refusal_references", []))
    return [
        {"candidate_label": r["candidate_label"], "status": r["status"]}
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
                "jurisdiction_present": "jurisdiction" in rec,
                "evidence_binding_count": len(rec["evidence_bindings"]),
                "evidence_classes": [b["evidence_class"] for b in rec["evidence_bindings"]],
                "claim_boundary_excluded_count": len(rec["claim_boundary"]["excluded"]),
                "claim_boundary_admissible_present": bool(rec["claim_boundary"].get("admissible")),
                "scope_override_present": "scope" in rec,
                "date_override_present": "date" in rec,
            }
        )

    return {
        "outcome": system["outcome"],
        "evidenced_layer_count": len(system["evidenced_layer_records"]),
        "scope_present": bool(system.get("scope")),
        "date_present": "date" in system,
        "layers": layers,
        "refusal_references": sorted(
            collect_refusal_references(system),
            key=lambda r: (r["candidate_label"], r["status"]),
        ),
        "negative_assessment_present": "negative_assessment" in system,
        "ambiguity_assessment_present": "ambiguity_assessment" in system,
        "refusal_assessment_present": "refusal_assessment" in system,
    }


def compare(extracted: dict, expected: dict) -> dict:
    diffs = []
    loss = inflation = distortion = False

    def note(kind: str, field: str, detail: str):
        nonlocal loss, inflation, distortion
        diffs.append({"kind": kind, "field": field, "detail": detail})
        if kind == "loss":
            loss = True
        elif kind == "inflation":
            inflation = True
        elif kind == "distortion":
            distortion = True

    if extracted["outcome"] != expected["outcome"]:
        note("distortion", "outcome", f"{extracted['outcome']!r} != {expected['outcome']!r}")

    if extracted["evidenced_layer_count"] != expected["evidenced_layer_count"]:
        note(
            "distortion",
            "evidenced_layer_count",
            f"{extracted['evidenced_layer_count']} != {expected['evidenced_layer_count']}",
        )

    if extracted["negative_assessment_present"] != expected["negative_assessment_present"]:
        note(
            "distortion",
            "negative_assessment_present",
            f"{extracted['negative_assessment_present']} != {expected['negative_assessment_present']}",
        )

    if extracted["ambiguity_assessment_present"] != expected["ambiguity_assessment_present"]:
        note(
            "distortion",
            "ambiguity_assessment_present",
            f"{extracted['ambiguity_assessment_present']} != {expected['ambiguity_assessment_present']}",
        )

    exp_refs = sorted(
        expected["refusal_references"],
        key=lambda r: (r["candidate_label"], r["status"]),
    )
    if extracted["refusal_references"] != exp_refs:
        # missing expected = loss; extra = inflation
        exp_set = {(r["candidate_label"], r["status"]) for r in exp_refs}
        got_set = {(r["candidate_label"], r["status"]) for r in extracted["refusal_references"]}
        if exp_set - got_set:
            note("loss", "refusal_references", f"missing {sorted(exp_set - got_set)}")
        if got_set - exp_set:
            note("inflation", "refusal_references", f"extra {sorted(got_set - exp_set)}")

    if len(extracted["layers"]) != len(expected["layers"]):
        note(
            "distortion",
            "layers.length",
            f"{len(extracted['layers'])} != {len(expected['layers'])}",
        )
    else:
        for i, (got, exp) in enumerate(zip(extracted["layers"], expected["layers"])):
            prefix = f"layers[{i}]"
            for key in (
                "layer_type",
                "mechanism",
                "locus",
                "holders",
                "jurisdiction_present",
                "evidence_binding_count",
                "evidence_classes",
                "claim_boundary_excluded_count",
            ):
                if got[key] != exp[key]:
                    kind = "distortion"
                    if key in ("mechanism", "locus") and not got[key]:
                        kind = "loss"
                    note(kind, f"{prefix}.{key}", f"{got[key]!r} != {exp[key]!r}")
            if not got.get("claim_boundary_admissible_present"):
                note("loss", f"{prefix}.claim_boundary.admissible", "missing admissible record")

    if not extracted.get("scope_present"):
        note("loss", "scope", "system scope missing")
    if not extracted.get("date_present"):
        note("loss", "date", "system date missing")

    structural_pass = not diffs
    return {
        "structural_round_trip": "PASS" if structural_pass else "FAIL",
        "loss": loss,
        "inflation": inflation,
        "distortion": distortion,
        "tautology": False,  # set by caller if extract used case-id branching (it does not)
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
    # extract_normalized body only — approximate by ensuring function source has no case tokens
    # We inspect this file's extract_normalized by reading our own source around the function.
    start = extractor_source.find("def extract_normalized")
    end = extractor_source.find("\ndef compare")
    body = extractor_source[start:end] if start != -1 and end != -1 else extractor_source
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
        if tautology_flags:
            cmp["tautology"] = True
            cmp["diffs"].append(
                {
                    "kind": "tautology",
                    "field": "extractor",
                    "detail": "; ".join(tautology_flags),
                }
            )

        row["structural_round_trip"] = cmp["structural_round_trip"]
        row["loss"] = cmp["loss"]
        row["inflation"] = cmp["inflation"]
        row["distortion"] = cmp["distortion"]
        row["tautology"] = cmp["tautology"]
        row["diffs"] = cmp["diffs"]
        row["extracted"] = extracted

        if cmp["structural_round_trip"] != "PASS":
            row["blocker"] = True
            any_blocker = True
            if cmp["loss"]:
                row["gate_falsifiers_triggered"].append("Falsifier 2 — Loss on round-trip")
            if cmp["inflation"]:
                row["gate_falsifiers_triggered"].append("Falsifier 3 — Inflation on round-trip")
            if cmp["distortion"]:
                row["gate_falsifiers_triggered"].append("Falsifier 2/3 — Distortion on round-trip")
            if cmp["tautology"]:
                row["gate_falsifiers_triggered"].append(
                    "Falsifier 15 — Tautological round-trip / extraction escape hatch"
                )

        # Structural checks against known gate falsifiers even on PASS
        if extracted["outcome"] == "no_evidenced_control_layer":
            if extracted["evidenced_layer_count"] != 0 or not extracted["negative_assessment_present"]:
                row["gate_falsifiers_triggered"].append("Falsifier 7 — Cannot represent negatives")
                row["blocker"] = True
                any_blocker = True
        if extracted["outcome"] == "multiple_evidenced_layers" and extracted["evidenced_layer_count"] < 2:
            row["gate_falsifiers_triggered"].append("Falsifier 9 — Cannot represent multiples")
            row["blocker"] = True
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
            for d in r["diffs"]:
                print(f"  - {d['kind']}: {d['field']}: {d['detail']}")
        if r.get("validation_errors"):
            for e in r["validation_errors"]:
                print(f"  - validation: {e['path']}: {e['message']}")

    return 1 if any_blocker or tautology_flags else 0


if __name__ == "__main__":
    sys.exit(main())
