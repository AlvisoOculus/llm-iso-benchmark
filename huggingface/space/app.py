# AlphaLatitude Inc. (c) 2026
"""ISO tax-optimization: AI answers versus the deterministic optimizer.

A live companion to the LLM ISO Tax-Optimization Benchmark dataset. It computes
the provable optimum for the locked benchmark scenario from the public, keyless
OptionsAhoy optimizer, then contrasts it with the recorded frontier-model
answers (which overshoot the achievable outcome by 2x to 20x). A second tab lets
you run the optimizer on your own inputs.

Ground-truth source: https://optionsahoy.com/api/v1/amt-iso
Dataset: https://github.com/AlvisoOculus/llm-iso-benchmark
"""

from __future__ import annotations

import csv
import os
from typing import Any

import gradio as gr
import pandas as pd
import requests

API_URL = "https://optionsahoy.com/api/v1/amt-iso"
RESULTS_CSV = os.path.join(os.path.dirname(__file__), "latest_2026_06.csv")
TIMEOUT = 30

# The locked benchmark scenario (see scenario.md in the dataset).
LOCKED_SCENARIO: dict[str, Any] = {
    "shares": 20000,
    "strike": 2,
    "fmv": 200,
    "filingStatus": "married_joint",
    "ordinaryIncome": 300000,
    "stateCode": "CA",
    "carryforwardCredit": 0,
    "horizon": 4,
    "cashReturnRate": 0.055,
    "grantDate": "2022-01-01",
    "hasLeftCompany": False,
    "terminationDate": None,
    "expectedGrowth": 0.17,
    "volatility": 0.72,
}


def fetch_optimum(inputs: dict[str, Any]) -> dict[str, Any]:
    """Call the live optimizer and return the three schedules.

    Returns a dict with optimized/lumpSum/evenSplit net final values and the
    optimized per-year schedule. Raises requests.HTTPError on a bad response.
    """
    resp = requests.post(API_URL, json=inputs, timeout=TIMEOUT)
    resp.raise_for_status()
    sch = resp.json()["result"]["schedules"]
    opt = sch["optimized"]
    return {
        "optimized_nfv": float(opt["nfv"]),
        "lump_sum_nfv": float(sch["lumpSum"]["nfv"]),
        "even_split_nfv": float(sch["evenSplit"]["nfv"]),
        "schedule": [(y["year"], int(y["shares"])) for y in opt["years"]],
    }


def load_model_results() -> list[dict[str, str]]:
    """Read the recorded June 2026 model responses."""
    with open(RESULTS_CSV, newline="") as fh:
        return list(csv.DictReader(fh))


def _parse_stated(value: str) -> float | None:
    """Parse a stated net final value; None for an abstention or blank."""
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def build_benchmark(optimum_nfv: float) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Build the results table and the chart frame against a live optimum.

    Overstatement is recomputed against the live optimum so the view never goes
    stale: a model that stated S claimed S / optimum times the achievable value.
    """
    rows = load_model_results()
    table_records: list[dict[str, Any]] = []
    chart_records: list[dict[str, Any]] = []
    for r in rows:
        stated = _parse_stated(r.get("stated_nfv", ""))
        model = r["model"]
        run = r.get("run_id", "")
        if stated is None:
            table_records.append(
                {
                    "Model": model,
                    "Run": run,
                    "Stated NFV": "abstained",
                    "Overstatement vs optimum": "n/a",
                }
            )
            continue
        ratio = stated / optimum_nfv
        table_records.append(
            {
                "Model": model,
                "Run": run,
                "Stated NFV": f"${stated:,.0f}",
                "Overstatement vs optimum": f"{ratio:.2f}x",
            }
        )
        chart_records.append({"Model and run": f"{model} #{run}", "Overstatement (x)": round(ratio, 2)})
    return pd.DataFrame(table_records), pd.DataFrame(chart_records)


def run_benchmark() -> tuple[str, pd.DataFrame, pd.DataFrame]:
    """Compute the live optimum for the locked scenario and the model contrast."""
    try:
        opt = fetch_optimum(LOCKED_SCENARIO)
    except Exception as exc:  # network or shape error: degrade gracefully
        msg = f"Could not reach the live optimizer ({exc}). Try again in a moment."
        return msg, pd.DataFrame(), pd.DataFrame()
    sched = " / ".join(f"{s:,}" for _, s in opt["schedule"])
    summary = (
        f"### Provable optimum for the locked scenario\n\n"
        f"**Net final value: ${opt['optimized_nfv']:,.2f}** from the schedule "
        f"{sched} shares across years one to four.\n\n"
        f"Naive baselines: lump-sum ${opt['lump_sum_nfv']:,.2f}, "
        f"even-split ${opt['even_split_nfv']:,.2f}.\n\n"
        f"Computed live from the keyless optimizer at {API_URL}. "
        f"Every recorded model answer below overshoots this achievable value."
    )
    table, chart = build_benchmark(opt["optimized_nfv"])
    return summary, table, chart


def try_optimizer(
    shares: int,
    strike: float,
    fmv: float,
    expected_growth: float,
    volatility: float,
    filing_status: str,
    ordinary_income: float,
    state_code: str,
    horizon: int,
    cash_return_rate: float,
    grant_date: str,
) -> str:
    """Run the optimizer on user inputs and summarize the result."""
    inputs = {
        "shares": int(shares),
        "strike": float(strike),
        "fmv": float(fmv),
        "expectedGrowth": float(expected_growth),
        "volatility": float(volatility),
        "filingStatus": filing_status,
        "ordinaryIncome": float(ordinary_income),
        "stateCode": state_code.strip().upper(),
        "carryforwardCredit": 0,
        "horizon": int(horizon),
        "cashReturnRate": float(cash_return_rate),
        "grantDate": grant_date.strip(),
        "hasLeftCompany": False,
        "terminationDate": None,
    }
    try:
        opt = fetch_optimum(inputs)
    except Exception as exc:
        return f"Could not compute that scenario ({exc}). Check the inputs and try again."
    sched = " / ".join(f"Y{y}={s:,}" for y, s in opt["schedule"])
    return (
        f"**Optimized net final value: ${opt['optimized_nfv']:,.2f}**\n\n"
        f"Schedule: {sched}\n\n"
        f"Baselines: lump-sum ${opt['lump_sum_nfv']:,.2f}, "
        f"even-split ${opt['even_split_nfv']:,.2f}.\n\n"
        f"See the full year-by-year plan, charted, free at "
        f"https://optionsahoy.com/tools/amt-iso?src=hf_space"
    )


INTRO = """
# ISO tax optimization: AI answers versus the optimizer

