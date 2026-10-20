---
layout: post
lane: presence
order: 1
title: your company's facts must be correct on every place ai tools read
description: buyers and coding agents meet your company on pages you set up once and forgot. a method to map those places and fix them, and a skill that runs it.
skill:
  name: presence-map
  summary: asks for your sources, maps every place your company controls, sorts them into one-time and recurring, and audits the one-time places first. it never publishes anything.
  zip: /downloads/presence-map.zip
---

# your company's facts must be correct on every place ai tools read

a buyer asks a coding agent how to fix a problem. the agent reads your github readme, your docs, a registry entry and a plugin listing. then it answers. you were not in that room. the pages were.

most companies set those pages up once, years ago, and then forgot them. the readme still describes the product from two pivots back, and the docker hub page has no description at all. nobody owns them, because nobody thinks of them as marketing.

they are marketing now. they might be the only marketing an agent ever reads.

## the places you already control

make a list. most technical companies have more of these than they think:

- github: the org page, the main repo's readme and about box, topics, releases, and `SECURITY.md`.
- package and image registries: docker hub, artifact hub, pypi, npm. each one shows a description, and most companies leave it blank or stale.
- model and dataset hubs: a hugging face organization page, its cards, its collections.
- docs that agents can read: a docs site, and an mcp server in front of it if your docs platform offers one.
- agent surfaces: a public agent skill, an entry in the official mcp registry, the claude connectors directory, the cursor marketplace, the gemini cli extensions gallery.

some of these are one-time setups. you write the page well once and check it each quarter. others need posting every week. start with the one-time places. they are cheap, and they stay correct for a long time.

## why it goes wrong

three reasons, in my experience.

1. no single source. each page was written by a different person on a different day. so each page describes the company in different words, and some of them are wrong.
2. nobody looks at the live page. the team reads the brand doc, but the agent reads what ships, so the two drift apart.
3. nobody knows what good looks like on that place. a good docker hub description is not a good github readme. each place has its own form and its own best examples.

## the method

for each place, the same five steps.

1. get the sources first. your approved descriptions of the company, word for word. your cleared numbers. your docs and your technical guides. do no work until you have them.
2. audit the live page. not the doc about the page. open it and check it against a short list: is it live, is it accurate, is it on message, is it current, and is it level with the best pages in its category.
3. find the best pages on that place. look at ten good examples, pick the three best, and write down what makes them good. keep the links.
4. draft every field from your sources. every description of the company is one of your approved blocks. every number comes from the cleared list. a technical claim with no source gets a mark for an engineer to fill.
5. hand it over. do not publish it yourself. the owner of the place makes it live. then you check the live page again.

the last step matters more than it looks. the person who drafts the fix is not the person who should push it live. that split keeps mistakes out of public view.

## what you get

at the end you have a map of every place, a verdict per place, and a fix you can paste for each one. you also have a reason for every word in it, because every word points to a source.

## download the skill

i packaged this method as an agent skill. it asks for your sources, builds the map of places, sorts them into one-time and recurring, and audits the one-time places first. it never publishes anything. download it below, read the `SKILL.md`, and run it in claude code or any agent that reads skills.
