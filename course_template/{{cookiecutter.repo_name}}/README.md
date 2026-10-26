# {{cookiecutter.package_name}}

Predict the date each medical device reaches its usage limit from daily measurement
counts. The data are synthetic.

## Install a Release

Pick a version tag from the repository's tags and install it into a fresh virtual
environment:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install "git+https://github.com/your-org/{{cookiecutter.repo_name}}.git@v0.1.0"
```

## Run

```bash
{{cookiecutter.package_name}} --input data/device_counts.csv --output limits.csv
```

The output has one row per device. Its SHA-256 should equal the reference in
`data/expected_limits.sha256`:

```bash
shasum -a 256 limits.csv
```

## Make a new Release

1. Change `__version__` in `src/{{cookiecutter.package_name}}/__init__.py` in a pull request.
2. After it is merged, tag `main` and push the tag: `git tag v0.1.1 && git push --tags`.

## Develop

```bash
pip install -e '.[test]'
make test-formatting-linting
```

Checks run automatically on every push. The pytest job in
`.github/workflows/github_actions.yml` is switched on in Session 3.