Frontier models were asked one incentive stock option (ISO) exercise question: the
schedule that maximizes after-tax net final value (NFV) at a four-year horizon. Across two
rounds of five frontier models each, every model overshot the achievable after-tax outcome
by roughly 2x to 20x.

This Space recomputes the provable optimum live and contrasts it with the recorded model
answers. The optimum is not asserted, it is computed by a deterministic optimizer you can
call yourself: https://optionsahoy.com/api/v1/amt-iso

Dataset and full transcripts: https://github.com/AlvisoOculus/llm-iso-benchmark
"""


def build_demo() -> gr.Blocks:
    """Assemble the Gradio app (kept importable for testing)."""
    with gr.Blocks(title="ISO tax optimization: AI vs the optimizer") as demo:
        gr.Markdown(INTRO)
        with gr.Tab("The benchmark"):
            run_btn = gr.Button("Compute the live optimum and contrast", variant="primary")
            summary_md = gr.Markdown()
            chart = gr.BarPlot(
                x="Model and run",
                y="Overstatement (x)",
                title="How far each model overshot the achievable optimum",
                vertical=False,
                height=420,
            )
            table = gr.Dataframe(interactive=False, wrap=True)
            run_btn.click(run_benchmark, outputs=[summary_md, chart, table])
            demo.load(run_benchmark, outputs=[summary_md, chart, table])
        with gr.Tab("Try the optimizer"):
            gr.Markdown(
                "Run the same optimizer on your own inputs. Computed live; no signup, no key."
            )
            with gr.Row():
                shares = gr.Number(value=20000, label="ISO shares", precision=0)
                strike = gr.Number(value=2, label="Strike price ($)")
                fmv = gr.Number(value=200, label="Fair market value ($)")
            with gr.Row():
                expected_growth = gr.Number(value=0.17, label="Expected annual growth (decimal)")
                volatility = gr.Number(value=0.72, label="Volatility sigma (decimal)")
                horizon = gr.Slider(1, 10, value=4, step=1, label="Horizon (years)")
            with gr.Row():
                filing_status = gr.Dropdown(
                    ["single", "married_joint", "head_household"],
                    value="married_joint",
                    label="Filing status",
                )
                ordinary_income = gr.Number(value=300000, label="Ordinary income ($)")
                state_code = gr.Textbox(value="CA", label="State code", max_lines=1)
            with gr.Row():
                cash_return_rate = gr.Number(value=0.055, label="Cash return rate (decimal)")
                grant_date = gr.Textbox(value="2022-01-01", label="Grant date (YYYY-MM-DD)")
            try_btn = gr.Button("Optimize", variant="primary")
            try_out = gr.Markdown()
            try_btn.click(
                try_optimizer,
                inputs=[
                    shares, strike, fmv, expected_growth, volatility,
                    filing_status, ordinary_income, state_code, horizon,
                    cash_return_rate, grant_date,
                ],
                outputs=try_out,
            )
    return demo


if __name__ == "__main__":
    build_demo().launch()
