# Proofs and Remarks

## 1. Proof architecture

Use the smallest sequence that makes the implication auditable. The following
is a useful route for error-system proofs, not a compulsory recipe:

```text
define error/transformation/Lyapunov object
-> derive dynamics or inequality
-> split observable/stable/decaying components if needed
-> invoke the exact lemma under its assumptions
-> propagate the obtained property
-> state the claimed conclusion
```

Signal each real transition with an exact connector: `by Lemma ...`, `under
Assumption ...`, `hence`, `therefore`, or `which implies`.  Do not use a
connector when no implication has occurred.

Partition by the proof's actual obligations. A multi-part statement can be
closed part by part; a one-claim proof can still require several stages. Use
`First`, `Next`, or numbered steps only when the boundaries help. An equivalence
may use symmetry for one direction if the symmetry and preserved hypotheses
are specified; a lower-bound argument may need contradiction rather than an
error-dynamics narrative. Do not introduce a Lyapunov function mechanically.

For a cascade or perturbed error system, distinguish the homogeneous system's
property from the perturbation/forcing estimates. Establish the relevant
boundedness, decay, and lemma hypotheses before concluding convergence of the
actual error. Then return from transformed variables to every advertised
target. Closing parameter error alone does not close state/output error.

## 2. Dependency verification

For every invoked result, verify:

- its object matches the current transformed system;
- dimensions and time domain match;
- all hypotheses have been established;
- the conclusion is strong enough: asymptotic, exponential, uniform, global,
  or semiglobal are not interchangeable.

If the theorem follows from multiple earlier results, show the composition.
A short application can be enough when the object correspondence and all
hypotheses are already explicit. Do not reconstruct an entire cited proof or
expand a verified one-line application merely to appear rigorous.

Choose detail by the work the passage performs:

- an imported result: give accurate attribution and check its scope;
- a direct application: identify the current system and the relevant
  hypothesis correspondence, unless already unambiguous nearby;
- an adaptation: explain the changed setting and verify the affected steps;
- a substantive new argument or proof repair: show the step that the cited
  argument cannot supply; never conceal it behind `similar` or `standard`.

An Appendix pointer is legitimate only when it resolves to the actual proof.
Never fabricate an Appendix or claim to have checked an unavailable source.
Source-paper descriptions of a literature gap are attributions until verified
against the cited work; do not turn them into independent accusations.

## 3. Long derivations

Keep a long equation chain when it exposes causality.  Align it so each equality
or implication has a visible reason.  Split the display at logical transitions,
not arbitrary line lengths.

Move routine but lengthy algebra to an Appendix when the main text can state:

- what is proved there;
- why it is needed here;
- which equation/result it establishes.

Keep a decisive chain in the main text when it explains the contribution or
establishes the exact rate or domain. Before a display, identify the operation
or premise; afterwards, state what it establishes when that is not evident.
`Substituting ... gives ...` is grammatical without an added `we obtain`.
Do not require a commentary sentence after every equation. Dense algebra and
short functional transitions coexist in the corpus.

## 4. Prohibited shortcuts

Avoid `clearly`, `obviously`, `trivially`, or `straightforward` when they stand
in for:

- a missing bound;
- an unverified rank claim;
- a stability implication;
- an assumption use;
- a convergence-rate upgrade;
- an interchange of limits or sums.

The defect is an unsupported inference, not the mere presence of one of these
words. Prefer the calculation or precise reference when the word adds nothing;
do not invent an extra derivation to justify a routine transition. The corpus
contains such expressions, so do not label their presence alone a style error.
See [language-style.md](language-style.md) for conditional language choices.

## 5. Remarks

Give each Remark a coherent point, selected from these functions:

1. assumption interpretation;
2. exact comparison with a named result;
3. special case or counterpart;
4. design freedom or parameter selection;
5. convergence-rate, robustness, or implementation meaning;
6. proof-mechanism distinction;
7. precise limitation.

Anchor it to an identified assumption, construction, or result. It may explain
a construction before its theorem, compare an enabling lemma with a special
case, or interpret a result afterwards. A good Remark answers `What does this
object mean, change, or enable?`

One coherent point can combine a special case, a comparison, and its technical
reason. Do not split a connected explanation merely to enforce one category
per Remark. Conversely, separate unrelated discussion. Keep the principal
function as an analysis label and note secondary functions without counting
them as independent evidence.

For a comparison, preserve its named target, changed property, and conditions;
do not upgrade a particular comparison to `all existing methods`. For a rate
comment, distinguish a proved bound, a design-dependent estimate, and measured
transients. Do not infer arbitrary tunability or an exact rate from a bound.
An excluded case may be the point of a limitation Remark; do not remove it
solely to force positive framing. A scope-changing reduction described in a
Remark does not silently erase a theorem's original hypothesis.

Do not maximize the number of Remarks.  Merge adjacent comments when they have
the same function, and keep essential hypotheses in the theorem rather than a
Remark.

## 6. Proof review checklist

- Are all symbols defined before use?
- Does every equality preserve dimensions?
- Is every inequality justified?
- Is each assumption consumed or declared only for scope?
- Are boundedness and existence established before taking limits?
- Does the final sentence match the theorem's exact convergence property?
- Is any claim deferred to a reference that proves a weaker statement?

## 7. Source anchors and limits

The result/proof calibration examines selected passages in six papers, not all
proofs in the corpus. Publication years and PDF pages identify the examples:

- **2018 TAC, adaptive cooperative output regulation, pp5–6:** the main proof
  uses earlier rate estimates to control forcing and returns to the regulated
  output. Remark 9 separates offline design information from runtime use.
- **2022 Automatica, global exponential frequency estimation, pp3–4:** Lemma 1
  develops observability and finite-window contraction; Theorem 2 reuses that
  result, controls the decaying forcing, then closes output error by an identity.
- **2023 TAC, discrete-time distributed state estimation, pp3–4:** Lemma 4
  matches three hypotheses of Lemma 1. Lemma 3 points to Appendix B. The main
  theorem separates observable and unobservable error components.
- **2024 TAC, uncertain linear leader observer, pp5–6:** Lemma 3 proves rank,
  filter excitation, then regressor excitation. Proposition 1 closes its two
  conclusions in order. Remark 5 discusses removing unexcited modes; the
  proposition still states the nonzero-mode condition.
- **2025 TAC, uncertain discrete-time leader observer, pp3–5:** the attributed
  Proposition 1 has no separate proof there; Theorem 1 has a full two-part
  proof, identifying the system for an Appendix lemma at each use.
- **2025 TAC, uniform observability w.r.t. subspaces, pp3–5:** Lemma 3 reduces
  an equivalence to one direction and develops a contradiction argument.
  Remark 5 explains why the authors supplied a self-contained proof. Theorem 1
  proceeds from nonincrease to a finite-window estimate before claiming
  exponential convergence; nonincrease alone is not used as the rate argument.

These observations justify conditional choices, not universal proof lengths
or personally distinctive habits. Correctness checks constrain imitation;
they are not additional author-style evidence.
