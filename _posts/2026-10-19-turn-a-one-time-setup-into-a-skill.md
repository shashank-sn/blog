---
layout: post
lane: presence
order: 2
title: turn a one-time setup into a skill any company can run
description: the judgment you build setting up one company's page leaves with the task. put the rules in a skill and let each company supply its own facts.
skill:
  name: skill-from-setup
  summary: a skill that builds skills. name a place, and it walks you through the audit of real pages, the split between rules and sources, the seven-step workflow and a clean test run. it writes the `SKILL.md` and its reference files.
  zip: /downloads/skill-from-setup.zip
---

# turn a one-time setup into a skill any company can run

you set up a company's github readme once. it takes a week to do well. you read the best readmes in the category, you pull the right descriptions from the brand docs, you check every number. then the next company asks for the same thing, and you start from zero again.

that second week is the waste. the judgment you built in the first week lived in your head, so it left with the task.

so stop writing pages and start writing skills. a skill is a `SKILL.md` file that an agent reads and follows. it holds the method, and the company supplies the facts.

## the split that makes it work

every task like this has two parts.

the objective part holds for every company. a good readme says what the product does in the first screen. a registry description names the category in the words a reader would search for. a good listing has a clear install path. these rules don't change from client to client, so they belong in the skill.

the subjective part changes from company to company. the tone, the approved one-line description, the numbers legal has cleared and the product facts all belong to the company. none of that goes in the skill. the skill only says where to find it, for example the brand doc or the docs site.

if you get this split wrong, you get one of two bad skills. put the company's words in the skill, and it works for one client. leave the rules out, and it is a form with empty boxes.

## the workflow inside every skill

you can use the same seven steps for every place.

1. intake. ask for the company's sources, or a repo that holds them. do no work until you have them.
2. audit the live page against a checklist. each item is either something a script can check or something a person must read.
3. draft every field from the company's sources.
4. check the drafts, run a plain-language pass on the prose, and check again.
5. write the report with what is wrong, then list the engineering tasks and the content suggestions.
6. prepare go-live: the exact steps, and who makes each change live.
7. verify after the company publishes.

a few rules never bend. every description of the company is one of its approved blocks, word for word. every number comes from the cleared list. a technical fact with no source gets a mark for an engineer. and nothing goes live from your side.

## audit the place before you write the skill

a thin skill says "this field takes 350 characters, paste the text here", and whoever runs it still has to guess what good text is.

a good skill knows what good looks like on that place. so before you write one, go and look. read a lot of real pages, pick the best few, and work out why they are good. the links and the numbers go into the skill as exemplars, with the date you read them. whoever runs the skill can hold their draft up against them.

## test it on a clean machine

the last step is the one people skip. run the finished skill with a fresh agent, in an empty folder that holds only the skill and the company's source file. the agent starts with nothing but what the skill tells it.

the first time i did this, the agent matched the output i had made by hand. it also found two errors i had missed: a claim about product scope that contradicted the company's approved status line, and a typo in a contact email address. i fixed both, and i added the checks that caught them to the skill.

that is the point of a skill. the judgment stays, and it gets better each time someone runs it.

## download the skill

i packaged this method as a skill that builds skills. you name a place, and it walks you through the audit of real pages, the split between rules and sources, the seven-step workflow, and a clean test run. it writes the `SKILL.md` and its reference files. download it below and run it in claude code or any agent that reads skills.
