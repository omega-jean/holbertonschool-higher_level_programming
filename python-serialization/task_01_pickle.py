#!/usr/bin/env python3
"""Serialization and Deserialization Example with CustomObject"""


import pickle


class CustomObject:
    """create a new class"""

    def __init__(self, name, age, is_student):
        """initialization"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """method to print out the objects\
        attributes with the following format"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """serialize"""
        with open(filename, "wb", encoding="utf-8") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """deserialize"""
        with open(filename, "rb", encoding="utf-8") as file:
            return pickle.dump(file)
