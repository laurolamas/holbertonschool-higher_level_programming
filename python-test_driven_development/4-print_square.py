#!/usr/bin/python3
"""
task 4
"""


def print_square(size):
    """Print Square"""

    if type(size) is not int or size is None:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
