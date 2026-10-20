# Process notes

## Rule file shape

```yaml
question: "How often does <brand> appear in answers to buyer questions about <category>?"
engines:
  chat: [engine-a, engine-b, engine-c]
  search: [search-a]          # reported apart, never pooled with chat
repeats: 3
brand_pattern: ["<brand>", "<brand> inc", "<product>"]
owned_hosts: ["example.com", "docs.example.com"]
controls:
  - id: c1
    text: "<a question whose answer should not change>"
retired_controls: []
counts_as_mention: "brand_pattern appears in the answer text, or an owned host is cited"
```

## Effective sample size

Repeats of one question are correlated. With `k` repeats per question and an intra-question correlation `rho` (estimate it from the calibration and the first runs):

```text
design_effect = 1 + (k - 1) * rho
effective_n   = raw_n / design_effect
```

If you cannot estimate `rho`, report the two bounds: `effective_n` is between the number of questions and `raw_n`.

## Minimum detectable rate

For a two-run comparison, at about 95% confidence and 80% power, with `p` the baseline rate (or the current rate when there is no comparable baseline):

```text
mdr ≈ 2.8 * sqrt(2 * p * (1 - p) / effective_n)
```

Report it with every rate. A change smaller than `mdr` is reported as "no detectable change".

## Blind spots to consider

- Personalised answers the readings cannot reproduce.
- Engines or tiers not in the rule file.
- Questions buyers ask that are not in the set.
- Answers that paraphrase the brand without naming it.
