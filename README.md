# Uncommon Python Error: Unhandled Exceptions

This repository demonstrates a common yet often overlooked error in Python: failing to handle all possible exceptions. While the provided `function_with_uncommon_error` handles `ZeroDivisionError` and `TypeError`, it's crucial to consider other potential issues. This could lead to unexpected program termination and challenges in debugging.

The `bug.py` file showcases the problematic code. The `bugSolution.py` file offers a solution by adding comprehensive exception handling.  Good exception handling should improve code robustness and user experience.

## How to run

1. Clone the repository.
2. Run `bug.py` to see the exceptions being handled and the errors printed to the console.  Note that it may not show the full range of exceptions that can occur. 
3. Run `bugSolution.py` to see the improved version with more comprehensive exception handling.