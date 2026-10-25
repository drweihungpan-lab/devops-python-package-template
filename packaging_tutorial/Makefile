AWS_REGION=us-east-1
AWS_ACCOUNT_ID=123456789012
AWS_ECR_URL=$(AWS_ACCOUNT_ID).dkr.ecr.$(AWS_REGION).amazonaws.com

DOCKER_IMAGE_REPO=$(AWS_ECR_URL)/example

CODE_ARTIFACT_REPO=python-packages
CODE_ARTIFACT_DOMAIN=code-artifacts

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
install-dev:	## Install package with dev and test dependencies and allow code edits to the installed package 
	pip install -e .[test,dev]

.PHONY: install-test
install-test:	## Install package with test dependencies for testing locally and in CI
	pip install .[test]

.PHONY: update-requirements
update-requirements:	## Generate or update the requirements.txt file based on requirements from setup.cfg
	pip-compile setup.cfg

.PHONY: test-all
test-all: 	## Run all the formating/linting and pytest tests
test-all: test-formatting-linting test-pytest

.PHONY: test-formatting-linting
test-formatting-linting: 	## Run all the formating/linting
test-formatting-linting: test-isort test-black test-flake8 test-pylint test-docker-lint

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
	# Run coverage only on the unit tests
	pytest --cov=example tests/unit

	# Then run tests without coverage
	pytest

.PHONY: format
format:		## Applies isort and black formatting
	isort --profile black .
	black .


.PHONY: docker-build
docker-build:	## Build the docker image for the package
# don't copy over any build files
	make clean
	docker buildx build --load --tag $(DOCKER_IMAGE_REPO):$(call get_current_version) \
		--cache-from type=gha \
		--cache-to "type=gha,mode=max" .

.PHONY: test-docker-lint
test-docker-lint:	## Check linting of Dockerfile using hadolint
	docker run --rm -i hadolint/hadolint < Dockerfile

.PHONY: docker-test
docker-test:	## Run the integration test on the built image
	docker run -v $$PWD/tests:/usr/app/tests $(DOCKER_IMAGE_REPO):$(call get_current_version) --message=Hallo

.PHONY: docker-login
docker-login:	## Login in to AWS ECR - requires AWS credentials to be set
	aws ecr get-login-password --region $(AWS_REGION) | docker login --username AWS --password-stdin $(AWS_ECR_URL)

.PHONY: docker-push
docker-push:	## Push docker image to AWS ECR - requires docker-login step
	docker push $(DOCKER_IMAGE_REPO):$(call get_current_version)

.PHONY: get-code-artifact-url
get-code-artifact-url:
	$(eval CODEARTIFACT_AUTH_TOKEN := $(shell aws codeartifact get-authorization-token --domain $(CODE_ARTIFACT_DOMAIN) --domain-owner $(AWS_ACCOUNT_ID) --query authorizationToken --output text))
	$(eval CODEARTIFACT_URL := https://aws:$(CODEARTIFACT_AUTH_TOKEN)@$(CODE_ARTIFACT_DOMAIN)-$(AWS_ACCOUNT_ID).d.codeartifact.$(AWS_REGION).amazonaws.com/pypi/$(CODE_ARTIFACT_REPO)/simple/)

.PHONY: code-artifact-read-access
code-artifact-read-access: get-code-artifact-url	## Login in to AWS Code Artifact requires AWS credentials to be set
	# This sets pip index url on a user level
	@pip config set --user global.extra-index-url https://pypi.org/simple/
	# This allows us to add the Code Artifact URL with temporary credentials as an extra index
	@pip config set --user global.index-url $(CODEARTIFACT_URL) 

help:		## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

# Define a function that gets the current package version
# Note: python must be set up with release dependencies installed first.
define get_current_version
$(shell semantic-release print-version --current)
endef
