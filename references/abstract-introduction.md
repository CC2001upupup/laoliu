# Abstract and Introduction

## Abstract

### Select content before imposing an order

Represent the supplied problem, actual contribution, and established result
with the fewest claims that retain their meaning. A checked prior limitation,
technical mechanism, comparison, independent result, application, or example
belongs here when it helps distinguish the paper. None is a mandatory slot.
An Abstract is not a miniature Introduction or a list of theorem statements.

Eight of the 14 Abstracts open with prior work; six open directly with the
present problem or contribution. Choose by relevance, not by recency alone.
Do not add an importance paragraph, an unsolved-problem assertion, or an old
method's failure merely to lead into the work.

Use the following as content-selection alternatives, not sentence templates:

- **An extension:** identify the closest supported result and the precise
  change. The contribution may modify a design, strengthen its analysis, or
  change an admissible condition. A weaker prior theorem does not establish
  method failure; new analysis does not necessarily mean a new algorithm.
- **A direct design or application:** state the object and setting, the
  construction that matters, and what it achieves. A prior-work opening is
  optional, as is a detailed preview of the construction.
- **Dependent stages:** show what one stage supplies to the next and what the
  composition achieves. `First/Second` can mark actual stages, but can also
  enumerate limitations or properties. Several advantages do not create
  several design steps. A single change may address several limitations.
- **A concept or theorem result:** distinguish establishing a property of an
  existing concept from introducing a concept. Preview property -> enabling
  result -> application when that is the actual dependency. Do not claim the
  concept is new, insufficient, or renamed without supporting input. The
  no-coinage requirement still applies.

The guarantee may precede its enabling analysis, as in C10, or follow a
construction, as in C13. Keep the logical link readable without forcing one
universal mechanism-before-result order.

### Compress without broadening

Retain the system class, information pattern, network condition, convergence
property, or gain/initialization restriction that materially limits the
headline claim. A short separate scope sentence is useful when it prevents a
long qualification chain. Do not reproduce every assumption or drop a decisive
one; `a class of systems` alone does not repair an otherwise overbroad claim.

Keep the objects of estimation and guarantees distinct. A result for an
intermediate estimator does not automatically establish the same property
for every downstream estimate. State only the supplied or checked composition
result. Do not upgrade convergence to exponential convergence, a rate
characterization to an arbitrarily assignable rate, or robustness to small
disturbances to a noise-independent guarantee. Preserve `may` when a possible
use is not an established application.

Use comparison to expose a particular difference, not superiority on every
axis. Prior solutions to the application can coexist with a useful new proof
or implementation. Keep any decisive remaining restriction. The Introduction
claim-strength distinctions below apply here too; compression is not a reason
to turn `may not apply` into `cannot work` or to add unchecked firstness.

### Ending and presentation

End with the result that best completes the paper's account: a scoped
guarantee, a specific advantage, an additional theoretical result, a proved
application, or an illustrative example. Only 5/14 Abstracts end with an
example or simulation. Do not append a stock simulation sentence when none
was supplied, or turn an illustration into proof of a universal theorem.

The sampled Abstracts are single paragraphs with 4--9 sentences. These are
descriptive observations, not sentence or word limits. Follow the user's and
venue's actual format and length requirements. No sampled Abstract contains
a display equation; avoid derivations and symbol-heavy machinery by default,
not a necessary technical condition or a requested quantitative result.

Avoid citation catalogues. A concise attribution may be appropriate when an
existing concept's provenance matters and the venue permits it; C14 contains
one. Verify the source, and do not copy its citation format as a universal
house rule. Do not invent a reference or remove attribution to imply novelty.

### Wording, syntax, and grammar

Choose technical verbs for the actual contribution: `establish`, `show`,
`estimate`, `design`, `modify`, `apply`, or `strengthen`. Use `propose` for a
proposal, not automatically for a new proof of an unchanged design. Reuse
established terms instead of adding names or acronyms to shorten the Abstract.
Keep technical modifiers; replace unsupported praise with the supplied
difference. Corpus uses of `novel`, `interesting`, or `much simpler` do not
make those words obligatory or automatically justified.

Give distinct assertions distinct sentence jobs where it improves readability.
Preserve a condition-result or stage-dependency relation when splitting would
obscure it. Recent examples include both 9 short sentences (C12) and a
52-token causal sentence (C09); neither sets a template or threshold.

Author, method, system, and result subjects all occur. `We` appears in 10/14
Abstracts, and passive constructions occur throughout the sample. Present
tense is economical for stated contributions; past and present perfect can
locate prior work. Prospective `will` appears in C02, C03, and C14 and can
preview an actual derivation; it must not disguise unfinished work as a result.
Only one of 83 sentences has the sampled initial `-ing` construction, C14's
`Leveraging ...`. Keep an economical, correctly attached opening rather than
enforcing a ban. Apply [language-style.md](language-style.md) for the shared
lexical, syntactic, and grammatical checks; do not imitate source errors.

## Introduction

### Choose an entry and a local argument

