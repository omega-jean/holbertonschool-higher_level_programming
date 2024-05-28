#!/usr/bin/python3
"""student generation modul"""


class Student:
    """create new class student"""

    def __init__(self, first_name, last_name, age):
        """initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns the dictionary description with simple data structure"""
        return self.__dict__
