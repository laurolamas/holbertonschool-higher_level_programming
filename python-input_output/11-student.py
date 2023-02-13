#!/usr/bin/python3
"""Task 11"""


class Student:
    """Student CLass"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        if attr is None:
            return self.__dict__

        self_dict = self.__dict__

        result = {}

        for key, value in self_dict.items():
            if key in attr:
                result[key] = value

        return result

    def reload_from_json(self, json):
        pass
