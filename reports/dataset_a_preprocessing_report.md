# Dataset A Preprocessing Report (Stage 2)

Generated: 2026-07-17 21:29:08 UTC

## 1. Input

- Input: `data/raw/yahoo/dataset_a_adjusted_close_repaired.csv`
- Shape: 798 rows x 100 assets (+ date column), 2020-01-02 to 2023-02-03
- Structural checks passed: `date` first column, 100 asset columns in official first-occurrence order, unique sorted dates, no non-positive prices.
- Raw file unmodified (SHA-256 verified before/after): CONFIRMED
- The official M6 file was used only to confirm asset names and order; its prices were not used.

## 2. Weekday alignment

- A single shared Monday-to-Friday calendar is used so that every asset — trading on US or London exchanges with different holidays — shares one index, which later stages require for cross-sectional work. Individual exchange calendars are deliberately not used.
- Output range: 2020-01-02 to 2023-02-03; 807 weekday rows (Saturdays/Sundays excluded: confirmed).
- Dates added by reindexing (shared holidays absent from the raw union calendar): 9

## 3. Forward-filling

- Forward-filling copies the most recently observed price of the same asset onto later missing weekdays. On a day a market is closed the holder's position cannot change value, so a carried-forward price (and hence a zero log return) is the faithful representation.
- Total cells forward-filled across all assets: 2851. Per-asset counts (assets with at least one filled cell):

| symbol | forward-filled cells | longest internal gap (weekdays, pre-fill) |
|---|---|---|
| ABBV | 28 | 1 |
| ACN | 28 | 1 |
| AEP | 28 | 1 |
| AIZ | 28 | 1 |
| ALLE | 28 | 1 |
| AMAT | 28 | 1 |
| AMP | 28 | 1 |
| AMZN | 28 | 1 |
| AVB | 28 | 1 |
| AVY | 28 | 1 |
| AXP | 28 | 1 |
| BDX | 28 | 1 |
| BF-B | 28 | 1 |
| BMY | 28 | 1 |
| BR | 28 | 1 |
| CARR | 26 | 1 |
| CDW | 28 | 1 |
| CE | 28 | 1 |
| CHTR | 28 | 1 |
| CNC | 28 | 1 |
| CNP | 28 | 1 |
| COP | 28 | 1 |
| CTAS | 28 | 1 |
| CZR | 28 | 1 |
| DG | 28 | 1 |
| DPZ | 28 | 1 |
| DRE | 113 | 1 |
| DXC | 28 | 1 |
| EWA | 28 | 1 |
| EWC | 28 | 1 |
| EWG | 28 | 1 |
| EWH | 28 | 1 |
| EWJ | 28 | 1 |
| EWL | 28 | 1 |
| EWQ | 28 | 1 |
| EWT | 28 | 1 |
| EWU | 28 | 1 |
| EWY | 28 | 1 |
| EWZ | 28 | 1 |
| FTV | 28 | 1 |
| GOOG | 28 | 1 |
| GPC | 28 | 1 |
| GSG | 28 | 1 |
| HIG | 28 | 1 |
| HIGH.L | 26 | 2 |
| HST | 28 | 1 |
| HYG | 28 | 1 |
| IAU | 28 | 1 |
| ICLN | 28 | 1 |
| IEAA.L | 26 | 2 |
| IEF | 28 | 1 |
| IEFM.L | 26 | 2 |
| IEMG | 28 | 1 |
| IEUS | 28 | 1 |
| IEVL.L | 26 | 2 |
| IGF | 28 | 1 |
| INDA | 28 | 1 |
| IUMO.L | 26 | 2 |
| IUVL.L | 26 | 2 |
| IVV | 28 | 1 |
| IWM | 28 | 1 |
| IXN | 28 | 1 |
| JPEA.L | 26 | 2 |
| JPM | 28 | 1 |
| KR | 28 | 1 |
| LQD | 28 | 1 |
| MCHI | 28 | 1 |
| META | 28 | 1 |
| MVEU.L | 26 | 2 |
| OGN | 16 | 1 |
| PG | 28 | 1 |
| PPL | 28 | 1 |
| PRU | 28 | 1 |
| PYPL | 28 | 1 |
| RE | 28 | 1 |
| REET | 28 | 1 |
| ROL | 28 | 1 |
| ROST | 28 | 1 |
| SEGA.L | 26 | 2 |
| SHY | 28 | 1 |
| SLV | 28 | 1 |
| SPMV.L | 26 | 2 |
| TLT | 28 | 1 |
| UNH | 28 | 1 |
| URI | 28 | 1 |
| V | 28 | 1 |
| VRSK | 28 | 1 |
| VXX | 28 | 1 |
| WRK | 28 | 1 |
| XLB | 28 | 1 |
| XLC | 28 | 1 |
| XLE | 28 | 1 |
| XLF | 28 | 1 |
| XLI | 28 | 1 |
| XLK | 28 | 1 |
| XLP | 28 | 1 |
| XLU | 28 | 1 |
| XLV | 28 | 1 |
| XLY | 28 | 1 |
| XOM | 28 | 1 |

- Unusually long internal gaps (> 5 consecutive weekdays) before filling: none found.
- No backward-filling, interpolation, zero-substitution or cross-asset copying occurred; leading pre-inception values were never filled.

## 4. Special assets

