.PHONY: run

VENV_PYTHON := .venv/bin/python

run:
	$(VENV_PYTHON) -m linkml_flattener
