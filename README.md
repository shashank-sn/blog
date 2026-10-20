<a href="#the-workflows"><img src="assets/header.svg" width="100%" alt="workflows: real workflows, written down step by step. every one comes with an agent skill you can install."></a>

## about

i'm shashank. online i sometimes go by stupidpreneur, and people describe me as an idiot savant.

i'm the co-founder of [ellora](https://getellora.com), the ai content editor inside chatgpt, claude and the other apps your team writes in. it learns how your brand sounds and fixes each draft before anyone has to.

most of my work is turning a messy job into a process that runs the same way twice. the job changes. the habit doesn't. i write down the steps, add a gate where things usually go wrong, and keep the evidence.

this repo is where those processes go once they've held up in real work. each workflow is one page with the exact steps, and one skill you can install in your own agent.

## the workflows

<p>
<a href="build/README.md"><img src="assets/topic-build.svg" width="49%" alt="build"></a>
<a href="write/README.md"><img src="assets/topic-write.svg" width="49%" alt="write"></a>
<a href="research/README.md"><img src="assets/topic-research.svg" width="49%" alt="research"></a>
<a href="operate/README.md"><img src="assets/topic-operate.svg" width="49%" alt="operate"></a>
<a href="presence/README.md"><img src="assets/topic-presence.svg" width="49%" alt="presence"></a>
</p>

### [build](build/README.md)

shipping code with a coding agent, with a gate and evidence at every stage.

- **[most coding-agent failures are skipped stages](build/delivery-loop/README.md)**  
  the agent builds before anyone agreed on what to build, or says "tests pass" about an old commit. an eleven-stage loop where every gate leaves evidence. skill: `delivery-loop`

### [write](write/README.md)

making a voice explicit, so a draft can be checked instead of argued about.

- **[stop telling writers to match the voice. measure it.](write/voice-profile/README.md)**  
  every team says "match our voice" and almost none can say what it means. turn the writing you've published into a profile you can check a draft against. skill: `voice-profile`

### [research](research/README.md)

turning a noisy system into a number you can defend.

- **[the fastest way to fake progress is to change the measurement](research/measurement-protocol/README.md)**  
  add an engine or a few brand questions and the number goes up while the work stays the same. eight rules for measuring a system that moves while you measure it. skill: `measurement-protocol`

### [operate](operate/README.md)

the unglamorous fixes that keep a small business running.

- **[a broken link is a content bug with a customer attached](operate/deliverable-audit/README.md)**  
  six customers said the link was broken. the real picture was six written complaints, nineteen written reviews and thirty-eight ratings. how to audit a product library and fix it at the source. skill: `deliverable-audit`

### [presence](presence/README.md)

getting a company's facts right on every place buyers and ai tools read.

- **[your company's facts must be correct on every place ai tools read](presence/presence-map/README.md)**  
  buyers and coding agents meet your company on pages you set up once and forgot. a method to map those places and fix them. skill: `presence-map`
- **[turn a one-time setup into a skill any company can run](presence/skill-from-setup/README.md)**  
  the judgment you build setting up one company's page leaves with the task. put the rules in a skill and let each company supply its own facts. skill: `skill-from-setup`

## install

in claude code, add this repo as a marketplace once, then install any skill by name. in any other agent, paste the prompt and name the skill you want.

**claude code**

```text
/plugin marketplace add shashank-sn/workflows
/plugin install delivery-loop@shashank-workflows
/plugin install voice-profile@shashank-workflows
/plugin install measurement-protocol@shashank-workflows
/plugin install deliverable-audit@shashank-workflows
/plugin install presence-map@shashank-workflows
/plugin install skill-from-setup@shashank-workflows
```

**any other agent**: paste this prompt.

```text
install an agent skill from https://github.com/shashank-sn/workflows
each workflow folder (for example build/delivery-loop) has a skills/<name> folder. copy the skill i name into your skills directory (for claude code: ~/.claude/skills/<name>), read its SKILL.md, and use it on my task.
skill: <name>
task: <your task>
```

## follow along

star the repo to keep it in your list. watch it to hear when a new workflow lands. if a step breaks or you get stuck, [open an issue](https://github.com/shashank-sn/workflows/issues/new/choose). that's the best way to reach me, and it helps the next person who hits the same thing.

## license

skills and plugin manifests are [mit](LICENSE). the posts are copyright shashank sn.
