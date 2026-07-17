# Project rules

- After every implementation stage, update documentation.txt with the work
  completed, methodological decisions, data provenance, validation results,
  limitations, unresolved issues and next step. Never record secrets.
- The EODHD API token lives in the git-ignored local env file (`proj.env`,
  variable `EODHD_API_KEY`, also accepted as `EODHD_API_TOKEN`). Never print,
  log, commit or embed it anywhere.
- `data/raw/yahoo/dataset_a_adjusted_close.csv` (Stage 1 raw) must never be
  overwritten; later stages read `dataset_a_adjusted_close_repaired.csv`.
