# Verification Checklist — The Core Discipline

This is the file that makes the writing rigorous. The goal is zero errors. A
checklist cannot make a wrong derivation right, but it can make sure no step
goes unchecked. Run every applicable item below **before** showing a
derivation, citation, or assumption to the user. Apply it to the claims the
requested passage actually makes; it does not expand a passage request into a
whole-paper audit. Do not treat any item as
optional because the claim "looks obviously true" — the obvious-looking claims
are exactly the ones that slip through.

---

## 1. Algebraic and numerical claims

**Verify every nontrivial algebraic identity numerically before asserting it.**

- When a derivation produces an equality, inequality bound, eigenvalue claim,
  matrix identity, rank condition, or norm estimate, check it with a quick
  numerical script (random or structured instances) before writing it down.
- For a claimed matrix decomposition (observability/Kalman decomposition,
  similarity transform, block-diagonalization), construct the matrices
  numerically and confirm the claimed structure holds (correct zero blocks,
  correct spectrum, observability of the claimed observable pair, dimension of
  the unobservable subspace).
- For a worked numerical example, recompute every stated quantity (eigenvalues,
  gains, observability ranks, partition coverage) from the actual matrices.
  Confirm the example satisfies every assumption it is supposed to illustrate.
- If a bound is claimed to scale a certain way (e.g. $O(1/\gamma)$), check the
  scaling numerically across several values, not just one.

**Never write a number, gain, eigenvalue, or coefficient from memory or
expectation. Compute it.**

When the algebra and a clean closed form disagree, the algebra wins — chase the
discrepancy rather than rounding it away.

---

## 2. Citations and the literature

**Confirm every citation against the actual source. Use Zotero (the MCP tools)
to check.**

For each `\cite{...}`:

- **The paper exists and the cite key resolves.** Look it up. Do not rely on a
  remembered key spelling — keys are case-sensitive and easy to mistype. A
  typo'd key (e.g. an author surname swapped) silently points at nothing or at
  the wrong entry.
- **The content matches the claim.** If the text says "[cite] relaxes the
  neutral stability assumption" or "[cite] uses a constant gain," read enough of
  the source (abstract, the relevant lemma/assumption) to confirm it actually
  does that. Mis-describing a cited paper — claiming it proves something it does
  not, or assumes something it does not — is caught here and only here.
- **The assumption matches the cited assumption.** When citing a paper as the
  precedent for an assumption, verify the cited paper assumes the *same* thing,
  not a stronger or weaker cousin. (E.g. "neutrally stable / semisimple with
  zero real parts" is not the same as "all eigenvalues simple with zero real
  parts"; an exosystem condition on the leader matrix is not the same as a
  condition on the observed plant matrix.) State the precedent only for what it
  actually establishes.
- **The bibitem and the body agree on the key.** If the body uses one spelling
  and the bibliography defines another, fix one so they match — usually the body
  `\cite` is what's wrong; the bibitem key is what the reference list commits
  to. After any rename, search the whole document for the old key.

**Never invent an attribution, a venue, a volume/page, or a result.** If a fact
about the literature cannot be confirmed, leave it out rather than guess.

**Unpublished / concurrent submissions.** When citing the authors' own
preliminary or concurrent work, state its status plainly (e.g. "submitted to
[venue]"). Do not let a remembered description of an unpublished paper stand in
for checking what that paper actually contains.

---

## 3. Assumption–proof matching

For every assumption stated in the paper:

- **Is it actually used?** Trace where each hypothesis enters the proofs. An
  assumption the proof never uses should be removed or its necessity questioned.
- **Is its strength exactly right?** Check both directions:
  - *Too strong:* does the proof only use a weaker property than the assumption
    states? (E.g. the proof needs eigenvalues *semisimple* on the imaginary
    axis, but the assumption demands them *simple* — the assumption is narrower
    than necessary and excludes legitimate cases, such as repeated frequencies
    from structural symmetry.) Weaken the assumption to what the proof uses.
  - *Too weak:* does the proof secretly need more than the assumption provides?
    (E.g. the stated assumption is "neutrally stable," which permits decaying
    modes, but the argument relies on "$A$ similar to skew-symmetric," which
    forbids them — a gap.) Either strengthen the assumption or restrict the
    claim.
- **Is the remark consistent with the assumption?** If a remark restates or
  names the assumption (e.g. calls it "neutral stability" and then says "hence
  similar to skew-symmetric"), confirm the implication actually holds. Insert
  the missing qualifier ("for a real matrix") or the equivalence step rather
  than letting two non-equivalent descriptions sit side by side.

**Definitions before first use.** Any symbol used in a lemma or theorem (a
constant like $\bar\chi$, a bound, a set) must be defined before it appears, and
defined as a *consequence* of an existing assumption if that is what it is —
not silently postulated.

---

## 4. Dimensions, indices, and structure

- **Dimension check.** Every matrix product, Kronecker product, stacked vector,
  and block matrix must conform. Verify row/column counts at each step,
  especially after $\otimes$, `col`, and `blockdiag`.
- **Index coverage.** When a state is partitioned into sub-states, confirm the
  pieces cover the whole (e.g. $\sum_j E_{ij}^T E_{ij} = I_n$) and that every
  index range is consistent across the definition, the sum, and the stacked
  form.
- **Left/right and transpose.** Check left- vs. right-multiplication and
  transpose placement in every identity — a swapped $E_{ij}$ vs. $E_{ij}^T$ or a
  multiply-on-the-wrong-side breaks the derivation silently.
- **Subscript discipline across the paper.** The same object must carry the same
  subscripts everywhere. A symbol that switches index conventions between
  sections is a real inconsistency, not a typo.

---

## 5. Internal consistency across the document

- **Lemma statement vs. its proof/appendix.** If a lemma is stated in one form
  (e.g. a pointwise bound $\gamma(t)\|d(t)\| \le K_0 + K_1\sup\|e\| + r(t)$ with
  $r(t)\to 0$) the appendix that proves it must deliver *that* form, not an
  earlier variant. When a statement is revised, revise its proof to match.
- **Abstract vs. body.** Terminology, claims, and the headline result in the
  abstract must match the body exactly. If the body changed (e.g. from ultimate
  bound to exact convergence, or from constant to time-varying gain), the
  abstract must change with it.
- **Conclusion vs. body.** The conclusion must not restate stale numbers,
  superseded examples, or a weaker result than the body now proves.
- **Cross-references resolve.** Every `\ref`/`\eqref` points at the right label;
  no renamed section/equation is left dangling.

---

## How to run this checklist

When a piece of writing involves math, do not present it until:

1. its algebra is numerically verified (§1),
2. its citations are Zotero-confirmed and correctly described (§2),
3. its assumptions are matched to the proof in strength and use (§3),
4. its dimensions/indices conform (§4),
5. it is consistent with the rest of the document (§5).

If any item cannot be satisfied — a value won't verify, a citation won't
confirm, an assumption doesn't match — surface it to the user as an open
question rather than papering over it. Flagging a real gap is the rigorous move;
smoothing it over is the failure mode this skill exists to prevent.
