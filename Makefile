# mdx_journal (c) Ian Dennis Miller

install:
	python setup.py install

release:
	python setup.py sdist upload -r https://pypi.python.org/pypi

.PHONY: install release
