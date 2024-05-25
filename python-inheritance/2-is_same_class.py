#!/usr/bin/python3

def is_same_class(obj, a_class):
    """Check if obj is exactly an instance of cls."""
    if type(obj) is a_class:
        return True
    else:
        False
