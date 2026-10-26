"""CLI script for the {{cookiecutter.package_name}} package. Called on the command line."""

import csv

import click

from {{cookiecutter.package_name}}.{{cookiecutter.module_name}} import (
    load_counts,
    predict_limit_dates,
)


@click.command()
@click.option(
    "--input",
    "input_path",
    required=True,
    type=click.Path(exists=True, dir_okay=False),
    help="CSV of daily counts with columns device_id, date, daily_count.",
)
@click.option(
    "--output",
    "output_path",
    required=True,
    type=click.Path(dir_okay=False),
    help="CSV file to write: one limit date per device.",
)
@click.version_option()
def {{cookiecutter.package_name}}_cli(input_path, output_path):
    """Write the predicted usage-limit date of each device."""
    try:
        dates = predict_limit_dates(load_counts(input_path))
    except ValueError as error:
        raise click.ClickException(str(error)) from error
    with open(output_path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["device_id", "limit_date"])
        for device_id, limit_date in sorted(dates.items()):
            writer.writerow([device_id, limit_date.isoformat()])
    click.echo(f"Wrote {len(dates)} limit dates to {output_path}")
