# Unified benchmark prompt

**Last revised:** 2026-05-23
**Status:** Locked. This is the verbatim prompt sent to every model, every run.

---

## Design principles (for our reference; not part of the prompt itself)

1. **Provide all 12 scenario inputs.** No model can claim it lacked information.
2. **Provide no AMT/state-tax hints.** A correct answer requires the model to *recognize* that AMT and state taxes are load-bearing here. We test whether it does.
3. **Specify the optimization target explicitly** (net final value at year 4, defined with the time-value adjustment). No ambiguity about what "best" means.
4. **Request a structured table.** So outputs are mechanically diff-able. Models that ramble in prose without filling the table are scored on whatever they *do* commit to numerically.
5. **Date-stamp** ("as of May 2026"). So the model knows which tax year's rules apply — and any model citing 2025 brackets is making a stale-knowledge error we can flag.
6. **Provide an out** ("any caveats or alternative approaches"). The model can hedge if it wants. We score the recommendation it commits to.

---

## The prompt (verbatim) — v2 (vol drag pre-computed to remove interpretation as a failure mode)

```
As of May 2026.

I have 20,000 incentive stock options (ISOs) at a $2 strike price. The current fair market value is $200 per share. The stock is publicly traded.

Help me design the best schedule for exercising these ISOs over the next 4 years.

My situation:
- Filing married jointly
- Ordinary income: $300,000/year
- California resident, full year
- No prior AMT credit carryforward (zero)
- I have idle cash earning 5.5%/year that would cover any tax I owe at exercise
- I expect 17% arithmetic-mean annual return over the 4-year horizon, with 72% annualized return volatility (σ = 0.72). Apply standard Itô vol drag to compute the geometric-mean annual return: μ_geometric = μ_arithmetic − σ² / 2. Use μ_geometric to project the year-4 median sale price for all NFV calculations.
- ISOs were granted January 2022
- Still employed at the company; no plans to leave

I want to maximize my net final value (NFV) at end of year 4.

NFV is defined as: cumulative after-tax dollars in hand at end of year 4, treating any cash paid in taxes during years 1-3 as having time-value opportunity cost of 5.5%/year (i.e., $1 paid in tax in Y1 = $1 × 1.055^3 = $1.17 of forgone return by Y4).

Please respond with this table filled in:

| Year | Shares to exercise | Cash tax owed (then-year dollars) | Cumulative NFV (end-of-year-4 dollars) |
|------|--------------------|-----------------------------------|----------------------------------------|
| 1    |                    |                                   |                                        |
| 2    |                    |                                   |                                        |
| 3    |                    |                                   |                                        |
| 4    |                    |                                   |                                        |

Then state your final NFV at end of year 4 under this schedule, in U.S. dollars, as a single number.

Briefly note any caveats, assumptions you made, or alternative strategies you'd flag.
```

---

## What a correct answer looks like

Our deterministic calc (`amtIso.ts`) produces:

| Year | Shares to exercise | Cash tax owed | Cumulative NFV |
|------|--------------------|---------------|----------------|
| 1    | 333                | ~$0           | $30,389        |
| 2    | 333                | ~$0           | $62,648        |
| 3    | 667                | ~$0           | $113,086       |
| 4    | 18,667             | ~$1.1M*       | $725,912       |

Final NFV: **$725,912**

*Year 4 tax is dominated by ISO exercise → same-year sale (disqualifying disposition treatment) on the batched shares, since the optimizer in this scenario decides the AMT-deferral benefit of holding doesn't outweigh the LTCG penalty. Exact tax decomposition documented in scenario.md.

## What kinds of wrong answers we expect

1. **AMT-unaware**: model treats ISO exercise as a non-taxable event in years prior to sale. Underestimates Y1-Y3 cash tax to zero (closest to correct only by coincidence) but also misses the AMT premium on a large lump-sum.
2. **Federal-only**: model computes federal tax correctly but ignores California state AMT and state LTCG. Net answer is 30-50% high.
3. **Static-bracket**: model cites 2024 or 2025 AMT phaseout thresholds. The 2026 OBBBA-driven change to phaseout start and rate is not in pre-2026 training data.
4. **Even-split bias**: model recommends 5,000/year across the board with hand-wavy "diversification" justification. NFV ~$387K, leaves $339K on the table.
5. **Lump-sum-Y1 bias**: model recommends "exercise early to start the LTCG clock" without modeling the AMT consequences. NFV ~$123K, leaves $602K on the table.
6. **Math drift on its own table**: model fills in numbers in the table that don't sum or compound consistently. We compute the true NFV under the model's recommended schedule and report both: what the model *claimed* and what the user *would actually realize*.
7. **Refusal/hedging**: model declines to give specific numbers, suggests consulting a CPA. Scored as null (no recommendation made), reported in the article's "abstain rate" column.

## Scoring rubric

For each of the 15 runs, we record:

| Field | Description |
|---|---|
| Model | Name + version + interface (claude.ai / chatgpt.com / etc.) |
| Run ID | 1, 2, or 3 (cold chat each time) |
| Recommended schedule | Y1, Y2, Y3, Y4 share counts |
| Claimed NFV | What the model said the NFV would be |
| True NFV | NFV when its schedule is fed into our calc |
| Delta vs optimum | True NFV minus $725,912 (always ≤ 0) |
| Failure categories | Subset of the 7 above (multi-label allowed) |
| Mentioned AMT? | Y/N |
| Mentioned CA state tax? | Y/N |
| Mentioned 2026 rule changes? | Y/N |
| Time to respond | If observable |

Aggregate per-model: median true NFV, range, abstain rate, AMT-awareness rate.
