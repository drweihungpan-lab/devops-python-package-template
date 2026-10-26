.PHONY: clean
clean:		## Clean up python build files
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	rm -fr build
	rm -f .coverage

.PHONY: install
install:	## Install package
	pip install .

.PHONY: install-dev
install-dev:	## Install package with test dependencies and allow code edits to the installed package
	pip install -e .[test]

.PHONY: install-test
install-test:	## Install package with test dependencies for testing locally and in CI
	pip install .[test]

.PHONY: test-all
test-all: 	## Run all the formatting/linting and pytest tests
test-all: test-formatting-linting test-pytest

.PHONY: test-formatting-linting
test-formatting-linting: 	## Run all the formatting/linting
test-formatting-linting: test-isort test-black test-flake8 test-pylint

.PHONY: test-isort
test-isort:	## Check that all files have their import statements correctly formatted, fails if not
	isort --profile black --check .

.PHONY: test-black
test-black:	## Check that Black formatting is correct, fails if not
	black --check .

.PHONY: test-flake8
test-flake8:	## Check flake8 formatting, fails if not
	flake8

.PHONY: test-pylint
test-pylint:	## Check pylint is OK or fails
	pylint src

.PHONY: test-pytest
test-pytest:	## Run tests with pytest
	pytest --cov={{cookiecutter.package_name}} tests/unit
	pytest

.PHONY: format
format:		## Applies isort and black formatting
	isort --profile black .
	black .

help:		## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