- DRE: final genuine observation 2022-10-03 at price 48.2000 (positive, non-null: confirmed). The processed price is constant over the 89 subsequent weekdays through 2023-02-03, and every DRE log return after 2022-10-03 equals exactly zero — the official M6 zero-return treatment. No zero prices, no PLD prices, no jump at the acquisition date.
- CARR: first genuine date 2020-03-19 unchanged; all earlier weekdays remain missing (no backfill).
- OGN: first genuine date 2021-05-14 unchanged; all earlier weekdays remain missing (no backfill).
- RE remains the canonical column (repair provider identifier was EG.US). WRK remains the canonical column (provider identifier WRK.US, delisted list).

## 5. Returns

- Formula: `log_return[t] = log(price[t] / price[t-1])`, implemented as `np.log(processed_prices).diff()`, per asset, on the shared weekday index in official column order.
- A return is missing exactly where the current or preceding processed price is missing (pre-inception periods and each asset's first row); remaining missing returns were NOT replaced with zero.
- No scaling, averaging, smoothing, clipping, winsorising or normalisation was applied; no statistics were fitted.
- Infinite values: none (checked; prices are strictly positive).

Valid / missing return counts per asset:

| symbol | valid returns | missing returns |
|---|---|---|
| ABBV | 806 | 1 |
| ACN | 806 | 1 |
| AEP | 806 | 1 |
| AIZ | 806 | 1 |
| ALLE | 806 | 1 |
| AMAT | 806 | 1 |
| AMP | 806 | 1 |
| AMZN | 806 | 1 |
| AVB | 806 | 1 |
| AVY | 806 | 1 |
| AXP | 806 | 1 |
| BDX | 806 | 1 |
| BF-B | 806 | 1 |
| BMY | 806 | 1 |
| BR | 806 | 1 |
| CARR | 751 | 56 |
| CDW | 806 | 1 |
| CE | 806 | 1 |
| CHTR | 806 | 1 |
| CNC | 806 | 1 |
| CNP | 806 | 1 |
| COP | 806 | 1 |
| CTAS | 806 | 1 |
| CZR | 806 | 1 |
| DG | 806 | 1 |
| DPZ | 806 | 1 |
| DRE | 806 | 1 |
| DXC | 806 | 1 |
| EWA | 806 | 1 |
| EWC | 806 | 1 |
| EWG | 806 | 1 |
| EWH | 806 | 1 |
| EWJ | 806 | 1 |
| EWL | 806 | 1 |
| EWQ | 806 | 1 |
| EWT | 806 | 1 |
| EWU | 806 | 1 |
| EWY | 806 | 1 |
| EWZ | 806 | 1 |
| FTV | 806 | 1 |
| GOOG | 806 | 1 |
| GPC | 806 | 1 |
| GSG | 806 | 1 |
| HIG | 806 | 1 |
| HIGH.L | 806 | 1 |
| HST | 806 | 1 |
| HYG | 806 | 1 |
| IAU | 806 | 1 |
| ICLN | 806 | 1 |
| IEAA.L | 806 | 1 |
| IEF | 806 | 1 |
| IEFM.L | 806 | 1 |
| IEMG | 806 | 1 |
| IEUS | 806 | 1 |
| IEVL.L | 806 | 1 |
| IGF | 806 | 1 |
| INDA | 806 | 1 |
| IUMO.L | 806 | 1 |
| IUVL.L | 806 | 1 |
| IVV | 806 | 1 |
| IWM | 806 | 1 |
| IXN | 806 | 1 |
| JPEA.L | 806 | 1 |
| JPM | 806 | 1 |
| KR | 806 | 1 |
| LQD | 806 | 1 |
| MCHI | 806 | 1 |
| META | 806 | 1 |
| MVEU.L | 806 | 1 |
| OGN | 450 | 357 |
| PG | 806 | 1 |
| PPL | 806 | 1 |
| PRU | 806 | 1 |
| PYPL | 806 | 1 |
| RE | 806 | 1 |
| REET | 806 | 1 |
| ROL | 806 | 1 |
| ROST | 806 | 1 |
| SEGA.L | 806 | 1 |
| SHY | 806 | 1 |
| SLV | 806 | 1 |
| SPMV.L | 806 | 1 |
| TLT | 806 | 1 |
| UNH | 806 | 1 |
| URI | 806 | 1 |
| V | 806 | 1 |
| VRSK | 806 | 1 |
| VXX | 806 | 1 |
| WRK | 806 | 1 |
| XLB | 806 | 1 |
| XLC | 806 | 1 |
| XLE | 806 | 1 |
| XLF | 806 | 1 |
| XLI | 806 | 1 |
| XLK | 806 | 1 |
| XLP | 806 | 1 |
| XLU | 806 | 1 |
| XLV | 806 | 1 |
| XLY | 806 | 1 |
| XOM | 806 | 1 |

## 6. Rolling-origin readiness (verification only)

- All 13 M6 Friday anchor dates exist in both processed panels: 2022-03-04, 2022-04-01, 2022-04-29, 2022-05-27, 2022-06-24, 2022-07-22, 2022-08-19, 2022-09-16, 2022-10-14, 2022-11-11, 2022-12-09, 2023-01-06, 2023-02-03

- Valid historical log returns available on or before the first origin (2022-03-04): min 210, max 566 across assets.
- Assets with fewer than 512 returns at the first origin: CARR (511), OGN (210)
- Rolling-origin model contexts were NOT created or padded in this stage.
