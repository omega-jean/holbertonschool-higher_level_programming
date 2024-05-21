#!/usr/bin/python3
"""This module contain a function that add two integers
Args:
    a (int): first parameter
    b (int): second parameter
"""


def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
