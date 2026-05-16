"""
SYNAPSE: Opportunity Swarm — Minimal Runnable Prototype
========================================================

A demonstration of the SYNAPSE protocol's three-layer architecture
(Scout, Researcher, Settlement) running end-to-end against real web data.

This is production code intended for deployment on the operator's
infrastructure. It uses standard API clients (Anthropic, Exa) rather
than platform-internal MCP tools, so it runs anywhere.

Usage:
    export ANTHROPIC_API_KEY=...
    export EXA_API_KEY=...
    python opportunity_swarm.py --domain "AI agent infrastructure"

Output:
    A JSON opportunity report written to ./reports/{timestamp}.json
    and a human-readable markdown summary printed to stdout.

Dependencies:
    pip install anthropic exa-py rich pydantic
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import Any

try:
    from anthropic import Anthropic
    from exa_py import Exa
    from pydantic import BaseModel, Field
    from rich.console import Console
    from rich.markdown import Markdown
    from rich.panel import Panel
except ImportError as e:
    print(f"Missing dependency: {e.name}. Run: pip install anthropic exa-py rich pydantic", file=sys.stderr)
    sys.exit(1)


# =========================================================================
# Memory Fabric — minimal episodic + procedural layers (single JSON file)
# =========================================================================

class MemoryFabric:
    """Persistent memory across runs. JSON-backed for simplicity; production
    deployments should use a real store (Postgres, vector DB)."""

    def __init__(self, path: str = "./memory.json"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.data: dict[str, list[dict]] = self._load()

    def _load(self) -> dict[str, list[dict]]:
        if self.path.exists():
            return json.loads(self.path.read_text())
        return {"episodic": [], "procedural": [], "strategic": []}

    def _save(self):
        self.path.write_text(json.dumps(self.data, indent=2, default=str))

    def ingest_execution(self, trace: dict):
        """Episodic layer: every execution gets logged."""
        trace["timestamp"] = datetime.utcnow().isoformat()
        self.data["episodic"].append(trace)
        self._save()

    def add_procedural(self, pattern: dict):
        """Procedural layer: validated workflows that worked."""
        pattern["created_at"] = datetime.utcnow().isoformat()
        self.data["procedural"].append(pattern)
        self._save()

    def recent_episodes(self, n: int = 5) -> list[dict]:
        return self.data["episodic"][-n:]


# =========================================================================
# Data shapes
# =========================================================================

class SignalEvidence(BaseModel):
    statement: str
    source_url: str
    excerpt: str = ""


class OpportunityReport(BaseModel):
    opportunity_statement: str = Field(description="2-sentence crisp framing")
    signal_evidence: list[SignalEvidence] = Field(description="3-5 concrete signals")
    why_now: str = Field(description="What changed recently that makes this winnable")
    why_asymmetric: str = Field(description="Why small effort produces large payoff")
    competitive_vacuum: str = Field(description="Who is NOT building this and why")
    estimated_value_usd: int = Field(description="Rough TAM or demand sizing in USD")
    confidence: int = Field(ge=1, le=10, description="1-10 confidence score")
    recommendation: str = Field(description="GO | NO_GO | INVESTIGATE_FURTHER")
    reasoning: str = Field(description="Why this confidence and recommendation")


@dataclass
class ScoutSignal:
    """A single raw opportunity signal Scout surfaces."""
    headline: str
    source_url: str
    snippet: str
    detected_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())


# =========================================================================
# Scout Agent — searches the web for asymmetric opportunity signals
# =========================================================================

class ScoutAgent:
    """Detects opportunity signals via Exa search.

    Scout is intentionally narrow: it produces high-recall candidate signals
    that Researcher then validates. The art is in the query, not the model.
    """

    def __init__(self, exa: Exa, anthropic: Anthropic, memory: MemoryFabric):
        self.exa = exa
        self.anthropic = anthropic
        self.memory = memory
        self.console = Console()

    def scan(self, domain: str, n_signals: int = 5) -> list[ScoutSignal]:
        self.console.print(Panel(f"[bold]Scout[/bold] scanning: {domain}", style="cyan"))

        # Query design: bias toward pain points, gaps, complaints, and recent shifts.
        queries = [
            f"unsolved pain points {domain} 2026",
            f"gaps in {domain} ecosystem developers complaining",
            f"recently failed or deprecated tools in {domain}",
            f"underserved market segments {domain}",
        ]

        signals: list[ScoutSignal] = []
        seen_urls: set[str] = set()

        for q in queries:
            try:
                results = self.exa.search_and_contents(
                    q,
                    num_results=4,
                    use_autoprompt=True,
                    text={"max_characters": 1200},
                )
                for r in results.results:
                    if r.url in seen_urls:
                        continue
                    seen_urls.add(r.url)
                    snippet = (r.text or "")[:600]
                    signals.append(ScoutSignal(
                        headline=r.title or "(untitled)",
                        source_url=r.url,
                        snippet=snippet,
                    ))
            except Exception as e:
                self.console.print(f"[yellow]Scout query failed: {q} — {e}[/yellow]")

            if len(signals) >= n_signals * 3:
                break

        self.console.print(f"[green]Scout surfaced {len(signals)} raw signals.[/green]")

        # Triage: rank signals by asymmetric-opportunity heuristic via Claude.
        return self._triage(signals, domain, n_signals)

    def _triage(self, signals: list[ScoutSignal], domain: str, n: int) -> list[ScoutSignal]:
        if not signals:
            return []

        signal_lines = "\n".join(
            f"[{i}] {s.headline}\n  URL: {s.source_url}\n  Snippet: {s.snippet[:300]}"
            for i, s in enumerate(signals)
        )

        prompt = f"""You are Scout, a SYNAPSE agent that identifies asymmetric opportunities.

