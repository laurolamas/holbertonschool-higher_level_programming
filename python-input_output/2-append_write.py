#!/usr/bin/python3
"""TAsk 2"""


def append_write(filename="", text=""):
    """READ file"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
