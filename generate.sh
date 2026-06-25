#!/bin/sh
# Generate _data files from the _artifinder submodule before running Jekyll locally.
[ -d .venv ] || { python3 -m venv .venv && .venv/bin/pip install pyyaml -q; }
.venv/bin/python3 generate_artifinder_data.py
