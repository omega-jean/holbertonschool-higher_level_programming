#!/usr/bin/python3
"""is_same_class"""


def is_same_class(obj, a_class):
    """Check if obj is exactly an instance of a_class."""
    if type(obj) is a_class:
        return True
    else:
        return False
