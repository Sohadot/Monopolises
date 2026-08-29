#!/usr/bin/env python3
"""
MON-G3-IT Step 3 — blind semantic/readback runner.

Pipeline (fixed):
  1. Load ontology instance (adopted encode; not re-classified)
  2. Render representation using ONLY general interface grammar (§1–§8)
     — no case-id branching; no §10 consultation
  3. Blind extract from representation TEXT only (no case id, no GT, no path)
  4. AFTER extract, map audit stem → locked ground truth for comparison
  5. Full-content compare (same normalized fields as MON-G2-OF GT)
  6. Separate: ambiguous_layer structural conformance (outside 8/8)

Ground truth: research/v0.2/ontology/ground-truth/normalized-fields.json
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # research/v0.2/interface
V02 = ROOT.parent
ONTOLOGY = V02 / "ontology"
INSTANCES_DIR = ONTOLOGY / "instances"
GROUND_TRUTH_PATH = ONTOLOGY / "ground-truth" / "normalized-fields.json"
THESIS_PATH = V02 / "CANDIDATE_INTERFACE_THESIS.md"
REPR_DIR = ROOT / "representations"
FIXTURES_DIR = ROOT / "fixtures"
REPORT_PATH = ROOT / "readback-report.json"

# Audit mapping only — used AFTER extract to select ground truth, never during render/extract.
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


def format_date(date_obj: dict | None) -> str:
    if date_obj is None:
        return ""
    return json.dumps(
        {k: date_obj[k] for k in ("as_of", "start", "end", "label") if k in date_obj},
        ensure_ascii=False,
        sort_keys=True,
    )


def parse_date(s: str) -> dict | None:
    s = s.strip()
    if not s or s == "—":
        return None
    return json.loads(s)


# ---------------------------------------------------------------------------
# Render — general grammar only (no case identity)
# ---------------------------------------------------------------------------


def render_refusal_note(ref: dict) -> list[str]:
    return [
        "=== REFUSAL NOTE ===",
        f"CANDIDATE_LABEL: {ref['candidate_label']}",
        f"STATUS: {ref['status']}",
        f"REASON: {ref['reason']}",
        "",
    ]


def render_boundary(cb: dict) -> list[str]:
    lines = [
        "BOUNDARY_ADMISSIBLE: " + cb["admissible"],
        "BOUNDARY_EXCLUDED:",
    ]
    for item in cb["excluded"]:
        lines.append(f"- {item}")
    return lines


def render_evidence_row(b: dict) -> list[str]:
    lines = [
        "=== CLAIM_EVIDENCE_ROW ===",
        f"CLAIM: {b['claim']}",
        f"EVIDENCE_CLASS: {b['evidence_class']}",
        f"SOURCE: {b['source']}",
        f"FACT: {b['fact']}",
    ]
    if b["evidence_class"] == "S1":
        lines.append(f"DERIVATION: {b['derivation']}")
    lines.append("")
    return lines


def render_layer_panel(rec: dict) -> list[str]:
    """Panel linear order: type → instrument → where → bounds → boundary → who → evidence."""
    lines = [
        "=== LAYER PANEL ===",
        f"LAYER_TYPE: {rec['layer_type']}",
        f"INSTRUMENT: {rec['control_mechanism']['statement']}",
        f"WHERE: {rec['locus']['statement']}",
    ]
    if "scope" in rec and rec["scope"] is not None:
        lines.append(f"LAYER_SCOPE: {rec['scope']}")
    if "date" in rec and rec["date"] is not None:
        lines.append(f"LAYER_DATE: {format_date(rec['date'])}")
    if "jurisdiction" in rec:
        lines.append(f"LAYER_JURISDICTION: {rec['jurisdiction']['statement']}")

    lines.extend(render_boundary(rec["claim_boundary"]))

    holders = rec.get("holders", [])
    if holders:
        lines.append("WHO:")
        for h in holders:
            lines.append(f"- {h['label']}")
    else:
        lines.append("WHO: holders not resolved at discrete-actor level")

    lines.append("")
    for b in rec["evidence_bindings"]:
        lines.extend(render_evidence_row(b))
    return lines


def render_negative_body(system: dict) -> list[str]:
    na = system["negative_assessment"]
    lines = [
        "=== NEGATIVE RESULT BODY ===",
        "ZERO_EVIDENCED_LAYERS: true",
        f"EXAMINED: {na['examined']}",
        "",
    ]
    for ref in na.get("refusal_references", []):
        lines.extend(render_refusal_note(ref))
    lines.extend(render_boundary(na["claim_boundary"]))
    lines.append("")
    return lines


def render_ambiguity_body(system: dict) -> list[str]:
    aa = system["ambiguity_assessment"]
    lines = [
        "=== AMBIGUITY RESULT BODY ===",
        "ZERO_EVIDENCED_LAYERS: true",
        "",
    ]
    for c in aa["competing_interpretations"]:
        lines.append("=== AMBIGUITY OPTION LINE ===")
        lines.append(f"INTERPRETATION: {c['interpretation']}")
        if "active_layer_type_considered" in c and c["active_layer_type_considered"] is not None:
            lines.append(
                f"ACTIVE_LAYER_TYPE_CONSIDERED_TEXT: {c['active_layer_type_considered']}"
            )
        lines.append("")
    lines.append(f"SEPARATION_GAP: {aa['separation_gap']}")
    lines.append("")
    for ref in aa.get("refusal_references", []):
        lines.extend(render_refusal_note(ref))
    lines.extend(render_boundary(aa["claim_boundary"]))
    lines.append("")
    return lines


def render_representation(instance: dict) -> str:
    """Apply interface grammar §§1–8. Must not receive or use a case id."""
    system = instance["system"]
    lines = [
        "=== SYSTEM READING UNIT ===",
        f"SYSTEM_SCOPE: {system['scope']}",
        f"SYSTEM_DATE: {format_date(system['date'])}",
        f"OUTCOME: {system['outcome']}",
        "",
    ]

    outcome = system["outcome"]
    layers = system["evidenced_layer_records"]

    if outcome in ("evidenced_control_layer", "multiple_evidenced_layers"):
        for rec in layers:
            lines.extend(render_layer_panel(rec))
        if "refusal_assessment" in system:
            lines.append("=== REFUSAL NOTES STRIP ===")
            lines.append("")
            for ref in system["refusal_assessment"]["refusal_references"]:
                lines.extend(render_refusal_note(ref))
    elif outcome == "no_evidenced_control_layer":
        lines.extend(render_negative_body(system))
    elif outcome == "ambiguous_layer":
        lines.extend(render_ambiguity_body(system))
    else:
        raise ValueError(f"unknown outcome {outcome!r}")

    return "\n".join(lines).rstrip() + "\n"


# ---------------------------------------------------------------------------
# Blind extract — representation text only
# ---------------------------------------------------------------------------


# Top-level body terminators (do not end a Layer panel on nested claim/refusal headers).
_TOP_LEVEL_HEADERS = (
    "=== SYSTEM READING UNIT ===",
    "=== LAYER PANEL ===",
    "=== NEGATIVE RESULT BODY ===",
    "=== AMBIGUITY RESULT BODY ===",
    "=== REFUSAL NOTES STRIP ===",
)


def _section_blocks(text: str, header: str, terminators: tuple[str, ...] | None = None) -> list[str]:
    """Split blocks starting at header until the next terminator header (or EOF)."""
    if terminators is None:
        # Default: any === line terminates (for nested rows / notes / option lines).
        term_pat = r"^=== "
    else:
        # Keep `header` among terminators so the next sibling block ends the current one.
        escaped = "|".join(re.escape(t) for t in terminators)
        term_pat = rf"^(?:{escaped})"
    pattern = re.compile(
        rf"^{re.escape(header)}\n(.*?)(?={term_pat}|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    return [m.group(1) for m in pattern.finditer(text)]


def _field(block: str, name: str) -> str | None:
    m = re.search(rf"^{re.escape(name)}: (.*)$", block, re.MULTILINE)
    return m.group(1).strip() if m else None


def _list_after(block: str, header: str) -> list[str]:
    """Collect '- item' lines immediately after HEADER: or HEADER alone."""
    # Match "HEADER:" or "HEADER" then newline then dash items
    m = re.search(
        rf"^{re.escape(header)}(?::[^\n]*)?\n((?:- .+\n?)+)",
        block,
        re.MULTILINE,
    )
    if not m:
        return []
    return [ln[2:].strip() for ln in m.group(1).strip().splitlines() if ln.startswith("- ")]


def _boundary_from_block(block: str) -> dict:
    admissible = _field(block, "BOUNDARY_ADMISSIBLE")
    excluded = _list_after(block, "BOUNDARY_EXCLUDED")
    return {"admissible": admissible, "excluded": excluded}


def extract_from_representation(text: str) -> dict:
    """Generic extract from grammar representation. Must not receive or use a case id."""
    if "=== SYSTEM READING UNIT ===" not in text:
        raise ValueError("missing system reading unit")

    # Forbid system-level jurisdiction strip (grammar: jurisdiction layer-scoped only)
    if re.search(r"^SYSTEM_JURISDICTION:", text, re.MULTILINE):
        raise ValueError("system-level jurisdiction strip forbidden by grammar")

    scope = _field(text, "SYSTEM_SCOPE")
    date = parse_date(_field(text, "SYSTEM_DATE") or "")
    outcome = _field(text, "OUTCOME")

    layers = []
    for panel in _section_blocks(text, "=== LAYER PANEL ===", _TOP_LEVEL_HEADERS):
        layer_type = _field(panel, "LAYER_TYPE")
        mechanism = _field(panel, "INSTRUMENT")
        locus = _field(panel, "WHERE")
        layer_scope = _field(panel, "LAYER_SCOPE")
        layer_date_raw = _field(panel, "LAYER_DATE")
        layer_date = parse_date(layer_date_raw) if layer_date_raw else None
        jurisdiction = _field(panel, "LAYER_JURISDICTION")

        who_line = _field(panel, "WHO")
        if who_line is not None and "not resolved at discrete-actor level" in who_line:
            holders = []
        else:
            holders = sorted(_list_after(panel, "WHO"))

        bindings = []
        for row in _section_blocks(panel, "=== CLAIM_EVIDENCE_ROW ==="):
            b = {
                "claim": _field(row, "CLAIM"),
                "evidence_class": _field(row, "EVIDENCE_CLASS"),
                "source": _field(row, "SOURCE"),
                "fact": _field(row, "FACT"),
            }
            if b["evidence_class"] == "S1":
                b["derivation"] = _field(row, "DERIVATION")
            bindings.append(b)

        layers.append(
            {
                "layer_type": layer_type,
                "mechanism": mechanism,
                "locus": locus,
                "holders": holders,
                "scope": layer_scope,
                "date": layer_date,
                "jurisdiction": jurisdiction,
                "evidence_bindings": bindings,
                "claim_boundary": _boundary_from_block(panel),
            }
        )

    # Structural panel-order check: BOUNDARY before WHO before evidence
    for i, panel in enumerate(
        _section_blocks(text, "=== LAYER PANEL ===", _TOP_LEVEL_HEADERS)
    ):
        b_pos = panel.find("BOUNDARY_ADMISSIBLE:")
        w_pos = panel.find("WHO:")
        e_pos = panel.find("=== CLAIM_EVIDENCE_ROW ===")
        if b_pos == -1 or w_pos == -1:
            raise ValueError(f"layer panel {i}: missing boundary or WHO")
        if not (b_pos < w_pos):
            raise ValueError(f"layer panel {i}: boundary must precede WHO (PASS-9)")
        if e_pos != -1 and not (w_pos < e_pos):
            raise ValueError(f"layer panel {i}: WHO must precede claim–evidence rows")

    refusal_refs = []
    for note in _section_blocks(text, "=== REFUSAL NOTE ==="):
        refusal_refs.append(
            {
                "candidate_label": _field(note, "CANDIDATE_LABEL"),
                "status": _field(note, "STATUS"),
                "reason": _field(note, "REASON"),
            }
        )
    refusal_refs = sorted(
        refusal_refs, key=lambda r: (r["candidate_label"], r["status"], r["reason"])
    )

    negative = None
    if "=== NEGATIVE RESULT BODY ===" in text:
        start = text.find("=== NEGATIVE RESULT BODY ===")
        end_candidates = [
            text.find("=== AMBIGUITY RESULT BODY ===", start + 1),
            text.find("=== LAYER PANEL ===", start + 1),
            text.find("=== REFUSAL NOTES STRIP ===", start + 1),
        ]
        ends = [e for e in end_candidates if e != -1]
        end = min(ends) if ends else len(text)
        neg_region = text[start:end]
        negative = {
            "examined": _field(neg_region, "EXAMINED"),
            "claim_boundary": _boundary_from_block(neg_region),
        }
        if _field(neg_region, "ZERO_EVIDENCED_LAYERS") != "true":
            raise ValueError("negative body must assert ZERO_EVIDENCED_LAYERS: true")

    ambiguity = None
    if "=== AMBIGUITY RESULT BODY ===" in text:
        start = text.find("=== AMBIGUITY RESULT BODY ===")
        end_candidates = [
            text.find("=== NEGATIVE RESULT BODY ===", start + 1),
            text.find("=== LAYER PANEL ===", start + 1),
            text.find("=== REFUSAL NOTES STRIP ===", start + 1),
        ]
        ends = [e for e in end_candidates if e != -1]
        end = min(ends) if ends else len(text)
        amb_region = text[start:end]
        comps = []
        for opt in _section_blocks(amb_region, "=== AMBIGUITY OPTION LINE ==="):
            entry = {"interpretation": _field(opt, "INTERPRETATION")}
            alt = _field(opt, "ACTIVE_LAYER_TYPE_CONSIDERED_TEXT")
            if alt is not None:
                entry["active_layer_type_considered"] = alt
            else:
                entry["active_layer_type_considered"] = None
            comps.append(entry)
        ambiguity = {
            "separation_gap": _field(amb_region, "SEPARATION_GAP"),
            "competing_interpretations": comps,
            "claim_boundary": _boundary_from_block(amb_region),
        }
        if _field(amb_region, "ZERO_EVIDENCED_LAYERS") != "true":
            raise ValueError("ambiguity body must assert ZERO_EVIDENCED_LAYERS: true")

    # EvidenceBinding rows must not appear outside layer panels
    if outcome in ("no_evidenced_control_layer", "ambiguous_layer"):
        if "=== CLAIM_EVIDENCE_ROW ===" in text:
            raise ValueError("EvidenceBinding rows forbidden on zero-record assessments")
        if "=== LAYER PANEL ===" in text:
            raise ValueError("Layer panels forbidden on zero-record outcomes")

    return {
        "outcome": outcome,
        "evidenced_layer_count": len(layers),
        "scope": scope,
        "date": date,
        "layers": layers,
        "refusal_references": refusal_refs,
        "negative_assessment": negative,
        "ambiguity_assessment": ambiguity,
        "refusal_assessment_present": "=== REFUSAL NOTES STRIP ===" in text,
    }


# ---------------------------------------------------------------------------
# Compare (same semantics as MON-G2-OF full-content)
# ---------------------------------------------------------------------------


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
        elif "derivation" in got and got.get("derivation") is not None:
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
    # Scan only render + extract function bodies
    for fn_name, next_marker in (
        ("def render_representation", "def _section_blocks"),
        ("def extract_from_representation", "def note_diff"),
    ):
        start = source.find(fn_name)
        end = source.find(next_marker, start + 1) if start != -1 else -1
        # Also include helpers used by render: scan from render_refusal through render_representation end
        body = source[start:end] if start != -1 and end != -1 else ""
        for token in forbidden:
            if token in body:
                flags.append(f"{fn_name} contains forbidden token {token!r}")
    # Broader scan of render helpers
    helper_start = source.find("def render_refusal_note")
    helper_end = source.find("def _section_blocks")
    helper_body = source[helper_start:helper_end] if helper_start != -1 and helper_end != -1 else ""
    for token in forbidden:
        if token in helper_body:
            flags.append(f"render helpers contain forbidden token {token!r}")
    return flags


# ---------------------------------------------------------------------------
# ambiguous_layer structural conformance (outside 8/8)
# ---------------------------------------------------------------------------


AMBIGUITY_FIXTURE = {
    "schema_version": "mon-g2-of-candidate-v0.2",
    "system": {
        "scope": "Structural conformance fixture — not a MON-G1 evaluation case",
        "date": {"label": "fixture-only"},
        "outcome": "ambiguous_layer",
        "evidenced_layer_records": [],
        "ambiguity_assessment": {
            "competing_interpretations": [
                {
                    "interpretation": "Reading A — source-defensible but not separable as evidenced layer",
                    "active_layer_type_considered": "access_gatekeeping",
                },
                {
                    "interpretation": "Reading B — alternate source-defensible reading of the same record",
                    "active_layer_type_considered": "switching_dependency",
                },
            ],
            "separation_gap": "Competing readings cannot be separated into an evidenced layer without inventing a decisive fact not in the record.",
            "claim_boundary": {
                "admissible": "Zero evidenced layers; ambiguity assessment only.",
                "excluded": [
                    "Promoting either competing reading to an evidenced layer panel.",
                    "Treating this fixture as a ninth evaluation case.",
                ],
            },
        },
    },
}


def check_ambiguity_grammar_doc(thesis_text: str) -> list[str]:
    gaps = []
    required_phrases = [
        ("outcome = `ambiguous_layer`", "ambiguous_layer outcome rule"),
        ("Ambiguity result body", "ambiguity body presentation"),
        ("competing interpretation", "competing interpretations"),
        ("ZERO evidenced layer", "zero evidenced layers / empty array semantics"),
        ("Provisional layer", "forbid provisional/ghost layers"),
        ("EvidenceBinding rows render only inside evidenced Layer panels", "no EvidenceBinding on assessments"),
    ]
    lowered = thesis_text
    # softer checks
    checks = [
        ("ambiguous_layer" in lowered, "thesis defines ambiguous_layer"),
        ("Ambiguity result body" in lowered or "ambiguity result body" in lowered.lower(), "ambiguity body role"),
        ("CompetingInterpretation" in lowered or "competing interpretation" in lowered.lower(), "competing interpretations"),
        ("zero evidenced" in lowered.lower() or "evidenced_layer_records = []" in lowered or "`[]`" in lowered, "empty layer array"),
        ("ghost" in lowered.lower() or "provisional" in lowered.lower() or "possible layer" in lowered.lower(), "forbids ghost/provisional layers"),
        ("EvidenceBinding rows render only inside evidenced Layer panels" in lowered, "no invented EvidenceBinding on assessments"),
    ]
    for ok, label in checks:
        if not ok:
            gaps.append(f"grammar doc missing: {label}")
    return gaps


def run_ambiguity_structural() -> dict:
    thesis = THESIS_PATH.read_text(encoding="utf-8")
    grammar_gaps = check_ambiguity_grammar_doc(thesis)

    FIXTURES_DIR.mkdir(parents=True, exist_ok=True)
    fixture_path = FIXTURES_DIR / "ambiguous_layer_structural.json"
    fixture_path.write_text(
        json.dumps(AMBIGUITY_FIXTURE, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    repr_text = render_representation(AMBIGUITY_FIXTURE)
    repr_path = REPR_DIR / "ambiguous_layer_structural.md"
    REPR_DIR.mkdir(parents=True, exist_ok=True)
    repr_path.write_text(repr_text, encoding="utf-8")

    checks = {
        "grammar_doc_complete": len(grammar_gaps) == 0,
        "grammar_gaps": grammar_gaps,
        "outcome_ambiguous": False,
        "zero_layers_asserted": False,
        "no_layer_panels": False,
        "no_evidence_rows": False,
        "competing_interpretations_ge_2": False,
        "separation_gap_present": False,
        "boundary_present": False,
        "no_ghost_layer_chrome": False,
        "extract_ok": False,
    }
    failures = []

    extracted = None
    try:
        extracted = extract_from_representation(repr_text)
        checks["extract_ok"] = True
    except Exception as e:
        failures.append(f"extract failed: {e}")

    checks["no_layer_panels"] = "=== LAYER PANEL ===" not in repr_text
    checks["no_evidence_rows"] = "=== CLAIM_EVIDENCE_ROW ===" not in repr_text
    checks["zero_layers_asserted"] = "ZERO_EVIDENCED_LAYERS: true" in repr_text
    # ghost chrome markers forbidden in this grammar representation
    ghost_tokens = ["possible layer", "provisional layer", "faded", "ghost layer"]
    checks["no_ghost_layer_chrome"] = not any(t in repr_text.lower() for t in ghost_tokens)

    if extracted:
        checks["outcome_ambiguous"] = extracted["outcome"] == "ambiguous_layer"
        checks["competing_interpretations_ge_2"] = (
            extracted["ambiguity_assessment"] is not None
            and len(extracted["ambiguity_assessment"]["competing_interpretations"]) >= 2
        )
        checks["separation_gap_present"] = bool(
            extracted["ambiguity_assessment"]
            and extracted["ambiguity_assessment"].get("separation_gap")
        )
        checks["boundary_present"] = bool(
            extracted["ambiguity_assessment"]
            and extracted["ambiguity_assessment"]["claim_boundary"].get("admissible")
            and extracted["ambiguity_assessment"]["claim_boundary"].get("excluded")
        )
        if extracted["evidenced_layer_count"] != 0:
            failures.append("extracted layer count != 0")
        if extracted["layers"]:
            failures.append("extracted layers non-empty")

    for key, ok in checks.items():
        if key == "grammar_gaps":
            continue
        if ok is False:
            failures.append(f"check failed: {key}")

    verdict = "PASS" if not failures and not grammar_gaps else "FAIL"
    return {
        "verdict": verdict,
        "outside_8_of_8": True,
        "checks": checks,
        "failures": failures,
        "fixture_path": str(fixture_path.relative_to(V02.parent.parent)),
        "representation_path": str(repr_path.relative_to(V02.parent.parent)),
    }


def main() -> int:
    ground = load_json(GROUND_TRUTH_PATH)["cases"]
    self_source = Path(__file__).read_text(encoding="utf-8")
    tautology_flags = check_tautology_controls(self_source)

    REPR_DIR.mkdir(parents=True, exist_ok=True)
    results = []
    any_blocker = False

    for case_id in EVALUATION_ORDER:
        path = INSTANCES_DIR / f"{case_id}.json"
        row = {
            "case_id": case_id,
            "semantic_readback": None,
            "gate_falsifiers_triggered": [],
            "blocker": False,
        }

        instance = load_json(path)

        # Render WITHOUT case_id.
        representation = render_representation(instance)
        # Filename carries audit identity only; extractor never sees the path.
        repr_path = REPR_DIR / f"{case_id}.md"
        repr_path.write_text(representation, encoding="utf-8")
        row["representation_path"] = str(repr_path.relative_to(V02.parent.parent))

        try:
            extracted = extract_from_representation(representation)
        except Exception as e:
            row["semantic_readback"] = "FAIL"
            row["blocker"] = True
            row["error"] = str(e)
            row["gate_falsifiers_triggered"].append(
                "Falsifier 15/readback — extract failed on representation"
            )
            any_blocker = True
            results.append(row)
            continue

        expected = ground[case_id]
        cmp = compare(extracted, expected)

        tautology = bool(tautology_flags)
        diffs = list(cmp["diffs"])
        if tautology:
            diffs.append(
                {
                    "kind": "tautology",
                    "field": "render/extract",
                    "detail": "; ".join(tautology_flags),
                }
            )

        content_ok = not cmp["loss"] and not cmp["inflation"] and not cmp["distortion"]
        readback_pass = content_ok and not tautology

        row["semantic_readback"] = "PASS" if readback_pass else "FAIL"
        row["loss"] = cmp["loss"]
        row["inflation"] = cmp["inflation"]
        row["distortion"] = cmp["distortion"]
        row["tautology"] = tautology
        row["diffs"] = diffs
        row["extracted"] = extracted

        # Interface-specific pressure checks (still general outcome/structure, not case-keyed recovery)
        if extracted["outcome"] == "no_evidenced_control_layer":
            if extracted["evidenced_layer_count"] != 0 or extracted["negative_assessment"] is None:
                row["gate_falsifiers_triggered"].append("Falsifier 7 — Negative as absence")
                readback_pass = False
        if (
            extracted["outcome"] == "multiple_evidenced_layers"
            and extracted["evidenced_layer_count"] < 2
        ):
            row["gate_falsifiers_triggered"].append("Falsifier 6 — Multiple-layer merge/collapse")
            readback_pass = False

        # S6-style: equal panels — representation must have N layer panels matching count
        if extracted["outcome"] == "multiple_evidenced_layers":
            panel_count = representation.count("=== LAYER PANEL ===")
            if panel_count != extracted["evidenced_layer_count"]:
                row["gate_falsifiers_triggered"].append(
                    "Falsifier 6 — panel count != evidenced layer count"
                )
                readback_pass = False

        if not readback_pass:
            row["semantic_readback"] = "FAIL"
            row["blocker"] = True
            any_blocker = True
            if cmp["loss"]:
                row["gate_falsifiers_triggered"].append("Loss on interface readback")
            if cmp["inflation"]:
                row["gate_falsifiers_triggered"].append("Inflation on interface readback")
            if cmp["distortion"]:
                row["gate_falsifiers_triggered"].append("Distortion on interface readback")
            if tautology:
                row["gate_falsifiers_triggered"].append(
                    "Falsifier 15 — Tautological readback / case-keyed escape hatch"
                )

        results.append(row)

    ambiguity = run_ambiguity_structural()

    pass_count = sum(1 for r in results if r["semantic_readback"] == "PASS")
    summary = {
        "semantic_readback_pass_count": pass_count,
        "total_cases": len(results),
        "denominator": 8,
        "any_blocker": any_blocker,
        "extractor_tautology_flags": tautology_flags,
        "ambiguous_layer_structural": ambiguity["verdict"],
        "ambiguous_layer_outside_8_of_8": True,
        "compare_mode": "full_content_via_interface_grammar",
        "gate_verdict_candidate": (
            "PASS"
            if (
                not any_blocker
                and not tautology_flags
                and pass_count == 8
                and ambiguity["verdict"] == "PASS"
            )
            else "FAIL — do not close gate; if grammar is the cause, return to Step 2"
        ),
    }

    report = {
        "summary": summary,
        "cases": results,
        "ambiguous_layer_structural": ambiguity,
    }
    REPORT_PATH.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(json.dumps(summary, indent=2))
    for r in results:
        print(
            f"{r['case_id']}: readback={r['semantic_readback']} blocker={r['blocker']}"
        )
        for d in r.get("diffs", [])[:8]:
            print(f"  - {d['kind']}: {d['field']}: {d['detail'][:180]}")
        if r.get("error"):
            print(f"  - error: {r['error']}")
    print(f"ambiguous_layer structural: {ambiguity['verdict']} (outside 8/8)")
    for f in ambiguity.get("failures", []):
        print(f"  - {f}")

    return 1 if any_blocker or tautology_flags or ambiguity["verdict"] != "PASS" else 0


if __name__ == "__main__":
    sys.exit(main())
