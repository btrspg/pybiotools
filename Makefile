SRC = $(wildcard ./*.ipynb)

all: pybiotools4p docs

pybiotools4p: $(SRC)
	nbdev_build_lib
	touch pybiotools4p

sync:
	nbdev_update_lib

docs_serve: docs
	cd docs && bundle exec jekyll serve

docs: $(SRC)
	nbdev_build_docs
	touch docs

test:
	nbdev_test_nbs

release: pypi
	echo nbdev_bump_version

pypi: dist
	twine upload --repository pypi dist/*

dist: clean
	python setup.py sdist bdist_wheel

clean:
	rm -rf dist