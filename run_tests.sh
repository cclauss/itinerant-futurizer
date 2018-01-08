#!/bin/sh

python3 -m flake8 . --count --select=E901,E999,F821,F822,F823 --show-source --statistics
python2 -m flake8 . --count --select=E901,E999,F821,F822,F823 --show-source --statistics
python3 -m flake8 . --count --show-source --statistics
python2 -m flake8 . --count --show-source --statistics
python2 -m pytest --show-locals --tb=long # --pdb
python3 -m pytest --show_locals --tb=long # --pdb
