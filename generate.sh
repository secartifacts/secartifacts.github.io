#!/bin/sh
# Generate _data files from the _artifinder submodule before running Jekyll locally.
git submodule update --init
pip install pyyaml -q
python3 generate_artifinder_data.py
