#!/bin/bash
python3 -m venv venv-build
source ./venv-build/bin/activate
pip3 install setuptools wheel
pip3 install -r requirements.txt
python3 setup.py sdist bdist_wheel
rm -rf *.egg-info venv-build build
