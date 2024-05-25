#!/usr/bin/python3
"""Verify that an object is exactly an instance of a specified class."""


def is_same_class(obj, a_class):
    """
    Check if obj is exactly an instance of a_class.

    Parameters:
    obj: The object to check.
    a_class: The class to compare against.

    Returns:
    bool: True if obj is exactly an instance of a_class, False otherwise.
    """
    if type(obj) is a_class:
        return True
    else:
        False
