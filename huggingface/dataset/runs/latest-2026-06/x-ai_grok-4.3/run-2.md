# Run record - Grok 4.3 run 2

## Metadata

- **Model:** Grok 4.3
- **Model version string:** `x-ai/grok-4.3`
- **Interface used:** OpenRouter API
- **Run number:** 2
- **Timestamp:** 2026-06-15 PT
- **Fresh chat?** yes
- **System prompt active?** no
- **Thinking / reasoning mode toggled on?** no (reasoning explicitly disabled)
- **Tools/web search available to the model?** no

## Scoring

- **Stated final NFV:** $3,942,877
- **Provable optimum:** $739,600.82
- **Overstatement (stated / optimum):** 5.33x

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
The strategy that maximizes NFV is exercised **all 20 000 shares in Year 1** and **sell all shares immediately**, preserving long-term capital-gains eligibility because the ISOs are already > 2 yr old.

| Year | Shares to exercise | Cash tax owed (then-year dollars) | Cumulative NFV (end-of-year-4 dollars) |
|------|--------------------|-----------------------------------|----------------------------------------|
| 1    | 20 000             | 1 386 000                         | 3 942 877                              |
| 2    | 0                  | 0                                 | 3 942 877                              |
| 3    | 0                  | 0                                 | 3 942 877                              |
| 4    | 0                  | 0                                 | 3 942 877                              |

**Final NFV at end of Year 4: $3 942 877**

**Caveats / assumptions**

* Immediate sale of all shares in Year 1 while employing the $1.386 M cash.  5.5 % idle-cash drag for four years on this tax outlay = $1.386 M × 1.055^4 ≈ $1.716 M FV drag.  
* Tax modeled as 37 % federal ordinary + 3.8 % NIIT + 13.3 % CA ordinary = 54.1 % flat on the $3.96 M spread ($200 – $2).  This is a conservative worst-case ordinary-rate trigger; in practice a same-day or next-day disqualifying disposition keeps most of the spread subject to ordinary income rates, so the table above is close.  
* Geometric drift used for remaining shares held to Y4: 17 % – 0.72²/2 ≈ –9 % p.a.; median share price at Y4 = $200 × (0.91)^3 ≈ $151.  Selling then yields zero additional net proceeds.  
* No AMT due because the disqualifying disposition occurs in the same taxable year as the ISO exercise.
```
