import hashlib
from pathlib import Path

from click.testing import CliRunner

from {{cookiecutter.package_name}}.scripts.{{cookiecutter.package_name}}_script import (
    {{cookiecutter.package_name}}_cli,
)

ROOT = Path(__file__).parents[2]
DATA = ROOT / "data" / "device_counts.csv"
REFERENCE = (ROOT / "data" / "expected_limits.sha256").read_text().split()[0]


def test_cli_output_matches_the_reference_checksum(tmp_path):
    output = tmp_path / "limits.csv"
    result = CliRunner().invoke(
        {{cookiecutter.package_name}}_cli, ["--input", str(DATA), "--output", str(output)]
    )
    assert result.exit_code == 0, result.output
    assert hashlib.sha256(output.read_bytes()).hexdigest() == REFERENCE


def test_cli_reports_a_malformed_input_clearly(tmp_path):
    bad = tmp_path / "bad.csv"
    bad.write_text("device_id,date\nDEV-A,2025-01-01\n", encoding="utf-8")
    result = CliRunner().invoke(
        {{cookiecutter.package_name}}_cli,
        ["--input", str(bad), "--output", str(tmp_path / "out.csv")],
    )
    assert result.exit_code != 0
    assert "missing column" in result.output
