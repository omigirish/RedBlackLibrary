# Makefile for a Python project with all files in one directory

# Variables
PYTHON = python3
SRC_DIR = .
VENV_DIR = venv

# Targets
.PHONY: all clean test

all: venv

venv:
	$(PYTHON) -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install -r requirements.txt

clean:
	rm -rf $(VENV_DIR)
	rm -f *.pyc

test: venv
	$(VENV_DIR)/bin/python -m unittest discover

# Usage...........................................
# make         To run the default target (all)
# make clean   To clean up generated files
# make test    To run tests