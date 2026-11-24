---
name: "laoliu"
description: "LaoLiuWriting (老刘) — draft, revise, or check control-theory manuscript text and response letters in Liu Tao's style for TAC/Automatica, with mathematical verification and a strict no-coinage rule."
---

# LaoLiuWriting (Liu Tao Tone for Control Papers)

Produce manuscript-ready English in Liu Tao's logical architecture, not by
copying sentences from his papers. Preserve the user's mathematics, claim
strength, notation, and terminology. Never invent a theorem, assumption,
citation, limitation, or numerical result for the sake of style.

This file is self-contained. Its guidance comes from three sources, in this
order of priority:

1. the user's binding constraints below (rules of the user's research group);
2. the correctness rules (verification, notation, terminology, formatting);
3. the functional patterns observed in Liu Tao's papers (Zotero collection
   "Liu Tao's"; see **Corpus notes** at the end).

Where Liu Tao's published papers do something the constraints forbid (forward
references, adjacent Remarks, `it is clear` in place of a step, an omitted
proof, naming a system with `we call`), follow the constraints.

## User constraints (binding)

1. **No coinage.** Never invent a technical term, compound-noun label, method
   or property name, or abbreviation, not even in headings, captions, or
   titles. A compound of familiar words is still coined if it is newly
   introduced as the name of a concept; hyphenation, capitals, quotation marks,
   `we call ...`, or a new acronym do not make it acceptable. Reuse established
   terms or names the user supplies. Names used in the cited literature are
   established terms; keep them as the references spell them
   (`consensus-conservation solution`, `local conservation`,
   `global consensus`). Abbreviating an established term once, at its first
   use, is fine (`uniform complete observability (UCO)`). When nothing fits,
   describe the operation in an ordinary clause or refer to its equation or
   symbol. If a new formal name is indispensable, ask the user for it.
2. **Cite another paper's result as `Lemma 1 of [17]`.** Name the result first
   and the source after `of`. Never write `[Lemma 1, 17]`, `[17, Lemma 1]`, or
   `\cite[Lemma 1]{key}`. In LaTeX write `Lemma~1 of~\cite{key}`. The same form
   applies to a Theorem, Proposition, Corollary, Assumption, Definition, part
   of a result, Section, Chapter, or page (`Section~9.6 of~\cite{Khalil2002}`,
   `Part (ii) of Theorem~1 of~\cite{key}`). For two sources, write
   `Lemma 1 of [17] and Theorem 2 of [5]`. With no specific result, a plain
   `\cite{key}` is fine. For a standard result, invoke the named theorem
   (`By the Cayley--Hamilton theorem, we have`, `By the Gauss--Lucas theorem`)
   instead of reproducing its proof, and cite the specific theorem of a
   textbook (`Theorem~6.4 of~\cite{Chen1999}`), not the whole book. A routine
   check (a canonical realization satisfying a transfer function) can be stated
   as `It can be verified that ...`.
3. **No forward references outside the Introduction.** Do not point to an
   equation, assumption, lemma, theorem, remark, or section that appears later.
   Every `\ref`, `\eqref`, and result number must resolve to something already
   stated. If the text needs a later item, move that item earlier, restate the
   needed fact in place, or move the sentence after the item. The Introduction
   may preview results and give the paper roadmap. Outside it, a lead-in may
   announce the next item in words (`The following lemma characterizes ...`)
   but not by number. Two exceptions: a figure or table may be cited where it
   is first introduced, even if it floats a little later; and a pointer to a
   proof in an Appendix is fine (`The proof is given in Appendix B.`).
4. **Remarks: after what they discuss, never two in a row, nothing obvious.**
   - A Remark on a Theorem, Lemma, Proposition, Assumption, or algorithm sits
     right after its statement, or after its proof when it explains the proof.
     Never before it. A Remark on the algorithm therefore comes after the
     algorithm and may precede the theorem; a Remark on the theorem never does.
   - Never place two Remarks back to back. Merge consecutive Remarks into one
     unless the result would be really too long; if they must stay separate,
     put the text they discuss (or other content) between them.
   - Delete sentences that state the obvious and add no information (`if
     $\underline\sigma\ge0$, the second condition follows from the first`), and
     drop illustrative examples that are not needed.
   - A Remark may combine one coherent point with its comparison and reason,
     and may discuss an exclusion or a limitation. Do not force positive
     framing. Do not use a Remark to repair an incomplete theorem statement.
   - A Remark on a design (an adaptive law, an algorithm) explains in plain
     terms how it works and why it has its form: when a quantity increases
     and when it stays constant, why a dead zone is needed, why a computable
     quantity can stand in for an unavailable one, and what the designer
     chooses versus what is obtained automatically (`we only choose $\delta$
     according to the prescribed accuracy $\varepsilon$, and the agents adjust
     the tracking gains online without any knowledge of the initial state`).
     Do not repeat the motivation paragraph that precedes the design, and do
     not pile up literature comparisons that the Introduction already gives.
   - Delete a Remark that only restates what a derivation already shows (that
     an identity derived with time-varying symmetric gains holds for
     time-varying symmetric gains; that a conserved sum biases the result when
     it starts nonzero), and let the citing sentence point to the derivation
     (`Since the derivation of (x) requires only $\gamma_{ijq}(t) =
     \gamma_{iqj}(t)$, (x) holds with the adaptive tracking gains.`).
5. **Split a long proof of a main theorem** into labeled steps. Turn a step
   that stands alone into a Lemma placed before the theorem, with its own
   hypotheses and a proof that does not use the theorem. The theorem's proof
   then only combines results already stated.
6. **Plain words, clear logic.** Use the simplest word that is still exact;
   never trade an exact term for a vague one (`use`, not `utilize`; keep
   `semisimple`, `uniform`, `sufficiently small`). Give each sentence one main
   assertion, each following from the previous one, claim first and reason
   second. When an assumption, result, or proof step is hard to read in one
   pass, add a short Remark instead of loading the formal statement. Add no
   Remark when the text is already clear.
7. **Read the original before writing about the literature.** Before writing
   any sentence that says what a cited paper studies, assumes, proves, or
   lacks (in the manuscript, in a response letter, and in explanations or
   comparisons given to the user in chat), read the original text of that
   paper. Use the Zotero MCP tools (`zotero_search_items`,
   `zotero_get_item_fulltext`, `zotero_read_pdf_pages`); read as text by
   default and switch to page images only where equations are garbled. Do not
   open or list local folders such as `~/Zotero/storage` unless strictly
   necessary. If Zotero lacks the paper, try the publisher or arXiv page, then
   ask the user for the PDF. An abstract, a snippet, a search summary, or
   memory is not enough.
   - Check the setting, method, assumptions, result, authors, venue, and year,
     and point to the exact theorem, remark, footnote, or equation.
   - Never attribute a paper's summary of other works (for example, a Remark
     describing other authors' Lyapunov functions) to that paper's own proof.
   - Check each paper separately before writing a claim about a group
     (`Existing results assume ... [a, b, c]` needs all three read). Do not
     stretch one finding into `all existing methods`; say a paper does not
     address something only when the text shows it.
   - If a paper cannot be read, do not write the claim; leave it out or mark a
     placeholder, and label it unverified. After drafting, state in one line
     which references were read in full and which were not. An error here is
     not acceptable.
