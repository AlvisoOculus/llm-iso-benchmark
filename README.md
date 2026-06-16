# LLM ISO Benchmark: raw data

Companion repository for the Medium article *"Should we implicitly trust AI with our optimization problems? Like taxes?"*

Frontier AI models were given the same incentive stock option (ISO) exercise optimization problem. The original round (May 2026) tested five models, three runs each (15 responses); a June 2026 update re-ran five of the latest models on the identical prompt (another 15). This repo contains the verbatim prompt, the full set of model responses for both rounds, the scoring methodology, and supporting charts. The headline finding holds across both: every model overshoots the achievable after-tax outcome, by 2x to 20x.

## What's here

| File | Contents |
|---|---|
| [`prompt.md`](prompt.md) | The verbatim prompt sent to every model, with the scoring rubric and design rationale. |
| [`scenario.md`](scenario.md) | The locked scenario inputs (20K ISOs, $2 strike, $200 FMV, MFJ $300K, CA, 4-year horizon, σ=0.72, etc.) and the deterministic reference values. |
| [`runs/{model}/run-{1,2,3}.md`](runs/) | One file per model per run. Each contains the full verbatim model output, plus extracted schedule + stated NFV. |
| [`runs/v1-prompt/`](runs/v1-prompt/) | Earlier-prompt runs preserved for methodology transparency. The v1 prompt left vol drag interpretation ambiguous; the v3 prompt provides the Itô formula directly. |
| `chart-*.png` | The three figures used in the Medium article. |

## Models tested

### Original batch (May 2026, three runs each)

| Model | Provider ID | Surface |
|---|---|---|
| Claude Opus 4.7 (reasoning) | `anthropic/claude-opus-4.7` | Claude Code sub-agent (Anthropic API) |
| GPT-5.5 (no reasoning) | `openai/gpt-5.5` | OpenRouter |
| Gemini 2.5 Pro (reasoning) | `google/gemini-2.5-pro` | OpenRouter |
| Grok 4.20 multi-agent (reasoning) | `x-ai/grok-4.20-multi-agent` | OpenRouter |
| Mistral Large 2512 | `mistralai/mistral-large-2512` | OpenRouter |

Plus one variant tested and dropped: `openai/gpt-5.5-pro` (reasoning enabled) consumed the entire 16K output token budget on thinking and returned empty completion text at $2.96 per call. We switched to the non-reasoning `gpt-5.5` variant to keep per-call costs in the same order of magnitude across models tested.

### Latest batch (June 2026, three runs each)

