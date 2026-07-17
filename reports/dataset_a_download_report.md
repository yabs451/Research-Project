# Dataset A Download Report

Generated: 2026-07-17 14:34:11 UTC
Output file: `data/raw/yahoo/dataset_a_adjusted_close.csv`

## Download summary

- Requested date range: 2020-01-01 to 2023-02-04 (end exclusive; last included calendar date 2023-02-03)
- Actual earliest returned date: 2020-01-02
- Actual latest returned date: 2023-02-03
- Official assets: 100
- Successfully downloaded (≥1 non-null observation): 97
- Required individual retries: DRE, RE, WRK
- Failed / only-null assets: DRE, RE, WRK

## Status

- **Structurally valid**: YES — the output contains `date` plus all 100 official asset columns in official order.
- **Data complete**: NO — one or more assets failed or lack sufficient usable history (see below). Structural validity alone does not make Dataset A complete.

## Integrity confirmations

- No missing values were filled, interpolated, forward-/backward-filled or replaced with zeros; gaps caused by differing exchange holidays remain missing.
- No official asset was silently removed: all 100 assets are present as columns, including any that failed to download (kept as all-null columns).
- No returns were calculated, no standardisation was applied, no shared business-day calendar was constructed, and the official M6 price file was not used to fill Yahoo values.

## META findings

META series spans 2020-01-02 to 2023-02-03 with 779 non-null observations. It contains 614 observations before the FB→META ticker change on 2022-06-09, so Yahoo's META series does include the pre-change (FB-era) history. The asset is stored as a single continuous `META` column; no separate FB column was created and no artificial values were inserted at the ticker-change date.

## DRE findings

DRE returned no data from Yahoo Finance. Dataset A is therefore INCOMPLETE for DRE; no values were fabricated.

> **Note for Stage 2**: to reproduce the official competition treatment, Stage 2 must carry DRE's final available price forward after 2022-10-03 (zero subsequent return). This was deliberately NOT applied in this raw-download stage.

## Ticker-related errors

- `DRE`: no data or only null values from Yahoo Finance
- `RE`: no data or only null values from Yahoo Finance
- `WRK`: no data or only null values from Yahoo Finance

## Assets with fewer than 513 non-null observations on or before 2022-03-04

- `CARR` (495 observations)
- `DRE` (0 observations)
- `OGN` (204 observations)
- `RE` (0 observations)
- `WRK` (0 observations)

## Per-asset availability

| symbol | first date | last date | non-null obs | non-null obs ≤ 2022-03-04 | ≥ 513 by cutoff |
|---|---|---|---|---|---|
| ABBV | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| ACN | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| AEP | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| AIZ | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| ALLE | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| AMAT | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| AMP | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| AMZN | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| AVB | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| AVY | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| AXP | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| BDX | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| BF-B | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| BMY | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| BR | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| CARR | 2020-03-19 | 2023-02-03 | 726 | 495 | NO |
| CDW | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| CE | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| CHTR | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| CNC | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| CNP | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| COP | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| CTAS | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| CZR | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| DG | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| DPZ | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| DRE | — | — | 0 | 0 | NO |
| DXC | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| EWA | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| EWC | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| EWG | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| EWH | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| EWJ | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| EWL | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| EWQ | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| EWT | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| EWU | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| EWY | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| EWZ | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| FTV | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| GOOG | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| GPC | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| GSG | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| HIG | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| HIGH.L | 2020-01-02 | 2023-02-03 | 781 | 551 | yes |
| HST | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| HYG | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| IAU | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| ICLN | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| IEAA.L | 2020-01-02 | 2023-02-03 | 781 | 551 | yes |
| IEF | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| IEFM.L | 2020-01-02 | 2023-02-03 | 781 | 551 | yes |
| IEMG | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| IEUS | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| IEVL.L | 2020-01-02 | 2023-02-03 | 781 | 551 | yes |
| IGF | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| INDA | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| IUMO.L | 2020-01-02 | 2023-02-03 | 781 | 551 | yes |
| IUVL.L | 2020-01-02 | 2023-02-03 | 781 | 551 | yes |
| IVV | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| IWM | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| IXN | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| JPEA.L | 2020-01-02 | 2023-02-03 | 781 | 551 | yes |
| JPM | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| KR | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| LQD | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| MCHI | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| META | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| MVEU.L | 2020-01-02 | 2023-02-03 | 781 | 551 | yes |
| OGN | 2021-05-14 | 2023-02-03 | 435 | 204 | NO |
| PG | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| PPL | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| PRU | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| PYPL | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| RE | — | — | 0 | 0 | NO |
| REET | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| ROL | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| ROST | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| SEGA.L | 2020-01-02 | 2023-02-03 | 781 | 551 | yes |
| SHY | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| SLV | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| SPMV.L | 2020-01-02 | 2023-02-03 | 781 | 551 | yes |
| TLT | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| UNH | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| URI | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| V | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| VRSK | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| VXX | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| WRK | — | — | 0 | 0 | NO |
| XLB | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| XLC | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| XLE | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| XLF | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| XLI | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| XLK | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| XLP | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| XLU | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| XLV | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| XLY | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
| XOM | 2020-01-02 | 2023-02-03 | 779 | 548 | yes |
