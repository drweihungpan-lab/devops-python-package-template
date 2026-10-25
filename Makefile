example_package_dir := packaging_tutorial

.PHONY: clean
clean:	## Remove any artifacts created by the tests
	rm -fr tests/$(example_package_dir)
	cd $(example_package_dir) \
	&& make clean

.PHONY: test-template
test-template:		## Test that the cookiecutter template reproduces the example package
	cookiecutter -f --no-input package_template/ repo_name=$(example_package_dir) package_name=example module_name=demo_module --output-dir tests author="John Doe" author_email="j.doe@example.com"
	diff -r --exclude .pytest_cache --exclude  __pycache__ --exclude .coverage $(example_package_dir)/ tests/$(example_package_dir)

.PHONY: test-example-package
test-example-package:	## Test that the example package installs correctly
	pip install ./$(example_package_dir)[test]
	python tests/test_package.py
	example --message=HELLO
	cd $(example_package_dir) \
	&& make test-all

help:			## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'