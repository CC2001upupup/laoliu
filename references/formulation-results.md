# Formulation, Preliminaries, and Main Results

## 1. Problem Formulation / Problem Description

Organize by dependency, not a compulsory six-step section template. Establish
the model, available information, unknown quantities, designed object, and
target property wherever each becomes necessary. Reuse an already introduced
model by equation reference rather than restating it for a conventional opening.

For a network problem, connect graph edges to actual measurement or message
access before constraining a distributed law. For a single-signal estimation
problem, omit graph and agent machinery. Do not add an admissible-law formula
when the input specifies only the estimation target.

Two supported arrangements are:

- model -> measurements/network -> admissible design and objective ->
  assumptions and interpretation;
- objective referring to an existing model -> relevant assumptions and
  information constraints -> optional preview of the design stages.

Place assumptions before the objective if it needs them for interpretation,
after it if they state conditions for solvability, or at the first design stage
that consumes them. Keep essential hypotheses visible in the relevant formal
result. Define symbols near first use; do not invent technical names.

Keep four aspects of the target distinct: what is to be estimated/regulated;
from which information; for which initial conditions, parameters, and agents;
and with what convergence or boundedness property. A compact formulation may
use `Given ... , design ... such that, for ... , ...`. This is a functional
pattern, not wording to copy or a reason to add a missing guarantee.

If the advertised target is recovered through an estimated surrogate
parameter, state that recovery relation explicitly and avoid claiming a
convergence property that has not been established for the advertised target.

## 2. Decide whether to use a formal Problem environment

Consider a formal problem statement when the task needs a precise combination of:

- given data;
- designed object;
- admissible information pattern;
- quantification over initial conditions or uncertainty;
- convergence/stability/regulation objective.

For a direct construction with an obvious target, a prose formulation may be
clearer. Mathematical explicitness is required; `Problem 1` is not. A complex
problem can also be expressed in prose if its conditions and target remain
unambiguous. Preserve an appropriate existing heading or environment.

## 3. Assumptions as contracts

When needed to resolve an ambiguity, silently identify:

```text
object constrained:
property imposed:
result/proof step that consumes it:
whether standard, relaxed, or restrictive:
```

Do not require a user worksheet or move all assumptions merely to match a
template. Never strengthen or weaken one for tone. In particular, preserve
`simple` versus `semisimple`, discrete-time versus continuous-time spectral
conditions, aggregate versus local observability, compact-set restrictions,
and conditional boundedness. State-estimation and leader-observer information
patterns are not interchangeable. Treat an exposition-specific coordinate
reduction separately from the original problem class.

Use a Remark when the supplied reasoning explains:

- why it gives well-posedness, observability, stability, PE, or connectivity;
- how it compares with the closest result;
- which common system class satisfies it;
- an established limitation or supported relaxation, not a guessed extension.

Do not claim an assumption is mild or standard without a technical basis.

### Source anchors and variation

The six-paper calibration below uses PDF page numbers and publication years;
the writing-time proxies remain the basis for recency weighting. It identifies
usable variants, not their prevalence across all 14 papers.

- **2018 TAC, adaptive cooperative output regulation, p2:** a `Definition 1`
  states the problem before assumptions. Boundedness is conditional on a
  bounded leader signal; asymptotic regulation must not become exponential.
- **2019 Automatica, cooperative robust output regulation, pp2–3:** `Problem 1`
  precedes assumptions and retains compact-set quantifiers. Further assumptions
  are introduced with the distributed-observer stage, not all at the beginning.
- **2022 Automatica, global exponential frequency estimation, pp1–2:** the
  signal model is introduced in `Review of the existing result`. There is no
  graph or formal problem label. The reviewed theorem's restrictions belong
  to the earlier result, not automatically to the proposed design.
- **2023 TAC, discrete-time distributed state estimation, p2; 2024 Automatica,
  continuous-time counterpart, pp2–3:** model, local measurements, graph, then
  `Problem 1`, then assumptions. Their similar layout does not authorize
  copying spectral conditions across time domains. These are related studies,
  not two independent votes for a rule.
- **2025 TAC, uncertain discrete-time leader observer, pp2–3:** prose objective
  references the earlier system; assumptions and their interpretation follow.
  A further observability assumption appears at the first Main Results stage.
  No `Problem 1` label is needed. Its `simple` nonreal unit-modulus eigenvalues
  must not be rewritten as merely `semisimple`.

