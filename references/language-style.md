# Lexical, Syntactic, and Grammatical Style

Apply these choices within the requested passage. Do not turn language revision
into a whole-paper audit or require a terminology spreadsheet from the user.

## Evidence and priority

Keep three sources of guidance distinct:

- **Corpus observations:** the 14-paper reanalysis found technical modifiers,
  evaluation, several types of `-ing` openings, and naming acts. None of these
  is universally absent. The papers are coauthored; do not infer personal
  psychology or individual sentence authorship.
- **Editorial recommendations:** prefer direct verbs, clear main assertions,
  stable terminology, and economical phrasing. These choices guide revision;
  they are not mechanical deletion rules or uniqueness claims.
- **User constraint:** do not autonomously create technical names or terms.
  This remains binding even though the corpus contains descriptive naming.
  The user's impressions about adjectives, adverbs, and `-ing` were hypotheses
  to test, not permanent prohibitions after contrary evidence was found.

The comparable language sample is 14 complete Abstracts: 83 sentences and
2,009 lexical tokens. Early versus recent per-paper mean sentence length is
26.9 versus 23.2, with long recent sentences still present. Automatic ADJ rates
per 1,000 tokens are 116.6 versus 114.1; ADV rates are 40.8 versus 46.1.
These POS estimates do not count decorative wording and do not support a
general decline in modifiers. There is no other-author baseline.

One of the 83 Abstract sentences has a target `-ing` opening. Body retrieval
confirmed 48 examples in 12 papers: 17 participial supplements, 16 gerund-clause
subjects, and 15 preposition-plus-`-ing` clauses. These are retrieval lower
bounds, not full-text frequencies. Recent counterexamples include `Leveraging
...` (2025, uniform-observability paper, Abstract) and `Noting that ...`
(2024, uncertain-linear-leader observer paper, PDF p6).

Grammar correctness is not a personal style trait. Keep lexical choice,
syntactic organization, and grammatical form as separate primary categories;
check semantic fidelity across all three rather than counting it three times.

## Lexical choices

### Existing terms only

Never invent a name for a method, object, condition, transformation, or proof
step. A compound made of familiar words is still a coined term if it is newly
introduced as the name of a concept. Hyphenation, capitalization, quotation
marks, `we call ...`, and a new acronym do not make that acceptable.
This prohibits new technical designations, not ordinary nouns. It does not
assert that every source-paper designation is historically original: the
corpus alone cannot establish terminology's first use.

Use terminology already established in the field, in the supplied sources, or
explicitly named by the user. Keep its meaning and spelling consistent. Do not
rename an existing object for rhetorical variety. Do not create a new synonym
or acronym for it. Mathematical symbol definitions remain possible when the
task requires them; they do not authorize an invented verbal name.

When the status of a proposed technical term is uncertain, use an ordinary
sentence stating what the object does, or refer to the object by its existing
symbol/equation. Do not interrupt routine writing to research a new name. If a
new formal name is indispensable to the user's requested task, ask the user
to supply it rather than proposing one autonomously.

### Plain words and verbs

Prefer `use`, `show`, `define`, `choose`, `satisfy`, `imply`, `obtain`, `bound`,
and `converge` when they express the intended action. Prefer `we estimate x`
to `we perform the estimation of x`. Preserve established nouns such as
`observability` and `persistent excitation`; reducing nominalization is not
a ban on existing technical nouns.

### Adjectives and adverbs

Classify a modifier by its function before editing:

1. Mathematical restriction: retain it if it changes the object or claim.
2. Logical or discourse relation: retain it when the relation is real.
3. Comparison or evaluation: check its object and supplied evidence.
4. Degree or emphasis: remove it when it adds only unsupported intensity.

Do not add ornamental praise such as `remarkably powerful`. Prefer the
particular demonstrated difference to `significantly better`, when that
difference is supplied. A supported `simpler` comparison may remain; do not
invent a complexity analysis to make it specific. Words such as `clearly` and
`interestingly` are not automatically errors, but often add no information.
They must never replace an unstated proof step. Recent source Abstracts contain
`novel` (2023, discrete-time state-estimation paper) and `much simpler` (2025,
uniform-observability paper); presence refutes a ban, not establishes merit.

