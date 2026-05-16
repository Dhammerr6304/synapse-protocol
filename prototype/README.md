# SYNAPSE Prototype — Opportunity Swarm

A minimal runnable demonstration of the SYNAPSE protocol's three-layer architecture: Scout → Researcher → Settlement, with a JSON-backed memory fabric.

This is production code intended for deployment on the operator's infrastructure. It uses standard API clients rather than platform-internal tools so it runs anywhere.

## What it does

1. **Scout** issues four web-search queries against a domain you specify, surfaces 5–20 candidate opportunity signals via Exa, and ranks them through a triage prompt.
2. **Researcher** pulls deep content from each top signal's primary source plus related context, validates the asymmetric-opportunity hypothesis, and produces a structured `OpportunityReport` (Pydantic model).
3. **Settlement** logs the execution trace to the memory fabric (episodic layer), generates a procedural-memory entry for high-confidence GO recommendations, and emits a JSON report to `./reports/`.

## Setup

```bash
pip install -r ../requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...
export EXA_API_KEY=...
```

## Run

```bash
# Default: AI agent infrastructure
python opportunity_swarm.py

# Custom domain
python opportunity_swarm.py --domain "biotech tooling 2026" --n 5
```

## Output

The script produces:

1. A live console rendering of each opportunity report (via `rich`).
2. A JSON file in `./reports/<timestamp>.json` with the full cycle output.
3. An updated `./memory.json` with episodic and procedural entries.

## Sample run

See [`../docs/operating-log-01.md`](../docs/operating-log-01.md) for the actual output of the v0.2.1 hardening pass — a GO recommendation on the AutoGen migration vacuum with five independently sourced evidence signals and a documented audit trail.

## Architecture mapping

| Code class | Spec concept |
|------------|--------------|
| `MemoryFabric` | Five-layer memory store (this prototype implements episodic + procedural) |
| `ScoutAgent` | The Scout archetype (§ 04 of the spec) |
| `ResearcherAgent` | The Researcher archetype (§ 04 of the spec) |
| `Settlement` | The economic settlement primitive (§ 07 of the spec) |
| `SYNAPSECycle` | The compounding flywheel (§ 05 of the spec) |

The four archetypes not yet implemented (Builder, Growth, Optimizer, Coordinator) are scaffolded in `../archetypes/`.

## Production considerations

The prototype is intentionally single-file and JSON-backed. A production deployment should:

1. Replace `MemoryFabric` with Postgres + a vector store (pgvector or Pinecone) for the semantic layer.
2. Add concurrency (the current loop is sequential; Scout's signals can be Researched in parallel).
3. Wire a real settlement backend — Stripe Connect for revenue share, equity tracking via a CRM.
4. Run inside an isolated container per the IsolateGPT pattern (see `../docs/bibliography.md`).
