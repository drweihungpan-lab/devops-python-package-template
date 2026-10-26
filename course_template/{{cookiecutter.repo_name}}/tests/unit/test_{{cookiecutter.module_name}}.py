from datetime import date
from pathlib import Path

import pytest

from {{cookiecutter.package_name}}.{{cookiecutter.module_name}} import (
    load_counts,
    predict_limit_dates,
)

DATA = Path(__file__).parents[2] / "data" / "device_counts.csv"
EXPECTED_LIMIT_DATES = {
    "DEV-A": date(2026, 6, 30),
    "DEV-B": date(2026, 4, 1),
    "DEV-C": date(2026, 1, 16),
}


def test_limit_dates_are_pinned_for_the_fixed_synthetic_data():
    assert predict_limit_dates(load_counts(DATA)) == EXPECTED_LIMIT_DATES


def test_missing_column_is_reported(tmp_path):
    bad = tmp_path / "bad.csv"
    bad.write_text("device_id,date\nDEV-A,2025-01-01\n", encoding="utf-8")
    with pytest.raises(ValueError, match="daily_count"):
        load_counts(bad)
