"""Fit a linear trend to each device's running total and find its limit date."""

from datetime import timedelta

import numpy as np
import pandas as pd

from .logger_config import logger

LIMIT = 100_000
REQUIRED_COLUMNS = ["device_id", "date", "daily_count"]
# 10,000 measurements arrived late and belong to 1 December.
LATE_FROM = pd.Timestamp("2025-12-01")
LATE_COUNT = 10_000


def load_counts(path, label=None):
    """Read daily measurement counts from a CSV file or open file.

    `label` names the input in error messages; it defaults to `path`.
    """
    label = label or path
    counts = pd.read_csv(path, parse_dates=["date"])
    missing = [column for column in REQUIRED_COLUMNS if column not in counts]
    if missing:
        raise ValueError(f"{label} is missing column(s): {', '.join(missing)}")
    logger.info("Read %d rows from %s", len(counts), label)
    return counts


def running_totals(counts):
    """Return one `total` per device and day: the measurements so far."""
    counts = counts.sort_values(["device_id", "date"])
    return counts.assign(total=counts.groupby("device_id")["daily_count"].cumsum())


def add_late_arrivals(totals):
    """Return a copy of `totals` with the late measurements added."""
    late = totals["date"] >= LATE_FROM
    return totals.assign(total=totals["total"] + late * LATE_COUNT)


def predict_limit_dates(counts, limit=LIMIT):
    """Return {device_id: date the running total reaches `limit`}."""
    totals = add_late_arrivals(running_totals(counts))
    dates = {}
    for device_id, device in totals.groupby("device_id"):
        slope, intercept = np.polyfit(
            np.arange(len(device)), device["total"].to_numpy(), 1
        )
        days = int(np.ceil((limit - intercept) / slope))
        dates[device_id] = device["date"].iloc[0].date() + timedelta(days=days)
    return dates
