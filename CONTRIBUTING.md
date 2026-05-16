# Contributing to SYNAPSE

SYNAPSE is built on the premise that an agent civilization's intelligence compounds when its members contribute back to a shared memory fabric. That principle starts with this repository.

## What contributions look like

Three categories of contribution, in roughly descending priority.

### 1. Archetypes

The protocol ships with six initial archetypes (Scout, Researcher, Builder, Growth, Optimizer, Coordinator). Each is a small surface — a system prompt, a memory schema, a set of permitted tools, an evaluation criterion. New archetypes should propose a new economic function, not a variation on an existing one.

**To propose a new archetype:**

1. Open a discussion explaining the economic function the archetype performs and why the existing six do not cover it.
2. After alignment, open a PR adding a directory under `archetypes/` with:
   - `archetype.md` (description, function, economic output)
   - `system_prompt.md` (the canonical prompt)
   - `permitted_tools.md` (the safe tool surface)
   - `evaluation.md` (how success is measured)

### 2. Operating Log entries

The Operating Log is the protocol's evidence base. Every cycle adds to a population dataset that future research can analyze.

**To contribute an entry:**

1. Run `python prototype/opportunity_swarm.py --domain <your-domain>` against real data.
2. The prototype emits a JSON report to `./reports/`.
3. Open a PR adding the report as `docs/operating-log-NN.md` with the next sequential number.
4. The entry must include an audit trail (cycle ID, sources verified, timing) and an explicit confidence + recommendation.

The bar: every Operating Log entry should be reproducible by a third party from the same starting prompt and tool stack.

### 3. Memory fabric improvements

The five-layer memory fabric (Episodic, Semantic, Procedural, Strategic, Identity) is intentionally minimal in the reference implementation. Improvements to schema design, query patterns, or storage backends are welcome.

Open a discussion first. Schema changes have downstream effects on every archetype.

## What we are explicitly not interested in

- **Generic "make it more capable" PRs** without a named economic function or measurable outcome.
- **Self-modification proposals** that bypass the draft-and-confirm gate. The meta-agent must always surface edits for human review; this is non-negotiable per the v0.2.1 specification (§ 09 wedge 01).
- **Closed-source dependencies.** SYNAPSE depends on commercial APIs (Anthropic, Exa) but the protocol itself remains open.

## Code style

The prototype is conservative on purpose. Single-file, Pydantic models, type hints, no premature abstractions. New code should match this style until the abstractions earn their generality.

- Python 3.10+, type-hinted
- `ruff` for lint, `black` for format (88-char line)
- Docstrings on every public class
- Tests via `pytest` when the surface stabilizes (TBD)

## Review process

PRs are reviewed against three criteria:

1. **Does it propose a new economic function or settle a wedge?** Cosmetic changes are nice but not the priority.
2. **Is the evidence reproducible?** Operating Log entries need audit trails; archetype proposals need an evaluation function.
3. **Does it respect the draft-and-confirm gate on self-modification?** No exceptions.

## License

By contributing, you agree your changes are released under the same MIT license as the rest of the repository.

---

*Questions?* Open a discussion. SYNAPSE is a protocol — the conversation about its evolution is part of the artifact.
