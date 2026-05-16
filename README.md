# SYNAPSE Protocol

> *An economic coordination layer for persistent, recursively self-improving agent civilizations.*

**v0.2.1** &middot; `DOC/SYNAPSE/2026` &middot; REV 003 &middot; Submission to the HyperAgent Founding 500

---

## The thesis in one paragraph

The highest-leverage use of self-modifying agents is not to assist humans, but to replace organizational primitives. A research team, a growth loop, a product discovery process — each is a structure that can be expressed as a population of economically-motivated agents whose collective intelligence compounds with use. **SYNAPSE** is the protocol for spawning, coordinating, and recursively improving those populations.

## What this repository contains

```
synapse-protocol/
├── README.md                       (this file)
├── LICENSE                         (MIT)
├── CONTRIBUTING.md                 (how to add archetypes)
├── requirements.txt                (Python deps for the prototype)
├── prototype/
│   ├── opportunity_swarm.py        (Scout + Researcher + Settlement pipeline)
│   └── README.md                   (how to run)
├── docs/
│   ├── spec.md                     (v0.2.1 canonical specification)
│   ├── operating-log-01.md         (live evidence: AutoGen migration cycle)
│   ├── monetization-cases.md       (three worked cases — $1.76M aggregate)
│   ├── bibliography.md             (9 verified sources)
│   └── competitive-landscape.md    (the honest map, May 2026)
└── archetypes/
    └── README.md                   (planned: Scout, Researcher, Builder, Growth, Optimizer, Coordinator)
```

## Live artifacts (hosted)

- **v0.2.1 specification** — [editorial HTML version](https://hyperagent.com/api/files/usergenerated/threads/cmp7ikixy1u5307adffyafp09/artifacts/19515d89-b942-4ac6-aa91-8666273e3c27.html)
- **Submission landing page** — [hosted on HyperAgent](https://hyperagent.com/api/files/usergenerated/threads/cmp7ikixy1u5307adffyafp09/artifacts/84c783e7-9c83-41de-ae4a-a5d09145b7d3.html)
- **Operating Log Entry #01** — [the AutoGen Migration Vacuum cycle](https://hyperagent.com/api/files/usergenerated/threads/cmp7ikixy1u5307adffyafp09/artifacts/c0767bd4-ec5d-4171-aed4-fbd4ba519c62.html)
- **Three Worked Monetization Cases** — [the economic model in concrete](https://hyperagent.com/api/files/usergenerated/threads/cmp7ikixy1u5307adffyafp09/artifacts/934ddcd8-f518-4326-ba99-7f89218a99d3.html)

## Quick start

```bash
git clone https://github.com/Dhammerr6304/synapse-protocol.git
cd synapse-protocol
pip install -r requirements.txt

export ANTHROPIC_API_KEY=sk-ant-...
export EXA_API_KEY=...

python prototype/opportunity_swarm.py --domain "AI agent infrastructure"
```

Produces a real Operating Log Entry in `./reports/`. See [`docs/operating-log-01.md`](docs/operating-log-01.md) for a worked example.

## The three insights

| # | Insight | Why it matters |
|---|---------|---------------|
| 1 | **Replace organizational primitives, not workflows.** | The unit of competition shifts from agent quality to organizational intelligence density. |
| 2 | **Memory must be executable.** | The procedural layer stores validated workflows, tested code, proven coordination patterns — most platforms have nothing here. |
| 3 | **Self-improvement is a first-class loop.** | Sakana's DGM and MIT's SEAL validate the mechanism. SYNAPSE's contribution is operationalizing it under economic pressure. |

## The three honest weak wedges

A submission that does not name its own weaknesses is not credible. SYNAPSE's are these.

1. **Alignment stability** of recursive self-modification at scale. The DGM paper validates the mechanism on coding benchmarks; it says nothing about stability in open-ended economic environments.
2. **"Faster than incumbents" is unproven.** The first ninety days of operating evidence settle whether SYNAPSE's agents recognize opportunities faster than Cognition, Salesforce, or OpenAI.
3. **"Who pays and why" needs concrete answers.** GPT Store proved aggregation does not create value. We have one worked case anchor (AutoGen migration); the cohort funding is to produce ten more.

## What we want from the HyperAgent Founding 500 cohort

The $20K credit grant funds compute for ninety days of operating evidence at honest scale — not five toy agents over a weekend, but a population large and persistent enough to produce data that distinguishes the architecture from a manually-tuned multi-agent script.

The deliverable back to the cohort is:

1. **Open-source agent archetypes** — six initial archetypes published as installable packages (this repository is the seed).
2. **Documented memory schema** — five-layer fabric specification with reference implementation.
3. **Public operating log** — every spawn, every outcome, every meta-agent proposal, for the full ninety days. Transparency as evidence.

## Citation

If you reference SYNAPSE in academic work or industry analysis:

> SYNAPSE Protocol v0.2.1 (2026). *An economic coordination layer for agent civilizations.* DOC/SYNAPSE/2026 · REV 003. github.com/Dhammerr6304/synapse-protocol.

## License

MIT — see [`LICENSE`](LICENSE). The protocol's intent is that improvements made by cohort members flow back to a shared memory fabric; the code license is permissive on purpose.

---

*Built at REKT☆WRLD Labs.* &middot; *v0.2.1 &middot; 2026-05-15*
