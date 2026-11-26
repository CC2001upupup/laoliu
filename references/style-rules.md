# Style Rules — Terse, Verb-Driven Journal Prose

The target is the house style of Liu Tao, suited to IEEE TAC and Automatica:
terse, verb-driven, no wasted words, complexity pushed into proofs. The reader
meets each result cleanly and only then meets its machinery.

---

## Prose

- **Terse and verb-driven.** Short declarative sentences. Cut hedging and
  filler. Prefer a verb to a nominalization ("we bound $d$" over "we provide a
  bound on $d$" where it reads naturally).
- **Roadmaps by function.** A section-opening or paper-level roadmap is
  allowed when it exposes a real multi-stage dependency; omit it when the
  architecture is already obvious. Avoid rhetorical questions.
- **Preferred transitions**, used sparingly and precisely: *To begin with /
  Next / Now / Then / Thus / Therefore / Hence / Moreover / In particular /
  Specifically / As a result.* These carry the logical flow; do not pile them up.
- **Plain, simple words — this is a primary rule, not a preference.** Use the
  simplest word that is still precise. When a common word and an exotic word mean
  the same thing, choose the common one. Ornate vocabulary does not make a paper
  look more sophisticated; it makes it harder to read and signals insecurity.
  Clarity is the sophistication.
  - Prefer the everyday word: "use" over "utilize", "show" over "demonstrate"
    when the plain verb fits, "near" over "in the vicinity of", "remove" over a
    fancier synonym, a plain noun over a Latinate one when both are exact.
  - If a reader of the paper would have to stop and wonder what a word means, it
    is the wrong word — replace it, unless it is a genuine technical term with no
    plain equivalent.
  - Never coin a technical name, compound label, or acronym, even for a
    recurring quantity (user constraint; see SKILL.md and
    language-style.md). Refer to the object by its symbol or equation, or
    describe the operation in an ordinary clause.
  - Technical precision still wins: never trade an exact term for a vague one to
    sound simpler. The rule is *simplest word that is still correct*, not
    *simplest word*. Keep exact terms such as "semisimple" or "simple" as
    supplied; do not dress up "grows" as "exhibits unbounded growth".
  - Self-check: on rereading, if any word feels chosen to impress rather than to
    communicate, swap it for the plain one.

## The connector rule (critical)

A display equation must be governed by a grammatical predicate. A bare
connector phrase **never emits a display formula directly**: "By Lemma 1," /
"Taking norms," / "Integrating," / "Letting $t\to\infty$," must be followed
by a finite verb such as "we have" / "we obtain" / "it follows that" — or the
`-ing` clause must itself be the subject of a finite verb, as in
"Substituting (5) into (4) gives".

- Wrong: `Taking norms, \begin{equation} ... \end{equation}`
- Right: `Taking norms, we obtain \begin{equation} ... \end{equation}`
- Also right: `Substituting (5) gives \begin{equation} ... \end{equation}`

The fixed words "we have" are not required; the predicate is. This applies
every time, including inside proofs and appendices.

## Parentheses

**No parenthetical explanatory asides.** Supplementary content is rephrased as a
separate clause or sentence, or folded grammatically into the sentence —
not dropped into parentheses.

- Acceptable in parentheses: equation/assumption labels woven into grammar
  (e.g. "condition (i)", "by (14)"), and citation cross-references.
- Not acceptable: an explanatory remark in parentheses. Rewrite it as a clause.

## Display equations

- **No trailing comma on a display equation.** End the displayed line with no
  punctuation. (A following period is used only if the next text begins a new
  capitalized sentence and the grammar genuinely requires it; the default is no
  trailing punctuation.) This rule overrides any reviewer suggestion to "add
  commas to aligned rows."
- Keep aligned blocks clean; break long derivations across lines so each line is
  readable, but never insert trailing commas to do it.

## Theorem / lemma / proof structure

- **Keep statements lean, but complete.** Theorem and lemma statements should
  be readable without the apparatus. Move proof-only constructions and
  intermediate constants into the proof or an appendix. Keep effective
  validity conditions — an admissible gain range, an initial-state exclusion,
  an invariant-subspace restriction — visible in the statement or in an
  explicitly referenced construction; they are not disposable machinery.
- **Name a result by what it does, not by its machinery.** Prefer "there exists
  $g>0$ such that ... solves Problem 1" in the statement, with any internal
  threshold constructed inside the proof.
- **Proof step formatting.** For a multi-step proof, label steps with a
  consistent format and visual separation, e.g. `\medskip` then
  `\noindent\emph{Step k: short title.}`. Keep the steps parallel in form.
- **Proof endings.** End proofs with the project's chosen symbol
  (`\hfill $\blacksquare$`, or `$\Box$` if the proof environment supplies it).
  Be consistent within the paper.
- **Well-posedness up front when relevant.** For a linear time-varying system,
  open the proof by noting the solution is well defined and bounded on every
  compact interval, so later boundedness on an initial interval is automatic.

## Remarks

- **Say what the assumption does.** A remark on an assumption should state
  what the hypothesis *enables* (what it lets the proof conclude). An excluded
  case may be the point of a limitation remark; do not remove it solely to
  force positive framing. Describe a design parameter as a design choice and
  the assumption as the class of admissible designs.
- **One coherent point per remark.** A special case, its comparison, and the
  technical reason may share a remark when they form one connected
  explanation; separate unrelated discussion. See proofs-remarks.md.
- **Necessity claims stay conditional.** If a property is only needed under a
  side condition, state the necessity conditionally, not as an unconditional
  claim.

## Citing textbooks

- Prefer a specific section to a whole textbook (`\cite[Section 9.6]{Khalil2002}`
  rather than `\cite{Khalil2002}`), or no citation at all if the step is
  self-contained. Avoid citing an entire book for a standard fact.

## On framing contributions (introductions)

- When the paper extends the authors' own prior work, state the prior work's
  setting and limitation plainly, then state what the present paper removes or
  upgrades. Make clear that the extension is not mere retuning when it is not —
  name the new analysis it requires.
- Do not rely on a near-duplicate of a prior abstract; rewrite sentence
  structure so the new abstract is genuinely distinct, even when the result is
  related.