DOMAIN: {domain}

CANDIDATE SIGNALS:
{signal_lines}

Rank these signals by their asymmetric-opportunity score. An asymmetric opportunity is one where:
- A specific gap or pain point is named (not generic vibes)
- The signal cites concrete evidence (numbers, named entities, dated events)
- The pain is large enough that a small builder could capture meaningful value
- The space is not already saturated with funded incumbents

Return the indices of the top {n} signals as a JSON array, e.g. [3, 7, 1, 5, 0]. No prose."""

        resp = self.anthropic.messages.create(
            model="claude-opus-4-7",
            max_tokens=200,
            messages=[{"role": "user", "content": prompt}],
        )
        text = resp.content[0].text.strip()

        # Extract JSON array
        try:
            start = text.find("[")
            end = text.find("]") + 1
            indices = json.loads(text[start:end])
        except Exception:
            indices = list(range(min(n, len(signals))))

        return [signals[i] for i in indices if i < len(signals)][:n]


# =========================================================================
# Researcher Agent — validates one signal into a full opportunity report
# =========================================================================

class ResearcherAgent:
    """Validates a Scout signal via deep search + synthesis."""

    def __init__(self, exa: Exa, anthropic: Anthropic, memory: MemoryFabric):
        self.exa = exa
        self.anthropic = anthropic
        self.memory = memory
        self.console = Console()

    def validate(self, signal: ScoutSignal) -> OpportunityReport:
        self.console.print(Panel(f"[bold]Researcher[/bold] validating: {signal.headline}", style="magenta"))

        # Pull additional context from the signal's URL and adjacent sources.
        try:
            context = self.exa.get_contents(
                [signal.source_url],
                text={"max_characters": 4000},
            )
            primary_text = context.results[0].text if context.results else signal.snippet
        except Exception:
            primary_text = signal.snippet

        # Find supporting/contradicting evidence.
        try:
            related = self.exa.search_and_contents(
                f"{signal.headline} market size competitors",
                num_results=5,
                use_autoprompt=True,
                text={"max_characters": 1000},
            )
            related_blocks = "\n\n".join(
                f"- {r.title}\n  {r.url}\n  {(r.text or '')[:500]}"
                for r in related.results
            )
        except Exception:
            related_blocks = "(no related context available)"

        prompt = f"""You are Researcher, a SYNAPSE agent validating opportunity signals.

PRIMARY SIGNAL:
Headline: {signal.headline}
URL: {signal.source_url}
Primary text: {primary_text[:3000]}

RELATED CONTEXT:
{related_blocks}

Validate this as an asymmetric opportunity. Produce a structured opportunity report with:
- opportunity_statement: 2 crisp sentences
- signal_evidence: array of 3-5 evidence items, each with statement, source_url, excerpt
- why_now: what changed recently
- why_asymmetric: small effort, large payoff justification
- competitive_vacuum: who is NOT building this and why
- estimated_value_usd: integer rough TAM or demand signal
- confidence: 1-10
- recommendation: "GO" | "NO_GO" | "INVESTIGATE_FURTHER"
- reasoning: why this confidence and recommendation

Be honest. If the signal is weak, return NO_GO. If evidence is thin, return INVESTIGATE_FURTHER. Only return GO when at least three independent evidence points support the opportunity.

