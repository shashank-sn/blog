# Clean test

A clean test shows what the skill does when nobody is there to fill the gaps.

## Set up

1. Make an empty folder.
2. Copy in only the skill folder and one company's sources file. Nothing else: no notes, no earlier output.
3. Start a fresh agent session in that folder. With Claude Code, for example:

```bash
claude -p "Use the <place>-presence skill to prepare <company>'s fixes. The sources are in sources.yaml." --permission-mode acceptEdits
```

4. Limit the agent to the tools the skill needs. Do not give it sign-in, publish, or push access.

## Judge the run

Compare the output with the output you made by hand. Record:

- **Same:** findings and drafts that match yours.
- **Missing:** things you found that the agent did not. Each one usually means a rule or a checklist item is missing.
- **Better:** things the agent found that you missed. Check each one and keep the real ones.
- **Unsafe:** any attempt to publish, sign in, or write outside the folder. Any of these is a failure. Fix the skill before anything else.
- **Invented:** any fact or number not in the sources. Each one is a failure.

## Fix

For each Missing, Unsafe, or Invented item, change the skill and add a check that would catch it. Then run the clean test again in a new empty folder. Stop when a run has no Unsafe or Invented items and nothing important is Missing.
