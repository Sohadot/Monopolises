"""Integrity checks for Monopolises Strategic Intelligence (MON-SI) case files.

Checks source dates against the cutoff, register schema, evidence references,
and forbidden cross-period contamination. Standard library only; no network.

    python3 research/strategic-intelligence/tools/check_registers.py

Passing these checks is necessary, not sufficient: it does not establish that
the research is correct or that any forecast is accurate.
"""

from datetime import datetime
from pathlib import Path
import json
import re
import sys

SI_ROOT = Path(__file__).resolve().parents[1]
CASES = SI_ROOT / "cases"

SOURCE_FIELDS = ("source_id", "status", "publisher", "title", "canonical_ref", "url",
                 "source_class", "publication_date", "availability_utc",
                 "availability_basis", "retrieved", "discovery_path", "hindsight_flag")
CLAIM_FIELDS = ("claim_id", "source_ids", "assertion", "pinpoint", "supporting_passage",
                "evidence_class", "scope", "excluded_implications",
                "counterevidence_or_alternative")
EVIDENCE_CLASSES = {"S0", "S1", "S2"}
NON_FINDING_CLASSES = {"secondary_lead", "short_seller_report", "proprietary"}
# Keys that would turn a research register into a scored / classified product.
FORBIDDEN_KEYS = {"score", "rank", "ranking", "layer", "severity", "dominance",
                  "monopoly_probability", "price_target", "signal", "rating"}
VALIDATION_CLASSES = ("Independently anticipated", "Partially corroborated later",
                      "Unresolved", "Contradicted",
                      "Not discoverable with the pre-event evidence")
# Facts first public after the MON-SI-001 cutoff. They may appear in the
# pre-event analysis only inside the hindsight-disclosure block.
POST_EVENT_TERMS = {
    "MON-SI-001": ("Culper", "Alice Huang", "Speedmatrix", "Apex Enterprise", "Aivres",
                   "Alibaba", "resign", "Kress", "Hugging Face", "physical control",
                   "Q1 FY2027 10-Q", "SI1-PST-", "SI1-V-"),
}
DISCLOSURE = re.compile(r"<!-- hindsight-disclosure:start -->.*?<!-- hindsight-disclosure:end -->",
                        re.S)
ID_REF = re.compile(r"\bSI\d-(?:SRC-\d{3}|PST-\d{3}|C-\d{2}|V-\d{2})\b")


def parse_utc(value):
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")


