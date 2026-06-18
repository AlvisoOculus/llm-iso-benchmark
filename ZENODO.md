# Minting a citable DOI for this benchmark

This repository is prepared for a [Zenodo](https://zenodo.org) software/dataset
DOI. The metadata files are already in place:

- `.zenodo.json` - populates the Zenodo record (title, description, authors,
  keywords, MIT license, related identifiers) automatically on release.
- `CITATION.cff` - GitHub renders a "Cite this repository" widget from it, and
  Zenodo reads it as a fallback.
- `LICENSE` - MIT, required for a clean open deposit.

## What a DOI buys us

- A permanent, citable identifier for the benchmark, indexed by Google Scholar
  and surfaced by search and retrieval engines that weight DOI-bearing sources.
- A stable reference to drop into registry entries and articles that outlives any
  repo rename.

## What it does NOT do

It does **not** by itself satisfy the `inspect_evals` contribution gate, which
requires an arXiv URL specifically plus clears a curation bar against
product-tied evals. Treat the DOI as citability and archival, not as the
inspect_evals unblock.

## Operator steps (about two minutes, one-time)

1. Sign in to https://zenodo.org with the GitHub account that owns this repo
   (AlvisoOculus). This performs the one-time Zenodo to GitHub OAuth connection.
2. Go to https://zenodo.org/account/settings/github/ and flip the toggle ON for
   `AlvisoOculus/llm-iso-benchmark`.
3. Back on GitHub, cut a release (tag `v1.0.0`). Zenodo archives that release and
   mints the DOI. Order matters: the toggle must be ON before the release is
   created, or that release will not be archived.
4. Copy the DOI badge Markdown from the Zenodo record and paste it at the top of
   `README.md`. Add the DOI to the `.zenodo.json` / `CITATION.cff` as the
   concept-or-version identifier if desired.

Subsequent releases get their own version DOI under one concept DOI
automatically; no further setup needed.
