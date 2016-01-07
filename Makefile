# mdx_journal (c) Ian Dennis Miller

install:
	python setup.py install

clean:
	rm -rf build dist *.egg-info
	find . -name '*.pyc' -delete

release:
	python setup.py sdist upload -r https://pypi.python.org/pypi

.PHONY: install release clean
