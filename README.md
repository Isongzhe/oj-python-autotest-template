# OJ Python Judge Helper

A local batch testing and judging tool for Online Judge (OJ) problems, designed for TAs, problem setters, and students.  
Easily manage test cases, debug solutions, and generate detailed feedback without uploading to the OJ platform.

## Features

- **Automatic test case discovery:** Reads `.in`/`.out` files from problem folders.
- **Batch testing:** Runs all test cases for each problem automatically.
- **Detailed logging:** Shows input, expected output, and actual output for each test.
- **No hardcoded paths:** Uses the current Python interpreter for subprocesses.
- **Easy to extend:** Add new problems and test cases by simply adding files.

## Project Structure

```
Lab/
├── Q1/
│   ├── 1.in
│   ├── 1.out
│   └── ...
├── Q2/
│   └── ...
├── Q3/
│   └── ...
├── Q4/
│   └── ...
├── Q5/
│   └── ...
├── q1.py
├── q2.py
├── q3.py
├── q4.py
├── test_q1.py
├── test_q2.py
├── test_q3.py
├── test_q4.py
└── ...
```

- `Q1/`, `Q2/`, ...: Folders containing input/output test cases for each problem (can extend to `Q5/`, `Q6/` as needed).
- `q1.py`, `q2.py`, ...: Your solution scripts.
- `test_q1.py`, `test_q2.py`, ...: Pytest scripts for automated testing.

## Usage

1. **Install Python 3 (if not already installed).**
2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```
    or
    ```sh
    pip install pytest loguru
    ```
    (You need `pytest` and `loguru`.)

3. **Add your solution and test cases:**
    - Place your solution (e.g., `q1.py`) in the root directory.
    - Place test cases in the corresponding folder (e.g., `Q1/1.in`, `Q1/1.out`).

4. **Run all tests:**
    ```sh
    pytest -v
    ```

5. **Run a single test file:**
    ```sh
    pytest -v test_q1.py
    ```

6. **See detailed logs:**
    - Use the `-s` flag to show print/log output:
      ```sh
      pytest -v -s
      ```

## Utility Functions (utils.py)

To avoid code duplication, all test scripts now use the shared `utils.py` for:
- Reading test case files
- Discovering all `.in`/`.out` pairs
- Running and checking subprocess output

Example usage in a test file:

```python
from utils import read_file, get_in_out_files, run_and_check

Q_DIR = os.path.join(os.path.dirname(__file__), "Q1")
PYTHON = sys.executable
TARGET = os.path.join(os.path.dirname(__file__), "q1.py")

def test_q1_cases():
    for base, in_file, out_file in get_in_out_files(Q_DIR):
        input_data = read_file(in_file)
        expected_output = read_file(out_file)
        run_and_check(PYTHON, TARGET, input_data, expected_output)
```

This makes all test scripts concise and easy to maintain.

## For Teaching Assistants

- Download OJ test cases and organize them into folders as shown above.
- Use or adapt the provided `test_qX.py` scripts to automate local grading.
- Share this framework with students for self-testing before submission.

## License

MIT License. See [LICENSE](./LICENSE) for details.

## Author

SUNG-CHE, LIN
