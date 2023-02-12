#!/usr/bin/python3
"""Task 0"""


def read_file(filename=""):
    """READ file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
