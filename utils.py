"""
utils.py
--------
Common utility functions for test automation scripts.
"""
import os
import glob
import subprocess
from typing import List, Tuple


def read_file(path: str) -> str:
    """
    Read the content of a file and return it as a stripped string.

    Args:
        path (str): Path to the file.
    Returns:
        str: Stripped content of the file.
    """
    with open(path, encoding="utf-8") as file:
        return file.read().strip()


def get_in_out_files(case_dir: str) -> List[Tuple[str, str, str]]:
    """
    Get a sorted list of (base, in_file, out_file) tuples for all test cases in a directory.

    Args:
        case_dir (str): Directory containing .in/.out files.
    Returns:
        List[Tuple[str, str, str]]: List of (base, in_file, out_file) tuples.
    """
    in_files = sorted(glob.glob(os.path.join(case_dir, "*.in")))
    cases = []
    for in_file in in_files:
        base = os.path.splitext(os.path.basename(in_file))[0]
        out_file = os.path.join(case_dir, f"{base}.out")
        if os.path.exists(out_file):
            cases.append((base, in_file, out_file))
    return cases


def run_and_check(python_exec: str, target: str, input_data: str, expected_output: str, logger=None, base: str = ""):
    """
    Run the target script with input_data and check if output matches expected_output.

    Args:
        python_exec (str): Path to Python interpreter.
        target (str): Path to target script.
        input_data (str): Input string to pass to the script.
        expected_output (str): Expected output string.
        logger: Logger object for info output (optional).
        base (str): Case name for error message (optional).
    Raises:
        AssertionError: If actual output does not match expected output.
    """
    result = subprocess.run(
        [python_exec, target],
        input=input_data,
        text=True,
        capture_output=True,
        timeout=5
    )
    actual_output = result.stdout.strip()
    if logger:
        logger.info(f"Input:\n{input_data}")
        logger.info(f"Expected:\n{expected_output}")
        logger.info(f"Actual:\n{actual_output}")
    assert actual_output == expected_output, f"Failed on {base}: {actual_output} != {expected_output}"
