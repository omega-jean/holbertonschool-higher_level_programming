#!/usr/bin/python3
"""fonction read-file"""


def read_file(filename=""):
    """Read a UTF-8 text file and print its content to stdout."""
    with open(filename, 'r', encoding='utf-8') as f:
        read_file = f.read()
        print(read_file, end="")
