#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status


pip install pylint


pylint src/*.py tests/*.py --fail-under=8.0
