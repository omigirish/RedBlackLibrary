# Makefile for a Python project with all files in one directory
# Variables
PYTHON = python3
SRC_DIR = .

all: 
	$(PYTHON) gatorLibrary.py test1.txt

test: 
	$(PYTHON) gatorLibrary.py test1.txt
	$(PYTHON) gatorLibrary.py test2.txt
	$(PYTHON) gatorLibrary.py test3.txt
	$(PYTHON) gatorLibrary.py test4.txt
	$(PYTHON) gatorLibrary.py example1.txt
	$(PYTHON) gatorLibrary.py example2.txt
	$(PYTHON) gatorLibrary.py example3.txt

# Usage...........................................
# make         To run the default target (all)
# make test    To run tests