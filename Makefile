TARGETS ?= simpleCli

PYTHON ?= python3
TWINE ?= $(PYTHON) -m twine
SPHINX ?= $(PYTHON) -m sphinx.cmd.build
SPHINX_SOURCE     = sphinx
SPHINX_BUILD      = docs

PYPI_URL ?= https://test.pypi.org/legacy/

.PHONY: doc

all: clean package publish
clean: clean_code clean_doc

clean_code:
	@find . -type f -iname '*.pyc' -exec rm {} \; 2>/dev/null && false || echo ".pyc files cleaned"
	@find . -type d -iname '__pycache__' -exec rmdir {} \; 2>/dev/null && false || echo "__pycache__ directories cleaned"
	@rm -rf build dist python*.egg-info && false || echo "Build artifacts cleaned"

clean_doc:
	@rm -rf $(SPHINX_BUILD)/doctest $(SPHINX_BUILD)/doctrees && false || echo "Docs cleaned"

package:
	$(PYTHON) setup.py sdist bdist_wheel

publish:
	$(TWINE) upload --repository-url $(PYPI_URL) dist/*

doc: 
	$(SPHINX) -b html "$(SPHINX_SOURCE)" "$(SPHINX_BUILD)" $(SPHINXOPTS)

test: clean
	$(PYTHON) -m pylint $(TARGETS)
	$(PYTHON) -m compileall $(TARGETS)
	$(SPHINX) -M doctest "$(SPHINX_SOURCE)" "$(SPHINX_BUILD)" $(SPHINXOPTS)
