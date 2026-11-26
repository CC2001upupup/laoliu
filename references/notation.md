# Notation Conventions

Notation choices, like terminology, are held consistent across the whole
document. The same object carries the same symbol and the same subscripts
everywhere.

---

## Indexing a family of quantities

**Use expanded index form, not set-builder notation, when listing a family
inline.**

- Right: `$x_{ij}$, $j=1,\ldots,k_i$,` — with a comma before and after the range
  when it sits as an inserted qualifier, e.g. "the sub-states $x_{ij}$,
  $j=1,\ldots,k_i$, form a complete decomposition ...".
- Avoid: `$\{x_{ij}\}_{j=1}^{k_i}$` for an inline family. The compact
  set-builder form reads as pure-math/functional-analysis style and clashes with
  the surrounding convention.
- Summations `$\sum_{j=1}^{k_i}$`, stacked vectors
  `$\operatorname{col}(w_{i1},\ldots,w_{ik_i})$`, and `blockdiag` expansions are
  fine as-is — they are already in the expanded-listing spirit and are
  consistent with the rule.

When in doubt, sweep the document for compact set-builder families
(`\{...\}_{...}^{...}`) used as inline lists and convert them to the
"$\cdots$, $j=1,\ldots,k_i$" form.

## Zero

- **Plain `0`** for a zero vector or matrix of appropriate dimension — not
  `\mathbf{0}`. (Follow whatever the document's notation paragraph declares, but
  the default here is plain `0`.)

## Spacing in displays

- **`\quad`, not `\qquad`,** to separate an equation from its qualifier or two
  parts of a display. Keep horizontal spacing modest and uniform.

## Graph symbols (when the paper has a double-layered / switching structure)

Keep the layers visually distinct and consistent:

- **Intra-cluster graphs:** `\mathbb G_i` (blackboard) — together with its vertex
  and edge sets in the same family.
- **Inter-cluster switching modes:** `\mathcal G_p` (calligraphic, plain
  subscript) — *not* a parenthesized subscript `\mathcal G_{(p)}`.
- **Active inter-cluster graph under the switching signal:** `\mathcal G_{\sigma(t)}`.

Apply the chosen convention in every location: notation paragraph, problem
formulation, assumptions, observer design, and appendices. A whole-document
find-replace is the right tool when the convention is fixed or changed.

## Equation labels

- **Hyphenated, descriptive labels:** `\label{eq-thm-rate}`,
  `\label{eq-error-def}`, `\label{eq-d-weighted-bound}`. Use a consistent prefix
  scheme (`eq-`, `sec-`, `lem-`, `thm-`, `ass-`, `rem-`, `app-`).
- After renaming a label, search the document for every `\ref`/`\eqref` to it.

## Environment names

- Use the project's environment-name capitalization consistently
  (e.g. `\begin{Assumption}`, `\begin{Lemma}`, `\begin{Theorem}`,
  `\begin{Remark}`, `\begin{Proof}`). Pick one casing and never mix.
- Appendices under `\appendices` (plural form) to keep titles displaying
  correctly when there is more than one.

## Typographic small rules

- Multi-letter subscripts that are abbreviations (e.g. a "c" for "common") use
  the upright form intended by the project (`T_{\mathrm{c}}` rather than
  `T_c` when "c" is a label, not an index). Be consistent.
- Do not switch between `\mathcal`, `\mathbb`, and plain for the same symbol
  across sections.
