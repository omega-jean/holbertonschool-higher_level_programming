#!/usr/bin/python3
"""fonction read-file"""

def read_file(filename=""):
    """function that reads a text file in UTF-8"""
    with open(filename, 'r', encoding="utf-8") as file:
        content = file.read()
        print(content, end='')
