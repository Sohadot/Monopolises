# Ground-truth provenance — MON-G2-OF Step 3

`normalized-fields.json` is the **locked comparison target** for full-content round-trip.

## Source of truth

Expected fields are the normalized form of the MON-G1-LI case records under:

`research/v0.2/cases/MON-G1-S{1-8}.md`

plus mechanism wording where the frozen gate / DEC-005 encode discipline is more precise than first-draft case paraphrases (notably S6 Layer A: mechanism = concentrated capacity; evidence = BIS — per MON-G2-OF R3).

## What it is not

- Not regenerated from instance files at compare time.
- Not a live `extract(instance)` echo inside the runner.
- Instance files remain the **encode under test**; editing an instance without updating this file must fail round-trip.

## Compared fields (full content)

Per system: `outcome`, `scope`, `date`, layer count, refusal references (`candidate_label`, `status`, `reason`), negative/ambiguity assessment bodies.

Per layer record: `layer_type`, `mechanism`, `locus`, `holders`, `scope`, `date`, `jurisdiction`, every `evidence_bindings[]` field (`claim`, `evidence_class`, `source`, `fact`, `derivation` when S1), full `claim_boundary.admissible` and `excluded[]`.
