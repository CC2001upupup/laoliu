# Global Architecture

Use this reference for whole-paper drafting, restructuring, contribution
framing, or any revision that spans multiple modules.

## 1. Build the causal spine

Write the paper around one auditable chain:

```text
known result and scope
-> exact missing property or proof obstruction
-> mechanism introduced or modified
-> auxiliary mathematical property
-> main guarantee
-> capability, comparison, or application
```

Do not skip from `gap` to `main theorem` if an enabling property explains why
the theorem is possible.

## 2. Compare properties, not papers in bulk

For the closest result, record:

| Dimension | Existing result | Present result |
|---|---|---|
| system class | | |
| information available | | |
| network/connectivity | | |
| design mechanism | | |
| convergence mode/rate | | |
| gain or initialization restriction | | |
| centralization/implementation | | |

Use only rows that materially change.  A novelty sentence must identify at
least one changed row and must not imply improvements in unchanged rows.

## 3. Preserve contribution isomorphism

When the contribution has `k` parts, create a private correspondence table:

| Contribution part | Obstacle | Mechanism | Formal result | Proof dependency | Evidence |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |

Use the same conceptual labels across Abstract, Introduction, section openings,
theorem discussion, example narration, and Conclusion.  Avoid synonymous
renaming that makes one part appear to be a new contribution.

## 4. Order by dependency

Prefer:

```text
definitions and assumptions
-> enabling lemma or estimator
-> component theorem
-> composition/main theorem
-> interpretation
-> application/evidence
```

Do not move a necessary lemma after the theorem merely to make section titles
look conventional.  If a technical proof is essential but interrupts the main
flow, state the result in place, explain its role, and move the calculation to
an Appendix.

## 5. Separate formal validity from interpretation

- Theorem/Lemma/Proposition: assumptions, object, guarantee.
- Proof: derivation and dependency use.
- Remark: meaning, comparison, scope, construction, rate, or limitation.
- Example: evidence for the stated property.

Do not use a Remark to repair an incomplete theorem statement.  Do not use a
theorem statement as a literature-review paragraph.

## 6. Whole-paper audit

Before delivery, check:

- every contribution part has a formal or analytical realization;
- every claimed advantage is supported by a theorem, derivation, or explicit
  design property;
- every nonstandard assumption has a visible function;
- every auxiliary result is invoked later or removed;
- the Conclusion does not introduce a new claim;
- notation and property names remain stable across modules.

