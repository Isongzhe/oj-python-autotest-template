import os
import sys
from loguru import logger
from utils import read_file, get_in_out_files, run_and_check

Q_DIR = os.path.join(os.path.dirname(__file__), "Q5")
PYTHON = sys.executable
TARGET = os.path.join(os.path.dirname(__file__), "q5.py")

def test_q5_cases():
    """
    Run all Q5 test cases using the shared utility functions.
    """
    for base, in_file, out_file in get_in_out_files(Q_DIR):
        input_data = read_file(in_file)
        expected_output = read_file(out_file)
        run_and_check(PYTHON, TARGET, input_data, expected_output, logger=logger, base=base)