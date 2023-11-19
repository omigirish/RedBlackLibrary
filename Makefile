# Makefile for a Python project with all files in one directory

# Variables
PYTHON = python3
SRC_DIR = .

all: venv
	$(PYTHON) gatorlibrary.py test1.txt

test: venv
	$(PYTHON) gatorlibrary.py test1.txt
	$(PYTHON) gatorlibrary.py test2.txt
	$(PYTHON) gatorlibrary.py test3.txt
	$(PYTHON) gatorlibrary.py test4.txt

# Usage...........................................
# make         To run the default target (all)
# make test    To run tests