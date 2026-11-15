"""Integrity checks for Monopolises Strategic Intelligence (MON-SI) case files.

Checks source dates against the cutoff, register schema, evidence references,
and forbidden cross-period contamination. Standard library only; no network.

    python3 research/strategic-intelligence/tools/check_registers.py

Passing these checks is necessary, not sufficient: it does not establish that
the research is correct or that any forecast is accurate.
"""

from datetime import datetime
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

SI_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = SI_ROOT.parents[1]
# Immutable anchor for the MON-SI-001 pre-event freeze. Pinned in code (not only in
# the manifest) so that editing the manifest cannot move the anchor silently.
FREEZE_ANCHORS = {"MON-SI-001": "5b3b756caaf1b084752981528ec1aceea3bb05c4"}
FROZEN_CUTOFFS = {"MON-SI-001": "2026-05-12T23:59:00Z"}
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
                  "monopoly_probability", "probability", "price_target", "target_price",
                  "signal", "trading_signal", "rating", "recommendation"}
EVIDENTIARY_STATUS = ("Confirmed", "Partially corroborated", "Unresolved", "Contradicted",
                      "Not established")
RETROSPECTIVE_RELATION = ("Retrospectively consistent — no prospective credit",
                          "Not discoverable with the pre-event evidence", "Not applicable")
# Labels that would award prediction credit to a retrospective case.
PROSPECTIVE_CREDIT_LABELS = ("independently anticipated", "anticipated", "predicted",
                             "prospectively validated", "forecast confirmed")
AVAILABILITY_LEVELS = ("demonstrated", "inferred_from_official_date",
                       "insufficiently_demonstrated")
CLAIM_CATEGORIES = ("A_documented_primary_fact", "B_reproducible_calculation",
                    "C_allegation_or_hypothesis", "D_unsupported_or_unresolved")
ERRATA_FIELDS = ("date", "affects", "correction", "interpretation_changed", "reason")
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
        cat = c.get("claim_category")
        if cat is not None:
            if cat not in CLAIM_CATEGORIES:
                errors.append(f"{label}:{cid} bad claim_category {cat!r}")
            elif cat == "A_documented_primary_fact" and c["evidence_class"] != "S0":
                errors.append(f"{label}:{cid} category A requires S0")
            elif cat == "C_allegation_or_hypothesis" and c["evidence_class"] != "S2":
                errors.append(f"{label}:{cid} allegations must stay S2")
    addenda = reg.get("addenda", {})
    for e in addenda.get("errata", []):
        eid = e.get("erratum_id", "?")
        missing = [f for f in ERRATA_FIELDS if f not in e]
        if missing:
            errors.append(f"{label}:{eid} erratum missing {missing}")
        elif e["date"] < reg.get("frozen", "0000-00-00"):
            errors.append(f"{label}:{eid} erratum predates the freeze")
    review = {r["source_id"]: r for r in addenda.get("availability_review", [])}
    if period == "pre_event" and review:
        for sid, s in sources.items():
            if s["status"] == "admitted" and sid not in review:
                errors.append(f"{label}:{sid} admitted but missing from availability_review")
        for sid, r in review.items():
            if r.get("demonstrated_public_availability") not in AVAILABILITY_LEVELS:
                errors.append(f"{label}:{sid} bad availability level")
        for cid, c in claims.items():
            if c["evidence_class"] in ("S0", "S1") and c["source_ids"] and all(
                    review.get(ref, {}).get("demonstrated_public_availability")
                    == "insufficiently_demonstrated" for ref in c["source_ids"]):
                errors.append(f"{label}:{cid} S0/S1 claim rests only on sources with "
                              "insufficiently demonstrated availability")
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
        if (s["status"] == "admitted" and s["availability_utc"]
                and parse_utc(s["availability_utc"]) <= cutoff
                and not s.get("pre_cutoff_document_located_post_hoc")):
            errors.append(f"{label}/post:{sid} is pre-cutoff; it belongs in the pre-event register")

    analysis = (case_dir / "PRE_EVENT_ANALYSIS.md").read_text(encoding="utf-8")
    manifest_path = case_dir / "FREEZE_MANIFEST.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        check_freeze(case_dir, manifest, pre, analysis, errors, label)
        if label in FREEZE_ANCHORS and case_dir.name == label and case_dir.parent == CASES:
            verify_freeze_against_git(label, analysis, pre,
                                      (case_dir / "event-study-pre-event.json").read_bytes(),
                                      manifest, errors)
    elif label in FREEZE_ANCHORS:
        errors.append(f"{label}: FREEZE_MANIFEST.json missing for an anchored case")
    frozen_analysis = analysis.split("\n" + ERRATA_POINTER, 1)[0]
    body = DISCLOSURE.sub("", frozen_analysis)
    if body == frozen_analysis:
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
    rows = re.findall(r"^\|([^|]+)\|([^|]+)\|\s*\*\*([^*]+)\*\*\s*\|([^|]+)\|\s*$",
                      section.group(0), re.M)
    if not rows:
        errors.append(f"{label}: no classified rows in validation section 2")
    for item, _evidence, status, relation in rows:
        if status.strip() not in EVIDENTIARY_STATUS:
            errors.append(f"{label}: unknown evidentiary status {status.strip()!r}")
        if relation.strip() not in RETROSPECTIVE_RELATION:
            errors.append(f"{label}: unknown retrospective relation {relation.strip()!r}")
        for bad in PROSPECTIVE_CREDIT_LABELS:
            if bad in (status + relation).lower():
                errors.append(f"{label}: prospective-credit label {bad!r} in {item.strip()!r}")
    if "**Prospective credit:** **none." not in validation:
        errors.append(f"{label}: validation must state that no prospective credit is awarded")
    return len(pre_src), len(post_src)


