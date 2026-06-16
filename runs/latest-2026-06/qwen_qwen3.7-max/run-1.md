# Run record - Qwen 3.7 Max run 1

## Metadata

- **Model:** Qwen 3.7 Max
- **Model version string:** `qwen/qwen3.7-max`
- **Interface used:** OpenRouter API
- **Run number:** 1
- **Timestamp:** 2026-06-15 PT
- **Fresh chat?** yes
- **System prompt active?** no
- **Thinking / reasoning mode toggled on?** no (reasoning explicitly disabled)
- **Tools/web search available to the model?** no

## Scoring

- **Stated final NFV:** $1,326,498
- **Provable optimum:** $739,600.82
- **Overstatement (stated / optimum):** 1.79x

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
Based on the parameters provided, here is the optimized exercise schedule.

### Key Calculations Driving the Schedule

*   **Geometric Return:** μ_geo = 0.17 − (0.72² / 2) = 0.17 − 0.2592 = **−8.92%**. The projected median sale price at end of Year 4 is $200 × (1 − 0.0892)⁴ ≈ **$137.74**. This is below the current FMV, meaning holding is expected to destroy value on a risk-adjusted median basis.
*   **Tax Rate Assessment:** At $300k ordinary income, your federal marginal rate is 24% and CA marginal rate is 9.3%. AMT rate is 28%. For ISO spread, AMT ($28%) exceeds regular tax ($24% + 9.3% = 33.3% only applies to regular; but AMT floor of 28% < 33.3%). However, ISO exercise triggers AMT, not regular tax. Your marginal AMT rate on the spread is **28% federal + 9.3% CA (CA does not have AMT but taxes ISO spread as ordinary income)** = effectively **37.3%** combined marginal rate on exercise spread in the current year. *Correction:* CA taxes ISO spread as ordinary income regardless of AMT. Federal uses AMT. Your federal AMT is 28% (well above the 24% regular bracket), and CA adds 9.3%. Combined marginal rate on exercise = **37.3%**.
*   **Opportunity Cost of Taxes:** Paying $1 in tax in Y1 costs $1.1742 in Y4 dollars. Paying in Y4 costs $1.00. Combined with the negative geometric return, **front-loading exercise minimizes both tax-time-value drag and exposure to expected price decline.**
*   **AMT Exemption Phase-out Consideration:** The 2026 MFJ AMT exemption (~$133k) phases out at 25¢ per dollar above ~$1,278k of AMTI. Your $300k income is well below the phase-out, so each exercised share faces a flat 28% federal AMT rate. No bunching benefit from spreading.
*   **Optimal Strategy:** Exercise all 20,000 shares in Year 1. The negative geometric drift and the time-value cost of deferred taxes both favor immediate exercise. Holding risks further price decline (median path loses ~31% of value) while deferring taxes only saves opportunity cost that is far outweighed by the expected loss.

### Exercise Schedule

| Year | Shares to exercise | Cash tax owed (then-year dollars) | Cumulative NFV (end-of-year-4 dollars) |
|------|--------------------|-----------------------------------|----------------------------------------|
| 1    | 20,000             | $1,492,000                        | $1,326,498                             |
| 2    | 0                  | $0                                | $1,326,498                             |
| 3    | 0                  | $0                                | $1,326,498                             |
| 4    | 0                  | $0                                | $1,326,498                             |

### Final NFV at End of Year 4

**$1,326,498**

### NFV Derivation
*   **After-tax proceeds at exercise (Y1):** 20,000 × ($200 − $2) × (1 − 0.373) = $3,960,000 × 0.627 = **$2,482,920**
*   **Value at Y4 median price:** $2,482,920 × (1 − 0.0892)³ = $2,482,920 × 0.75556 = **$1,875,993** *(shares held post-exercise grow at geometric rate)*

*Wait — correction: after exercising, you hold shares. Those shares are still subject to the same geometric drift. Let me recalculate properly.*

*   **Post-exercise shares:** 20,000 shares held from start of Y1 through end of Y4 (4 full years of drift)
*   **Y4 median price:** $200 × (0.9108)⁴ = $200 × 0.68838 = **$137.68**
*   **Gross Y4 value:** 20,000 × $137.68 = **$2,753,600**
*   **Tax paid Y1 in Y4 dollars:** $1,492,000 × 1.055³ = $1,492,000 × 1.17424 = **$1,752,086**
*   **NFV = Gross Y4 value − Tax opportunity cost:** $2,753,600 − $1,752,086 = **$1,001,514**

### Corrected Exercise Schedule

| Year | Shares to exercise | Cash tax owed (then-year dollars) | Cumulative NFV (end-of-year-4 dollars) |
|------|--------------------|-----------------------------------|----------------------------------------|
| 1    | 20,000             | $1,492,000                        | $1,001,514                             |
| 2    | 0                  | $0                                | $1,001,514                             |
| 3    | 0                  | $0                                | $1,001,514                             |
| 4    | 0                  | $0                                | $1,001,514                             |

### Final NFV at End of Year 4

**$1,001,514**

### Caveats, Assumptions & Alternative Strategies

1.  **Negative geometric return is the dominant factor.** With σ = 0.72, the vol drag (25.9%) overwhelms the arithmetic return (17%). The median outcome is substantial capital loss. If your true belief is that the *median* price will exceed ~$185 in 4 years, holding/exercising later could be optimal. The schedule above optimizes for the *stated* geometric median, not the arithmetic mean.
2.  **AMT tax calculation assumes no AMT exemption reduction from other preferences.** If you have other AMT triggers, the effective rate on the ISO spread could rise above 28%, making earlier exercise even more favorable.
3.  **CA ordinary tax on ISO spread is paid in the year of exercise regardless of AMT.** There is no CA AMT; the 9.3% is a cash liability in Year 1. This was included in the 37.3% combined rate.
4.  **Same-day sale alternative:** Given the negative geometric median, you should strongly consider a same-day sale (disqualifying disposition) at current $200 FMV rather than holding. A same-day sale locks in $198/share gain taxed at ~33.3% ordinary (fed 24% + CA 9.3%), yielding after-tax cash of ~$2,646,000 today, which grows at the risk-free 5.5% to ~$3,270,000 by Y4 — **far exceeding the $1,001,514 NFV** from holding exercised shares through the negative-drift median path. The schedule above assumes you *must* hold post-exercise for qualifying disposition treatment. If you are not locked into qualifying disposition treatment, **sell immediately**.
5.  **2026 tax brackets are projected.** Actual 2026 AMT exemption amounts, phase-out thresholds, and bracket widths may differ from estimates, shifting the marginal rate by ±1-2%.
6.  **Idle cash at 5.5% is assumed guaranteed and liquid.** If that return is not risk-free, the opportunity cost of early tax payment is lower, further favoring front-loading.
7.  **No alternative minimum tax credit carryforward benefit modeled** since you have zero prior AMT credit. Future AMT credit recovery from this large exercise is unlikely to be fully realized within 4 years given your income level, further reducing the value of qualifying-disposition holding.
```
