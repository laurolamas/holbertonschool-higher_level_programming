#!/usr/bin/python3
""" Input Check """


def check_width(width):
    """ Checks Input """
    if type(width) is not int:
        raise TypeError("width must be an integer")
    if width <= 0:
        raise ValueError("width must be > 0")


def check_height(height):
    """ Checks Input """
    if type(height) is not int:
        raise TypeError("height must be an integer")
    if height <= 0:
        raise ValueError("height must be > 0")


def check_x(x):
    """ Checks Input """
    if type(x) is not int:
        raise TypeError("x must be an integer")
    if x < 0:
        raise ValueError("x must be >= 0")


def check_y(y):
    """ Checks Input """
    if type(y) is not int:
        raise TypeError("y must be an integer")
    if y < 0:
        raise ValueError("y must be >= 0")
