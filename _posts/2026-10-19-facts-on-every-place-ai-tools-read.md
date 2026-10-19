---
layout: post
title: your company's facts must be correct on every place ai tools read
description: Buyers and coding agents meet your company on pages you set up once and forgot. A method to map those places and fix them, and a skill that runs it.
skill:
  name: presence-map
  summary: Asks for your sources, maps every place your company controls, sorts them into one-time and recurring, and audits the one-time places first. It never publishes anything.
  zip: /downloads/presence-map.zip
---

# your company's facts must be correct on every place ai tools read

A buyer asks a coding agent how to fix a problem. The agent reads your GitHub README, your docs, a registry entry and a plugin listing. Then it answers. You were not in that room. The pages were.

Most companies set those pages up once, years ago, and then forgot them. The README still describes the product from two pivots back, and the Docker Hub page has no description at all. Nobody owns them, because nobody thinks of them as marketing.

They are marketing now. They might be the only marketing an agent ever reads.

## the places you already control

Make a list. Most technical companies have more of these than they think:

- GitHub: the org page, the main repo's README and About box, topics, releases, and SECURITY.md.
- Package and image registries: Docker Hub, Artifact Hub, PyPI, npm. Each one shows a description, and most companies leave it blank or stale.
- Model and dataset hubs: a Hugging Face organization page, its cards, its collections.
- Docs that agents can read: a docs site, and an MCP server in front of it if your docs platform offers one.
- Agent surfaces: a public agent skill, an entry in the official MCP Registry, the Claude connectors directory, the Cursor Marketplace, the Gemini CLI extensions gallery.

Some of these are one-time setups. You write the page well once and check it each quarter. Others need posting every week. Start with the one-time places. They are cheap, and they stay correct for a long time.

## why it goes wrong

Three reasons, in my experience.

1. No single source. Each page was written by a different person on a different day. So each page describes the company in different words, and some of them are wrong.
2. Nobody looks at the live page. The team reads the brand doc. The agent reads what ships. Those two drift apart.
3. Nobody knows what good looks like on that place. A good Docker Hub description is not a good GitHub README. Each place has its own form and its own best examples.

## the method

For each place, the same five steps.

1. Get the sources first. Your approved descriptions of the company, word for word. Your cleared numbers. Your docs and your technical guides. Do no work until you have them.
2. Audit the live page. Not the doc about the page. Open it and check it against a short list: is it live, is it accurate, is it on message, is it current, and is it level with the best pages in its category.
3. Find the best pages on that place. Look at ten good examples, pick the three best, and write down what makes them good. Keep the links.
4. Draft every field from your sources. Every description of the company is one of your approved blocks. Every number comes from the cleared list. A technical claim with no source gets a mark for an engineer to fill.
5. Hand it over. Do not publish it yourself. The owner of the place makes it live. Then you check the live page again.

The last step matters more than it looks. The person who drafts the fix is not the person who should push it live. That split keeps mistakes out of public view.

## what you get

At the end you have a map of every place, a verdict per place, and a fix you can paste for each one. You also have a reason for every word in it, because every word points to a source.

## download the skill

I packaged this method as an agent skill. It asks for your sources, builds the map of places, sorts them into one-time and recurring, and audits the one-time places first. It never publishes anything. Download it below, read the SKILL.md, and run it in Claude Code or any agent that reads skills.
