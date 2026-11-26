# Numerical Examples and Conclusion

## Numerical examples

### Purpose

Use an example to illustrate a theorem-level property or a claimed design
advantage.  It does not replace proof.

Before showing figures, state:

1. the system and unknown quantities;
2. the graph or switching pattern;
3. parameters selected under the theorem's conditions;
4. initial-condition policy;
5. the exact property each figure tests.

### Comparative examples

When the contribution removes a limitation, compare the old and new designs
under the condition that exposes the difference.  Explain why the condition is
within or outside each theorem's scope.  Do not claim superiority from an
uncontrolled parameter change.

### Figure narration

Prefer:

```text
Figure X shows [measured quantity].  Its convergence/boundedness/agreement
illustrates [specific theorem property].
```

Avoid `the effectiveness is obvious` or a sentence that merely restates the
caption.

## Conclusion

### Select the content, not a fixed template

Close with the established result and enough of its mechanism to explain what
the paper accomplished. Select from the problem and scope, construction or
enabling result, main guarantee, and established application or comparison.
These are content choices, not four mandatory sentences or a fixed order.

- Lead with the problem/result when introducing what was accomplished; lead
  with the mechanism when a small design change is the central contribution.
- Retain the stage dependency when it explains how the result was obtained.
  Do not retell the proof or list every auxiliary lemma.
- Reuse the terminology and claims already established in the manuscript body
  or supplied result summary. The Introduction need not have been written yet.
- Keep claim-defining conditions: system class, admissible initialization,
  network conditions, and the exact convergence or rate property. Not every
  technical assumption needs repetition, but compression must not broaden the
  claim. A rate bound is not an exact rate; illustrative simulations are not a
  robustness theorem; a possible application is not a completed application.
- Do not introduce notation, coin names or acronyms, strengthen novelty, or
  start a new literature review. A brief grounded comparison or existing
  citation is permissible when it closes the paper's established contribution.

### Wording and grammar

Prefer concrete retrospective verbs such as `have developed`, `have
established`, and `have shown` when their objects describe completed work.
Present perfect occurs in all 14 corpus Conclusions; it is a useful default,
not a requirement for every sentence. Use present tense for composition,
current scope, or a result's property. Choose `we`, `this paper`, or the result
as subject according to the sentence's focus; none is mandatory.

Use `first`, `then`, or `by` when they express an actual dependency. Do not add
them to force a template. Follow [language-style.md](language-style.md) for
modifiers and sentence-initial `-ing`; neither has a blanket ban. Preserve
technical qualifiers rather than shortening a sentence at the cost of scope.

### Limitations and future work

Distinguish a remaining restriction of this paper from a limitation of earlier
work that this paper removed. Neither automatically implies a future-work
sentence. A remaining restriction can be stated directly; explain its
proof/design cause only if that cause is known and useful. Never invent one.

Include a future direction only when supplied or clearly supported by the
manuscript's established scope. Name the specific change, such as relaxing a
stated spectral restriction, extending to discrete time, or broadening the
network class. Do not pad the ending with `more general systems` alone.

Match the wording to the evidence about research status:

| Supplied status | Permissible treatment |
|---|---|
| No defensible direction supplied or established | End with the completed result; do not demand or invent future work. |
| A technically motivated possibility | Use possibility language, such as `It would be interesting to...`; do not imply the work has begun. |
| An explicit author plan | A planned-work statement is permissible; do not invent a commitment to obtain a result. |
| Author-confirmed work already in progress | `We are studying...` or `...are under way` is permissible; do not describe it as completed. |

Future or ongoing work appears in 12/14 Conclusions, including all six recent
papers; three of the 12 explicitly report ongoing work. This supports keeping
a specific closing direction available, not making it obligatory or treating
research status as a stylistic decoration. C01 and C02 close without one;
C13 includes an ongoing-application sentence, despite having no separate
future-work paragraph.