Return strictly valid JSON matching the schema. No prose outside the JSON."""

        resp = self.anthropic.messages.create(
            model="claude-opus-4-7",
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}],
        )
        text = resp.content[0].text.strip()

        # Robust JSON extraction
        try:
            start = text.find("{")
            end = text.rfind("}") + 1
            data = json.loads(text[start:end])
            return OpportunityReport(**data)
        except Exception as e:
            self.console.print(f"[red]Failed to parse researcher output: {e}[/red]")
            # Fail-safe: return a NO_GO report
            return OpportunityReport(
                opportunity_statement=f"Could not validate signal: {signal.headline}",
                signal_evidence=[SignalEvidence(
                    statement="Researcher parse failure",
                    source_url=signal.source_url,
                    excerpt=text[:200],
                )],
                why_now="Unknown",
                why_asymmetric="Unknown",
                competitive_vacuum="Unknown",
                estimated_value_usd=0,
                confidence=1,
                recommendation="NO_GO",
                reasoning="Researcher could not parse a structured report from the signal.",
            )


# =========================================================================
# Settlement — captures value, logs to memory, generates procedural patterns
# =========================================================================

class Settlement:
    """Records outcomes and proposes procedural-memory entries."""

    def __init__(self, memory: MemoryFabric, value_share: float = 0.10):
        self.memory = memory
        self.value_share = value_share
        self.console = Console()

    def settle(self, signal: ScoutSignal, report: OpportunityReport) -> dict[str, Any]:
        outcome = {
            "signal_headline": signal.headline,
            "signal_url": signal.source_url,
            "recommendation": report.recommendation,
            "estimated_value_usd": report.estimated_value_usd,
            "synapse_share_usd": int(report.estimated_value_usd * self.value_share)
                if report.recommendation == "GO" else 0,
            "confidence": report.confidence,
        }

        self.memory.ingest_execution({
            "type": "opportunity_cycle",
            "signal": asdict(signal),
            "report": report.model_dump(),
            "outcome": outcome,
        })

        # Generate procedural memory if GO with high confidence
        if report.recommendation == "GO" and report.confidence >= 7:
            self.memory.add_procedural({
                "pattern": f"High-confidence GO on signals matching: {signal.headline[:80]}",
                "context": report.why_asymmetric,
                "applicable_to": "future Scout queries",
            })

        return outcome


# =========================================================================
# Orchestrator — runs the full cycle
# =========================================================================

class SYNAPSECycle:
    """One end-to-end pass: Scout -> Researcher -> Settlement."""

    def __init__(self):
        anthropic_key = os.environ.get("ANTHROPIC_API_KEY")
        exa_key = os.environ.get("EXA_API_KEY")
        if not anthropic_key:
            raise RuntimeError("ANTHROPIC_API_KEY not set")
        if not exa_key:
            raise RuntimeError("EXA_API_KEY not set")

        self.anthropic = Anthropic(api_key=anthropic_key)
        self.exa = Exa(exa_key)
        self.memory = MemoryFabric()
        self.scout = ScoutAgent(self.exa, self.anthropic, self.memory)
        self.researcher = ResearcherAgent(self.exa, self.anthropic, self.memory)
        self.settlement = Settlement(self.memory)
        self.console = Console()

    def run(self, domain: str, max_signals: int = 3) -> list[dict[str, Any]]:
        # 1. Scout for raw signals
        signals = self.scout.scan(domain, n_signals=max_signals)
        if not signals:
            self.console.print("[red]No signals found. Aborting cycle.[/red]")
            return []

        # 2. Researcher validates each (sequentially to be safe with rate limits)
        results = []
        for sig in signals:
            try:
                report = self.researcher.validate(sig)
                outcome = self.settlement.settle(sig, report)
                results.append({
                    "signal": asdict(sig),
                    "report": report.model_dump(),
                    "outcome": outcome,
                })
                self._print_report(sig, report, outcome)
            except Exception as e:
                self.console.print(f"[red]Cycle failure on signal: {e}[/red]")

        # 3. Persist run summary
        reports_dir = Path("./reports")
        reports_dir.mkdir(exist_ok=True)
        report_path = reports_dir / f"{datetime.utcnow().strftime('%Y%m%dT%H%M%S')}.json"
        report_path.write_text(json.dumps(results, indent=2, default=str))
        self.console.print(f"\n[bold green]Cycle complete.[/bold green] Full report: {report_path}")

        return results

    def _print_report(self, sig: ScoutSignal, report: OpportunityReport, outcome: dict):
        md = f"""
## Opportunity: {sig.headline}

**Source:** {sig.source_url}

**Statement:** {report.opportunity_statement}

**Confidence:** {report.confidence}/10  |  **Recommendation:** {report.recommendation}

**Why now:** {report.why_now}

**Why asymmetric:** {report.why_asymmetric}

**Competitive vacuum:** {report.competitive_vacuum}

**Estimated value:** ${report.estimated_value_usd:,}  |  **SYNAPSE share (10%):** ${outcome['synapse_share_usd']:,}

**Reasoning:** {report.reasoning}
"""
        self.console.print(Markdown(md))


# =========================================================================
# CLI
# =========================================================================

def main():
    parser = argparse.ArgumentParser(description="SYNAPSE Opportunity Swarm prototype")
    parser.add_argument("--domain", default="AI agent infrastructure",
                        help="Domain to scan for opportunities")
    parser.add_argument("--n", type=int, default=3,
                        help="Number of signals to validate")
    args = parser.parse_args()

    cycle = SYNAPSECycle()
    cycle.run(args.domain, max_signals=args.n)


if __name__ == "__main__":
    main()
