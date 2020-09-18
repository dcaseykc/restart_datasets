all: install

install:
	python setup.py install

test:
	black .
	python -m flake8 restart_datasets
	python -m mypy restart_datasets
	rm -r build
	python setup.py build &&\
	  cd build/lib &&\
	  python -m pytest --pyargs --doctest-modules restart_datasets

test-coverage:
	python setup.py build &&\
	  cd build/lib &&\
	  python -m pytest --pyargs --doctest-modules --cov=vega_datasets --cov-report term restart_datasets

test-coverage-html:
	python setup.py build &&\
	  cd build/lib &&\
	  python -m pytest --pyargs --doctest-modules --cov=vega_datasets --cov-report html restart_datasets

## package: build package
.PHONY: package
package:
	python setup.py sdist bdist_wheel

## pypi: build package and push to pypi
.PHONY: pypi
pypi: package
	twine upload dist/*

.PHONY: pypi-test
pypi-test: package
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

## pypi-clean: Remove pypi build artifacts
.PHONY: pypi-clean
pypi-clean:
	rm -r build dist *.egg-info/