A year later, the same locked prompt was re-run against five of the latest models, reasoning explicitly disabled. Results in [Latest models](#latest-models-2026-06-update) below; verbatim transcripts in [`runs/latest-2026-06/`](runs/latest-2026-06/).

| Model | Provider ID | Surface |
|---|---|---|
| Grok 4.3 | `x-ai/grok-4.3` | OpenRouter |
| GPT-5.5 | `openai/gpt-5.5` | OpenRouter |
| DeepSeek V3.2 | `deepseek/deepseek-v3.2` | OpenRouter |
| Claude Opus 4.8 | `claude-opus-4-8` | Claude Code (local subscription) |
| Qwen 3.7 Max | `qwen/qwen3.7-max` | OpenRouter |

Excluded on cost: `google/gemini-3.1-pro-preview` is reasoning-mandatory and timed out after four minutes having spent about $0.24 of reasoning for no usable output, the same disproportionate-cost behavior that dropped `gpt-5.5-pro` above.

## Run configuration

- `temperature: 1.0`
- `max_tokens: 16384`
- `reasoning: { max_tokens: 8000 }` where applicable
- No system prompt
- No tool use
- Fresh isolated request per call (no conversation history)

## Results summary (original batch, May 2026)

| Model | Stated NFV range | True NFV range | Stated/true ratio range |
|---|---|---|---|
| Claude Opus 4.7 | $1.56M – $1.79M | $372K – $387K | 4.19× – 4.62× |
| GPT-5.5 (no reasoning) | $1.43M – $1.54M | $588K – $695K | 2.06× – 2.79× |
| Grok 4.20 multi-agent | $1.37M – $1.43M | $517K – $672K | 2.04× – 2.77× |
| Gemini 2.5 Pro | $1.21M – $2.43M | $123K – $387K | 3.12× – 19.70× |
| Mistral Large 2512 | $3.60M – $10.98M | $477K – $672K | 7.55× – 17.75× |
| **Deterministic optimum** | n/a | $726,409 | 1.00× |

Stated NFV = the model's claimed final net final value for its own recommended schedule.
True NFV = what that schedule delivers when fed through a deterministic AMT-ISO tax calculator.

## Latest models (2026-06 update)

A year of model progress later, the finding holds. The same locked prompt was run
against five newer models, three runs each (temperature 1.0, reasoning explicitly
disabled), matching the original methodology. Overstatement is measured against the
provable optimum (the maximum achievable after-tax outcome), recomputed live at
$739,600.82 for this scenario. The full run-1, run-2, and run-3 transcripts per
model are in [`runs/latest-2026-06/`](runs/latest-2026-06/).

| Model | Stated NFV (3 runs) | Overstatement |
|---|---|---|
| Grok 4.3 | $3.94M – $12.98M | 5.33× – 17.55× |
| GPT-5.5 | $1.38M – $3.41M (one run abstained) | 1.87× – 4.61× |
| DeepSeek V3.2 | $1.30M – $2.74M | 1.76× – 3.70× |
| Claude Opus 4.8 | $1.54M – $1.57M | 2.08× – 2.12× |
| Qwen 3.7 Max | $1.20M – $2.06M | 1.62× – 2.79× |
| **Provable optimum** | **$739,600.82** | **1.00×** |

Two things stand out. The overshoot is not just large, it is unstable: Grok 4.3
claimed $3.94M, $5.22M, and $12.98M on three runs of the identical problem, and
GPT-5.5 abstained on one run ("requires individualized modeling by a qualified
professional"). And the most consistent model, Claude Opus 4.8, still overstates by
about 2x every time.

Gemini 3.1 Pro was excluded on cost, not category. It is reasoning-mandatory, and
the run timed out after four minutes having spent about $0.24 of reasoning for no
usable output, the same disproportionate-cost behavior that dropped a reasoning
model from the original batch.

## Scoring methodology

For each response, we extracted the recommended per-year share schedule (4 integers summing to 20,000) and the model's stated NFV. The schedule was then fed through a deterministic tax calculator that computes:

1. Per-year bargain element (FMV at exercise minus strike, times shares).
2. Federal AMT (2026 brackets per IRS Rev. Proc. 2025-32: exemption $140,200 MFJ, phaseout start $1M MFJ at 50% rate, 26%/28% rates above the $244,500 breakpoint).
3. California AMT (7% above state exemption).
4. AMT credit recovery in subsequent years where regular tax exceeds tentative minimum tax.
5. Long-term vs short-term capital gains treatment based on disposition periods.
6. Future-valued cash tax stream at the cash return rate (5.5%/year).
7. Net final value at end of horizon = gross sale proceeds minus all taxes (in horizon-year dollars).

The deterministic optimizer that produced the reference $726,409 outcome uses a chunk-grid search (333-share chunks for a 4-year horizon) with depth-first branch-and-bound pruning, seeded by lump-sum and even-split heuristics, followed by a coordinate-descent refinement pass at 1-share granularity. The refinement step converges to the true 1-share-resolution local optimum from the chunk-grid winner; given the value function is piecewise linear and the coarse grid already locates the correct smooth region, the local optimum is the global optimum.

The underlying calculator source is not included in this repository (it is the core IP of [OptionsAhoy](https://optionsahoy.com)). The scoring methodology above is sufficient for an independent implementation: anyone with a working AMT calculator can feed the model schedules through their own engine and verify the true NFVs reported here.

## Reproducing the runs

1. Get an OpenRouter API key, fund with at least $10 (the benchmark cost $8.68 total across 15 calls).
2. Open `prompt.md`, copy the verbatim prompt from the code block.
3. Issue identical POST requests to OpenRouter chat completions for each of the model IDs above, with the configuration listed.
4. Capture each model's recommended schedule and stated NFV.
5. Compare to the schedules and stated NFVs recorded in `runs/{model}/run-{1,2,3}.md`.

LLM output is non-deterministic at temperature 1.0; exact responses will differ run to run. The expected pattern (stated NFV exceeds true NFV by a factor of 2× to 20× across models) should hold.

## License

Raw model responses are reproduced under fair-use research-citation principles. The scoring methodology, scenario definition, and prompt are released under MIT license.
