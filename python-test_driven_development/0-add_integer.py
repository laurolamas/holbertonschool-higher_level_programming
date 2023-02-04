#!/usr/bin/python3
"""
Task 0
"""


def add_integer(a, b=98):
    """Add Integer"""

    if a is None:
        raise TypeError("a must be an integer")
        return

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
