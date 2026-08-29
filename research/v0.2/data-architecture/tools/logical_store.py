#!/usr/bin/env python3
"""
MON-G4-DA candidate logical data architecture — in-memory normalized store.

Implements CANDIDATE_DATA_ARCHITECTURE.md (mon-g4-da-candidate-v0.2):
  - normalized ownership (not opaque JSON blob)
  - lossless-or-reject write
  - optional collection presence fidelity (absent vs explicit [])
  - immutable snapshots + external lineage keys (never in SystemRecord)
  - generic read → canonical SystemRecord

No case-id branching. No production DB/API.
"""

from __future__ import annotations

import copy
import json
import uuid
from pathlib import Path
from typing import Any

try:
    from jsonschema import Draft202012Validator
except ImportError:
    Draft202012Validator = None  # type: ignore

SCHEMA_PATH = Path(__file__).resolve().parents[2] / "ontology" / "candidate-schema.json"


class WriteRejected(Exception):
    """Ontology-invalid or architecture-probe-failed write."""


def _new_id(prefix: str) -> str:
    return f"{prefix}-{uuid.uuid4().hex[:12]}"


def _collection_presence(parent: dict, key: str) -> str:
    if key not in parent:
        return "absent"
    if parent[key] == []:
        return "explicit_empty"
    return "with_items"


def _norm_date(date_obj: dict | None) -> dict | None:
    if date_obj is None:
        return None
    return {k: date_obj[k] for k in ("as_of", "start", "end", "label") if k in date_obj}


def _check_w1_w2(system: dict) -> None:
    for rec in system.get("evidenced_layer_records", []):
        for b in rec.get("evidence_bindings", []):
            if b.get("evidence_class") == "S0" and "derivation" in b:
                raise WriteRejected("W1: S0 binding must not carry derivation")
    if system.get("outcome") == "no_evidenced_control_layer" and system.get(
        "evidenced_layer_records"
    ):
        raise WriteRejected("W2: negative outcome with non-empty evidenced_layer_records")


