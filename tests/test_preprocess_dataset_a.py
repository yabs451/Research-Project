"""Focused tests for the Stage 2 preprocessing rules.

Unit tests exercise the rules on small synthetic frames; integration tests
check the actual generated output files (run scripts/preprocess_dataset_a.py
first).
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from preprocess_dataset_a import (  # noqa: E402
    EXPECTED_WEEKDAYS,
    OUT_PRICES,
    OUT_RETURNS,
    daily_log_returns,
    forward_fill_after_inception,
    weekday_calendar,
)


# --------------------------------------------------------------------------- #
# Unit tests on synthetic data
# --------------------------------------------------------------------------- #

def test_weekday_calendar_is_weekdays_only_and_complete() -> None:
    cal = weekday_calendar()
    assert len(cal) == EXPECTED_WEEKDAYS == 807
    assert (cal.dayofweek <= 4).all()          # Mon=0 .. Fri=4
    assert cal.min() == pd.Timestamp("2020-01-02")
    assert cal.max() == pd.Timestamp("2023-02-03")
    assert cal.is_monotonic_increasing and not cal.duplicated().any()


def test_forward_fill_never_fills_leading_missing_period() -> None:
    idx = pd.date_range("2022-01-03", periods=6, freq="B")
    panel = pd.DataFrame(
        {"X": [np.nan, np.nan, 10.0, np.nan, 11.0, np.nan]}, index=idx
    )
    filled = forward_fill_after_inception(panel)
    assert filled["X"].iloc[:2].isna().all()          # leading stays missing
    assert filled["X"].iloc[3] == 10.0                # internal gap filled
    assert filled["X"].iloc[5] == 11.0                # trailing gap filled


def test_log_return_formula_exact() -> None:
    idx = pd.date_range("2022-01-03", periods=3, freq="B")
    prices = pd.DataFrame({"X": [100.0, 110.0, 110.0]}, index=idx)
    rets = daily_log_returns(prices)
    assert np.isnan(rets["X"].iloc[0])                # no preceding price
    assert rets["X"].iloc[1] == pytest.approx(np.log(110.0 / 100.0))
    assert rets["X"].iloc[2] == 0.0                   # unchanged price -> exact 0


def test_missing_prices_stay_missing_returns_not_zero() -> None:
    idx = pd.date_range("2022-01-03", periods=4, freq="B")
    prices = pd.DataFrame({"X": [np.nan, np.nan, 100.0, 101.0]}, index=idx)
    rets = daily_log_returns(prices)
    # Pre-inception and inception-day returns are missing, never zero.
    assert rets["X"].iloc[:3].isna().all()
    assert rets["X"].iloc[3] == pytest.approx(np.log(101.0 / 100.0))


def test_no_infinities_from_positive_prices() -> None:
    idx = pd.date_range("2022-01-03", periods=3, freq="B")
    prices = pd.DataFrame({"X": [1e-6, 1e6, 0.5]}, index=idx)
    rets = daily_log_returns(prices)
    assert np.isfinite(rets["X"].iloc[1:]).all()


# --------------------------------------------------------------------------- #
# Integration tests on the generated outputs
# --------------------------------------------------------------------------- #

@pytest.fixture(scope="module")
def processed() -> pd.DataFrame:
    if not OUT_PRICES.is_file():
        pytest.skip("run scripts/preprocess_dataset_a.py first")
    return pd.read_csv(OUT_PRICES, parse_dates=["date"]).set_index("date")


@pytest.fixture(scope="module")
def returns() -> pd.DataFrame:
    if not OUT_RETURNS.is_file():
        pytest.skip("run scripts/preprocess_dataset_a.py first")
    return pd.read_csv(OUT_RETURNS, parse_dates=["date"]).set_index("date")


def test_output_shape_and_calendar(processed: pd.DataFrame) -> None:
    assert processed.shape == (807, 100)
    assert (processed.index.dayofweek <= 4).all()
    assert not processed.index.duplicated().any()


def test_carr_ogn_not_backfilled(processed: pd.DataFrame) -> None:
    """The processed first valid date must equal the raw first genuine date
    (CARR 2020-03-19; OGN 2021-05-14, Yahoo's when-issued trading start),
    with every earlier weekday still missing."""
    raw = pd.read_csv(
        PROJECT_ROOT / "data" / "raw" / "yahoo"
        / "dataset_a_adjusted_close_repaired.csv",
        parse_dates=["date"],
    ).set_index("date")
    for symbol in ("CARR", "OGN"):
        s = processed[symbol]
        first_valid = s.first_valid_index()
        assert first_valid == raw[symbol].first_valid_index()
        assert s.loc[: first_valid - pd.Timedelta(days=1)].isna().all()


def test_dre_constant_price_and_zero_returns_after_acquisition(
    processed: pd.DataFrame, returns: pd.DataFrame
) -> None:
    cutoff = pd.Timestamp("2022-10-03")
    final_price = processed.loc[cutoff, "DRE"]
    assert final_price > 0
    after_prices = processed.loc[processed.index > cutoff, "DRE"]
    assert (after_prices == final_price).all()
    after_returns = returns.loc[returns.index > cutoff, "DRE"]
    assert (after_returns == 0.0).all()


def test_returns_align_with_prices_and_are_finite(
    processed: pd.DataFrame, returns: pd.DataFrame
) -> None:
    assert returns.index.equals(processed.index)
    assert list(returns.columns) == list(processed.columns)
    vals = returns.to_numpy()
    assert not np.isinf(vals).any()
    # A return exists exactly where both today's and yesterday's price exist.
    expected_valid = processed.notna() & processed.shift(1).notna()
    assert (returns.notna() == expected_valid).all().all()
