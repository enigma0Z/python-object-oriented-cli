PYTHON ?= python3
TWINE ?= python3 -m twine

PYPI_URL ?= https://test.pypi.org/legacy/

all: clean package publish

clean:
	@find . -type f -iname '*.pyc' -exec rm {} \; 2>/dev/null && false || echo ".pyc files cleaned"
	@find . -type d -iname '__pycache__' -exec rmdir {} \; 2>/dev/null && false || echo "__pycache__ directories cleaned"
	@rm -rf build dist python*.egg-info && false || echo "Build artifacts cleaned"

package:
	$(PYTHON) setup.py sdist bdist_wheel

publish:
	$(TWINE) upload --repository-url $(PYPI_URL) dist/*
