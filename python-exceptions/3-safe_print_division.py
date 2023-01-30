#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        c = a / b
    except (ValueError, ZeroDivisionError, UnboundLocalError):
        return None
    finally:
        try:
            print("Inside result: {}".format(c))
            print("{}".format(c))
            return c
        except (ValueError, ZeroDivisionError, UnboundLocalError):
            print("Inside result: None")
            return None