Use recent examples as default candidates and earlier examples to preserve
scope and reveal alternatives. Relevance to the user's problem outranks a
surface match to the newest paper.

## 4. Technical lemmas and preliminaries

Create an enabling section when the main result depends on a coherent layer of
graph, stability, observability, filtering, or decomposition results.  Begin by
stating its role.

For an imported result, distinguish:

- direct quotation/application;
- discrete/continuous-time counterpart;
- extension to a new graph/system class;
- strengthened convergence property;
- corrected or self-contained proof.

Do not restate an existing lemma as if it were new.

## 5. Main Results

For a multi-stage design, expose the dependency where the next stage begins:

```text
The design has two stages.  The first constructs [...].  The second uses that
object to [...].
```

Do not force every result section into construction -> theorem -> proof ->
Remark. Select the arrangement that makes the current dependency clear:

- **Construction-led:** define the design and parameters, establish its
  enabling properties, then state the guarantee. A design-motivation or
  comparison Remark may precede the theorem.
- **Lemma-led:** establish the decomposition or stability tools first, then
  give the design that uses them. Do not move all enabling mathematics into
  the main theorem's proof just to shorten the section opening.
- **Composition-led:** state the first component's guarantee, explain what
  that component supplies to the next construction, and state the combined
  result. A two-stage design need not have exactly two theorems.
- **Concept-led:** define the relevant property and its invariance conditions,
  establish a transfer result, then give the convergence result or application.
  Do not force an estimator/controller narrative onto a conceptual paper.

These are editorial descriptions of observed arrangements, not new technical
names to put in the manuscript. Use only the minimum transition needed; a
one-stage result does not need a two-stage roadmap.

### Theorem statement

Include only what defines formal validity:

- assumptions/conditions;
- system and designed object;
- parameter range if essential;
- guarantee and convergence mode;
- scope over agents, initial conditions, or uncertainty.

Do not repeat the Introduction's motivation inside the theorem.
Keep effective design conditions visible in the statement or an unambiguous
reference to the preceding construction. A gain range, initial-state exclusion,
or invariant-subspace restriction is not disposable proof machinery. Keep
proof-only intermediate constants in the proof. Preserve an explicit
admissible range instead of replacing it with a vague existence claim for tone.

When a result is imported, adapted, or composed from previous results, state
that provenance at its introduction. Do not add a proof solely because another
paper has one, or omit a needed argument solely because the source says
`based on`. Read [proofs-remarks.md](proofs-remarks.md) for proof detail and
closure choices. A title such as Lemma or Proposition does not alone establish
novelty or whether a proof may be omitted.

### Section-opening roadmap

A local roadmap is useful when a result section contains a non-obvious
multi-stage construction.  It must expose the dependency.  Do not ban it merely
because the Introduction already contains a paper-level roadmap.

### Result-section source anchors

Publication years and PDF pages below identify passages, not writing-time
weights. These six-paper examples supplement the formulation calibration.

- **2018 TAC, adaptive cooperative output regulation, pp5–6:** Lemma 3
  supplies an iterative solution before the control law and Theorem 1.
  The theorem retains distinct gain cases; its proof uses the earlier rate
  result before returning to the regulated output.
- **2022 Automatica, global exponential frequency estimation, pp2–4:** the
  modified law is followed by motivation/comparison Remarks, a stability
  lemma, and Theorem 2. Interpretation is not confined to a final Remark block.
- **2023 TAC, discrete-time distributed state estimation, pp3–4:** decomposition
  and stability lemmas precede the local observer. Remarks 4–5 explain the
  design before Theorem 1, whose construction is specified by reference.
- **2024 TAC, uncertain linear leader observer, pp5–6:** filter identities,
  a decaying error relation, the estimator, PE, and Proposition 1 form a
  dependency chain. The known-parameter corollary bypasses adaptation rather
  than merely repeating the proposition.
- **2025 TAC, uncertain discrete-time leader observer, pp3–5:** Proposition 1
  is explicitly based on an earlier theorem; Remark 4 connects its guarantee
  to the second construction. Theorem 1 proves the composed result.
- **2025 TAC, uniform observability w.r.t. subspaces, pp3–5:** an invariance
  lemma leads to a switched-system result, not a two-estimator construction.
  Theorem 1 restricts initial states to the invariant subspace. Remark 6
  extracts a rate lower bound from the proof, not an exact observed rate.
