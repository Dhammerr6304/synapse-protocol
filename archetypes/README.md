# Archetypes

The six initial archetypes that form SYNAPSE's evolutionary attractor set. Each is implemented as a HyperAgent named agent with its own skills, memories, and constraints.

| Archetype | Function | Status |
|-----------|----------|--------|
| **Scout** | Opportunity detection across web, trend APIs, social listening | Reference impl in [`prototype/`](../prototype/) |
| **Researcher** | Deep analysis, synthesis, technical validation | Reference impl in [`prototype/`](../prototype/) |
| **Builder** | Prototype generation via code, no-code, API composition | Scaffold |
| **Growth** | Distribution, acquisition, channel testing | Scaffold |
| **Optimizer** | Recursive improvement — A/B testing, analytics, meta-reasoning | Scaffold |
| **Coordinator** | Swarm orchestration, conflict resolution, resource allocation | Scaffold |

## Why six and not five or seven

The initial archetype count is six because that is the smallest set capable of running a full end-to-end opportunity-to-settlement cycle without redundancy. Fewer than six and some economic function is not covered. More than six and roles begin to overlap — Scout and Researcher both do information gathering; Builder and Optimizer both modify systems; Growth and Coordinator both manage flow.

Six is not a permanent target. The protocol's evolutionary mechanism (DGM-style mutation under economic pressure, see [`docs/spec.md`](../docs/spec.md) § 04) may discover Pareto-efficient subsets or supersets in operation. The six are the seed population, not the species.

## Per-archetype specification

Each archetype directory (e.g. `archetypes/scout/`) will contain:

- `archetype.md` — description, function, economic output
- `system_prompt.md` — the canonical prompt for the named agent
- `permitted_tools.md` — the safe tool surface
- `memory_schema.md` — what the archetype reads from and writes to
- `evaluation.md` — how success is measured per cycle

Contributors proposing new archetypes should follow [`../CONTRIBUTING.md`](../CONTRIBUTING.md).

## Current state

The Scout and Researcher archetypes have working reference implementations in [`../prototype/opportunity_swarm.py`](../prototype/opportunity_swarm.py). Builder, Growth, Optimizer, and Coordinator are scaffolded but not yet implemented — they are part of the 90-day plan in [`../docs/spec.md`](../docs/spec.md) § 11.

The Operating Log ([`../docs/operating-log-01.md`](../docs/operating-log-01.md)) demonstrates a working Scout → Researcher → Settlement cycle on real 2026 market evidence.
