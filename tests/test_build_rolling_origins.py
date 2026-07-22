"""Focused tests for the Stage 3 rolling-origin rules.

Run scripts/build_rolling_origins.py first; these tests validate the actual
generated context files against the Stage 2 return panel.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from build_rolling_origins import (  # noqa: E402
    ANCHORS,
    CONTEXT_STEPS,
    FORECAST_STEPS,
    OUT_DIR,
    RETURNS_CSV,
)


@pytest.fixture(scope="module")
def stage2_returns() -> pd.DataFrame:
    return pd.read_csv(RETURNS_CSV, parse_dates=["date"]).set_index("date")


@pytest.fixture(scope="module")
def contexts() -> dict[int, pd.DataFrame]:
    if not OUT_DIR.is_dir():
        pytest.skip("run scripts/build_rolling_origins.py first")
    out = {}
    for r in range(1, 13):
        path = OUT_DIR / f"round_{r:02d}_context.csv"
        assert path.is_file(), f"missing context file for round {r}"
        out[r] = pd.read_csv(path, parse_dates=["date"]).set_index("date")
    return out


def test_exactly_twelve_context_files() -> None:
    files = sorted(OUT_DIR.glob("round_*_context.csv"))
    assert len(files) == 12


def test_every_context_shape_and_calendar(contexts: dict[int, pd.DataFrame]) -> None:
    for r, ctx in contexts.items():
        assert ctx.shape == (CONTEXT_STEPS, 100), f"round {r}"
        assert ctx.index.is_monotonic_increasing and not ctx.index.duplicated().any()
        assert (ctx.index.dayofweek <= 4).all()


def test_context_ends_on_origin_with_no_future_dates(
    contexts: dict[int, pd.DataFrame]
) -> None:
    for r, ctx in contexts.items():
        origin = ANCHORS[r - 1]
        assert ctx.index[-1] == origin, f"round {r}"
        assert (ctx.index <= origin).all(), f"round {r}"


def test_origins_advance_by_twenty_weekdays(
    contexts: dict[int, pd.DataFrame], stage2_returns: pd.DataFrame
) -> None:
    idx = stage2_returns.index
    for r in range(1, 12):
        p0 = idx.get_loc(contexts[r].index[-1])
        p1 = idx.get_loc(contexts[r + 1].index[-1])
        assert p1 - p0 == FORECAST_STEPS
        # Rolling movement: drop oldest 20 dates, add newest 20 dates.
        shared = contexts[r].index.intersection(contexts[r + 1].index)
        assert len(shared) == CONTEXT_STEPS - FORECAST_STEPS


def test_forecast_periods_have_twenty_weekdays(stage2_returns: pd.DataFrame) -> None:
    idx = stage2_returns.index
    for a0, a1 in zip(ANCHORS, ANCHORS[1:]):
        assert idx.get_loc(a1) - idx.get_loc(a0) == FORECAST_STEPS


def test_values_copied_unmodified_from_stage2(
    contexts: dict[int, pd.DataFrame], stage2_returns: pd.DataFrame
) -> None:
    for r, ctx in contexts.items():
        expected = stage2_returns.loc[ctx.index]
        assert ctx.equals(expected), f"round {r} values differ from Stage 2"


def test_carr_ogn_leading_missing_preserved(
    contexts: dict[int, pd.DataFrame], stage2_returns: pd.DataFrame
) -> None:
    # Round 1 starts on CARR's first price date: its first return is missing.
    assert pd.isna(contexts[1]["CARR"].iloc[0])
    assert contexts[1]["CARR"].iloc[1:].notna().all()
    # OGN is short in every round, and its pre-inception rows stay missing.
    ogn_first_return = stage2_returns["OGN"].first_valid_index()
    for r, ctx in contexts.items():
        s = ctx["OGN"]
        assert s.notna().sum() < CONTEXT_STEPS, f"round {r}"
        assert s.loc[s.index < ogn_first_return].isna().all(), f"round {r}"


def test_dre_post_acquisition_zeros_unchanged(
    contexts: dict[int, pd.DataFrame]
) -> None:
    cutoff = pd.Timestamp("2022-10-03")
    seen_any = False
    for r, ctx in contexts.items():
        after = ctx.loc[ctx.index > cutoff, "DRE"]
        if not after.empty:
            seen_any = True
            assert (after == 0.0).all(), f"round {r}"
    assert seen_any  # rounds 9-12 must include the post-acquisition period