def walk_keys(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            yield key
            yield from walk_keys(value)
    elif isinstance(obj, list):
        for item in obj:
            yield from walk_keys(item)


def check_register(reg, period, errors, label):
    if reg.get("register") != period:
        errors.append(f"{label}: register field must be {period!r}")
    cutoff = parse_utc(reg["cutoff_utc"])
    bad = FORBIDDEN_KEYS & set(walk_keys(reg))
    if bad:
        errors.append(f"{label}: forbidden classification keys {sorted(bad)}")
    sources = {}
    for s in reg["sources"]:
        sid = s.get("source_id", "?")
        missing = [f for f in SOURCE_FIELDS if f not in s]
        if missing:
            errors.append(f"{label}:{sid} missing fields {missing}")
            continue
        if sid in sources:
            errors.append(f"{label}: duplicate source id {sid}")
        sources[sid] = s
        if s["status"] not in ("admitted", "excluded"):
            errors.append(f"{label}:{sid} bad status")
        if s["status"] == "excluded" and not s.get("exclusion_reason"):
            errors.append(f"{label}:{sid} excluded without exclusion_reason")
        if s["publication_date"]:
            datetime.strptime(s["publication_date"], "%Y-%m-%d")
        if s["availability_utc"]:
            avail = parse_utc(s["availability_utc"])
            if s["publication_date"] and avail.date().isoformat() < s["publication_date"]:
                errors.append(f"{label}:{sid} available before its publication date")
        if period == "pre_event":
            if not sid.startswith("SI1-SRC-"):
                errors.append(f"{label}:{sid} pre-event ids must use SI1-SRC-")
            if s["status"] == "admitted":
                if not s["availability_utc"]:
                    errors.append(f"{label}:{sid} admitted without demonstrated availability")
                elif parse_utc(s["availability_utc"]) > cutoff:
                    errors.append(f"{label}:{sid} admitted but available after cutoff")
                if s["publication_date"] and s["publication_date"] > cutoff.date().isoformat():
                    errors.append(f"{label}:{sid} admitted but published after cutoff")
                if s["source_class"] in NON_FINDING_CLASSES:
                    errors.append(f"{label}:{sid} non-primary class admitted pre-event")
        else:
            if not sid.startswith("SI1-PST-"):
                errors.append(f"{label}:{sid} post-event ids must use SI1-PST-")
    claims = {}
    for c in reg["claims"]:
        cid = c.get("claim_id", "?")
        missing = [f for f in CLAIM_FIELDS if f not in c]
        if missing:
            errors.append(f"{label}:{cid} missing fields {missing}")
            continue
        if cid in claims:
            errors.append(f"{label}: duplicate claim id {cid}")
        claims[cid] = c
        if c["evidence_class"] not in EVIDENCE_CLASSES:
            errors.append(f"{label}:{cid} bad evidence class")
        if not c["excluded_implications"]:
            errors.append(f"{label}:{cid} must list at least one excluded implication")
        if not c["source_ids"]:
            errors.append(f"{label}:{cid} cites no source")
        for ref in c["source_ids"]:
            src = sources.get(ref)
            if src is None:
                errors.append(f"{label}:{cid} cites unknown or out-of-period source {ref}")
            elif src["status"] != "admitted":
                errors.append(f"{label}:{cid} cites excluded source {ref}")
            elif c["evidence_class"] in ("S0", "S1") and src["source_class"] in NON_FINDING_CLASSES:
                errors.append(f"{label}:{cid} S0/S1 claim rests on non-primary source {ref}")
    return sources, claims


def check_case(case_dir, errors):
    label = case_dir.name
    pre = json.loads((case_dir / "register.pre-event.json").read_text(encoding="utf-8"))
    post = json.loads((case_dir / "register.post-event.json").read_text(encoding="utf-8"))
    if pre["cutoff_utc"] != post["cutoff_utc"]:
        errors.append(f"{label}: registers disagree on cutoff")
    pre_src, pre_claims = check_register(pre, "pre_event", errors, f"{label}/pre")
    post_src, post_claims = check_register(post, "post_event", errors, f"{label}/post")
    cutoff = parse_utc(pre["cutoff_utc"])
    for sid, s in post_src.items():
        if s["status"] == "admitted" and s["availability_utc"] and parse_utc(s["availability_utc"]) <= cutoff:
            errors.append(f"{label}/post:{sid} is pre-cutoff; it belongs in the pre-event register")

    analysis = (case_dir / "PRE_EVENT_ANALYSIS.md").read_text(encoding="utf-8")
    body = DISCLOSURE.sub("", analysis)
    if body == analysis:
        errors.append(f"{label}: PRE_EVENT_ANALYSIS.md lacks a hindsight-disclosure block")
    for ref in set(ID_REF.findall(analysis)):
        if ref not in pre_src and ref not in pre_claims:
            errors.append(f"{label}: pre-event analysis references non-pre-event id {ref}")
    for term in POST_EVENT_TERMS.get(label, ()):
        if term.lower() in body.lower():
            errors.append(f"{label}: post-event term {term!r} in pre-event analysis body")

    validation = (case_dir / "POST_EVENT_VALIDATION.md").read_text(encoding="utf-8")
    known = set(pre_src) | set(pre_claims) | set(post_src) | set(post_claims)
    for ref in set(ID_REF.findall(validation)):
        if ref not in known:
            errors.append(f"{label}: validation references unknown id {ref}")
    section = re.search(r"^## 2\..*?(?=^## 3\.)", validation, re.M | re.S)
    if not section:
        errors.append(f"{label}: validation lacks a section 2 classification table")
        return len(pre_src), len(post_src)
    classified = re.findall(r"^\|[^|]+\|[^|]+\|\s*\*\*([^*]+)\*\*", section.group(0), re.M)
    if not classified:
        errors.append(f"{label}: no classified rows in validation section 2")
    for row in classified:
        if row.strip() not in VALIDATION_CLASSES:
            errors.append(f"{label}: unknown validation class {row.strip()!r}")
    return len(pre_src), len(post_src)


def check_gate(errors):
    gate = (SI_ROOT / "GATE_MON-SI-G0.md").read_text(encoding="utf-8")
    status = re.search(r"^\*\*Status:\*\*\s*(\S+)", gate, re.M)
    if not status or status.group(1) != "PROPOSED":
        errors.append("GATE_MON-SI-G0.md status must remain PROPOSED until owner authorization")
    if re.search(r"^\*\*Verdict:\*\*\s*(PASS|FAIL)", gate, re.M):
        errors.append("GATE_MON-SI-G0.md must not declare a verdict")


def run():
    errors = []
    check_gate(errors)
    for case_dir in sorted(p for p in CASES.iterdir() if p.is_dir()):
        check_case(case_dir, errors)
    return errors


def main():
    errors = run()
    for e in errors:
        print("FAIL", e)
    print("OK" if not errors else f"{len(errors)} problem(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
