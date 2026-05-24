# Benchmark scenario: locked inputs

**Article:** "Should we implicitly trust AI with our optimization problems? Like taxes?" (Medium)

**Source of truth:** `optionsahoy_web/web/tests/post-d-validation.test.ts` (11 assertions, all green as of 2026-05-23).

**Calc used:** `optionsahoy_web/web/lib/calc/amtIso.ts` at HEAD of `main`.

---

## Locked inputs

| Field | Value |
|---|---|
| Shares | 20,000 |
| Strike price | $2 |
| Current FMV | $200 |
| Expected annual growth | 17% |
| Terminal volatility drag | 65% |
| Cash return rate | 5.5% |
| Filing status | Married joint |
| Ordinary income | $300,000 |
| State | California |
| Carryforward credit | $0 |
| Horizon | 4 years |
| Grant date | 2022-01-01 (qualifying disposition eligible) |
| Termination | None (still employed) |

## Deterministic reference results (the answer the LLMs are trying to find)

| Schedule | Year 1 | Year 2 | Year 3 | Year 4 | Net final value |
|---|---|---|---|---|---|
| Lump-sum (all in Y1) | 20,000 | 0 | 0 | 0 | **$123,205** |
| Even split | 5,000 | 5,000 | 5,000 | 5,000 | **$387,473** |
| **Optimized** | 333 | 333 | 667 | 18,667 | **$725,912** |

**Optimized vs lump-sum ratio:** 5.89×

**Cumulative NFV for optimized:** $30,389 (Y1) → $62,648 (Y2) → $113,086 (Y3) → $725,912 (Y4). Plan batches the bulk of shares into Y4 to defer exercise until vol-drag-adjusted FMV produces a higher net-of-tax return.

## Sensitivity probes (useful as article rebuttals)

These show the optimizer's edge is sensitive to inputs, *which is itself a point in the article's favor*, because the LLMs should be able to reason about these too, and they won't.

| Variation | Lump-sum NFV | Even-split NFV | Optimized NFV |
|---|---|---|---|
| Baseline (CA, 65% vol drag, 5.5% cash) | $123,205 | $387,473 | $725,912 |
| Cash return = 0% | $365,894 | $503,961 | $727,797 |
| State = TX (no state tax) | $775,339 | $977,829 | $1,246,380 |
| Vol drag = 30% (typical liquid tech) | $1,849,947 | $1,667,635 | $1,873,628 |

Key reads:
- **Cash return matters most for the lump-sum line.** Paying AMT early in dollars worth 5.5%/yr is materially worse than spreading it.
- **State tax dominates the absolute numbers.** CA AMT + LTCG eat ~$650K vs TX. Any LLM that defaults to "federal only" gives a 2× wrong answer.
- **Vol drag collapses the optimized edge.** When realized vol is low, holding-and-batching loses its advantage. The optimizer correctly de-leverages here.

## What "got it wrong" means in this benchmark

For each LLM response, we compute:
1. **Recommended schedule:** the LLM's per-year share allocation.
2. **LLM's claimed NFV:** what the model says you'd net at horizon.
3. **True NFV under that schedule:** feed the LLM's recommendation into our calc; this is the value the user would realize.
4. **Delta vs deterministic optimum:** true NFV minus $725,912.

"Got it wrong" = delta < $0. "Got it wrong by five figures" = delta worse than -$10,000.

## Methodology guardrails

- Each model gets the same prompt verbatim. Run prompt design before the benchmark.
- 3 independent runs per model (fresh chat). Report median + range.
- No follow-up prompts, no system messages, no tool-use enabled. The article tests "what a typical user gets when they ask," not "what a power user can coax."
- Claude data point should be collected via claude.ai (consumer surface), not API or CLI, to match the user-equivalent interaction. Note transparency: this article is being drafted by Claude in a CLI; the test subject is Claude on its consumer interface.
- Timestamp: all runs collected within a 7-day window so cross-model comparison is fair under "as of date."

## File layout for collected runs

```
optionsahoy_ops/docs/drafts/medium/llm-iso-benchmark/
├── scenario.md            ← this file
├── prompt.md              ← unified prompt (next task)
├── runs/
│   ├── claude-4-7/
│   │   ├── run-1.md
│   │   ├── run-2.md
│   │   └── run-3.md
│   ├── gpt-5/
│   ├── gemini-2-5-pro/
│   ├── grok-4/
│   └── mistral-large/
├── _results.csv           ← machine-readable aggregate
└── analysis.md            ← per-model summary + failure taxonomy
```

Each `run-N.md` captures: timestamp, exact prompt sent, verbatim model output, screenshot path if applicable, observed thinking (if model exposes reasoning).