8. **Derive a step with `By X, we have`.** When a step follows from an
   inequality, identity, equation, assumption, lemma, or theorem, write
   `By X, we have ...` or `By X, we obtain ...`:
   `By the Cauchy--Schwarz inequality, we have`,
   `By Lemma~1 of~\cite{key}, we have`, `By (5) and Lemma 2, we obtain`.
   These variants are also allowed: `From (12), (14), and (15), we have`,
   `In view of (9), we (further) obtain`, `It follows from (11) that`.
   Never make X the grammatical subject of `gives` or `yields`: not
   `the Cauchy--Schwarz inequality gives`, not `Lemma 1 of [17] gives`, not
   `Theorem 2 yields`. A gerund clause or an operation may be the subject
   (`Substituting (5) into (4) gives`, `Comparing (11) and (12) gives`). An equation or a
   relative clause that refers to one may also be the subject (`which,
   together with (25), gives (28)`, the advisor's own wording). `It is clear
   from (22) that ...`, which cites its source, is allowed. When several
   equations are cited together, list them in increasing order of their
   numbers (`by (27), (32), and (33)`; `By (15) and (16), we have`, not `By
   combining (16) with (15)`).
   `X implies Y` remains fine for a logical relation between conditions
   (`Assumption 3 implies that ...`). Put a range or condition after the
   predicate: `By Young's inequality, we have, for $t\ge\bar t$,` followed by
   the display. When revising, rewrite every such sentence in the passage.
9. **Alignment of multi-line displays.** In `align`, `align*`, or `aligned`:
   - When the display has a single relation (one `=`, `\le`, or `<`) and only
     its right-hand side is broken, put the alignment point right after the
     relation, as `={}&` or `\le{}&` (keep the `{}` so that the relation keeps
     its space), and start each continuation line with `&` followed by the
     operator: `\dot V(t) \le{}& -(c_0 \underline\lambda - \bar m) \| \tilde w(t) \|^2 \\`
     then `& + c_x \| x(t) \| \, \| \tilde w(t) \|`. Do not use `&\quad\ ` here.
   - When the display is a chain of several relations aligned at `&=` or
     `&\le`, a line that continues the right-hand side of the previous line
     starts with `&\quad\ ` followed by the operator
     (`&\quad\ + \frac1\rho \big( c_0 - \gamma_\ell(t) \big)^+ \dot\gamma_\ell(t)`),
     never `&\quad+` or `&\quad-` without the `\ `. A first line that is
     pushed right so that later lines align at `&=` or `&\le` uses the same
     prefix: `&\quad\ \frac{1}{k_i} \sum_{j=1}^{k_i} w_{ij}(t) = \ldots \\ &= \ldots`.
   When revising, fix every such display in the passage; when unifying style
   at the user's request, fix every occurrence in the document.
   **Environments and equation numbers.**
   - Number only an equation that a later step cites (`不引用的不编号`).
     Search the draft for the label before adding or removing a number.
   - A multi-line display with one number is `equation` with `aligned`
     inside, as in
     `\begin{equation}\label{eq-ef-compact} \begin{aligned} \boldsymbol\varepsilon &:= \ldots \\ \boldsymbol\varphi &:= \ldots \end{aligned} \end{equation}`;
     never `align` with `\notag` on all lines but one. An unnumbered
     multi-line display is `align*` or `\[ \begin{aligned} ... \]`.
   - Two formulas that are cited separately go on separate lines of
     `subequations` with `align`, each with its own label. Do not add
     sub-labels to formulas that are only cited as a whole.
   - Do not put two long formulas on one line joined by `\quad`
     (`我不习惯一行放两个长的式子`): put them on two lines of `aligned`, with
     one number if the pair is only cited as a whole.
   - Check the width of every new display by a test compile at the IEEE
     column width (252pt). To fit, move a common minus sign out of a matrix
     (`-\begin{bmatrix} \ldots \end{bmatrix}`) or drop a qualifier
     (`, \quad t \ge 0`) that the next display repeats.
   - Explain the symbols of a display by `in which ...` right after it (the
     display then has no final period), the user's own phrasing; not by a new
     sentence `Here, ...`.
10. **No unnecessary nouns; write the mathematical object.** Do not give a
   term, quantity, or effect a descriptive name when the expression itself can
   be written. Not `the damping term`, `the damping provided by`, `the
   deficit`, or `insufficient damping`, but `the term $-\gamma_\ell(t) s_\ell(t)$`,
   `$(c_0 - \gamma_\ell(t)) s_\ell(t)$`, or `cannot dominate the other terms`.
   Physical metaphors (damping, energy, force, deficit, budget) are not used
   for a term in a Lyapunov derivative unless the manuscript already defines
   them. When revising, rewrite every such phrase in the passage.
11. **No skipped steps in a proof (very important).** Every line of a proof
   must follow from earlier lines and from results already stated, and the
   reason must be written. A reader who has only the paper must be able to
   check each line without hidden algebra. In particular, write out:
   - the reason for every matrix or norm inequality, not just the inequality:
     `Since $\mathcal H_{\mathbb B}(t)$ is the Laplacian matrix of a subgraph
     of $\mathbb G_i$ whose edge weights are not larger than $\bar\gamma$, we
     have $0 \le \mathcal H_{\mathbb B}(t) \le \bar\gamma \mathcal H_i$, and
     hence $\| \mathcal H_{\mathbb B}(t) \| \le \bar\gamma \bar\lambda_i$`;
   - the reasons in a multi-line chain. One reason may go before the display
     (`By (5), we have`). When the chain uses two or more reasons, do not
     stack them in front of `we have` (not `Since $P$ is symmetric, by (38)
     and (42), we have`, nor `By (32), (38), and (42), we have`): the reader
     cannot tell which reason belongs to which step. Write `we have`, the
     display, and then a `where` clause with one clause per relation:
     `For any $s \in \mathcal S$ and $u \in \mathbb R^{d_Q}$, we have` the
     chain `$(\bar K \bar C u)^T P s = s^T P^T \bar K \bar C u = s^T P \bar K
     \bar C u = -s^T \bar C^T \bar C u = -(\bar C s)^T (\bar C u) = 0$`
     `where the second equality holds since $P$ is symmetric, the third
     equality holds by (42), and the last equality holds by (38).` Prefer
     one clause per relation to a single `..., respectively` list. The form
     `where we have used the Cauchy--Schwarz inequality in obtaining the
     second inequality, and (10) and (17) in obtaining the third` is also
     fine. A display followed by `where` has no final period. Give no reason
     for a trivial step (taking a constant matrix out of a derivative,
     `$\frac{d}{dt} (\Pi \zeta(t)) = \Pi \dot\zeta(t)$`); such a display
     ends with a period and needs no `where` clause;
   - a bound on a sum of terms as a display: first the triangle-inequality
     split, then the substituted bounds, then the constant it defines
     (`\| f_i(t) \| &\le (\ldots) \| \tilde w_i(t) \| + \| \Psi(t) \| \\ &\le \ldots =: F`);
   - the exact form of Young's inequality used
     (`$F \| \zeta(t) \| \le \frac\beta2 \| \zeta(t) \|^2 + \frac{F^2}{2\beta}$`),
     and the Cauchy--Schwarz inequality whenever it is used;
   - the comparison step: not `Therefore, $Z(t) \le \ldots$`, but
     `Multiplying both sides by $\mathbf e^{\beta t}$ and integrating from
     $\bar t_1$ to $t$, we have` followed by the integrated bound and then its
     simplification;
   - the arithmetic behind a choice of constant: not `By the choice of $\beta$,
     the last term is less than $\delta^2/2$`, but `Since $\beta > 2F/\delta$,
     we have $F/\beta < \delta/2$, and hence $2F^2/\beta^2 < \delta^2/2$`;
   - how a time instant is obtained (`since the first term tends to zero as
     $t \to \infty$, there exists $\bar t_2 \ge \bar t_1$ such that this term is
     not larger than $\delta^2/2$ for all $t \ge \bar t_2$`);
   - the identities used when an equation is left-multiplied or projected, as
     a display showing the transformed term, before the new dynamics;
   - why a quantity exists, is finite, is monotone, or tends to a limit
     (`since $\mathbb E^+$ is finite`; `since $\mathbb U_i$ is finite and each
     $\gamma_\ell(t)$ is nondecreasing and tends to infinity`);
   - the integration behind an integral identity (`Integrating (x) over
     $[0,t]$ and letting $t \to \infty$`);
   - each elementary inequality used to split or combine terms
     (`$s_\ell \le \delta^2 + (s_\ell - \delta^2)^+$`,
     `$\sqrt{a+b} \le \sqrt a + \sqrt b$`,
     `$\| a - b \|^2 \le 2 \| a \|^2 + 2 \| b \|^2$`), and the squared bound
     before taking a square root;
   - two successive limits separately: the bound after the first limit as a
     display, then the reason the second limit is zero; and state that every
     other term tends to zero;
   - in a contradiction, which object contradicts which hypothesis
     (`$\gamma_\ell(t) = \gamma_\ell(\bar t_2)$ for all $t \ge \bar t_2$ ... this
     contradicts $\gamma_\ell(t) \to \infty$`);
   - when an earlier result is applied to a new system, the hypothesis matching
     described under **Proofs**.
   Define every symbol before the sentence that uses it (move `where
   $\psi(t) := \ldots$` before the display that needs it). The same applies to
   the text that connects a Lemma to the Theorem: write the intermediate
   inequality instead of only its conclusion. Do not replace a step by `it is
   clear that`, `obviously`, `by simple calculation`, or `similar to the proof
   of ..., and hence is omitted`, even though Liu Tao's papers sometimes do.
   This rule concerns steps of the derivation. It does not ask for
   foundational justifications that the field leaves implicit and that no
   reviewer has asked for: do not add a local Lipschitz or maximal-interval
   argument for the existence of solutions, a well-posedness paragraph at the
   start of a proof, the smoothness of a function such as $((c_0-\gamma)^+)^2$,
   or a comment on switching instants (differentiate and integrate across them
   as the cited switching-graph papers do). When the user says such a
   justification is not needed, leave it out. When asked to check or revise a
   proof, first list every skipped step, then fill them.
12. **Space the LaTeX source of formulas.** In math code, leave one space
   after each complete symbol, that is, a symbol with its subscripts and
   superscripts, a function with its argument, or a bracket or norm group, and
   put spaces around binary operators and relations and after commas:
   `h R^T K_{\sigma(\ell h)} C_{\sigma(\ell h)} R R^T \xi(\ell h)`, not
   `hR^TK_{\sigma(\ell h)}C_{\sigma(\ell h)}RR^T\xi(\ell h)`;
   `\| y_\text{r}(\ell h) \|^2`, `\Phi_\vartheta(\ell, \ell_0)`, `h < 2/c`,
   `\Big( 1 - \frac{c h}{2} \Big)`. Do not insert spaces inside a subscript,
   superscript, or short time argument (`t_{j_{k+1}}`, `\sigma(\ell h)`,
   `(\ell+1)h`). The spacing changes only the source, not the typeset output.
   Apply this to every formula given to the user, in manuscript and
   response-letter text alike. When the user asks for code, give the LaTeX
   directly in a code block, not as a .tex file, with every line flush-left
   (no indentation, also inside environments).
13. **Zero.** A plain `0` denotes a scalar. A zero matrix (a vector is an
   $n \times 1$ matrix) is written `\mathbf 0` in two cases: as a block of a
   block matrix, companion matrix, or stacked vector (`$[I_{cn}\ \mathbf 0]$`,
   `$\mathrm{col}(\mathbf 0, w_2)$`), and as the value of a matrix or
   row-vector expression (`$S^T Q + Q S = \mathbf 0$`,
   `$U^T \Phi_x(t, s) \mathbf F(s) = \mathbf 0$`,
   `$\mathbf 1_N^T L_{\sigma(t)} = \mathbf 0$`, `$Q (I_{n_C} - R R^T) = \mathbf
   0$`). An equation whose left-hand side is a column vector keeps plain `0`
   (`$U^T w(t) = 0$`, `$A v = 0$`, `$\hat L_{\mathbb G} w_2 = 0$`,
   `$\ker(A) = \{x \in \mathbb R^n : A x = 0\}$`), as in Liu Tao's papers
   (see **Corpus notes**). A limit or convergence statement keeps plain `0`:
   `$\lim_{t \to \infty} (\hat x_i(t) - x(t)) = 0$`,
   `$\lim_{t \to \infty} \tilde w(t) = 0$ exponentially`. If the manuscript's
   Notation paragraph defines `\mathbf 0`, use the wording
   `$\mathbf 0$ denotes a zero matrix with conformable dimensions`.
14. **Introducing coefficients.** Do not write `we write $\varphi(s) = \ldots$`.
   Write `Hence, $\varphi(s) = \ldots$ for some $\varphi_0, \ldots,
   \varphi_{q-2} \in \mathbb R$`, `let $\psi_0, \ldots, \psi_{q-1} \in
   \mathbb R$ be such that $\psi(s) = \ldots$`, or expand and define in one
   display (`... can be expanded as follows:` followed by
   `\ldots =: s^{2n} + \theta_{01} s^{2n-1} + \cdots`).
15. **Cutting length** (for a page limit): compress sentence by sentence;
   do not delete whole sentences, Remarks, or figures outright.
16. **MATLAB commands** are woven into the sentence next to the object they
   compute (`$R$ is obtained by \texttt{R = orth(Q)}`), never piled into a
   block, in manuscripts and response letters alike.
17. **Write for the reader: purpose and conclusion first.** A reader who has
   not seen the derivation must know why each paragraph, construction, and
   step is there before reading it. A long derivation whose purpose is not
   stated is unreadable however correct it is (the advisor's feedback that
   triggered this rule). Examples below are from the reduced-state analysis
   of the Ax = b manuscript.
   - **Purpose or conclusion first.** Open a paragraph or a derivation with
     what it does or what it shows, then give the steps.
     Before: a paragraph whose first words are `Since $\ker(R^T) =
     \mathrm{im}(R)^\perp$ and ..., we have ...`. After: `The set $\mathcal S$
     has the following properties. First, since ...`, followed by
     `Moreover, ...` and `Furthermore, ...`.
     Before: `For any $w \in \mathcal N$, by (31), we have $R R^T w = w -
     (I_{n_C} - R R^T) w \in \mathcal N$, since ...`. After: `We first show
     that, for any $s \in \mathbb R^{d_Q}$, $s \in \mathcal S$ if and only if
     $R s \in \mathcal N$. If $s \in \mathcal S$, then $s = R^T w$ for some
     $w \in \mathcal N$. Hence, ... Conversely, if $R s \in \mathcal N$,
     then ...`.
   - **Say why a construction is introduced**, with `since` or `To ..., we
     ...`: `Hence, the component of $\xi(t)$ in $\ker(Q)$ does not affect
     $e_x(t)$, and, since $\ker(Q) \subseteq \ker(C_{\sigma(t)})$, it does not
     affect the right-hand side of system (19) either. Thus, we start with the
     orthogonal projection of $\xi(t)$ onto $\mathrm{im}(Q)$.`; `To show that
     the component of $\zeta(t)$ in $\mathcal S^{\perp_P}$ converges to zero,
     we establish the UCO property of an auxiliary system.`; `Using the
     equivalence that $s \in \mathcal S$ if and only if $R s \in \mathcal N$,
     we now rewrite Lemma~2 in terms of $\mathcal S$.`; `The
     inner product $\langle \cdot, \cdot \rangle_P$ is used since $P \bar
     K_{\sigma(t)} \bar C_{\sigma(t)}$ is symmetric, as shown below.` (not the
     vague `since $P$ satisfies the following identity`). A purpose clause or one
     sentence is enough in the main text; a longer account of why goes into a
     Remark or is deleted (constraint 22). The advisor cut the first example
     above down to `We start with the orthogonal projection of the error
     system state $\xi(t)$ onto $\mathrm{im}(Q)$.`
   - **State the plan before a multi-part argument**, including what each
     part will show: `Hence, $\zeta(t)$ is not expected to converge to zero
     but to a point in $\mathcal S$. To show this, we decompose $\zeta(t)$ by
     an oblique projection into a component in $\mathcal S$ and a component
     in a complement of $\mathcal S$, where the complement is chosen such
     that the component in $\mathcal S$ remains constant. Then, it suffices to show that the
     component in the complement converges to zero.` (write the two objects
     out, not `the former` and `the latter`). A plan stated in words is not a forward
     reference (constraint 3). Do not repeat `next` within a subsection; use
     a purpose clause, `In what follows`, or `Now`.
   - **Say what a result means** when the formula alone does not show it:
     after (33) and $C_{\sigma(t)} \xi(t) = C_{\sigma(t)} R \zeta(t)$, add
     `By (33) and (35), we see that both $e_x(t)$ and its evolution depend only
     on the reduced state $\zeta(t)$. Thus, it suffices to study the evolution
     of $\zeta(t)$.` (the advisor's wording, which replaced
     `both $e_x(t)$ and the right-hand side $K_{\sigma(t)}
     C_{\sigma(t)} \xi(t)$ of system (19) can be expressed in terms of
     $\zeta(t)$. Hence, it suffices to study $\zeta(t)$ instead of $\xi(t)$.`:
     a relation is stated by `depend only on`, not by `can be expressed in
     terms of`)
     (cite the equations the meaning is read from, and name the object
     concretely; not the vague `determines`, nor the roundabout `depend on
     $\xi(t)$ only through $\zeta(t)$`); after a vector is constructed, say what it gives (`where
     $\mathbf x^\dagger + v$ is a solution to (1)`). In a long technical
     section, keep such a sentence in the main text only when it states a
     precise fact that the reader needs (constraint 22); do not delete that kind as
     repetition. Do not add parallels or commentary to the main text (`similarly to the
     reduction from $\xi(t)$ to $\zeta(t)$`).
   - **Explain a non-obvious choice** (an oblique instead of the orthogonal
     projection, a weighted instead of the Euclidean inner product) in a
     short Remark placed where the choice is made: state what the
     construction must achieve as a formula, and show why the obvious
     alternative fails. Open the Remark with what it explains (`Here, we explain
     why we use an oblique projection rather than the orthogonal projection to
     decompose $\zeta(t)$.`). Later text echoes the Remark with its key word only
     (`symmetric`); when it needs the Remark's condition, it writes the
     condition itself (`$\mathrm{im}(\bar K_{\sigma(t)} \bar C_{\sigma(t)})
     \subseteq \mathcal S^{\perp_P}$ for all $t \ge 0$`), not a pointer (`satisfies the condition in
     Remark~6`); it does not restate the Remark.
   - **Formulas over words.** Name the object and write the condition: `Let
     $\mathcal W$ be a subspace of $\mathbb R^{d_Q}$ such that $\mathbb R^{d_Q}
     = \mathcal S \oplus \mathcal W$.`, `$\dot\zeta(t) \in \mathcal W$`,
     `$\mathrm{im}(\bar K_{\sigma(t)} \bar C_{\sigma(t)}) \subseteq \mathcal
     W$`, and the set itself, `$\mathcal W = \{u \in \mathbb R^{d_Q} : u^T s
     = 0,\ \forall\, s \in \mathcal S\}$` (so that it can be compared with
     $\mathcal S^{\perp_P} = \{u : u^T P s = 0\}$), instead of an unnamed `the
     complement`, `has no component in`, `contains`, `cannot be observed`, or
     `restrict ... to` (a word the paper has not introduced). Introduce a new
     vector with `there exists $\eta \in \mathbb R^{d_P}$ such that $(I_{d_Q}
     - \Pi) u = U \eta$`, not `which is of the form $U \eta$`. Write a
     contrast as formulas that differ visibly (`$(\bar K_{\sigma(t)} \bar
     C_{\sigma(t)})^T s = 0$` versus `$\bar K_{\sigma(t)} \bar C_{\sigma(t)} s
     = 0$`). Do not introduce a temporary projector or symbol in a Remark when
     it duplicates a definition that follows.
   - **Reason level.** A step that uses a cited equation directly takes `By X,
     we have`. A step that needs a moment's thought gets its reason or the
     intermediate identity. Before: `Hence, by (24), we have (33)`. After:
     `By (31), we have $\xi(t) = R \zeta(t) + (I_{n_C} - R R^T) \xi(t)$ with
     $(I_{n_C} - R R^T) \xi(t) \in \ker(Q)$. Hence, by (24), we have
     $[I_{cn}\ \mathbf 0] (I_{n_C} - R R^T) \xi(t) = 0$. Thus,` followed by
     (33) written as the chain $e_x(t) = [I_{cn}\ \mathbf 0] \xi(t) =
     [I_{cn}\ \mathbf 0] R \zeta(t)$. Write identity
     chains in full (`$\bar C_{\sigma(t)} u = \bar C_{\sigma(t)} \Pi u + \bar
     C_{\sigma(t)} (I_{d_Q} - \Pi) u = \bar C_{\sigma(t)} (I_{d_Q} - \Pi) u$`;
     `$(\bar K \bar C u)^T P s = s^T P^T \bar K \bar C u = s^T P \bar K \bar C
     u = -s^T \bar C^T \bar C u = -(\bar C s)^T (\bar C u) = 0$`, not
     `Transposing this and using the symmetry of $P$ give`). A standard fact
     needs no proof: an orthogonal decomposition `$w = R R^T w + (I_{n_C} - R
     R^T) w$`, or `$\mathbb R^{d_Q} = \mathcal S \oplus \mathcal S^{\perp_P}$`
     right after $\mathcal S^{\perp_P}$ is defined as an orthogonal complement
     in an inner product space. When the user finds a justification
     cumbersome (for example, a proof that $P = R^T Q R$ is positive
     definite), revert to listing the conditions.
   - **Sentences and paragraphs.** One purpose per paragraph; start a new
     paragraph when the purpose changes (proving an equivalence, then using
     it). One claim per sentence: end a sentence at a display instead of
     continuing with `and, by ..., we have ...` after it; split `..., which,
     by ..., holds if ...` and `If ..., then ... if and only if ..., i.e., ...,
     which does not follow from ... since ...` into several sentences.
     **No long sentences chained from short clauses (stressed repeatedly).**
     A sentence that joins short clauses with commas and connectors is a
     long sentence, however short each clause is: `If ..., then ..., and
     hence, by ..., we have ...`; `Since ... and, by (24), ..., we have ...`;
     `Hence, if ..., then, by ..., we have ...`; `..., and, by Lemma 1, there
     exists ...`; `..., so that by ..., ..., but ... by ..., since ...`.
     Whenever a sentence carries a premise and a conclusion, or two
     derivation steps, end it after the first and start the next sentence
     with the connector. Before: `If $s \in \mathcal S$, then $s = R^T w$ for
     some $w \in \mathcal N$, and hence, by (31), we have $R s = R R^T w =
     \ldots$`. After: `If $s \in \mathcal S$, then $s = R^T w$ for some $w \in
     \mathcal N$. Hence, by (31), we have $R s = R R^T w = \ldots$`. A
     supposition becomes its own sentence (`Suppose that $w \in \mathcal N$.
     Then, by (33), ...`). Before returning text, check every sentence that
     contains two or more of `and hence`, `and thus`, `then, by`, `which,
     by`, `and, by`, `and, since`, and split it. Exception: keep the two
     clauses in one sentence when the second refers back to the first by a
     pronoun, since splitting would separate `it` from its antecedent
     (`Hence, the component of $\xi(t)$ in $\ker(Q)$ does not affect
     $e_x(t)$, and, since $\ker(Q) \subseteq \ker(C_{\sigma(t)})$, it does not
     affect the right-hand side of system (19) either.` stays one sentence).
     **No referring word at the start of a paragraph.** A paragraph must not
     open with a word that points back to the previous paragraph (`this`,
     `that`, `these`, `it`, `such`, `the above`), alone or as a determiner
     (`Using this equivalence`, `This implies`, `It follows`, `These
     properties`): after a paragraph break the reader cannot tell what it
     refers to. Name the object or write the fact itself: not `Using this
     equivalence, we now rewrite Lemma~2 in terms of $\mathcal S$.`, but
     `Using the equivalence that $s \in \mathcal S$ if and only if $R s \in
     \mathcal N$, we now rewrite Lemma~2 in terms of $\mathcal S$.` Fixed
     constructions with an anticipatory `it` are fine (`It can be verified
     that ...`, `It remains to show that ...`, `It is easy to see that ...`).
     When such a word inside a paragraph refers to something several
     sentences back, name the object as well. After splitting, do not let
     two adjacent sentences both start with `Hence`: use `Thus`, `Then`, or a
     plain `By X, we have`. Do not introduce a generic symbol when the step
     uses one specific vector: write `$[I_{cn}\ \mathbf 0] (I_{n_C} - R R^T)
     \xi(t) = 0$`, not `$[I_{cn}\ \mathbf 0] w = 0$ for all $w \in \ker(Q)$`.
     Put the
     fact that a following `Hence` uses directly before it (move
     `every $s \in \mathcal S$ is an equilibrium of system (34)` to the end of
     the paragraph, right before `Hence, $\zeta(t)$ is not expected to
     converge to zero ...`). Vary repeated connectors (`Therefore` after
     several `Hence`).
   - **No repetition.** When content moves from a Remark into the main text
     or into a Lemma, delete it from the Remark, and delete a Remark with
     nothing left. Do not restate a fact just proved (`the latter is
     equivalent to $R s \in \mathcal N$, i.e., $s \in \mathcal S$` right
     after proving that equivalence). Keep an identity chain the user wants
     for traceability (`$e_x(t) = [I_{cn}\ \mathbf 0] R s = \mathbf 1_c
     \otimes v$`).
   - **Equation numbers.** Number an equation only if it is cited later, and
     give a number to a formula that a later step uses. Cite an equation that
     holds several items only when all are used; otherwise write the needed
     item inline (`Since $\bar C_{\sigma(t)} = C_{\sigma(t)} R$, ...`). Move a
     definition that no longer needs a number into the text (`where $\bar
     K_{\sigma(t)} := R^T K_{\sigma(t)} \in \mathbb R^{d_Q \times n_C}$ and
     ...`). A conclusion not cited by number may stay inline in a Lemma (`and
     $\Pi \zeta(t) = \Pi \zeta(0)$ for all $t \ge 0$`); keep the key result
     in the Lemma rather than leaving it to a later proof.
   - When asked to improve readability, go sentence by sentence and ask for
     each: does the reader know why it is here, and can they check it from
     what is written?
18. **Revise only what is asked.** When the user points to a sentence,
   change that sentence and nothing else: do not touch neighboring
   sentences, add sentences, or polish passages they did not mention
   (stressed: `再说一遍只改我让你改的部分`). When the user says an earlier
   wording read better, return to it and change only what is still needed.
   Quote the original sentence, then give the revision. In a whole-paragraph
   review, list only real problems, and say plainly when nothing needs to
   change. Always follow the user's latest decision over earlier ones.
19. **Introduction and Abstract prose.**
   - Keep the Introduction at the level of ideas and leave algorithmic
     devices to the body. For example, multiplying each contribution by the
     number of agents so that an average equals a sum belongs to the DAC
     section, not the Introduction. Do not introduce nouns that only serve
     such a device (`scaled contributions`, `inputs`).
   - Each step of the motivation must follow from the previous one; add the
     missing link instead of jumping. Say why the agents must communicate
     before naming a consensus algorithm (each agent needs the entries of the
     local term associated with its sub-state, which depend on the
     contributions of all the agents within the cluster). Say that the
     tracking error enters the update of the sub-state estimates as a
     perturbation before turning from the tracking error to the estimation
     error.
   - Do not open by ruling out an option no reader would consider (`The
     local term cannot be computed by the aggregator, since ...`). State who
     does the job, mirroring the parallel sentence: `The consensus term is
     computed by the aggregators.` / `In contrast, the local term is handled
     by the agents within the cluster.`
   - Link paragraphs by parallel wording: `each agent estimates only part of
     the state using only part of the system and output matrices`, `each agent updates
     only part of the solution using only part of the equations`, `each
     sub-state corresponds to part of the solution`.
   - Lead with the conclusion and tie it to the previous sentence by a
     connector (`As a result, ...`, `Moreover, we add ...`, `Since then,
     ...`, `In this paper, inspired by \cite{x}, we ...`). A `however` needs
     the first half of the contrast in the preceding sentence; otherwise
     rephrase.
   - Balance sentence length. Merge tightly linked short sentences (`...,
     and hence ...`, a `with`-clause) instead of leaving a string of very
     short ones; split only genuinely long chains (constraint 17). Avoid two
     `and`s in one sentence (`..., and its bound depends on ... and scales as
     ...`).
   - Referents must be clear. No `here` without an obvious antecedent. No
     `its` that can attach to the wrong noun: not `collects the entries
     updated by its agents` (the agents belong to the cluster, not the
     aggregator) but `by the agents within the cluster`; not `Its model
     storage` but `The model storage of each agent`. Avoid vague `this` and
     `these`.
   - Keep the cited source's wording for quantitative claims (`scales as
     $O(1/\gamma)$`, not `of order`). Be exact about dependence: `the
     initial state of the system` when only the state enters a bound; `all
     initial conditions` for a guarantee over the system and the estimates.
   - Do not attach our construction to a cited paper's description: not
     `the edge-based adaptive law in \cite{x}, which assigns a tracking gain
     to each intra-cluster edge` (this puts our setting in [x]), but
     `Following the edge-based adaptive law in \cite{x}, we assign a tracking
     gain to each intra-cluster edge.` Do not call a borrowed method
     `proposed`; write `we design ... for ...`. When a clause states what an
     object does, use a relative clause (`..., which assigns ...`), not `and`.
   - Name plus symbol (Liu Tao's habit): define a symbol once (`We refer to
     the gain of the DAC algorithm as the tracking gain and denote it by
     $\gamma$.`) and afterwards write `the tracking gain $\gamma$`, neither a
     bare `$\gamma$` in prose nor a second definition. Write a term in full
     (`the edge-based adaptive law`, `each tracking gain`) when the paper has
     several gains.
   - The rule holds in both directions and everywhere, not only in the
     Introduction (stressed: `这些为什么做不到一致！符号有特定名字的都
     要加上！`): every object that has both a name and a symbol carries both,
     at every occurrence. A name gets its symbol (`the correction $g E_{ij}
     P_i v_i(t)$ from aggregator $i$`, `the first term $E_{ij} \bar w_i(t)$`,
     `the tracking gains $\gamma_{ijq}(t)$`, `the cluster-level output
     $y_i(t)$`, `the consensus term $g P_i v_i(t)$`), and a symbol in prose
     gets its name (`the observer gain $L_i$`). Once a term is written out, drop
     words it makes redundant (`acts, through $P_i$,`). When one sentence or
     two adjacent sentences list several objects, give every item the same
     form; do not leave one item bare. Before returning text, scan the whole
     passage for named objects without their symbols and fix every one.
   - The Abstract must not use terms it has not defined (`local term`,
     `consensus term`, `node`); describe the operation instead (`The
     aggregators exchange the estimates of the clusters over the
     inter-cluster graph, and the agents within each cluster combine the
     information from their local outputs by a dynamic average consensus
     (DAC) algorithm over the intra-cluster graph.`).
   - Once the Introduction is final, align the Abstract and the body with
     its wording (one term per object), changing only the sentences that
     disagree.
   - **A contrast between existing work and ours is two parallel clauses.**
     Use the same verbs and the same order of items on both sides, and put
     the word that carries the contrast on every item: `each agent estimates
     the full state using the full system matrix and its full output matrix`
     against `each agent estimates only one sub-state using only the column
     blocks of the system and output matrices associated with its
     sub-state`. Three checks:
     - Do not let another modifier take the stress. `its own output matrix`
       moves the reader's attention to `own`, while the contrast is `full`
       against `column blocks`; write `its full output matrix`.
     - Do not leave an item ambiguous, and do not drop an item to shorten
       the sentence. `the full system and output matrices` can be read as
       the stacked output matrix of all agents, which is not the matrix that
       is partitioned later; the possessive `its` names the right one. This
       is a matter of exactness, not of defensive writing.
     - When the parallel form would read `estimates ... and stores ... and
       ...`, replace `and stores` by `using` so that one `and` remains.
   - **No defensive writing in the Introduction** (`不用刻意的防御性写作`,
     `introduction整体要连贯的`). Do not add a sentence, a citation list,
     or a condition only to shield a summary sentence from a narrow
     counterexample: not a second sentence `In standard full-state
     distributed observers such as those in \cite{a,b}, each agent stores
     ...`, and not `when the system matrix is known, ...`. A qualifier must
     really restrict: `full-state` distinguishes nothing right after `In all
     of these works, each agent maintains an estimate of the full state`.
     When a reviewer's or a checking tool's comment proposes splitting a
     summary sentence, first see whether one more exact word in the same
     sentence solves it, and keep the paragraph coherent.
   - **Orders and analogies name their object.** Keep the order explicit and
     name the comparison object by a term the Introduction has already
     introduced instead of listing its items again: `scales as $O(n n_{ij} +
     n m_i)$ rather than $O(n^2)$ as in a standard full-state distributed
     observer`. An analogy with a cited paper names the object on the cited
     side: `The output of each cluster corresponds to a block of rows of the
     equations in \cite{x}`, not `As in \cite{x}, the output of each cluster
     corresponds to a block of rows`.
   - **Small checks on a final pass of the Abstract and Introduction.** A
     first mention takes `a`/`an` and says what the object is (`cluster-level
     estimates of the full state over an inter-cluster graph`); the second
     mention takes `the` (`To achieve a prescribed accuracy ...` and then
     `the prescribed accuracy is achieved`). A `This` right after an example
     sentence points at the example (`This has led to extensive research on
     ...`); name the subject instead (`Hence, distributed state estimation,
     where ..., has been extensively studied.`). Use one word per property
     across the paper (`fixed` graph everywhere, not `static` in one place).
     When a long `Unlike ..., we develop ..., where ...` sentence is hard to
     read, split it as `In existing ..., each agent .... In contrast, we
     develop ...`.
20. **Numerical examples must respect the setting and be checked.**
   - The example must not undercut the paper's premise. For a partitioned
     observer, no cluster may observe the state from the stacked local
     outputs of its agents; put each row of $C_i$ in the sub-state of one
     agent.
   - Every number in the text comes from the code output. Verify each
     qualitative claim (`almost coincide`, `about 10 times`, `remains above
     $\varepsilon$`) numerically before writing it, and change the wording
     when it fails.
   - Fix a poor figure by fixing its cause in the setup (for example,
     overlapping gain curves caused by symmetric agents without
     measurements), not by cherry-picking initial conditions or plot limits,
     and check that a tuning that looks good is not fragile.
21. **Passes over the body.**
   - When asked to tidy a section, remove only repetition and unimportant
     sentences; keep sentences that help understanding, and keep derivations
     complete. Do not reword for brevity alone; when the user rejects a cut
     (`太长了`, `正常人都看得懂`), restore the original.
   - An echo across a subsection boundary is not repetition: a subsection
     that ends with what remains to be done (`It thus remains to make the
     local term $\bar w_i(t)$ available to every agent ...`) and a next
     subsection that opens with the same purpose (`To make the local term
     $\bar w_i(t)$ available to every agent, we ...`) is good linking.
   - Do not repeat in prose what a nearby definition already says (once a
     `where` clause defines $\gamma_{ijq}(t)$ as the tracking gain of the edge
     between agents $i_j$ and $i_q$, do not say again that the agents at the
     ends of each edge update its gain). Do not write a sentence that rules
     out an approach nobody would take (`The tracking error cannot be used to
     adjust the tracking gains, since ...`).
   - No `i.e.` clause or explanation for what is intuitive or defined just
     above (`while $s_\ell(t) > \delta^2$` needs no `i.e., while the estimates
     ... differ by more than $\delta$`; a standard edge-set definition needs
     no justification). After removing such a clause, check that no referent
     is left dangling (`the two estimates` becomes `$s_\ell(t)$`).
   - Motivate a design directly, from the known result to the design:
     `With a constant tracking gain $\gamma$, it is shown in~\cite{x} that the
     estimation error is ultimately bounded by a constant that scales as
     $O(1/\gamma)$ and depends on the initial state of the system. Hence, ...
     has to be chosen according to a bound on the initial state, which is
     usually unknown. We therefore adjust the tracking gains online.`,
     followed by the law. Keep the quantity the reader cares about as the
     subject (the estimation error), and state a dependence directly instead
     of through an intermediate symbol (not `proportional to the upper bound
     $\chi$ of $\| x(t) \|$, which depends on $x(0)$`). Omit setting details
     that are not the point (the graph condition of the cited result).
   - Before an algorithm, present the idea it implements: define the object,
     show the key identity, then name the algorithm (`For each agent $i_j$,
     let $\eta_{ij}(t) := \ldots$ be the scaled contribution ... Then, by (x),
     we have $\frac{1}{k_i} \sum_{j=1}^{k_i} \eta_{ij}(t) = \bar w_i(t)$.
     Hence, ... Since the scaled contributions vary with time, we use the DAC
     algorithm ...`), and let later derivations cite the new identity instead
     of re-expanding it. After reordering equations, update every range
     citation (`\eqref{a}--\eqref{b}`) in the document.
   - The grammatical subject of an action is the object that acts: not `the
     adaptive law increases $\gamma_\ell(t)$`, but `Under the adaptive law (x),
     the tracking gain $\gamma_\ell(t)$ increases while ...`.
   - Define a symbol where its purpose becomes clear, usually right before its
     first use (a sum $S_i(t)$ used first in a Lemma is defined before that
     Lemma), keeping its label so later citations still resolve. Do not drop
     a statement that a later step needs (the symmetry
     $\gamma_{ijq}(t) = \gamma_{iqj}(t)$ of adaptive gains) when tidying.
   - Anchor every Abstract and Introduction term at the object's definition in
     the body (`$A$ is the system matrix`, `$C$ is the output matrix`, `$C_i$ is
     the output matrix of cluster $i$`). A formula in an early section may use
     only symbols already defined there (no $g$ or $P_i$ in the Problem
     Formulation when they are introduced in the design section); describe
     the object in words instead (`computes a correction from $v_i(t)$ using
     $E_{ij}$`).
   - A cited upper bound that depends on the initial state supports `has to be
     chosen according to a bound on the initial state`; it does not prove that
     constant gains fail. Do not upgrade it.
   - When a modeling choice needs a reason (fixed intra-cluster graphs, a
     switching inter-cluster graph), reuse the wording of the user's own
     related manuscript, and add no citation that the original lacks.

22. **Mathematically precise language; explanations go into Remarks (the
   advisor's feedback on the second round).** Liu Tao's instruction: `Please
   ensure that you use formal, rigorous, and mathematically precise language
   that everyone can fully understand.` The user's rule for applying it:
   write clearly in mathematical language and put explanatory material in
   Remarks (`写的清楚 数学语言 然后解释性的放在remark里面`). Where an example
   sentence in constraint 17 conflicts with this constraint, this constraint
   wins. Examples are from the reduced-state analysis of the Ax = b
   manuscript.
   - **What stays in the main text.** Definitions, results, and the
     derivations that a later proof uses, each written as a mathematical
     statement. For every sentence or derivation, ask whether a later step
     cites or uses it. If not, delete it or move it to a Remark. Deleted: the
     chain `$\bar C_{\sigma(t)} \Pi = \mathbf 0$ ... That is, similarly to the
     reduction from $\xi(t)$ to $\zeta(t)$, $\bar C_{\sigma(t)} u$ can be
     expressed in terms of $\eta$. Therefore, we consider the auxiliary
     system`, of which no later proof used a line. What remains is `Let ...
     the columns of the matrix $U$ form an orthonormal basis of $\mathcal
     S^{\perp_P}$ ... Consider the auxiliary system`. The advisor cut the two
     sentences explaining why to project and kept `We start with the
     orthogonal projection of the error system state $\xi(t)$ onto
     $\mathrm{im}(Q)$.` A purpose clause (`To show that ..., we ...`) or one
     sentence of plan is enough motivation in the main text. Before deleting,
     list which later steps use each fact; when a deleted fact is used
     later, give its source there (`Consequently, by (45), $\chi \in \mathcal
     S \cap \mathcal S^{\perp_P} = \{0\}$`).
   - **Verbs that state a mathematical relation.** `both $e_x(t)$ and its
     evolution depend only on the reduced state $\zeta(t)$`, not `can be
     expressed in terms of $\zeta(t)$`. Never `To describe the set $\mathcal
     N$ ... in terms of $\zeta(t)$` (the advisor: the relation between a set
     and a state is unclear). No `Therefore, we consider ...` unless the
     system follows from what precedes. Avoid `as shown above` and `the above
     equivalence`: number the equation and cite it.
   - **Name the concrete object** (the advisor's edits): `the error system
     state $\xi(t)$`, `the matrix $R$`, `the reduced state $\zeta(t)$`, `the
     columns of the matrix $U$`.
   - **Define an object by what it is, then derive its other forms.** After
     the analysis moves to a new system, define that system's own object
     first and relate it to earlier objects afterwards: `We next characterize
     the set of equilibria of system (36), which is given by $\mathcal S :=
     \{s \in \mathbb R^{d_Q} : \bar K_{\sigma(t)} \bar C_{\sigma(t)} s = 0,\
     \forall\, t \ge 0\}$`, then $\mathcal S = \{s \in \mathbb R^{d_Q} : \bar
     C_{\sigma(t)} s = 0,\ \forall\, t \ge 0\}$, then `$s \in \mathcal S \iff R
     s \in \mathcal N$`, then $\mathcal S = \{R^T w : w \in \mathcal N\}$. Do
     not define it as the image of an earlier set and prove afterwards that
     it is the wanted object. A definition needs no reason: not `Since
     $\zeta(t) = R^T \xi(t)$, the set $\mathcal N$ ... is mapped by $R^T$ to`
     (a motivation written as a premise). Name the object at its definition,
     so that later text says `$s \in \mathcal S$`, not `$s$ in the set (37)`.
     When a fact is the definition or an equivalent form of it, do not state
     it again as a separate numbered equation.
   - **No hypothetical that does not occur.** Not `Suppose that $\zeta(t) =
     s$` for a point $s \in \mathcal S$: the trajectory converges to a point
     of $\mathcal S$ and in general never equals one. State the property for
     the point itself, or leave it to the proof where the limit is taken.
   - **One form for one object.** If a set is displayed in set-builder form,
     keep that form in the following sentences (do not switch to
     `$\ker(\cdot)$`), and keep one phrase for membership (`in the set (x)`
     throughout, not `belongs to` in the next sentence).
   - **Connectors must match the logic.** Parallel results take additive
     connectors (`By (38), ... Moreover, by ..., ... Furthermore, by ...,
     ...`), not a mixture of `Hence`, `Moreover`, and none. `Conversely`
     needs a stated implication or inclusion to reverse. `On the other hand`
     is for a contrast, not for a second fact. Use `start`, `next`, and `now`
     at most once each in a subsection. `it suffices to show` names its goal
     (`Thus, to show that $\zeta(t)$ converges exponentially to $\zeta^*$, it
     suffices to show that $\zeta_\perp(t)$ converges exponentially to
     zero.`).
   - **A set equality is two inclusions, written as inclusions.** `Suppose
     that $s \in \mathcal S$. ... Hence, $\mathcal S \subseteq \{R^T w : w \in
     \mathcal N\}$. Suppose that $w \in \mathcal N$. ... Hence, $\{R^T w : w
     \in \mathcal N\} \subseteq \mathcal S$. Therefore,` followed by the
     equality. Without the two `Hence` sentences the reader takes the two
     halves for one fact said twice. When the equality follows from a chain
     of equivalences that are each immediate, the advisor prefers that chain
     over the two inclusions (see `The advisor's own edits` below).
   - **One reason, one conclusion.** Not `Then, by (39), $R s \in \mathcal
     N$, and $s = R^T (R s)$ since ...` (it reads as one reason giving two
     results), but two sentences. Do not write an identity as a sentence and
     again inside the next display.
   - **Hypotheses where they are used.** Drop an assumption from a Lemma
     whose proof no longer uses it, and write `Under Assumptions 2 and 3` at
     the first sentence that depends on them. When a textbook result is
     cited, read what it states: (5.11.1) of Meyer gives $\mathcal V =
     \mathcal M \oplus \mathcal M^\perp$ for any subspace of a
     finite-dimensional inner-product space, so no proof of $\mathcal S \cap
     \mathcal S^{\perp_P} = \{0\}$ is needed in front of it; state the
     hypothesis that it needs instead (`By (37), $\mathcal S$ is a subspace of
     $\mathbb R^{d_Q}$.`). A step such as `there exists a nonzero vector $\nu$
     such that $M_k \nu = 0$` needs its reason (`Since $M_k$ is symmetric and
     positive semi-definite`).
   - **Inside a Remark**, write conditions out instead of `this holds`, `this
     inclusion`, or `the latter`.
   - **No comparison without its object, no unclear referent (stressed:
     `牢记 please！`).** Check every sentence handed to the user for this,
     including sentences carried over unchanged from the user's draft when a
     passage is split, merged, or moved. Not `requires a number of operations
     of the same order`, but `requires $O(n n_{ij} + n m_i)$ operations`; not
     `the same order as the corresponding term of (x)`, but `as does the term
     $\gamma_{ijq}(t) \big( w_{ij}(t) - w_{iq}(t) \big)$ in (x)`; not `by a
     common procedure`, but what it guarantees (`all the aggregators compute
     the same matrix $Q$ from $A$`); not `an additional communication cost`,
     but `Compared with full-state distributed observers over a single-layer
     network, ...`; not `the total state dimension`, but whose state and
     compared with what. A modifier must attach to one object only (not
     `forms $\hat x_i(t)$ by (a) and $v_i(t)$ by (b) with $O(\cdot)$
     additions`), and `it` must have one possible antecedent. Watch `the
     same order`, `similar`, `comparable`, `additional`, `the corresponding`,
     `the above`, `a common`, `such`, `total`, and `it`. Apply the check where
     a reader would really misread (`现在太细了效果并不好`): do not add
     reasons for standard facts, do not expand a phrase that is already
     clear, and do not attach symbols to a generic statement (`each
     inter-cluster link carries $n$-dimensional cluster-level estimates`).
   - **Voice and variety.** The user prefers the active voice (`we choose
     $\mathcal W$ as ...`, `We introduce an output ... as follows:`, `Here,
     we explain why we use ...`). When `since` is overused, vary it (`The
     reason why we choose this inner product is that ...`).
   - **Standard phrases.** When the user doubts a phrase (`the orthogonal
     complement of $\mathcal S$ with respect to $\langle \cdot, \cdot
     \rangle_P$`, `the projector onto $\mathcal S$ along $\mathcal
     S^{\perp_P}$`, `oblique projection`), check it in the cited textbook and
     quote the passage (pages 385, 386, and 403 of Meyer) instead of
     asserting that it is standard.
   - **Working with the user in this mode.** Go one part, then one sentence,
     at a time. Prefer the simple version: when the user calls a fully
     written display `太复杂了`, keep the short sentence. Say plainly when the
     user's proposal does not hold (a set equality needs both inclusions).
     When the user keeps their own wording after hearing the concern
     (`留一些我的印记`), do not raise it again. When the advisor's text has a
     gap, do not call it an error and do not rewrite it: say plainly whether
     the conclusion holds, restore his version, and give the minimal fix,
     usually only the missing reason, written out instead of a bare
     equation number when that equation holds several items (`Since $R^T R =
     I_{d_Q}$ and, by (33), $C_{\sigma(t)} R R^T = C_{\sigma(t)}$, the
     equivalence (39) is further equivalent to`). Avoid defensive additions
     (extra numbered equations, where clauses, inclusion proofs) when the
     user asks for the advisor's version.
   - **Whole-paper pass.** Check by script: duplicate and undefined labels,
     citations against the bibliography and its order, forward references,
     and the order of equations cited together. Verify restructured claims
     numerically on the paper's example when possible. Report what could not
     be checked (the page count without the class file; literature
     statements not reread).
   - **The advisor's own edits (Nov 18 version of the Ax = b manuscript).**
     Follow these when writing in his style.
     - Obvious equivalences are stated, not proved: `Then, it is clear that
       $s \in \mathcal S \iff R s \in \mathcal N$.` A set is rewritten by a
       chain of equivalent characterizations: `Thus, the set $\mathcal S$ can
       be equivalently characterized as (38).`, `... the equivalence (39) is
       further equivalent to ...`, `Thus, the set $\mathcal S$ can be further
       characterized as (40).` He removed both the sentence giving the
       trivial reverse inclusion and the two-inclusion proof of a set
       equality; do not add them back.
     - Trivial steps leave a derivation chain: he merged `s^T P^T \bar K \bar C
       u = s^T P \bar K \bar C u` into one equality and dropped `the first
       equality holds since $P$ is symmetric`; he also dropped the reason
       `since $\gamma_2$ ... can always be chosen such that $\gamma_2 >
       \beta_1$` and kept only `where $\rho := 1 - \beta_1 / \gamma_2$ and
       satisfies $0 < \rho < 1$` (the user keeps his version). He drops
       `\forall\, t \ge 0` from a display with no switching matrix ($e_x(t) =
       [I_{cn}\ \mathbf 0] R \zeta(t)$), but adds `for all $t^* \ge 0$` where a
       bound must hold uniformly.
     - Varied verbs: `Left-multiplying (53) by $U^T$ yields`,
       `Differentiating ... gives`, `By integrating ..., we have`, `can be
       obtained from system (47) by injecting the output`, `as a result of
       Lemma 4`, `From (34) and (35), we see that`, `the integral ... exists`.
     - Words over symbols for matrix properties: `$M_k$ is positive definite`,
       not `$M_k > 0$`. A function itself is written `$G_\eta(\cdot, \cdot)$`.
       A constant is introduced as `a positive constant $\kappa$` (lower case;
       the user dislikes capitals for scalars, and $M$ clashed with the
       matrices $M_k$).
     - Name the object again at a key step: `we decompose the reduced state
       $\zeta(t) \in \mathbb R^{d_Q}$ as`, `if the step size $h \in (0,
       \tau]$`, `the proposed algorithm`.
     - Plain words: `an ordinary orthogonal projection` and `the ordinary
       orthogonal complement` (not `Euclidean`); `$P \bar K \bar C$ becomes
       symmetric`; Remark openers `The proof of Theorem 1 also provides`,
       `In addition, we note that`.
     - Purpose of the decomposition, in his words: `To facilitate the
       subsequent convergence analysis, we further decompose $\zeta(t)$ by an
       oblique projection ...`.
     - Symbols must be self-explanatory: he rejected the output subscripts
       `b` (base) and `r` (reduced); name an output after its system's state
       ($y_\eta(t)$, $y_\vartheta(t)$), matching $G_\eta$ and $G_\vartheta$.
     - Numerical example: state the assumption first and the consequence
       after (`Since $\mathrm{rank}([A\ b]) = \mathrm{rank}(A) = 4 < 5$,
       Assumption 1 is satisfied. In particular, this linear equation has
       infinitely many solutions.`). The simulation only shows that the
       algorithm finds a solution, so do not explain how the reached solution
       depends on the initial states (`To illustrate the convergence of the
       algorithm, we examine ...`).
     - Check his typing for typos (`oridinary`, `a shown`, `described Fig.`,
       `Note $\mathcal S$ is`) and report them separately from content.
     - When his PDF and the user's build differ, compare the extracted text
       first; differing figure files (Fig. 1 legend, figure height) can
       change the page count while the text is identical.
23. **Proof prose (from the user's line-by-line walk through the
   appendices).**
   - **Vary the connectives.** Never write several consecutive sentences of
     the form `Since/Hence ..., we have ...`. Choose by the logical relation:
     `..., and thus` for a tightly linked consequence; `it follows that`,
     `It then follows from (x) that`; `which, together with (y), gives (z)` to
     attach a second fact; a gerund for an operation on a numbered equation
     (`Differentiating both sides of (x) and using (y), we obtain`); `we
     further have`; `can be written as` for a decomposition. A conclusion that
     is a formula is introduced by `we have`: not `Hence, $X = Y$`, `Moreover,
     $X = Y$`, or `Then $X = Y$`.
   - **Operations name their equation.** `Multiplying both sides of (x) by`,
     `Integrating both sides of (x) over`, `Substituting (x) into (y)` (never a
     bare `substituting (x)`), `Left-multiplying both sides of (x) by`,
     `Summing (x) over`. The equation operated on gets a number, and so does
     every inequality cited later; give a lemma's inequality its own label
     instead of writing `the inequality in Lemma 3(ii)`.
   - **Give a reason only where a reader would stop.** No reason for a step
     that uses the sentence just before, the equation being differentiated, a
     definition given in the same or the previous sentence, a direct
     differentiation ($\frac{\partial}{\partial s} \Phi(s, t) =
     \mathcal A_{\sigma(s)} \Phi(s, t)$), or the norm of a stacked vector. Do
     not write `by the definition of X` when the definition is in the previous
     sentence. But state a step that is the purpose of a construction, even if
     it is algebraically trivial (the cancellation of the sums of
     $\dot\Gamma_\ell(t)$ in $\dot{\mathcal U}(t)$).
   - **One or two reasons per relation.** When one relation would need three
     or more reasons, add a line to the chain. When the remaining reasons are
     only substitutions, put them in the gerund (`Differentiating $\tilde
     w_i(t) = \Pi_i w_i(t)$ and using (x) and (y), we obtain`) and drop the
     `where` clause. An explanation of a display (which terms cancel) goes in
     the `where` clause after it, not before it, and names a formula once
     (`where the sums of $\dot\Gamma_\ell(t)$ in $\dot{\mathcal U}(t)$ and (x)
     cancel each other`). Do not stack two gerund steps or more in one
     sentence: display the intermediate result and attach the conclusion by
     `which, together with (x), gives (y)`.
   - **No restating.** Do not restate in a proof a definition given earlier
     ($A_{ij} := A E_{ij}^T$, $d_i(t)$), a formula that already has a number
     (cite the number), or an identity already derived in the same proof
     (`as in the proof of statement (i)`). Do not copy a numbered equation into
     a `Since` clause, and put at most one `formula by (x)` in a `Since` clause.
     Write a combination such as $(A - L_i C_i) + L_i C_i = A$ directly as its
     result in the display. Delete a sentence in a proof that repeats what the
     text before the lemma already established (`Since $L_i$ and $P_i$ are
     designed as in Remark~9 of [x], system (y) is the error system of ...`).
   - **No detours.** Do not introduce a quantity and its monotonicity to derive
     an inequality (`$\mathbf e^{2 \bar a (s - t)} \| \Phi(s, t) u \|^2$ is
     nondecreasing`); write the integrated inequality. Do not argue through
     orthogonal subspaces when an identity in (x) kills the cross terms. Do not
     introduce an abstract placeholder matrix (`for any matrix $G$`); state the
     identity for the matrices at hand and apply it. Delete a sentence that
     states a conclusion without its reason when the next display already
     contains it (`the integral defining $\Theta(t)$ converges`).
   - **Formulas, not descriptions.** Write the bound (`$\| v(t) \| \le
     \bar\ell \| e(t) \|$`, introducing $v(t) := \mathrm{col}(\ldots)$ when the
     symbol is free) instead of `whose norm is bounded by`; name the blocks
     ($\zeta_{ij}(t)$) instead of `the difference of the blocks of $\zeta(t)$`;
     write `$\sum_\ell \Gamma_\ell(t) \le \mathcal U_\gamma$` instead of `the
     last sum is bounded by its initial value`. When stacking with the
     triangle inequality, display the stacked inequality first and read the
     constant off it.
   - **Definitions.** Define a stacked vector by `\mathrm{col}(\cdot)` and a
     block-diagonal matrix by the operator in the Notation, never by `the
     stacked vector of`. In a narrow list item, put long definitions into the
     display they belong to rather than inline. Define a quantity where it is
     first used, also inside a proof ($\bar e$, $\mathbb K$, $V(t)$); a symbol
     that the main text never defines is defined in the appendix that uses it.
     Take maxima over the switching index set (`\max_{p \in \mathcal P}`), not
     over `t \ge 0`. No capital letters for scalar constants (`c_f`, not `F`);
     Lyapunov functions may stay capital.
   - **Structure of a multi-part proof.** Head each part with `\smallskip` and
     `\emph{Proof of statement (i):}`, and drop `We first prove statement
     (i).` and `This proves statement (i).`. Inside a part, use one paragraph
     per conclusion of the statement, in its order. A part with two stages
     opens with `We first show ..., and then ...`.
   - **Attribute each fact to its real cause.** Symmetric gains give
     $\mathbf 1^T \mathcal H_i^\gamma(t) = \mathbf 0$; $\mathcal H_i^\gamma(t)
     \mathbf 1 = 0$ holds for every Laplacian matrix, so do not put it after
     `Since the gains are symmetric`.
24. **Design and analysis sections (from the walk through the single-layer
   least squares manuscript).**
   - **Parallel sentences use identical wording** (`避免这样的错误`). Before
     returning a sentence, find its twins and compare them. An equation
     `holds`; variables `satisfy` an equation. Not `such that (x) holds` in
     one sentence and `such that ... satisfy (x)` in its twin.
   - **Introduce auxiliary quantities with the object they belong to.** `Let
     $\mathbf x^*$ and $\mathbf x'$ be least squares solutions to (1). For
     $\mathbf x^*$, let $r_i^*$, ..., be vectors such that $\mathbf x^*$,
     $r_i^*$, and $\mathbf w^{l*}$ satisfy (x). For $\mathbf x'$, let ...`.
     Not `suppose that A, B, C and A', B', C' both satisfy (x)` (ambiguous
     `both`), and not `(x) holds with ... replaced by ..., respectively`. Do
     not add `unknown` to a vector being introduced, and do not write the
     vague `associate a vector with`; say what is introduced (`introduce a
     vector in $\mathbb R^n$ for each edge`).
   - **State each conclusion the next step uses** (`..., i.e., $r_i' =
     r_i^*$`). After a `Since` clause, the main clause starts with `we have`,
     not with a formula (`Since $B$ has full column rank, we have ...`).
     Write a dimension as a derived formula (`$\dim(\ker(B^T)) =
     \dim(\mathrm{im}(B)^\perp) = c - \mathrm{rank}(B) = 1$`), not `has
     dimension one`, and write a subspace chain in full (`$\ker(\mathbf 1_c^T)
     = \mathrm{span}\,\{\mathbf 1_c\}^\perp = \ker(B^T)^\perp =
     \mathrm{im}(B)$`).
   - **Purpose sentences echo the problem statement word for word.** If a
     Remark says (x) `couples the pairs $(A_i, b_i)$ of all the agents and
     cannot be handled by any single agent`, the design opens with `To
     decouple the optimality condition (x), i.e., to rewrite it as separate
     equations, where ... can be handled by agent $i$ using only the pair
     $(A_i, b_i)$, ...`, and the Remark that checks the idea uses the same
     phrase. Do not repeat that phrase a third time in the next paragraph.
     A count in a purpose sentence must match the lemma it announces (drop
     `$c$` when the lemma has $2c$ equations).
   - **Define a term right after its first use**: end the sentence with the
     term, then `Here, a tree is a connected graph with no cycles.` State
     structural facts explicitly (`Since $\mathcal T$ is a tree with $c$
     vertices, it has $c-1$ edges.`), say when a choice is free (`assign a
     direction to each edge arbitrarily`), and state a labeling once (`We
     denote the set of the edges of $\mathcal T$ by $\mathcal E_{\mathcal T}
     := \{1, \ldots, c-1\}$`, without also `which we label by $1, \ldots,
     c-1$`).
   - **A lead-in to a lemma ties it to the section's purpose** (`In the
     following lemma, we use the incidence matrix $B$ to rewrite the
     optimality condition (x) as separate equations.`), not a bare `The
     following lemma rewrites ...` after an unrelated derivation. The Lemma
     itself states what its formulas mean (`i.e., $\mathcal N$ is the set of
     all the equilibria of system (x)`), so that it does not look like matrix
     manipulation; the lead-in then only says what the Lemma characterizes.
   - **Before introducing estimates, say why their targets exist.** Give the
     equivalence (`finding a least squares solution is equivalent to finding
     $\mathbf x^*$, $r_i^*$, and $\mathbf w^{l*}$ that together satisfy
     (x)`: three quantities found together, not one replaced by two), then
     existence, uniqueness, and independence of the choice of $\mathbf x^*$,
     then which targets depend on $i$, and only then `each agent $i$
     maintains an estimate ... of ...`. Then answer the objection to the
     extra variables in our own terms: `Introducing the estimates ... has two
     advantages. First, ... Second, ...`. A Remark that compares conditions
     with other papers goes after the main theorem, not after the algorithm.
   - **A Remark with an example shows the point of the construction** (the
     equations are decoupled and linked only through $\mathbf w^{1*}$ and
     $\mathbf w^{2*}$; summing them gives back (x)), not a computation the
     lemma already covers. Number its equations with `subequations` when the
     text refers to them one by one (`(13a), (13b), and (13c) can be handled
     by agents $1$, $2$, and $3$ ..., respectively`), and afterwards refer to
     them as a group (`These equations`, `the equations in (13)`). Avoid two
     `together with` in adjacent sentences (`which, by (12a), is ...`).
   - **Derived systems: the full form first, then the special form.** After
     substitution, display the error system with its full block matrix, then
     present the structure as a feature: `It is worth noting that the system
     matrix of the error system is symmetric and negative semi-definite.
     Indeed, the error system can be written as` followed by the numbered
     $-C_{\sigma(t)}^T C_{\sigma(t)}$ form. Do not jump from the substitution
     to the special form, and do not split a stacked state into component
     equations only to recombine them.
   - **Standard facts as in the user's earlier papers.** Do not prove
     $\ker(\hat L^{1/2}) = \ker(\hat L)$; write `In particular, we have ...`
     as in Axb_TAC. Check the user's earlier manuscript before adding a proof
     of a standard fact. Name a Kronecker step (`By (x) and $\hat
     L_{\sigma(t_r)} = L_{\sigma(t_r)} \otimes I_n$, we further obtain ...`).
   - **Setups in one sentence.** `In what follows, we fix a least squares
     solution $\mathbf x^\dagger$ to (1), let ... be the equilibrium of
     system (x) given by Lemma 2, and define the error as` followed by the
     display. Not `... denotes an equilibrium ... for a fixed ...` followed
     by `Then, we define the error between ... and ...`: `Then` is not a
     consequence here, and the display already shows what the error is.
   - **Definitions are not restated as conditions.** A Lemma that gives an
     equilibrium of a switched system says `is an equilibrium of system
     (x)`; `for all $t \ge 0$` belongs in the proof that checks it. The set
     of equilibria is $\bigcap_{t \ge 0}$, tied to the given $\sigma(t)$,
     not $\bigcap_{p \in \mathcal P}$.
   - **Name a key set at its first appearance**, even inside a Remark, when
     the next Lemma uses it (`Hence, every vector in $\mathcal N := \{\ldots\}$
     is an equilibrium ...`), instead of writing the set out in the Remark,
     the lead-in, and the Lemma.
   - **No hedges.** `$\xi(t)$ does not converge to zero in general`, not `is
     not expected to converge to zero`.
   - **Merge a short subsection** into the previous one when it continues
     the same topic; extend that subsection's opening sentence (`... derives
     the error system ... and characterizes its set of equilibria.`) and
     check that no `\ref` points to the removed label.

## Paper skeleton

Use it as a functional order, not a sentence template.

- **Abstract**, about five sentences, single paragraph, no display equation.
  The Abstract is the part outsiders read most, so it must be the easiest to
  understand: use only ordinary expressions that the body also uses (one term
  per object, aligned with the body), and no term that the Abstract itself
  does not explain (not `local term`, `consensus term`, `node`, or `the
  estimates of the local term`; write what is done, e.g., `uses only the
  information that neighboring agents already exchange in the DAC
  algorithm`). Order: what the paper studies; the setting; `Unlike existing results, which require
  A, this paper considers B, provided that C`; `By modeling ... and exploiting
  ..., we establish ... and derive ...`. Keep the system class, network
  condition, convergence property, and gain or initialization restriction that
  limit the headline claim. Do not upgrade asymptotic to exponential, a rate
  bound to an exact rate, or `may` to an established application. End with a
  simulation sentence only when a simulation exists.
- **Introduction**: application background, then why the problem is
  distributed, then prior work grouped by method (each cited paper read first,
  constraint 7), then the limitation, then the gap and why it matters in
  practice, then why the standard analysis fails, then one contribution
  paragraph (`Motivated by ..., this paper studies ...`), then the roadmap
  (`The rest of this paper is organized as follows.`), then a short unnumbered
  Notation paragraph.
  - Literature moves seen in Liu Tao's papers: `Reference [21] first solved
    ...`; `The monograph [2] further strengthened the result of [21] by ...`;
    `Later, reference [12] showed that ...`; `Nevertheless, ... has not been
    studied so far.`
  - Advantages are enumerated inline (`Compared with the existing results,
    our approach offers three advantages. First, ... Second, ... Third, ...`),
    not as a bulleted list.
  - Keep apart: a paper does not study a setting (say so); its theorem proves a
    weaker property (state what it proves); an assumption excludes the setting
    (say the result does not cover it); a checked construction fails (explain
    that obstruction only). `First`, `only`, `all existing`, and `has not been
    studied` need evidence for their scope.
  - Notation lines in the house form: `$\otimes$ denotes the Kronecker product
    of matrices.`, `$\mathbf e$ denotes the base of the natural logarithm.`,
    `For $x_i \in \mathbb R^{n}$, $i = 1, \ldots, N$, $\mathrm{col}(x_1,
    \ldots, x_N) = [x_1^T \ \cdots \ x_N^T]^T$.`, `$\lambda_{\max}(Q)$ denotes
    the largest eigenvalue of a real symmetric matrix $Q$.` Graph notation may
    go to an Appendix, pointed to by a footnote.
- **Problem Formulation**: the setup in words, with a figure if it helps; the
  data and its partition; how graph edges give message access (`the $i$th
  agent can access the information of the $j$th agent at the time instant $t$
  if and only if $(j,i) \in \mathcal E_{\sigma(t)}$`); the objective; a Remark
  right after the objective on what it gives; the Assumptions last.
  - A formal problem in the house form: `Problem 1: Given system (1), the local
    measurements (2), and the switching graph $\mathcal G_{\sigma(t)}$, design,
    for each agent, a local observer of the following form: [display] such
    that, for any initial conditions ..., the solutions of systems (1) and (3)
    satisfy $\lim_{t \to \infty} (\hat x_i(t) - x(t)) = 0$, $i = 1, \ldots, N$,
    exponentially.` Keep apart what is estimated, from which information, for
    which initial conditions, and with which convergence property.
  - Assumption lead-ins: `To achieve the above objective, the following
    assumptions are adopted.`, `We first introduce the following two
    assumptions on the matrix pair $(C, S)$.`, `Next, we impose ... on ...`,
    `Likewise, the following two assumptions are made on ...`.
  - Never strengthen or weaken an assumption for tone: keep `simple` versus
    `semisimple`, discrete- versus continuous-time spectral conditions,
    aggregate versus local observability, compact-set restrictions.
- **Main Results**: the algorithm and a Remark on it, its compact form, the
  technical Lemmas, then the Theorem. Open a subsection with one plain sentence
  on what it establishes (`Before showing X, we establish ...`). Introduce each
  Lemma with one or two sentences on what it gives and why it is needed, and
  define every object it uses before it. Before the theorem, a one-line
  lead-in is enough (`Now, we are ready to establish the main result of this
  paper.`). For an imported result, state its provenance at its introduction
  (`The following lemma is a combination of Lemma~1 of~\cite{a} and
  Theorem~24.7 of~\cite{b}.`) and do not restate it as new.
  - **Theorem statement**: assumptions, system and designed object, essential
    parameter range, guarantee and convergence mode, scope over agents and
    initial conditions. House forms: `Under Assumptions 1 to 3, Problem 1 is
    solvable by designing for each agent $i$, $i = 1, \ldots, N$, a local
    observer of the form (13).`; `Under Assumptions 1, 2, 7, and 8, design
    $L = \mu P^{-1} C^T$, where $\mu$ is any positive constant and ... Then,
    for any initial conditions ..., the solutions of systems (23) and (24)
    exist for all $t \ge 0$ and satisfy ... exponentially.` Keep a gain range,
    an initial-state exclusion, or an invariant-subspace restriction in the
    statement; keep proof-only constants in the proof.
  - **Corollary** lead-in: state the special case and why it fits (`If the
    matrix $S$ is skew-symmetric, then $P = I_n$ solves (3).`), then `Thus, we
    have the following corollary of Lemma 2.`
- **Proof of the main theorem**: state the number of steps (`We divide the
  overall proof into six steps.`), then head each step `\emph{Step k: short
  title.}`. Put `\smallskip` on its own line before each step heading, and
  do not use `\noindent` (nor `\medskip`):

  ```latex
  \smallskip
  \emph{Step 2: Convergence of the tracking gains.} Let ...
  ```

  Cite earlier Lemmas and equations, and keep each step to one purpose. End
  with one closing sentence (`Therefore, ..., and the proof is complete.`) and
  the paper's proof-end symbol. Follow with a Remark on what the proof shows
  and what it gives beyond the theorem, such as an explicit rate bound (a
  proved lower bound, not an exact or arbitrarily assignable rate).
- **Numerical example**: the data and network; which assumptions hold and why;
  invoke the theorem; plot exactly the error the theorem bounds; report the
  constants used. Describe the network and a periodic switching signal in the
  user's own form below. Never write `a cycle of N agents`, and never describe
  the switching signal in prose (`sigma(t) takes the values 1, 2, 3 on
  [0,0.5), [0.5,1), ...`):

  ```latex
  We consider the double-layered network of Fig.~\ref{fig-network}, in which
  the first cluster contains two agents, the second contains three agents, and
  the third contains four agents. The intra-cluster graphs $\mathbb G_i$,
  $i = 1, 2, 3$, are all connected. The switching inter-cluster graph
  $\mathcal G_{\sigma(t)}$ is given in Fig.~\ref{fig-switching} and is
  dictated by the following switching signal:
  \begin{equation*}
  	\sigma(t) = \begin{cases}
  		1, & \text{if } (s + 0) T_{\mathrm c} \leq t < (s + \frac13) T_{\mathrm c} \\
  		2, & \text{if } (s + \frac13) T_{\mathrm c} \leq t < (s + \frac23) T_{\mathrm c} \\
  		3, & \text{if } (s + \frac23) T_{\mathrm c} \leq t < (s + 1) T_{\mathrm c}
  	\end{cases}
  \end{equation*}
  where $s = 0, 1, 2, \ldots$ and $T_{\mathrm c} = 1.5$. Thus, Assumption~\ref{ass}
  is satisfied.
  ```

  Adapt the cluster sizes, the number of cases, $T_{\mathrm c}$, and the
  labels to the manuscript, and keep its own graph terms (write
  `communication graph` only if the manuscript does). Before `Thus`, add the
  reason the assumption holds when it is not obvious (for example, that each
  graph has a single edge, so the inter-cluster graph is disconnected at any
  time instant; Liu Tao's form notes that the assumption holds even though
  the graph is disconnected at every time instant). Keep $s$ as the period index; if $s$ already denotes
  another quantity in the same section, rename that other quantity. The rest
  of the example follows Liu Tao's order:
  - verify the system assumptions from the data (`The eigenvalues of the
    matrix $A$ are $\{\pm j, 0\}$, and the pair $(C, A)$ is observable. Hence,
    Assumptions 1 and 2 are satisfied.`), and give any matrix the design
    needs (`a symmetric and positive definite solution to (38) can be found as
    follows:`);
  - invoke the theorem (`By Theorem 1, we can design ... with ... and any
    $\mu > 0$.`);
  - report the simulation constants (`The simulation of the closed-loop system
    is performed with $\mu = 1$, $T_{\mathrm c} = 8$, and randomly generated
    initial conditions.`); a computed constant feeds the rate Remark
    (`Through calculation, we find that $\alpha_1 = 0.0206$ satisfies (9).
    Thus, according to Remark 3, ...`);
  - narrate figures by the property they show (`Fig. 2 shows ..., and Fig. 3
    further shows ...`), not `the effectiveness is obvious`. Every figure has a
    caption.
- **Conclusion**: a recap in present perfect (`In this paper, we have
  established ... Then, ... Moreover, ...`) in the same order as the
  Abstract's contribution, without new claims or notation; then, if supported,
  a stated restriction and one specific direction. Match the wording to its
  status: a possibility (`It would be interesting to ...`), a plan, or work
  confirmed under way (`Currently, we are working on ...`, `... are under
  way.`). Never invent future work.

## Proofs

- **Applying an earlier result to a new system** (Liu Tao's standard move,
  required by constraint 11): put the current system in the form of the
  earlier one and name every substitution, check each hypothesis of the
  earlier result in turn, then conclude.
  `It can be seen that system (21) is in the form of system (2) with
  $S = -A^T$, $C = B^T$, and $L = \mu P_{\mathrm d} B$. First, under
  Assumption 5, ... Second, ... Third, ... By Lemma 2, system (21) is
  exponentially stable.` A related form: `Then, system (25) with the output
  (26) is in the following form: [display]`.
- **Stacking equations**: `Let $\tilde\theta(t) = \mathrm{col}(\tilde\theta_1(t),
  \ldots, \tilde\theta_N(t))$. Then, the $N$ equations in (10) can be put into
  the following compact form:` followed by the display.
- Before using any result, verify that its object matches the current
  (transformed) system, that dimensions and time domain match, that every
  hypothesis has been established, and that its conclusion is strong enough
  (asymptotic, exponential, uniform, global are not interchangeable).
- For a cascade or perturbed error system, establish the homogeneous
  system's property and the forcing estimates separately, then return from
  transformed variables to every advertised target; parameter convergence
  alone does not close the state error.
- A display needs a grammatical predicate: `By (5), we have [display]`,
  `Substituting (5) into (4) gives [display]`, `Taking norms, we obtain [display]`.
  Never `Taking norms, [display]` or `Hence, by (5), [display]`.
- A constant is defined where it first appears, in the `where` clause of the
  first display that uses it, even inside an Appendix proof (`where $\bar m
  := \max_{i \in \mathcal K} \| \Pi_i M_i \Pi_i \|$`); a later proof cites
  that definition. Give a display a label and cite it instead of writing `the
  above inequality` or `the last term above`.
- Review before delivery: symbols defined before use; dimensions preserved;
  every inequality has its reason; each assumption is used or declared only
  for scope; boundedness and existence before limits; the last sentence
  matches the theorem's exact convergence property; no claim deferred to a
  reference that proves something weaker.

## Writing choices

- Prefer concise declarative sentences with an explicit subject and finite
  verb. Split independent claims and keep each condition attached to what it
  limits. Prefer a verb to a nominalization (`we estimate`, not `we perform
  the estimation of`).
- Judge modifiers by function. Keep mathematical qualifiers (`global`,
  `uniform`, `sufficiently small`, `exponentially`); remove unsupported
  praise and intensifiers. A grounded comparison is fine.
- Sentence-initial `-ing` is a conditional choice, not a ban. Fix dangling
  modifiers and cumbersome openings; keep concise, well-attached ones
  (`Using (5), we obtain`).
- Use `we`, passive voice, prospective `will`, and long sentences by function.
  Never enforce a fixed sentence length, Remark count, or future-work
  paragraph. Present tense for mathematical facts and the paper's results;
  past or present perfect for prior work and for the Conclusion.
- In a list of three or more items, put a comma before the final `and` or
  `or`: `$\mathcal G_1$, $\mathcal G_2$, and $\mathcal G_3$`;
  `By (19), (49), and (57), we have`. Two items take no comma:
  `(5) and (6)`. Index lists inside mathematics (`$i = 1, 2, 3$`) are not prose
  lists. When revising, fix every such list in the passage.
- Name the object before an equation number whenever the number refers to a
  system, an output, a state, an algorithm, or another defined object:
  `the observability Gramian of system (43)`, `the solutions of systems (23)
  and (24)`, `a local observer of the form (13)`. Write `system (43)` with no
  article. A plain equation used in a derivation keeps the bare number:
  `By (5), we have`.
- Use plain connectors for real logical steps: `Thus`, `Hence`, `Then`,
  `Next`, `Moreover`, `Specifically`, `To begin with`, `Now`. Use `It can be
  verified that` only for a purely mechanical check the reader can redo in one
  line; never for a step that needs an inequality or a choice of constant.
- No explanatory asides in parentheses; rewrite them as a clause. Equation
  labels and citations in parentheses are fine.
- Keep essential validity conditions visible in the formal statement;
  proof-only constants belong in the proof.

## Notation, terminology, and formatting

- One concept, one word, throughout the paper; one object, one symbol with the
  same subscripts everywhere. When two words compete, keep the one used
  earliest or most often and replace every occurrence of the other.
  Before writing a sentence that names an object already introduced, look up
  the word the manuscript used when it introduced that object, and use that
  word; do not switch to a synonym that feels natural in the local context
  (这种错误不要再犯了). When a new object shares a set with an earlier one
  (a tree on the agents' node set), it uses the same word, so that the reader
  sees it is the same set. Before returning any text, search it for each
  synonym pair the manuscript could mix (node/vertex, agent/node, edge/link,
  graph/network) and fix every occurrence, including text already agreed
  earlier in the session.
  Before writing a sentence that names an object already introduced, look up
  the word the manuscript used when it introduced that object, and use that
  word; do not switch to a synonym that feels natural in the local context
  (这种错误不要再犯了). Example: Section II defines `$\mathcal V = \{1, 2,
  \ldots, c\}$ is the node set`, so the tree $\mathcal T$ on the same set is
  `a fixed tree with the node set $\mathcal V$`, `a tree with $c$ nodes`,
  `edge $l$ leaves node $i$`, and `have node $i$ as an endpoint`, never
  `vertex`, even though graph theory books say vertex. When a new object
  shares a set with an earlier one (a tree on the agents' node set), it uses
  the same word, so that the reader sees it is the same set. Before
  returning any text, search it for each synonym pair the manuscript could
  mix (node/vertex, agent/node in prose, edge/link, graph/network) and fix
  every occurrence, including text already agreed earlier in the session.
- Defaults for the user's own manuscripts on double-layered or switching
  networks (do not apply them to change supplied mathematics):
  - `node` for the elements of $\mathcal V$ in every graph of the paper,
    including a tree or auxiliary graph on the same set (as in the user's
    Axb_TAC and in Liu--Huang SICON 2025: `the node set`, `node 0`); never
    `vertex`.
  - `node` versus `agent` for the elements of $\mathcal V$: `node` only in
    pure graph-theoretic definitions (`$\mathcal V = \{1, \ldots, c\}$ is the
    node set`, `a fixed tree with the node set $\mathcal V$`, `a tree with $c$
    nodes`, `edge $l$ leaves node $i$` in the incidence matrix); `agent`
    everywhere the text describes the algorithm or the analysis (`For each
    agent $i \in \mathcal V$, let $\mathcal I_i$ ... be the set of the edges
    of $\mathcal T$ that have agent $i$ as an endpoint`, `the two agents at
    the endpoints of edge $l$`). Never `vertex` (Axb_TAC and Liu--Huang SICON
    2025 use `node set`, `node 0`). A bare index in prose takes its name:
    `For each agent $i \in \mathcal V$`, not `For each $i \in \mathcal V$`.
  - `network` for the communication structure, never `topology` as a
    standalone noun; modifiers attach to `graph` (`inter-cluster graph`,
    `switching inter-cluster graph`); only `double-layered` attaches to
    `network`; `over` for graphs and networks.
  - `reconstruction` for the recovery mechanism's objects; `tracking` only in
    `dynamic average tracking`; `reconstruct` (recover the aggregate input in a
    cluster) and `realize` (make the ideal observer distributed) are distinct.
  - `semisimple with zero real parts` for neutral stability in the user's
    observer manuscripts; keep `simple` when a supplied or cited text says so.
  - `tunable`, not `adjustable`; `perturbation` for the forcing term, `mismatch`
    for its source, no `residual` between them; no `surrogate`.
- Graph symbols: intra-cluster graphs `\mathbb G_i`; inter-cluster switching
  modes `\mathcal G_p` (not `\mathcal G_{(p)}`); the active graph
  `\mathcal G_{\sigma(t)}`.
- List a family inline as `$x_{ij}$, $j = 1, \ldots, k_i$,`, not
  `$\{x_{ij}\}_{j=1}^{k_i}$`.
- State a symbol's dimension only where it first appears
  (`there exists $\eta \in \mathbb R^{d_P}$ such that ...`), not again in
  later sentences or in the `where` clause of a later display.
- `\quad`, not `\qquad`, between an equation and its qualifier. Upright labels
  in subscripts (`T_{\mathrm c}`). One environment-name casing. `\appendices`
  for several appendices. Hyphenated labels (`eq-thm-rate`, `lem-`, `thm-`,
  `ass-`, `rem-`); after renaming a label, check every reference to it.
- No trailing comma on a display equation, even if a reviewer suggests it.
- A vector stacked over all agents by `\mathrm{col}` is bold, with the letter
  of the agent quantity (`x_i` → `\mathbf x`, `r_i` → `\mathbf r`). For a
  lowercase Greek letter use `\boldsymbol`
  (`\boldsymbol\varepsilon := \mathrm{col}(\varepsilon_1, \ldots,
  \varepsilon_c)`), because `\mathbf` does not bold lowercase Greek letters;
  say so when the user asks why the two commands differ. An error defined as a
  difference (`e_x := \mathbf x - \hat{\mathbf x}`) and the whole error state
  $\xi$ are not bold.
- Avoid a letter that suggests another role: a residual `e_i` reads as an
  error when the errors are `e_x`, `e_r`, `e_w`. Rename the residual
  (`\varepsilon_i`, `\varphi_i`) and choose the renaming that touches the
  fewest later sections.
- Once notation is unified (`\mathcal C` → `\mathcal V`, neighbor index `k`
  → `j`), apply it in every passage handed back, including sentences
  carried over unchanged.
- A definition the reader may need (`semisimple`) may go in a footnote with its
  source (`see Definition 1.4.3 of [5]`).

## Mathematical correctness (non-skippable)

Before presenting any derivation, citation, assumption, or numerical value:

- **Numbers and identities.** Numerically check every nontrivial identity,
  bound, rank, decomposition, or spectral claim (random or structured
  instances; several values for a scaling claim). Recompute every quantity in
  a numerical example and confirm the example satisfies each assumption it
  illustrates. Never write a number from memory. When the algebra and a clean
  closed form disagree, chase the discrepancy.
- **Citations.** Confirm each `\cite` key resolves to the right entry and the
  body and bibliography agree; confirm the content against the source
  (constraint 7); when citing a precedent for an assumption, confirm the
  source assumes the same thing, not a stronger or weaker cousin. State an
  unpublished or concurrent paper's status plainly. Never invent an
  attribution, venue, volume, page, or result.
- **Assumptions against proofs.** Trace where each hypothesis is used; check
  it is neither too strong (excludes legitimate cases) nor too weak (the proof
  secretly needs more); check that a Remark's restatement of an assumption is
  actually equivalent to it.
- **Dimensions and indices.** Every product, Kronecker product, `col`, and
  `blockdiag` conforms; partitions cover the whole state; left/right and
  transpose placement are right; subscripts are consistent across sections.
- **Internal consistency.** A lemma's proof delivers the stated form; the
  Abstract and Conclusion match the body; every cross-reference resolves.

Analytic reasoning proves; numerical checks only supplement. Verify what the
requested passage asserts, not the whole paper. If an item cannot be
satisfied, tell the user as an open question instead of smoothing it over.

## Response letters

- Keep the previous submission and the revised manuscript strictly apart.
  Never reword the reviewers' comment text. Annotate previous-submission
  numbers inline in the advisor's format, in every comment:
  `(6) and (7) ((8) and (9) of the revised manuscript)`,
  `[23] (reference [17] of the revised manuscript)`, or
  `(of the previous submission)` when there is no counterpart.
- In each reply, first state the issue in terms of the previous submission,
  then what the revised manuscript does. Label items `of the revised
  manuscript` wherever numbers could clash (both versions have a Fig. 6).
- Use exactly the manuscript's own wording for its concepts (`reduces to`, as
  in the manuscript, not a coined noun such as `degeneration`), and keep such
  expressions consistent across all replies.
- Cite papers not in the manuscript's reference list as [R1], [R2], ..., with
  exact results (`Lemma~3.1 of [R1]`), and list them at the end of the
  response:

  ```latex
  \begin{enumerate}[label=\textbf{[R\arabic*]}]
  	\item A. Author and B. Author, ``Title,'' \emph{Journal}, vol. 1, no. 2,
  	pp. 3--4, 2025.
  \end{enumerate}
  ```
- Constraints 1, 2, 7, 8, 12, and 16 apply to response letters as to the
  manuscript; every statement about a cited work is checked first.

## Scope

- Work only on the passage or module requested. Do not turn a drafting request
  into a whole-paper novelty or proof audit.
- Return the drafted or revised text first, then only brief notes on missing
  information or claim risks that affect it. If the user asks only for
  analysis, do not rewrite. Do not modify the user's files without permission.
- Do not ask the user for a claim map. Infer the minimum structure the passage
  needs: closest result, obstacle, mechanism, formal guarantee, scope.
- For a template-derived draft, treat inherited text as context and revise
  only the requested region.
- State novelty as an exact property change when the passage compares. Keep
  the same contribution decomposition (obstacle -> mechanism -> guarantee)
  across the Abstract, Introduction, and Conclusion, and order definitions,
  lemmas, and claims by dependency. Keep formal statements lean; put
  interpretation, comparison, design meaning, and limitations in Remarks or
  surrounding prose.
- When unifying terminology or notation at the user's request, fix every
  occurrence in the document.
- In Chinese discussion, keep an English technical term when translation would
  blur it (`tone`, `claim`, `roadmap`).

## Corpus notes

The patterns above were checked against these papers in the Zotero collection
"Liu Tao's" (item keys in brackets):

- SICON 2025, duality and exponential stability of two classes of linear
  switched systems [YARABNQX]: assumption lead-ins; hypothesis matching in the
  proof of Lemma 3; rate Remark 3; numerical example with the cases form of
  $\sigma(t)$; Conclusion with work under way.
- IEEE TAC 2025, uniform observability w.r.t. subspaces [8Y9SFBV8]: Notation
  defines bold zero matrix; bold zero for matrix and row-vector expressions
  ($u^T \mathbf F(t) = \mathbf 0$ in (5), $U^T \Phi_x(t, s) \mathbf F(s) =
  \mathbf 0$ in the proof of Lemma 2, $S^T Q + Q S = \mathbf 0$ in (23),
  $\mathbf 1_N^T L_{\sigma(t)} = \mathbf 0$) but plain zero for column-vector
  equations ($U^T w(t) = 0$, $\mathbf C \mathbf A^k v = 0$), checked on the page
  image; the `where we have used ...` chain after (18);
  condition-by-condition proof of Theorem 2; cases form of $\sigma(t)$ with the
  disconnected-graph reason.
- Automatica 2024, distributed exponential state estimation [NQPNIMGV]:
  Problem 1 and Theorem 1 forms; bold zero blocks in (6) and (14); bold
  $\mathbf A = \mathbf 0$ in the proof of Lemma 2; plain 0 in
  $\ker(A) = \{x \in \mathbb R^n : Ax = 0\}$, in the column-vector equation
  (22), and in limits.
- IEEE TAC 2025, discrete-time adaptive distributed observer [DPPBU3JW]:
  `is in the form of system (18) ... with ...`; compact form of $N$ equations;
  coefficient expansion with `=:` in (5).
- IEEE TAC 2024, adaptive distributed observer for uncertain leaders
  [8R4ASWG4] (keyword check only).

Features of these papers that the constraints override: a forward reference
(SICON 2025, Remark 2 points to Remark 7); adjacent Remarks (Automatica 2024,
Remarks 6--8; SICON 2025, Remarks 3 and 4); `it is clear` or `by simple
calculation` in place of a step; a proof omitted as similar to another
paper's; naming a system with `we call`; the IEEE form `[3, Thm. 6.4]`.
These are coauthored papers; do not infer who wrote which sentence.

## Before returning text

Quietly check claim fidelity, dependency order, terminology consistency, and
repetition. Check constraints 1 to 24; in a proof, check that no two
consecutive sentences share the form `..., we have ...` and that every
equation operated on or cited later has a number (constraint 23); for each
sentence of the main text,
ask whether it is a mathematical statement that a later step uses, and move
the rest to a Remark or delete it (constraint 22); read each paragraph as a reader who
has not seen the derivation and check that its purpose or conclusion comes
first (constraint 17); in a proof, reread every line and ask
whether its reason is written (constraint 11). Check that no new name or
acronym was added, every named object carries its symbol and every symbol in
prose its name (constraint 19), no sentence, carried over or new, has a
comparison without its object or an unclear referent (constraint 22), no two Remarks are adjacent, no obvious sentence remains in
a Remark, zeros follow constraint 13, every list of three or more items has a
comma before the final `and` or `or`, every equation number referring to a
system or other object carries its noun, citations use `Lemma 1 of [17]`,
modifiers attach correctly, and compression kept every technical qualifier.