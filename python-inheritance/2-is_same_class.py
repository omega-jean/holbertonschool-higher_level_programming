#!/usr/bin/python3
"""Verify that an object is exactly an instance of a specified class."""


def is_same_class(obj, a_class):
    """Check if obj is exactly an instance of a_clas."""
    if type(obj) is a_class:
        return True
    else:
        False
