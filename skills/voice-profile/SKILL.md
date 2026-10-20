---
name: voice-profile
description: >-
  Builds an explicit, testable voice profile from a writer's or company's
  existing samples, checks it against held-out samples, writes an editing
  brief, and reviews drafts with voice fit, pattern findings, factual evidence
  and approval kept as four separate reports. Use when asked to "build a voice
  profile", "codify our style", or "review this draft against our voice".
license: MIT
metadata:
  author: Shashank SN
  version: "1.0.0"
  source: https://github.com/shashank-sn/blog
---

# Voice profile

Turn writing that already exists into a written-down description of a voice, then check drafts against it. This is an editorial system. It does not detect authorship or AI.

## When to use this

- "build a voice profile from these posts"
- "codify our house style"
- "review this draft against our voice"

## What you need

- **Scope:** one writer, one channel, one format.
- **Samples:** at least five published pieces you have the right to use.
- **Held-out samples:** at least two more pieces from the same scope, not used to build the profile.
- Optional: a list of banned phrases, and sources for factual checks.

## The process

1. **Scope.** Write the writer, channel and format to `voice/scope.md`.
   Stop if: the samples mix channels or writers. Ask which one to profile.
2. **Readiness.** For each sample, record length, format, date, and whether it fits the scope. Write `voice/readiness.md` with a verdict per sample (`use`, `exclude`, with reason).
   Stop if: fewer than five samples are `use`. A profile from fewer samples is `draft` only, never `strict`.
3. **Build.** Measure the traits in `reference/process.md` across the `use` samples. Write `voice/profile.md`, each trait with a number or a short list and one quoted example.
4. **Validate.** Check each held-out sample against the profile. Record which traits it matches and which it breaks.
   Stop if: most held-out samples break the profile. The profile describes the sample set, not the voice. Revisit step 2.
5. **Brief.** Write `voice/brief.md`: what an editor must keep (meaning, evidence, uncertainty, attribution, emphasis, rhythm) and what to cut (filler, repeated ideas, setup that delays the point).
6. **Version.** Add a version and a SHA-256 digest of `profile.md` at the top of the profile. Every later review names this version and digest.
7. **Review a draft** (when asked). Produce four separate reports in `voice/reviews/<draft>.md`:
   - voice fit against the profile,
   - pattern findings (generic phrasing, stacked hedges, formulaic structures),
   - factual evidence (each claim and its source, or `unsourced`),
   - approval (always `waiting` until a person signs off).
8. **Revise** (when asked). Change a profile rule only when two or more examples support the change. Log each change in `voice/changelog.md` and bump the version.

## What good looks like

See `examples/input.md` and `examples/output.md`.

## Guardrails

- No strict profile from fewer than five samples.
- No blending of channels, formats or writers.
- No profile change from a single example.
- Never merge the four review reports into one score.
- Never claim a passing check proves authorship, truth or quality.
- Never rewrite a draft into a different voice while reviewing it. Point at the trait and quote the sentence.
- Do not quote samples that are not licensed for reuse in any published output.

## Output format

```text
voice/
  scope.md
  readiness.md
  profile.md      version, digest, traits with numbers and examples
  brief.md
  changelog.md
  reviews/<draft>.md   four reports, kept apart
```

## Failure modes

- **Too few samples:** build a `draft` profile, label it, and list what more samples would settle.
- **Samples disagree with each other:** report the split. It may be two voices.
- **No sources for facts:** mark every claim `unsourced`. Do not judge truth.
