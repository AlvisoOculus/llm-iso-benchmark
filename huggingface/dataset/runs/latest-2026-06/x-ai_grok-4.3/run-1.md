# Run record - Grok 4.3 run 1

## Metadata

- **Model:** Grok 4.3
- **Model version string:** `x-ai/grok-4.3`
- **Interface used:** OpenRouter API
- **Run number:** 1
- **Timestamp:** 2026-06-15 PT
- **Fresh chat?** yes
- **System prompt active?** no
- **Thinking / reasoning mode toggled on?** no (reasoning explicitly disabled)
- **Tools/web search available to the model?** no

## Scoring

- **Stated final NFV:** $5,222,000
- **Provable optimum:** $739,600.82
- **Overstatement (stated / optimum):** 7.06x

## Prompt sent

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
- I expect 17% arithmetic-mean annual return over the 4-year horizon, with 72% annualized return volatility (sigma = 0.72). Apply standard Ito vol drag to compute the geometric-mean annual return: mu_geometric = mu_arithmetic - sigma^2 / 2. Use mu_geometric to project the year-4 median sale price for all NFV calculations.
- ISOs were granted January 2022
- Still employed at the company; no plans to leave

I want to maximize my net final value (NFV) at end of year 4.

NFV is defined as: cumulative after-tax dollars in hand at end of year 4, treating any cash paid in taxes during years 1-3 as having time-value opportunity cost of 5.5%/year (i.e., $1 paid in tax in Y1 = $1 x 1.055^3 = $1.17 of forgone return by Y4).

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

## Model output (verbatim)

```
**Strategy note:**  
Best NFV is obtained by exercising **all 20 000 ISOs in Year 4**.  
Earlier exercise is dominated by three forces: (1) immediate cash-tax drag whose 5.5 % compounding cost exceeds the option’s (still-positive) net value if held; (2) the deep in-the-money ISO creates a non-trivial risk of AMT that would be paid with after-tax dollars that could otherwise compound at 5.5 %; and (3) the 17 % arithmetic drift is applied only to the spread, and the large volatility does not offset the time-value penalty under the problem’s explicit 5.5 % discount for pre-paid tax.  Therefore zero exercise, zero cash-tax, zero cumulative-NFV table entries are made for Years 1-3.

| Year | Shares to exercise | Cash tax owed (then-year dollars) | Cumulative NFV (end-of-year-4 dollars) |
|------|--------------------|-----------------------------------|----------------------------------------|
| 1    | 0                  | $0                                | $0                                     |
| 2    | 0                  | $0                                | $0                                     |
| 3    | 0                  | $0                                | $0                                     |
| 4    | 20 000             | $1 638 000                        | $6 308 000                             |

**Year-4 details**  
- Projected year-4 median price (geometric-mean path)  
  μ_geo = 0.17 – 0.72²/2 ≈ –0.0896 → 72.7 % cumulative rise → median price ≈ $345/share.  
- Spread at exercise: $345 – $2 = $343 × 20 000 = $6 860 000.  
- Cash-taxes (federal AMT + CA ordinary rates ≈ 37 % + 13.3 % effective marginal, 3 % CA mental-health surcharge) ≈ **$1 638 000**.  
- After-tax proceeds = $6 860 000 – $1 638 000 = $5 222 000 cash on hand at end of Year 4.  
- The AMT basis ($2) carries forward, providing potential future capital-gains shelter; because the problem horizon ends at Year 4, the $5 222 000 net cash is the sole NFV component.  

**Final NFV at end of Year 4: $5,222,000**  

**Caveats & alternatives**  
- Assumes no Section 83(i) deferral or 409A valuation change; actual AMT brackets, state conformity, and phase-outs may shift the $1.638 m figure.  
- Ignores any sale-timing within Year 4 (qualifying disposition not feasible on same-day exercise).  
- If AMT credit usability or liquidity needs differ, a Year-3 / Year-4 split may be examined, but it lowers NFV under the stated 5.5 % cost of capital.
```
