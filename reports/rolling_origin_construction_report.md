# Rolling-Origin Construction Report (Stage 3)

Generated: 2026-07-17 21:55:14 UTC

## 1. Rolling-origin design

- A forecast origin is the last date whose information a model may use: the Friday close ending an M6 round. Each context ends on that Friday because submissions were due the following Sunday, when the Friday close was already public — so the origin-date return is legitimately known and included.
- The following 20 weekdays form the evaluation period being forecast; they are excluded from model input entirely, since including any of them would leak the future being predicted.
- Each context is a fixed window of 512 shared weekday rows — 512 time positions on the common calendar, not 512 non-null values per asset.

## 2. Context validation

- 12 contexts were created, one per scored M6 round; every context has exactly 512 date rows and 100 asset columns (101 columns with `date`), official order, ascending unique dates.
- No context contains any date after its origin (verified positionally for every round).
- Context values are copied byte-for-byte from the Stage 2 return file (written from an unparsed string copy) — no transformation, rounding or recalculation. Stage 2 input files verified unchanged by SHA-256: CONFIRMED.

| round | context (512 weekdays) | forecast (20 weekdays) | submission deadline |
|---|---|---|---|
| 1 | 2020-03-19 → 2022-03-04 | 2022-03-07 → 2022-04-01 | 2022-03-06 |
| 2 | 2020-04-16 → 2022-04-01 | 2022-04-04 → 2022-04-29 | 2022-04-03 |
| 3 | 2020-05-14 → 2022-04-29 | 2022-05-02 → 2022-05-27 | 2022-05-01 |
| 4 | 2020-06-11 → 2022-05-27 | 2022-05-30 → 2022-06-24 | 2022-05-29 |
| 5 | 2020-07-09 → 2022-06-24 | 2022-06-27 → 2022-07-22 | 2022-06-26 |
| 6 | 2020-08-06 → 2022-07-22 | 2022-07-25 → 2022-08-19 | 2022-07-24 |
| 7 | 2020-09-03 → 2022-08-19 | 2022-08-22 → 2022-09-16 | 2022-08-21 |
| 8 | 2020-10-01 → 2022-09-16 | 2022-09-19 → 2022-10-14 | 2022-09-18 |
| 9 | 2020-10-29 → 2022-10-14 | 2022-10-17 → 2022-11-11 | 2022-10-16 |
| 10 | 2020-11-26 → 2022-11-11 | 2022-11-14 → 2022-12-09 | 2022-11-13 |
| 11 | 2020-12-24 → 2022-12-09 | 2022-12-12 → 2023-01-06 | 2022-12-11 |
| 12 | 2021-01-21 → 2023-01-06 | 2023-01-09 → 2023-02-03 | 2023-01-08 |

## 3. Context movement

- Each origin lies exactly 20 weekday rows after the previous one, and each round's evaluation-end anchor is the next round's origin (verified for all 12 rounds).
- Consecutive contexts therefore share 492 dates: each round drops the oldest 20 dates and appends the 20 newest observed dates (verified). Contexts overlap by design — they are histories — while the 12 evaluation periods are strictly disjoint (verified: no shared dates between consecutive forecast windows).

## 4. Missing history

- CARR valid context returns by round: R1: 511, R2: 512, R3: 512, R4: 512, R5: 512, R6: 512, R7: 512, R8: 512, R9: 512, R10: 512, R11: 512, R12: 512.
- OGN valid context returns by round: R1: 210, R2: 230, R3: 250, R4: 270, R5: 290, R6: 310, R7: 330, R8: 350, R9: 370, R10: 390, R11: 410, R12: 430.
- No other asset-round pair has fewer than 512 valid returns (verified).
- Leading missing values were preserved exactly as produced by Stage 2: no zero padding, backward-filling, window extension or fabricated history anywhere. Model-specific input preparation for short histories is deferred to the model-wrapper stage.

## 5. DRE

- Round contexts including the post-acquisition period (context end after 2022-10-03): rounds 9, 10, 11, 12.
- In every such context, DRE's returns after 2022-10-03 are exactly zero — the Stage 2 competition treatment, copied unchanged; nothing was recalculated and no PLD data was used.
- Documented future modelling rule (not implemented here): when later stages generate forecasts for rounds after the acquisition, DRE's competition return is known to remain zero, so forecast generation must respect that known-zero treatment where applicable rather than modelling DRE's stale series as if it were still trading.

## 6. Readiness

- All 12 rolling-origin contexts passed validation and are ready for the later model-wrapper stage.
- Unresolved issues: none. Known accommodations for later stages: CARR (round 1: 511 returns) and OGN (all rounds: fewer than 512) require shorter model contexts; DRE requires the known-zero rule above.
- No model inference, realised targets, quintile probabilities or RPS were produced, and no descriptive statistics of the returns were calculated.
