---
layout: post
lane: write
order: 1
title: stop telling writers to match the voice. measure it.
description: every team says "match our voice" and almost none can say what it means. turn the writing you've published into a profile you can check a draft against.
skill:
  name: voice-profile
  summary: checks your samples are ready, builds a profile from them, tests it on held-out pieces, writes an editing brief, and reviews drafts with voice fit, patterns, facts and approval kept as four separate reports.
  zip: /downloads/voice-profile.zip
---

# stop telling writers to match the voice. measure it.

every team says "match our voice". almost none can tell you what they mean.

so the new writer guesses. the editor rewrites the draft into their own voice and calls it feedback. the ai tool gets a paragraph of adjectives like "warm but direct" and produces something that is neither. three months later the blog reads like four different people, because it is.

the fix is to stop treating voice as a feeling and start treating it as a spec. you already have the raw material. it's the writing you've published.

## what a voice is made of

a voice is a set of habits you can count. how long the sentences run, and how much that length varies. which words keep showing up. how often there's a question, a colon, a dash. how paragraphs open and how they end. which constructions never appear at all.

none of that is mysterious. it's just that nobody wrote it down.

when i did this for my own writing, i started with 2,624 of my posts from linkedin, x and typefully. i also classified a 94-author corpus of 2,394 pieces. the traits that make a voice recognisable are small and countable, and the adjectives people use to describe a voice rarely point at them.

## the process

nine steps. the order matters.

1. **set the scope.** one writer, one channel, one format. a founder's posts on x and a company's emails are two voices. blend them and the profile describes nobody.
2. **collect at least five samples.** use pieces you have the right to use. prefer published work over drafts, because a draft has not been through the edit that makes it sound like you.
3. **check the samples are ready.** are they long enough? consistent with each other? in the right format? do they represent the voice you want, or the voice you had two years ago?
4. **build the profile.** rhythm, vocabulary, punctuation, openings, endings, paragraph shape, and a list of banned constructions.
5. **hold out validation samples.** keep a few real pieces that were not used to build the profile. if the profile can't recognise those, it's describing your sample set, not your voice.
6. **write the editing brief.** what to keep: meaning, evidence, uncertainty, attribution, emphasis, rhythm. what to cut: filler, repeated ideas, setup that delays the point.
7. **check a draft against it.** run the candidate through the checks and keep the results apart (more on that below).
8. **change the profile slowly.** only change a rule after more than one example supports it. one draft you liked is not a new rule.
9. **version it.** store the profile with a version and a digest, so every review says exactly which profile judged it.

<figure class="fig">
{% include figs/voice-pipeline.svg %}
<figcaption>the held-out pieces never touch the profile. they only test it.</figcaption>
</figure>

## keep the reports apart

most voice checks go wrong here. they collapse everything into one score.

a draft can sound exactly like you and still be wrong about a fact. it can be accurate and still read like a template. it can pass both and still not be approved, because approval is a person's call. so the check produces four separate reports:

- **voice fit.** does it match the profile?
- **pattern findings.** generic phrasing, stacked hedges, the tells that make writing sound produced.
- **factual evidence.** is every claim backed by a source?
- **approval.** did a person sign off?

if you merge them, a high voice score hides a wrong number. keep them apart and each one can fail on its own.

<figure class="fig">
{% include figs/four-reports.svg %}
<figcaption>a draft that sounds right can still fail on facts. one merged score would hide that.</figcaption>
</figure>

## what this is not

this is an editorial system, not a detector. a passing voice check does not prove who wrote something, and it does not prove the writing is true or good. it proves the draft matches a written-down description of a voice. that's useful, because it turns "this doesn't sound like us" into "the sentences are twice as long as ours and every paragraph opens the same way". a writer can fix the second one.

it also changes how you onboard people. instead of "read our old posts and get a feel for it", you hand a new writer the profile and the brief, and they can check their own draft before anyone else reads it.

## download the skill

i packaged this as a skill. give it your samples and a few held-out pieces, and it checks they're ready and builds the profile. then it writes the editing brief and reviews drafts with the four reports kept apart. it refuses to build a strict profile from fewer than five samples, and it won't change a rule because of one example. download it below and run it in claude code or any agent that reads skills.
