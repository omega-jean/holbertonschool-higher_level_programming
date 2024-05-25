#!/usr/bin/python3
"""is_king_of_class"""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of, or if the object is\
            an instance of a class that inherited from, a_class."""
    if isinstance(obj, a_class):
        return True
    else:
        return False
