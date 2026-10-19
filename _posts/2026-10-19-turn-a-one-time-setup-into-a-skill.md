---
layout: post
title: turn a one-time setup into a skill any company can run
description: The judgment you build setting up one company's page leaves with the task. Put the rules in a skill and let each company supply its own facts.
skill:
  name: skill-from-setup
  summary: A skill that builds skills. Name a place, and it walks you through the audit of real pages, the split between rules and sources, the seven-step workflow and a clean test run. It writes the SKILL.md and its reference files.
  zip: /downloads/skill-from-setup.zip
---

# turn a one-time setup into a skill any company can run

You set up a company's GitHub README once. It takes a week to do well. You read the best READMEs in the category, you pull the right descriptions from the brand docs, you check every number. Then the next company asks for the same thing, and you start from zero again.

That second week is the waste. The judgment you built in the first week lived in your head, so it left with the task.

So stop writing pages and start writing skills. A skill is a SKILL.md file that an agent reads and follows. It holds the method, and the company supplies the facts.

## the split that makes it work

Every task like this has two parts.

The objective part holds for every company. A good README says what the product does in the first screen. A registry description names the category in the words a reader would search for. A good listing has a clear install path. These rules don't change from client to client, so they belong in the skill.

The subjective part changes from company to company. The tone, the approved one-line description, the numbers legal has cleared and the product facts all belong to the company. None of that goes in the skill. The skill only says where to find it, for example the brand doc or the docs site.

If you get this split wrong, you get one of two bad skills. Put the company's words in the skill, and it works for one client. Leave the rules out, and it is a form with empty boxes.

## the workflow inside every skill

You can use the same seven steps for every place.

1. Intake. Ask for the company's sources, or a repo that holds them. Do no work until you have them.
2. Audit the live page against a checklist. Each item is either something a script can check or something a person must read.
3. Draft every field from the company's sources.
4. Check the drafts, run a plain-language pass on the prose, and check again.
5. Write the report with what is wrong, then list the engineering tasks and the content suggestions.
6. Prepare go-live: the exact steps, and who makes each change live.
7. Verify after the company publishes.

A few rules never bend. Every description of the company is one of its approved blocks, word for word. Every number comes from the cleared list. A technical fact with no source gets a mark for an engineer. And nothing goes live from your side.

## audit the place before you write the skill

A thin skill says "this field takes 350 characters, paste the text here", and whoever runs it still has to guess what good text is.

A good skill knows what good looks like on that place. So before you write one, go and look. Read a lot of real pages, pick the best few, and work out why they are good. The links and the numbers go into the skill as exemplars, with the date you read them. Whoever runs the skill can hold their draft up against them.

## test it on a clean machine

The last step is the one people skip. Run the finished skill with a fresh agent, in an empty folder that holds only the skill and the company's source file. The agent starts with nothing but what the skill tells it.

The first time I did this, the agent matched the output I had made by hand. It also found two errors I had missed: a claim about product scope that contradicted the company's approved status line, and a typo in a contact email address. I fixed both, and I added the checks that caught them to the skill.

That is the point of a skill. The judgment stays, and it gets better each time someone runs it.

## download the skill

I packaged this method as a skill that builds skills. You name a place, and it walks you through the audit of real pages, the split between rules and sources, the seven-step workflow, and a clean test run. It writes the SKILL.md and its reference files. Download it below and run it in Claude Code or any agent that reads skills.
