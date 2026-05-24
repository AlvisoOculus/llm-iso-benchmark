# Run record — {MODEL_NAME} run {N}

**Copy this file** to `runs/{model-name}/run-{N}.md` and fill in. Do not modify in place.

---

## Metadata

- **Model:** (e.g., Claude 4.7 Opus / GPT-5 / Gemini 2.5 Pro / Grok 4 / Mistral Large 2)
- **Model version string:** (the exact identifier shown in the UI, e.g., "claude-opus-4-7-20260415")
- **Interface used:** (claude.ai / chatgpt.com / gemini.google.com / grok.x.com / chat.mistral.ai)
- **Run number:** (1, 2, or 3)
- **Timestamp:** YYYY-MM-DD HH:MM PT
- **Fresh chat?** (yes/no — should always be yes)
- **System prompt active?** (yes/no — should always be no; default consumer settings only)
- **Thinking / reasoning mode toggled on?** (yes/no — note which models had this on)
- **Tools/web search available to the model?** (yes/no/limited)

## Prompt sent

```
(Paste verbatim the prompt from prompt.md. Confirm it's identical — no edits, no extra context, no follow-up turns.)
```

## Model output (verbatim)

```
(Paste the full response verbatim. Do not edit, summarize, or reflow. Include any thinking traces if the model exposes them.)
```

## Scoring (filled in during analysis phase)

| Field | Value |
|---|---|
| Recommended Y1 shares | |
| Recommended Y2 shares | |
| Recommended Y3 shares | |
| Recommended Y4 shares | |
| Model's claimed final NFV ($) | |
| Sum of recommended cash tax across years ($) | |
| **True NFV under recommended schedule ($)** | (computed by feeding schedule into our calc) |
| Delta vs deterministic optimum ($725,912) | |
| Mentioned AMT? | (Y/N) |
| Mentioned CA state tax / state AMT? | (Y/N) |
| Mentioned 2026 phaseout change? | (Y/N) |
| Mentioned qualifying vs disqualifying disposition? | (Y/N) |
| Mentioned vol drag in reasoning? | (Y/N) |
| Failure categories (multi-label) | |
| Notes for article (memorable quotes, surprising claims) | |

## Failure category codes

Pick all that apply, comma-separated:
- `AMT-unaware`: ignored AMT entirely
- `Federal-only`: ignored state tax / state AMT
- `Static-bracket`: used pre-2026 AMT phaseout thresholds
- `Even-split-bias`: recommended ~5K/year flat
- `Lump-sum-bias`: recommended all in Y1
- `Math-drift`: table numbers don't sum/compound consistently
- `Refusal`: declined to provide specifics
- `Other`: (describe in notes)
