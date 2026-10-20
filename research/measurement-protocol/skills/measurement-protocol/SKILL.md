---
name: measurement-protocol
description: >-
  Designs and runs a measurement of a noisy, moving system (for example how
  often a brand appears in AI answer engines) without inventing progress: one
  rule file, equal readings, held-out controls and brand questions, repeats
  clustered by question, a minimum detectable rate, a calibration run, and a
  list of blind spots. Use when asked to "design a measurement", "build a
  baseline", or "measure visibility".
license: MIT
metadata:
  author: Shashank SN
  version: "1.1.0"
  source: https://github.com/shashank-sn/workflows
---

# Measurement protocol

The fastest way to fake progress is to change the measurement and call it a trend. This skill keeps the instrument fixed and says how small a change it can see.

## When to use this

- "design a measurement for X"
- "build a baseline before we start"
- "measure our visibility in answer engines"

## What you need

- The question the measurement must answer.
- The engines or sources to read, and the budget per run.
- A question set, or the demand data to build one (search terms, sales calls, support questions).
- The brand pattern (names and spellings) and the hosts the company owns.
- At least three control questions whose answers should not change.

## The process

1. **One sentence.** Write the question the measurement answers to `measure/question.md`.
   Stop if: it needs "and". Split it into two measurements.
2. **Rule file.** Write `measure/rules.yaml` (`reference/process.md` has the shape): engines, repeats, controls, brand pattern, owned hosts, retired controls. Every script reads this file. No script has its own definitions.
3. **Question set.** Build it from real demand. Tag each question `measured`, `control`, or `brand` (it names the brand).
   Stop if: no question is tagged `control`.
4. **Calibrate.** Run the smallest useful slice: one repeat, two questions per engine. Check the parser, the output format, and that controls behave.
   Stop if: any engine's output fails to parse or a control moves.
5. **Collect.** Equal readings per engine per question. Record each reading with engine, question id, repeat number, timestamp, and the raw answer.
6. **Rates.** Hold `control` and `brand` questions out of every rate. Report search engines apart from chat assistants. Cluster repeats by question.
7. **Precision.** Report the effective sample size after clustering and the minimum detectable rate (`reference/process.md`).
8. **Blind spots.** List what the measurement cannot see in `measure/blind-spots.md`.
9. **Report.** Write `measure/report.md` with the method first, then the numbers. If the rule file changed since the last run, or the earlier number has no rule file on record, label the run a new baseline, not a trend. You may show the earlier number for context, but not as a comparison.

## What good looks like

See `examples/input.md` and `examples/output.md`.

## Guardrails

- No unequal readings across engines.
- No pooling of search results with chat answers.
- No control or brand question inside a rate.
- No rate without its denominator.
- No change called a trend when it is smaller than the minimum detectable rate.
- No number that the stored raw readings cannot reproduce.
- No expensive run before a calibration passes.

## Output format

```text
measure/
  question.md
  rules.yaml
  questions.csv        id, text, tag, source of demand
  readings/<run>.jsonl engine, question_id, repeat, timestamp, raw
  calibration.md
  report.md            method, rates, n, effective n, mdr, blind spots
  blind-spots.md
```

## Changelog

- 1.1.0: after a clean test with a fresh agent. An earlier number with no rule file is context, not a baseline. The minimum detectable rate uses the baseline rate as `p`.
- 1.0.0: first version.

## Failure modes

- **A control moves:** stop. The instrument changed. Find out why before any rate is reported.
- **An engine fails mid-run:** do not fill the gap. Report that engine's rate as `incomplete` with its count.
- **Budget too small for a useful minimum detectable rate:** say so before collecting, and offer fewer engines or more repeats.
