"""Common code"""
import os
import inspect


def read_input() -> str:
    """The input.txt is always stored in the same directory as whatever file we're running."""
    caller_file = inspect.stack()[1].filename
    input_file_path = os.path.join(os.path.dirname(caller_file), "input.txt")
    with open(input_file_path) as flines:
        input = flines.read()
    return input
