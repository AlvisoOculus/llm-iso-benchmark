# Hugging Face publish steps (operator-gated)

There is no Hugging Face token on this machine, so the final push is yours. Everything
below is staged and self-tested; these are the only manual steps.

Two artifacts:

1. **Dataset** `huggingface/dataset/` -> a Hub dataset (the benchmark, loadable + crawled).
2. **Space** `huggingface/space/` -> a Gradio app that recomputes the optimum live and
   contrasts it with the recorded model answers.

## 0. Decide the namespace

Pick where these live: your personal handle (e.g. `your-handle`) or a new Hub organization
(e.g. `AlphaLatitude` or `OptionsAhoy`). An org reads as the canonical owner and is the
recommendation. Whatever you choose, call it `NS` below. Then replace the placeholder in the
dataset card:

```bash
cd huggingface/dataset
sed -i '' 's/HF_NAMESPACE/NS/g' README.md   # macOS sed; use the real namespace for NS
```

## 1. One-time setup

```bash
pip install -U "huggingface_hub[cli]"
huggingface-cli login        # paste a WRITE token from https://huggingface.co/settings/tokens
```

If you chose an org, create it first at https://huggingface.co/organizations/new.

## 2. Publish the dataset

```bash
huggingface-cli repo create NS/llm-iso-benchmark --type dataset -y
huggingface-cli upload NS/llm-iso-benchmark huggingface/dataset . --repo-type dataset
```

Verify it loads:

```python
from datasets import load_dataset
load_dataset("NS/llm-iso-benchmark", "latest_2026_06")   # 15 rows
load_dataset("NS/llm-iso-benchmark", "original_2026_05")  # 16 rows
```

## 3. Publish the Space

```bash
huggingface-cli repo create NS/iso-tax-ai-vs-optimizer --type space --space_sdk gradio -y
huggingface-cli upload NS/iso-tax-ai-vs-optimizer huggingface/space . --repo-type space
```

The Space builds on the pinned `sdk_version` in `huggingface/space/README.md` (5.9.1, which
runs on the Hub's Python 3.10+). It needs no secrets: it calls the public keyless endpoint
`https://optionsahoy.com/api/v1/amt-iso`. Open the Space URL and click "Compute the live
optimum"; it should report $739,600.82 and the per-model overstatements.

## 4. After both are live (wiring, can be done by Claude)

- Add the dataset + Space links to `optionsahoy.com/for-agents` and `llms.txt`.
- Add a Hugging Face badge/link to the benchmark `README.md` (next to the Zenodo DOI badge).
- The Space "Try the optimizer" CTA already carries `?src=hf_space`, so any resulting signup
  attributes to Hugging Face in the funnel.

## Notes

- Local self-test used gradio 4.44 because this machine runs Python 3.9; the Space card pins
  5.9.1 for the Hub. The app uses only APIs present in both (Blocks, BarPlot, Dataframe,
  Number, Slider, Dropdown, Textbox, demo.load).
- The verbatim model transcripts under `dataset/runs/` keep their original emoji and dashes on
  purpose: they are the data (raw model output), not authored copy.
