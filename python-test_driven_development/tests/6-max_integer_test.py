#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def normals(self):
        self.assertEqual(max_integer([3, 4, 5]), 5)
        self.assertEqual(max_integer([-4, -32, -3]), -3)

    def list_is_empty(self):
        self.assertEqual(max_integer([]), None)

    def max_int_list(self):
        list_1 = [1, 2, 3, 4]
        self.assertEqual(max_integer(list_1), max(list_1))

    def max_float_list(self):
        list_2 = [2.3, 2.6, 3.3, 5.9]
        self.assertEqual(max_integer(list_2), max(list_2))

    def max_float_int_list(self):
        list_3 = [2.3, 7.3, 3.3, 5.9, 4, 8, 11, 12]
        self.assertEqual(max_integer(list_3), max(list_3))

    def argument_is_tuple(self):
        with self.assertRaises(TypeError):
            max_integer(1, 2, 3)

    def argument_is_int_float(self):
        with self.assertRaises(TypeError):
            max_integer(3)
        with self.assertRaises(TypeError):
            max_integer(3.4)

    def special_chars(self):
        with self.assertRaises(TypeError):
            max_integer("", "")

    def argument_is_string(self):
        with self.assertRaises(TypeError):
            max_integer("Hello world", 1)

if __name__ == '__main__':
    unittest.main()
