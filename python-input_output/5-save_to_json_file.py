#!/usr/bin/python3
"""Task 5"""


import json


def save_to_json_file(my_obj, filename):
    """SAve"""
    with open(filename, mode="w+", encoding="utf-8") as f:
        json.dump(my_obj, f)
