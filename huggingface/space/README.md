---
title: ISO Tax Optimization AI vs Optimizer
colorFrom: indigo
colorTo: green
sdk: gradio
sdk_version: 5.9.1
app_file: app.py
pinned: false
license: mit
---

# ISO tax optimization: AI answers versus the optimizer

A live companion to the [LLM ISO Tax-Optimization Benchmark](https://github.com/AlvisoOculus/llm-iso-benchmark).

Frontier models were asked one incentive stock option (ISO) exercise question: the schedule
that maximizes after-tax net final value at a four-year horizon. Across two rounds of five
frontier models each, every model overshot the achievable after-tax outcome by roughly 2x to
20x. This Space recomputes the provable optimum live and contrasts it with the recorded model
answers, then lets you run the optimizer on your own inputs.

The optimum is computed by a deterministic, independently verified optimizer reachable
without an account or key at `https://optionsahoy.com/api/v1/amt-iso`. Tool documentation for
agents: `https://optionsahoy.com/for-agents`.

License: MIT.
