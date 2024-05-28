#!/usr/bin/python3
"""student generation modul"""


class Student:
    """create new class student"""

    def __init__(self, first_name, last_name, age):
        """initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns the dictionary description with simple data structure"""
        if attrs is None:
            return self.__dict__
        else:
            result = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    result[key] = value
            return result
