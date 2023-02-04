#!/usr/bin/python3
"""
Test Module
"""


import unittest

max_integer = __import__('6-max_integer').max_integer


class Max_int_test(unittest.TestCase):

    def test_max(self):
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([3, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([4, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([1, 5, 3, 4]), 5)
        self.assertAlmostEqual(max_integer([]), None)

    def test_values(self):
        self.assertRaises(TypeError, max_integer, None)
