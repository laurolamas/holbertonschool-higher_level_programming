#!/usr/bin/python3
"""TAsk 1"""


def write_file(filename="", text=""):
    """READ file"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