class LogicalStore:
  """Normalized logical store for MON-G4-DA Step 3 evaluation."""

  def __init__(self) -> None:
    self.snapshots: dict[str, dict] = {}
    self.layers: dict[str, dict] = {}
    self.bindings: dict[str, dict] = {}
    self.boundaries: dict[str, dict] = {}
    self.refusal_refs: dict[str, dict] = {}
    self.competing: dict[str, dict] = {}
    self.negatives: dict[str, dict] = {}
    self.ambiguities: dict[str, dict] = {}
    self.refusal_assessments: dict[str, dict] = {}
    self.lineages: dict[str, dict] = {}  # key -> {snapshot_ids, latest_id}
    self.entity_labels: dict[str, str] = {}  # normalized -> canonical label
    self.source_labels: dict[str, str] = {}
    self._validator: Draft202012Validator | None = None

  def _validator_instance(self) -> Draft202012Validator:
    if self._validator is None:
      if Draft202012Validator is None:
        raise RuntimeError("jsonschema package required")
      schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
      self._validator = Draft202012Validator(schema)
    return self._validator

  def write(self, instance: dict, lineage_key: str | None = None) -> str:
    """Canonical write. Returns snapshot_id. Raises WriteRejected on invalid input.

    Validation here is machine-readable structural check (candidate-schema.json)
    plus frozen gating probes W1/W2. Full semantic ontology validity of the eight
    frozen cases is inherited from the adopted ontology instances — this store
    does not re-adjudicate every INV-1…INV-11 rejection class in Step 3.
    """
    errors = sorted(self._validator_instance().iter_errors(instance), key=lambda e: list(e.path))
    if errors:
      raise WriteRejected(
        "structural schema validation failed: "
        + "; ".join(e.message for e in errors[:3])
      )

    system = instance["system"]
    _check_w1_w2(system)

    sid = _new_id("snap")
    layer_ids: list[str] = []

    for rec in system.get("evidenced_layer_records", []):
      lid = _new_id("layer")
      layer_ids.append(lid)
      holders_presence = _collection_presence(rec, "holders")
      holder_labels = (
        [h["label"] for h in rec["holders"]] if holders_presence == "with_items" else []
      )
      for label in holder_labels:
        self.entity_labels.setdefault(label.strip().lower(), label)

      binding_ids = []
      for b in rec["evidence_bindings"]:
        bid = _new_id("bind")
        binding_ids.append(bid)
        src = b["source"]
        self.source_labels.setdefault(src.strip().lower(), src)
        self.bindings[bid] = {
          "layer_id": lid,
          "claim": b["claim"],
          "evidence_class": b["evidence_class"],
          "source": src,
          "fact": b["fact"],
          **({"derivation": b["derivation"]} if b["evidence_class"] == "S1" else {}),
        }

      bid_boundary = _new_id("bnd")
      self.boundaries[bid_boundary] = {
        "owner_kind": "layer",
        "owner_id": lid,
        "admissible": rec["claim_boundary"]["admissible"],
        "excluded": list(rec["claim_boundary"]["excluded"]),
      }

      self.layers[lid] = {
        "snapshot_id": sid,
        "layer_type": rec["layer_type"],
        "control_mechanism": copy.deepcopy(rec["control_mechanism"]),
        "locus": copy.deepcopy(rec["locus"]),
        "holders_presence": holders_presence,
        "holder_labels": holder_labels,
        "scope": rec.get("scope"),
        "date": _norm_date(rec.get("date")),
        "jurisdiction": (
          copy.deepcopy(rec["jurisdiction"]) if "jurisdiction" in rec else None
        ),
        "binding_ids": binding_ids,
        "boundary_id": bid_boundary,
      }

    negative_id = None
    if "negative_assessment" in system:
      negative_id = _new_id("neg")
      na = system["negative_assessment"]
      refs_presence = _collection_presence(na, "refusal_references")
      ref_ids = self._persist_refusal_refs(negative_id, "negative", na, refs_presence)
      bid = _new_id("bnd")
      self.boundaries[bid] = {
        "owner_kind": "negative",
        "owner_id": negative_id,
        "admissible": na["claim_boundary"]["admissible"],
        "excluded": list(na["claim_boundary"]["excluded"]),
      }
      self.negatives[negative_id] = {
        "snapshot_id": sid,
        "examined": na["examined"],
        "refusal_refs_presence": refs_presence,
        "refusal_ref_ids": ref_ids,
        "boundary_id": bid,
      }

    ambiguity_id = None
    if "ambiguity_assessment" in system:
      ambiguity_id = _new_id("amb")
      aa = system["ambiguity_assessment"]
      refs_presence = _collection_presence(aa, "refusal_references")
      ref_ids = self._persist_refusal_refs(ambiguity_id, "ambiguity", aa, refs_presence)
      comp_ids = []
      for c in aa["competing_interpretations"]:
        cid = _new_id("comp")
        comp_ids.append(cid)
        self.competing[cid] = {
          "ambiguity_id": ambiguity_id,
          "interpretation": c["interpretation"],
          "active_layer_type_considered": c.get("active_layer_type_considered"),
        }
      bid = _new_id("bnd")
      self.boundaries[bid] = {
        "owner_kind": "ambiguity",
        "owner_id": ambiguity_id,
        "admissible": aa["claim_boundary"]["admissible"],
        "excluded": list(aa["claim_boundary"]["excluded"]),
      }
      self.ambiguities[ambiguity_id] = {
        "snapshot_id": sid,
        "separation_gap": aa["separation_gap"],
        "refusal_refs_presence": refs_presence,
        "refusal_ref_ids": ref_ids,
        "competing_ids": comp_ids,
        "boundary_id": bid,
      }

    refusal_id = None
    if "refusal_assessment" in system:
      refusal_id = _new_id("ref")
      ra = system["refusal_assessment"]
      ref_ids = self._persist_refusal_refs(refusal_id, "refusal_assessment", ra, "with_items")
      self.refusal_assessments[refusal_id] = {
        "snapshot_id": sid,
        "refusal_ref_ids": ref_ids,
      }

    self.snapshots[sid] = {
      "scope": system["scope"],
      "date": _norm_date(system["date"]),
      "outcome": system["outcome"],
      "layer_ids": layer_ids,
      "negative_id": negative_id,
      "ambiguity_id": ambiguity_id,
      "refusal_assessment_id": refusal_id,
    }

    if lineage_key is not None:
      lin = self.lineages.setdefault(
        lineage_key, {"snapshot_ids": [], "latest_id": None}
      )
      lin["snapshot_ids"].append(sid)
      lin["latest_id"] = sid

    return sid

  def _persist_refusal_refs(
    self, owner_id: str, owner_kind: str, assessment: dict, presence: str
  ) -> list[str]:
    ref_ids: list[str] = []
    if presence == "with_items":
      for r in assessment["refusal_references"]:
        rid = _new_id("rref")
        ref_ids.append(rid)
        self.refusal_refs[rid] = {
          "owner_kind": owner_kind,
          "owner_id": owner_id,
          "candidate_label": r["candidate_label"],
          "status": r["status"],
          "reason": r["reason"],
        }
    return ref_ids

  def read(self, snapshot_id: str) -> dict:
    """Generic retrieval → canonical SystemRecord (`system` object only)."""
    if snapshot_id not in self.snapshots:
      raise KeyError(f"unknown snapshot_id {snapshot_id!r}")
    snap = self.snapshots[snapshot_id]
    system: dict[str, Any] = {
      "scope": snap["scope"],
      "date": copy.deepcopy(snap["date"]),
      "outcome": snap["outcome"],
      "evidenced_layer_records": [],
    }

    for lid in snap["layer_ids"]:
      layer = self.layers[lid]
      rec: dict[str, Any] = {
        "layer_type": layer["layer_type"],
        "control_mechanism": copy.deepcopy(layer["control_mechanism"]),
        "locus": copy.deepcopy(layer["locus"]),
        "evidence_bindings": [],
        "claim_boundary": self._read_boundary(layer["boundary_id"]),
      }
      hp = layer["holders_presence"]
      if hp == "explicit_empty":
        rec["holders"] = []
      elif hp == "with_items":
        rec["holders"] = [{"label": lbl} for lbl in layer["holder_labels"]]

      if layer["scope"] is not None:
        rec["scope"] = layer["scope"]
      if layer["date"] is not None:
        rec["date"] = copy.deepcopy(layer["date"])
      if layer["jurisdiction"] is not None:
        rec["jurisdiction"] = copy.deepcopy(layer["jurisdiction"])

      for bid in layer["binding_ids"]:
        b = self.bindings[bid]
        row = {
          "claim": b["claim"],
          "evidence_class": b["evidence_class"],
          "source": b["source"],
          "fact": b["fact"],
        }
        if b["evidence_class"] == "S1":
          row["derivation"] = b["derivation"]
        rec["evidence_bindings"].append(row)

      system["evidenced_layer_records"].append(rec)

    if snap["negative_id"]:
      system["negative_assessment"] = self._read_negative(snap["negative_id"])
    if snap["ambiguity_id"]:
      system["ambiguity_assessment"] = self._read_ambiguity(snap["ambiguity_id"])
    if snap["refusal_assessment_id"]:
      system["refusal_assessment"] = self._read_refusal_assessment(
        snap["refusal_assessment_id"]
      )

    return system

  def _read_boundary(self, boundary_id: str) -> dict:
    b = self.boundaries[boundary_id]
    return {"admissible": b["admissible"], "excluded": list(b["excluded"])}

  def _read_refusal_refs(self, ref_ids: list[str]) -> list[dict]:
    return [
      {
        "candidate_label": self.refusal_refs[rid]["candidate_label"],
        "status": self.refusal_refs[rid]["status"],
        "reason": self.refusal_refs[rid]["reason"],
      }
      for rid in ref_ids
    ]

  def _emit_refusal_refs_field(self, assessment: dict, presence: str, ref_ids: list[str]) -> None:
    if presence == "explicit_empty":
      assessment["refusal_references"] = []
    elif presence == "with_items":
      assessment["refusal_references"] = self._read_refusal_refs(ref_ids)

  def _read_negative(self, negative_id: str) -> dict:
    n = self.negatives[negative_id]
    out = {
      "examined": n["examined"],
      "claim_boundary": self._read_boundary(n["boundary_id"]),
    }
    self._emit_refusal_refs_field(out, n["refusal_refs_presence"], n["refusal_ref_ids"])
    return out

  def _read_ambiguity(self, ambiguity_id: str) -> dict:
    a = self.ambiguities[ambiguity_id]
    comps = []
    for cid in a["competing_ids"]:
      c = self.competing[cid]
      entry = {"interpretation": c["interpretation"]}
      if c.get("active_layer_type_considered") is not None:
        entry["active_layer_type_considered"] = c["active_layer_type_considered"]
      comps.append(entry)
    out = {
      "competing_interpretations": comps,
      "separation_gap": a["separation_gap"],
      "claim_boundary": self._read_boundary(a["boundary_id"]),
    }
    self._emit_refusal_refs_field(out, a["refusal_refs_presence"], a["refusal_ref_ids"])
    return out

  def _read_refusal_assessment(self, refusal_id: str) -> dict:
    r = self.refusal_assessments[refusal_id]
    return {"refusal_references": self._read_refusal_refs(r["refusal_ref_ids"])}

  def lineage_latest(self, lineage_key: str) -> str | None:
    lin = self.lineages.get(lineage_key)
    return lin["latest_id"] if lin else None

  def lineage_snapshots(self, lineage_key: str) -> list[str]:
    lin = self.lineages.get(lineage_key)
    return list(lin["snapshot_ids"]) if lin else []