ERRATA_POINTER = "<!-- errata-pointer -->"


def canonical_core(reg):
    core = {k: reg[k] for k in ("case_id", "register", "cutoff_utc", "frozen", "sources", "claims")}
    return json.dumps(core, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()


def check_freeze(case_dir, manifest, pre, analysis, errors, label):
    """Frozen pre-event content may only be extended by dated, appended errata."""
    files = manifest["files"]
    actual = {
        "PRE_EVENT_ANALYSIS.md": hashlib.sha256(
            analysis.split("\n" + ERRATA_POINTER, 1)[0].encode("utf-8")).hexdigest(),
        "register.pre-event.json": hashlib.sha256(canonical_core(pre)).hexdigest(),
        "event-study-pre-event.json": hashlib.sha256(
            (case_dir / "event-study-pre-event.json").read_bytes()).hexdigest(),
    }
    for name, digest in actual.items():
        if files.get(name, {}).get("sha256") != digest:
            errors.append(f"{label}: frozen file {name} changed since {manifest['frozen_commit']}")
    tail = analysis.split(ERRATA_POINTER, 1)[1] if ERRATA_POINTER in analysis else ""
    for term in POST_EVENT_TERMS.get(label, ()):
        if term.lower() in tail.lower():
            errors.append(f"{label}: post-event term {term!r} in pre-event errata pointer")


def git_show(commit, repo_path):
    """Return the bytes of repo_path at commit, or None if git/commit unavailable."""
    try:
        return subprocess.run(["git", "show", f"{commit}:{repo_path}"], cwd=REPO_ROOT,
                              capture_output=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError):
        return None


def verify_freeze_against_git(label, analysis, pre, event_bytes, manifest, errors):
    """Compare frozen content with the original Git objects at the pinned anchor.

    Permitted after the freeze: an `addenda` key in the pre-event register and text
    after the errata pointer in PRE_EVENT_ANALYSIS.md. Everything else must be
    byte-identical (analysis, event study) or canonically identical (register core)
    to the anchor commit. The manifest must also agree with hashes computed from
    the Git objects, so changing content and manifest together is still detected.
    """
    anchor = FREEZE_ANCHORS.get(label)
    if anchor is None:
        errors.append(f"{label}: no pinned freeze anchor")
        return
    if manifest.get("frozen_commit") and not anchor.startswith(manifest["frozen_commit"]):
        errors.append(f"{label}: manifest frozen_commit differs from pinned anchor {anchor[:7]}")
    rel = f"research/strategic-intelligence/cases/{label}/"
    originals = {name: git_show(anchor, rel + name) for name in
                 ("PRE_EVENT_ANALYSIS.md", "register.pre-event.json", "event-study-pre-event.json")}
    missing = [n for n, v in originals.items() if v is None]
    if missing:
        errors.append(f"{label}: cannot read {missing} at freeze anchor {anchor[:7]} "
                      "(full git history required; freeze not verified)")
        return
    git_reg = json.loads(originals["register.pre-event.json"])
    if "addenda" in git_reg:
        errors.append(f"{label}: anchor register unexpectedly has addenda")
    frozen_text = analysis.split("\n" + ERRATA_POINTER, 1)[0].encode("utf-8")
    if frozen_text != originals["PRE_EVENT_ANALYSIS.md"]:
        errors.append(f"{label}: PRE_EVENT_ANALYSIS.md differs from anchor {anchor[:7]}")
    if canonical_core(pre) != canonical_core(git_reg):
        errors.append(f"{label}: register.pre-event.json sources/claims differ from anchor {anchor[:7]}")
    if pre.get("cutoff_utc") != git_reg.get("cutoff_utc") or pre.get("cutoff_utc") != FROZEN_CUTOFFS.get(label):
        errors.append(f"{label}: cutoff changed from frozen {FROZEN_CUTOFFS.get(label)}")
    if event_bytes != originals["event-study-pre-event.json"]:
        errors.append(f"{label}: event-study-pre-event.json differs from anchor {anchor[:7]}")
    expected = {
        "PRE_EVENT_ANALYSIS.md": hashlib.sha256(originals["PRE_EVENT_ANALYSIS.md"]).hexdigest(),
        "register.pre-event.json": hashlib.sha256(canonical_core(git_reg)).hexdigest(),
        "event-study-pre-event.json": hashlib.sha256(originals["event-study-pre-event.json"]).hexdigest(),
    }
    for name, digest in expected.items():
        if manifest.get("files", {}).get(name, {}).get("sha256") != digest:
            errors.append(f"{label}: manifest hash for {name} does not match the anchor Git object")


def p1_status(pre):
    """MON-SI-G0 P1 provenance status under the unchanged criterion.

    P1 requires *demonstrated* public availability at or before the cutoff for every
    admitted pre-event source (EVIDENCE_PROTOCOL.md section 2). Date consistency,
    document existence and an official date are recorded but do not satisfy it.
    """
    review = {r["source_id"]: r["demonstrated_public_availability"]
              for r in pre.get("addenda", {}).get("availability_review", [])}
    admitted = [s["source_id"] for s in pre["sources"] if s["status"] == "admitted"]
    unresolved = {sid: review.get(sid, "not_reviewed") for sid in admitted
                  if review.get(sid) != "demonstrated"}
    return {"established": not unresolved, "admitted": len(admitted),
            "demonstrated": len(admitted) - len(unresolved), "unresolved": unresolved}


def check_gate(errors):
    gate = (SI_ROOT / "GATE_MON-SI-G0.md").read_text(encoding="utf-8")
    status = re.search(r"^\*\*Status:\*\*\s*(\S+)", gate, re.M)
    if not status or status.group(1) != "PROPOSED":
        errors.append("GATE_MON-SI-G0.md status must remain PROPOSED until owner authorization")
    if re.search(r"^\*\*Verdict:\*\*\s*(PASS|FAIL)", gate, re.M):
        errors.append("GATE_MON-SI-G0.md must not declare a verdict")
    state = gate.split("## Current evaluation state", 1)
    p1_row = re.search(r"^\| P1 \|(.*)\|\s*$", state[1], re.M) if len(state) == 2 else None
    p1_open = any(not p1_status(json.loads((d / "register.pre-event.json").read_text(
        encoding="utf-8")))["established"] for d in CASES.iterdir() if d.is_dir()
        and (d / "register.pre-event.json").exists())
    if not p1_row:
        errors.append("GATE_MON-SI-G0.md lacks a P1 status row")
    elif p1_open:
        text = p1_row.group(1)
        if "NOT ESTABLISHED" not in text or re.search(r"\b(passes|passed|PASS)\b", text):
            errors.append("GATE_MON-SI-G0.md must report P1 as NOT ESTABLISHED while availability "
                          "conditions remain unresolved, and must not say it passes")
    if "permanently excluded from P5" not in gate:
        errors.append("GATE_MON-SI-G0.md must state that retrospective cases are permanently excluded from P5")


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
    for case_dir in sorted(p for p in CASES.iterdir() if p.is_dir()):
        st = p1_status(json.loads((case_dir / "register.pre-event.json").read_text(encoding="utf-8")))
        print(f"{case_dir.name}: P1 {'ESTABLISHED' if st['established'] else 'NOT ESTABLISHED'} "
              f"({st['demonstrated']}/{st['admitted']} admitted sources with demonstrated availability)"
              + (f"; unresolved: {st['unresolved']}" if st["unresolved"] else ""))
    print("Structural checks: " + ("OK" if not errors else f"{len(errors)} problem(s)")
          + " (structural consistency only; not a gate verdict)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
