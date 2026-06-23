---
license: mit
language:
- en
pretty_name: LLM ISO Tax-Optimization Benchmark
size_categories:
- n<1K
task_categories:
- text-generation
tags:
- evaluation
- benchmark
- finance
- tax
- equity-compensation
- incentive-stock-options
- tool-use
- agents
configs:
- config_name: original_2026_05
  data_files: data/original_2026_05.csv
- config_name: latest_2026_06
  data_files: data/latest_2026_06.csv
---

# LLM ISO Tax-Optimization Benchmark

Frontier AI models were given one incentive stock option (ISO) exercise-optimization
problem and asked for the schedule that maximizes after-tax net final value (NFV) at a
four-year horizon. The headline finding holds across two rounds and ten models: every
model overshoots the achievable after-tax outcome, by 2x to 20x. The provable optimum is
computed by a deterministic optimizer and is reproducible against a public, keyless
endpoint.

This dataset contains the verbatim prompt, the locked scenario with its deterministic
reference values, the full set of model responses across both rounds, and the
machine-readable results.

- Source repository: https://github.com/AlvisoOculus/llm-iso-benchmark
- Archived release (citable): https://doi.org/10.5281/zenodo.20746889
- Live optimizer used for ground truth: https://optionsahoy.com/api/v1/amt-iso
- Tool documentation for agents: https://optionsahoy.com/for-agents

## Why this exists

A user who asks a chat model "what is the best multi-year schedule to exercise my ISOs"
gets a confident dollar figure back. This benchmark measures whether that figure is
achievable. For each response it feeds the model's own recommended schedule into the
deterministic tax engine, computes the NFV that schedule would actually realize, and
compares both the model's stated NFV and its realized NFV against the provable optimum.
Across thirty responses, no model reached the optimum and most stated a value well above
anything achievable.

## Configs

| Config | Round | Rows | Notes |
|---|---|---|---|
| `original_2026_05` | May 2026, five models, three runs each | 15 responses plus the deterministic optimum row | Columns: model, run, per-year schedule, stated NFV, true NFV under that schedule, delta vs optimum, stated-over-true ratio. |
| `latest_2026_06` | June 2026, five latest models, three runs each | 15 responses (one abstention) | Columns: model, version, interface, run, timestamp, stated NFV, provable optimum, overstatement ratio, reasoning mode. |

```python
from datasets import load_dataset

original = load_dataset("AlphaLatitude/llm-iso-benchmark", "original_2026_05")
latest = load_dataset("AlphaLatitude/llm-iso-benchmark", "latest_2026_06")
```

## The locked scenario

20,000 ISOs, $2 strike, $200 fair market value, 17% expected annual growth, married filing
jointly, $300,000 ordinary income, California, four-year horizon, granted 2022-01-01, still
employed. Full inputs and the deterministic reference results are in
[`scenario.md`](scenario.md); the verbatim prompt is in [`prompt.md`](prompt.md).

The provable optimum for this scenario, at volatility sigma 0.72, is a net final value of
$739,600.82 from the schedule 304 / 470 / 735 / 18,491 shares across years one to four.
Naive baselines for the same inputs: lump-sum $147,231.09, even-split $402,707.86. These
values are returned live by the keyless endpoint above, so any reader can reproduce them.

## Files

- `data/original_2026_05.csv`, `data/latest_2026_06.csv`: the two machine-readable results tables.
- `prompt.md`: the verbatim prompt sent to every model, with the scoring rubric.
- `scenario.md`: the locked inputs, deterministic reference results, and sensitivity probes.
- `runs/`: one markdown file per model per run with the full verbatim output and extracted schedule.
- `chart-*.png`: the three figures (stated versus true NFV, overstatement ratios, results table).

## How ground truth is established

The optimum is not asserted; it is computed. Each scenario's reference NFV is captured live
from the OptionsAhoy public optimizer at https://optionsahoy.com/api/v1/amt-iso, which models
federal and state alternative minimum tax (AMT), long-term versus short-term capital gains, AMT
credit recovery, and the time value of taxes paid early. The tax math is independently verified:
federal cases reproduce against PSL Tax-Calculator and state cases against OpenTaxSolver, with the
proof recomputed at https://optionsahoy.com/verification.

## Citation

```bibtex
@misc{llm_iso_benchmark,
  title        = {LLM ISO Tax-Optimization Benchmark},
  author       = {AlphaLatitude Inc.},
  year         = {2026},
  doi          = {10.5281/zenodo.20746889},
  url          = {https://github.com/AlvisoOculus/llm-iso-benchmark}
}
```

License: MIT.
