# Terminology Consistency

> **Scope note.** The established choices below are defaults for the user's
> own manuscripts on distributed estimation over double-layered / switching
> networks. They are not universal replacement rules: never alter a supplied
> mathematical property (e.g. `simple` versus `semisimple`, continuous- versus
> discrete-time spectral conditions, the object of an observability condition)
> to match this list. Keep the supplied mathematics and flag the discrepancy.
> The core rule — one word per concept — applies everywhere.

## The core rule

**Within a paper, each concept gets exactly one word.** Never alternate between
near-synonyms for the same thing. Choose a term on first use and hold it to the
last line. If two words could mean the same thing in the manuscript, that is the
signal to pick one and purge the other from the whole document.

Reviewers read inconsistent terminology as imprecision. A single concept wearing
three different names across three sections makes the writing look careless even
when the math is sound.

**This rule is the point. The list below is examples of the rule in action, not
a closed catalogue.** When a new concept appears, apply the same discipline:
choose one word, define it once, use it throughout, and never let a synonym
creep in.

## Established choices (extend this list; do not treat it as finished)

- **"network" for the communication structure — never "topology" as a
  standalone noun.** Write "double-layered network", "switching network". The
  bare noun "topology" is banned. Modifiers attach to "graph": "inter-cluster
  graph", "intra-cluster graph", "switching inter-cluster graph". Only
  "double-layered" attaches to "network".
- **Preposition: "over" for graphs and networks.** "over jointly connected
  switching graphs", "over double-layered networks", "estimation over a switching
  network". Do not drift to "on" or "under" for this relation.
- **"reconstruction" for the recovery mechanism's objects** — "reconstruction
  mismatch", "reconstruction gain", "reconstruction error / variable". Do **not**
  call these "tracking ..." The only place "tracking" survives is the fixed
  mechanism name **"dynamic average tracking"**.
- **Verb split, not interchangeable:** **"reconstruct"** = recover the aggregate
  observer input within a cluster; **"realize"** = make the ideal observer
  distributed (the architecture-level act). Keep them distinct.
- **"semisimple with zero real parts" for neutral stability in the user's own
  observer manuscripts.** There "simple" (algebraic multiplicity one) would be
  strictly stronger and wrongly exclude repeated imaginary eigenvalues. This is
  a mathematical choice made for those papers, not a spelling rule: when a
  supplied text or cited result states `simple`, keep it and ask if in doubt.
- **"tunable" — not "adjustable".** One word for "the rate can be set by the
  gain profile."
- **"perturbation" for the forcing quantity (e.g. $d$); "mismatch" for its
  source.** These name two different things (the term in the error equation vs.
  the reconstruction disagreement that causes it). Do **not** introduce
  "residual" as a third synonym floating between them.
- **Banned standalone nouns:** "topology", "surrogate". (And avoid vague
  intensifiers the prose does not need.)

## When unsure which word to keep

If you catch two candidate words for one idea, do not deliberate at length —
pick the one already used earliest or most often, then **search the entire
document for the rejected word and replace every occurrence.** Half-converted
terminology is worse than either choice made consistently.

## Mechanism and object names, once fixed, are fixed

Once the paper commits to a name for a recurring object (a stacked vector, a
gain, an error), that exact name is used everywhere — same word, same symbol,
same subscripts. Do not let a section reintroduce the concept under a fresh
label. The name must already be established or user-supplied: this skill never
coins one (see SKILL.md).
