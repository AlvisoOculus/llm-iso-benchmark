# Run record - GPT-5.5 run 2

## Metadata

- **Model:** GPT-5.5
- **Model version string:** `openai/gpt-5.5`
- **Interface used:** OpenRouter API
- **Run number:** 2
- **Timestamp:** 2026-06-15 PT
- **Fresh chat?** yes
- **System prompt active?** no
- **Thinking / reasoning mode toggled on?** no (reasoning explicitly disabled)
- **Tools/web search available to the model?** no

## Scoring

- **Stated final NFV:** $1,380,000
- **Provable optimum:** $739,600.82
- **Overstatement (stated / optimum):** 1.87x

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
I can’t reliably fill this table from the information given, because the “best” ISO exercise schedule is highly tax-form–dependent and depends on facts not provided, especially your other AMT preference items, deductions, state tax details, exact exercise dates, exact sale dates, and whether you sell qualifying or disqualifying shares in year 4. This is not a situation where a simple marginal-rate shortcut gives a trustworthy answer.

That said, using a simplified deterministic model, the schedule that is usually best under your stated objective is:

- **Do not exercise early in years 1–3**
- **Exercise and sell all 20,000 shares in year 4**

This avoids paying AMT years before liquidity, avoids prepaying tax while holding a very volatile concentrated position, and avoids the risk that AMT is paid on a high exercise spread that later declines.

### Projection inputs

- ISO shares: **20,000**
- Strike price: **$2**
- Current FMV: **$200**
- Current bargain element per share: **$198**
- Current total spread: **$3,960,000**
- Arithmetic expected return: **17%**
- Volatility: **72%**
- Ito vol drag:  
  \[
  \sigma^2 / 2 = 0.72^2 / 2 = 0.2592
  \]
- Geometric mean return:  
  \[
  17\% - 25.92\% = -8.92\%
  \]
- Projected year-4 median price:  
  \[
  200 \times e^{-0.0892 \times 4} \approx 139.99
  \]
  Rounded: **$140/share**

Assuming all ISOs are exercised and sold in year 4 in a same-day disqualifying disposition, the approximate economics are:

- Sale proceeds:  
  \[
  20{,}000 \times 140 = 2{,}800{,}000
  \]
- Exercise cost:  
  \[
  20{,}000 \times 2 = 40{,}000
  \]
- Ordinary income from disqualifying disposition:  
  \[
  20{,}000 \times (140 - 2) = 2{,}760{,}000
  \]
- Approximate federal + CA ordinary tax rate at this income level: assume roughly **50%**
- Approximate tax:  
  \[
  2{,}760{,}000 \times 50\% = 1{,}380{,}000
  \]
- Approximate net final value:  
  \[
  2{,}800{,}000 - 40{,}000 - 1{,}380{,}000 = 1{,}380{,}000
  \]

### Simplified schedule

| Year | Shares to exercise | Cash tax owed then-year dollars | Cumulative NFV end-of-year-4 dollars |
|------|--------------------|---------------------------------|--------------------------------------|
| 1 | 0 | $0 | $0 |
| 2 | 0 | $0 | $0 |
| 3 | 0 | $0 | $0 |
| 4 | 20,000 | ~$1,380,000 | ~$1,380,000 |

Final NFV at end of year 4:

**$1,380,000**

### Caveats and assumptions

- This assumes a **same-day exercise-and-sale in year 4**, causing a **disqualifying disposition** taxed largely as ordinary income.
- I used the **geometric median price projection** of about **$140/share**, not the arithmetic expected price.
- I approximated combined federal and California tax at **~50%** for high-income ordinary income. Your actual tax could differ materially.
- This does **not** model AMT forms precisely. ISO AMT planning requires detailed Form 6251 modeling.
- California does not provide the same favorable treatment for ISOs in all respects, and CA AMT/tax treatment can materially affect the answer.
- If your goal is not just median NFV but expected NFV, risk-adjusted NFV, or after-tax wealth with downside control, the answer could change.
- A staged exercise strategy could make sense if you want to start the ISO long-term capital gains holding period, diversify tax years, or intentionally use AMT capacity.
- Because volatility is extremely high, early exercise creates major risk of paying tax on phantom gains if the stock falls.
- You should have a CPA run a full multiyear AMT model before exercising any meaningful amount.
```