Establish enough context to make the target problem and contribution legible.
The corpus enters through applications or field development, a problem/tool
definition, an information constraint, a concept's role, or the closest prior
result. Choose the entry suited to the paper; do not force an importance
paragraph or invent a broad growth claim. A narrowly focused extension can
start with its predecessor; a concept paper need not invent an application
motivation before explaining the concept.

Use context -> relevant literature -> gap -> contribution as a useful local
argument, not a fixed sequence of paragraphs. Literature, obstacles, and
comparisons may recur after the objective or design preview when they explain
a component's origin or a specific trade-off. Keep each return purposeful.

A concise existing model or technical definition may appear here when it is
needed to distinguish the settings being compared. Do not automatically move
it to Problem Formulation, or expand the Introduction into full assumptions
and derivations. Keep Notation/Nomenclature distinct from the argument even
when the venue places it inside the Introduction's section boundary.

### Literature synthesis

Organize sources by the capability, assumption, or mechanism that matters to
the present question. Useful contrasts include:

- static versus switching networks;
- state-based versus output-based information;
- asymptotic versus exponential convergence;
- continuous versus discrete time;
- centralized versus distributed construction;
- known versus uncertain parameters.

Chronology is useful when it traces an actual capability change; the corpus
also combines historical stages with these contrasts. Do not mechanically
sort citations by year or discuss each paper with an identical sentence.

Locate the citation beside the particular claim it supports. Preserve the
source's setting, information requirements, and guarantee. Distinguish a
description of a cited result from the present authors' interpretation of its
limitations. Never copy a source Introduction's literature judgments as newly
verified facts about the whole field.

### Gap and claim strength

Identify what is missing relative to the closest supported result: a setting,
an information pattern, a guarantee, an implementation property, or a useful
property of an existing concept. A gap need not mean that nobody has solved
the application before; a different proof route or a specific design advantage
can be the contribution.

Do not treat these statements as interchangeable:

| Evidence available | Appropriate scope of claim |
|---|---|
| A cited paper does not study a setting or property | Say it does not address that item; do not infer method failure. |
| Its theorem establishes only a weaker property | State the guarantee it establishes; do not infer the method cannot do better. |
| A stated assumption excludes the target setting | Say the reported result does not cover the target setting. |
| A verified construction or proof dependency fails in that setting | Explain that specific obstruction and its conditions; do not generalize to every variant of the method. |

Explain a technical obstacle when the manuscript or checked source supplies
one. A concrete gap plus the new mechanism can suffice without a separate
proof-obstacle paragraph. Do not manufacture impossibility, an unproved
failure mechanism, or `challenging` language to fill a template. A precise
technical question is permissible if it identifies a task the paper answers.

`First`, `only`, `all existing`, and `has not been studied` are substantive
literature claims, not tone markers. Use them only with adequate evidence for
the stated scope. `To our knowledge` does not make an unchecked claim sound.
With incomplete source coverage, retain a narrower supported comparison or
flag the one claim needing verification; do not fabricate references or turn
a passage request into an unsolicited literature survey.

### Contribution and comparison

State the actual action and what it establishes. When there are dependent
stages, show what the first supplies to the next and what the composition
achieves. For a single modification, describe that modification directly;
several removed limitations need not imply several design stages or separately
named contributions. Use only terminology already established or supplied.

Connected prose is the observed default: none of the 14 Introductions uses a
visually separate numbered/bulleted contribution list. Inline `First/Second`
may enumerate limitations, design operations, advantages, or explanatory
points; these are different functions, not interchangeable contribution items.
Do not force a fixed count or list. An explicit user/venue request for a list
takes priority over this corpus preference.

Compare by the changed property while retaining the conditions that define
it. A simpler construction or distributed implementation is not superiority
on every axis. Acknowledge a relevant advantage of the alternative if needed
for a fair comparison. Do not upgrade `asymptotic` to `exponential`, a rate
bound to an exact rate, or a gain/initialization restriction to no restriction.
Do not delete a remaining system-class condition to make the contribution
sound broader. An unchanged estimator with a new analysis is not a new design.

### Wording, syntax, and grammar

Use direct technical verbs for author actions and let a method, property, or
result serve as subject when it clarifies the relation. Past tense can recount
specific prior work; present perfect can summarize a development or a scoped
research gap; present tense can state capabilities and contributions;
prospective `will` can preview the paper's actual derivation. No single tense
or subject is mandatory throughout the Introduction.

Use contrast, cause, and sequence only for the relation established by the
content. Preserve the scope of `only`, `not every`, `none`, `may not apply`,
and `does not address`. Keep necessary technical modifiers. Gerund subjects,
participial openings, and `By + -ing` all occur; apply the attachment and
concision checks in [language-style.md](language-style.md), not a word ban.
Grounded evaluation is possible, but do not transplant praise, superlatives,
or source-paper grammatical errors merely to imitate tone.

### Roadmap

Section-by-section roadmaps occur in 13/14 Introductions; C10 omits one while
still previewing the proof dependencies. Treat a paper roadmap and a technical
design/proof preview as different devices. Include a concise roadmap when
useful for the supplied section structure; describe what sections accomplish.
Omit it when unnecessary, requested, or when writing only a local passage.
Never invent section numbers, an Appendix, or an application to complete it.