Retain modifiers that change the proposition: `global`, `uniform`, `distinct`,
`unknown`, `positive definite`, `exponentially`, `almost surely`, `locally`, and
`sufficiently small` can be essential. Do not replace a precise compound term
with a vague shorter description. Logical transitions such as `hence` and
`therefore` may remain when they express an actual inference.

The decision is semantic: if deletion changes the mathematical property,
quantifier, rate, or scope, keep the modifier. Do not apply a blanket POS filter.

## Sentence structure

- Prefer a direct subject and finite verb: `The estimator uses ...`,
  `We define ...`, `Lemma 2 implies ...`.
- Distinguish three constructions before judging an `-ing` opening:
  a participial supplement (`Using (5), we obtain ...`), a clause acting as
  subject (`Choosing the gain changes ...`), and a prepositional construction
  (`By choosing ..., we ...`). None requires automatic rewriting. A gerund
  subject can have a finite predicate, as in `Substituting ... gives ...`.
- Keep an opening when it expresses an operation or dependency economically
  and attaches to the right subject. Rewrite a dangling modifier or a long
  preamble with a finite clause or direct verb. `By (5), we obtain ...` is an
  option, not a mandatory formula. Do not infer causality merely from sequence.
- Preserve lexicalized terms such as `switching networks`; their spelling
  does not identify a participial supplement or a style defect.
- Give each sentence one main assertion. Separate independent design actions
  or guarantees, and keep the condition attached to the assertion it limits.
- Avoid nested relative clauses, long preambles, and chains of `which` clauses.
  A longer sentence is appropriate when it keeps one conditional implication
  intact. Do not impose a word-count threshold or split equations arbitrarily.
- Avoid explanatory parentheses where a direct clause or short sentence is
  clearer. Preserve citation/equation references and venue-required notation.

## Grammatical choices

- **Tense and aspect:** use present tense for mathematical facts, definitions,
  and the paper's stated results. Use past tense for completed procedures or
  prior work when appropriate. Use prospective `will` only for a genuine
  preview. Do not force all modules into one tense or routinely add progressive
  and perfect constructions when simple tense expresses the same meaning.
  Present perfect is a recurring retrospective choice in all 14 sampled
  Conclusions; do not normalize it away because present tense suits a theorem.
- **Voice and subject:** use `we` for author actions and an existing object or
  result as subject when natural. Use passive voice when the action's recipient
  matters more than its agent. Do not ban either first person or passive voice.
- **Articles, number, and agreement:** distinguish `an estimator` introduced
  for the first time from `the estimator` already specified; check singular/
  plural nouns and agreement, including references to equations and results.
- **Verb patterns and prepositions:** use the established pattern, for example
  `converges to zero`, `depends on`, `satisfies the condition`, and `is subject
  to`. Do not select a preposition solely by translating Chinese literally.
- **Modifiers and reference:** attach each qualifier to its intended object;
  make the antecedent of `it`, `this`, and `which` clear. Rephrase dangling
  participles. Judge `by choosing` by function and attachment, not whether it
  occurs at the beginning or inside the sentence.
- **Modality:** preserve the difference among `can`, `may`, `must`, and
  `suffices`. Do not remove necessary uncertainty or convert a sufficient
  condition into a necessary one to make a sentence sound more confident.

## Illustrative rewrites

These are constructed examples, not quotations or empirical corpus evidence.
Only apply a rewrite when its mathematical content is supported by the input.

| Before | Preferred wording | Reason |
|---|---|---|
| Using (5), we obtain (6). | No change required. | Clear participial supplement attached to `we` |
| Choosing the gain changes the transient response. | No change required. | Gerund clause is the subject of `changes` |
| Taking norms in (5), we obtain (6). | We take norms in (5) and obtain (6). | Optional direct-verb variant; the original is not banned |
| Using the measurements, the observer gains are selected by us. | We use the measurements to select the observer gains. | Repair the dangling modifier; retain the stated information source |
| We call the filter that removes the constant component [new name]. | The filter removes the constant component. | Describe the operation without coining a name |
| This remarkably powerful estimator successfully achieves global exponential convergence. | The estimator achieves global exponential convergence. | Remove praise while retaining the stated property |
| We perform the estimation of the unknown parameters. | We estimate the unknown parameters. | Prefer a direct verb |

Before delivery, check that no rewrite has added a name, claim, assumption,
or result, and that language compression has preserved mathematical meaning.
