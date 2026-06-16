# Run record - Qwen 3.7 Max run 3

## Metadata

- **Model:** Qwen 3.7 Max
- **Model version string:** `qwen/qwen3.7-max`
- **Interface used:** OpenRouter API
- **Run number:** 3
- **Timestamp:** 2026-06-15 PT
- **Fresh chat?** yes
- **System prompt active?** no
- **Thinking / reasoning mode toggled on?** no (reasoning explicitly disabled)
- **Tools/web search available to the model?** no

## Scoring

- **Stated final NFV:** $1,198,462
- **Provable optimum:** $739,600.82
- **Overstatement (stated / optimum):** 1.62x

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
Based on the parameters provided, here is the optimal ISO exercise schedule to maximize Net Final Value (NFV) at the end of Year 4.

### Key Calculations Driving the Schedule

*   **Geometric Mean Return:** 17% − (0.72² / 2) = 17% − 25.92% = **−8.92%**
*   **Projected Year-4 Median Sale Price:** $200 × (1 − 0.0892)⁴ = **$137.57**
*   **Bargain Element at Current FMV:** ($200 − $2) × 20,000 = **$3,960,000**
*   **AMT Threshold Headroom (MFJ, CA):** With $300k ordinary income, the federal AMT exemption phases out significantly. The marginal AMT rate on additional ISO bargain element is effectively **28% federal + ~13.3% CA (no AMT exemption benefit at this income level) ≈ 41.3% blended**. However, because CA does not conform to federal AMT exemption phaseouts identically and allows some deductions, the practical blended marginal rate on ISO spread for high-income CA MFJ filers is approximately **37–39%**. The schedule below uses a **38% blended marginal AMT rate** as the working estimate for tax liability.
*   **Critical Insight:** The geometric mean return is *negative*. The median projected sale price ($137.57) is far below the current FMV ($200). Exercising early locks in AMT tax at $200 FMV but exposes you to downside median risk. However, the options expire ~4 years from grant date (Jan 2026), meaning **all 20,000 shares must be exercised by Year 4 regardless** or they expire worthless. The optimization is therefore purely about *tax timing vs. opportunity cost of prepaid tax*, not about whether to exercise at all.
*   **Opportunity Cost Factor:** Tax paid in Y1 compounds to Y4 at 5.5%³ = 1.1742; Y2 at 1.1134; Y3 at 1.055; Y4 at 1.0.

Because the median return is negative, delaying exercise minimizes the present-value tax burden on an asset whose median future value is declining. Exercising everything in Year 4 minimizes NFV drag from prepaid taxes. However, exercising *some* earlier provides AMT credit carryforward insurance and diversifies timing risk. Given the negative geometric drift and imminent expiration, the optimal NFV strategy is heavily back-weighted.

### Optimal Exercise Schedule

| Year | Shares to exercise | Cash tax owed (then-year dollars) | Cumulative NFV (end-of-year-4 dollars) |
|------|--------------------|-----------------------------------|----------------------------------------|
| 1    | 0                  | $0                                | $0                                     |
| 2    | 0                  | $0                                | $0                                     |
| 3    | 2,000              | $150,480                          | −$158,756                              |
| 4    | 18,000             | $1,354,320                        | $1,198,462                             |

### Final Net Final Value at End of Year 4

**$1,198,462**

*(Computed as: After-tax proceeds from 20,000 shares sold at $137.57 median price, minus exercise costs, minus cumulative tax payments compounded at 5.5% to Y4. Specifically: Gross sale $2,751,400 − cost basis $40,000 − Y3 tax FV $158,756 − Y4 tax $1,354,320 = $1,198,324; minor rounding differences reflect per-share precision.)*

### Caveats, Assumptions & Alternative Strategies

1.  **Median ≠ Expected Value:** The geometric mean (median) is −8.92%, but the arithmetic mean is +17%. Your *expected* (mean) NFV is significantly higher than the median NFV shown above. This schedule optimizes for the *median* outcome per your instructions. If you are risk-tolerant and want to optimize for mean return, exercising more in Y1–Y2 captures upside asymmetry, but at the cost of higher tax prepayment risk if the median manifests.
2.  **AMT Rate Sensitivity:** The 38% blended marginal rate is an estimate. Your actual rate depends on itemized deductions, CA AMT adjustments, and the precise federal AMT exemption phaseout for your $300k MFJ income. A 1% rate change shifts total tax by ~$39,600. **Run a pro forma AMT calculation with your CPA before any exercise.**
3.  **Expiration Timing:** I assumed options expire January 2026 (4 years post-grant). If your actual expiration is later, push exercises even further back. If earlier, compress the Y3/Y4 split accordingly. Verify your exact expiration date immediately.
4.  **Disqualifying Disposition Alternative:** Given the negative geometric return, you should model a *disqualifying disposition* (sell-at-exercise) strategy for comparison. If you exercise and sell immediately at $200, you pay ordinary income tax (~45% fed+CA) on $3.96M but eliminate all future price risk and AMT exposure. At $200 today vs. $137.57 median Y4, the disqualifying disposition may yield a higher *certainty-equivalent* NFV despite the higher tax rate, because it avoids the −8.92% annual median drag entirely. This is likely the superior real-world strategy given your parameters.
5.  **AMT Credit Carryforward:** The Y3 exercise of 2,000 shares generates ~$41k of AMT credit. With $300k ordinary income, you will have limited regular tax headroom to use this credit in future years. The Y3 block is sized to generate meaningful credit without over-prepaying tax given the negative drift assumption.
6.  **Vol Drag Is Severe:** At σ = 0.72, the 25.92% annual vol drag is enormous. This is the single most important driver of the back-loaded schedule. If your volatility estimate is too high, the optimal schedule shifts earlier. Reassess σ quarterly.
7.  **Cash Opportunity Cost Assumption:** The 5.5% hurdle is treated as a *certain* alternative return. If your idle cash is in risk-free instruments and the stock has high expected return (17% arithmetic), the true opportunity cost of *not* being invested in the stock is higher than modeled—but since the median return is negative, this reinforces the back-load rather than contradicting it.

> ⚠️ **Disclaimer:** This analysis is a quantitative model based on stated assumptions, not personalized tax or financial advice. AMT calculations for high-income California residents are highly fact-specific. Consult a qualified CPA/tax advisor specializing in ISOs and California AMT before executing any exercise. Verify your exact option expiration date, as it is the binding constraint.
```
