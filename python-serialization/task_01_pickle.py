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
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (IOError, pickle.PickleError) as e:
            print(f"Serialization error: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """deserialize"""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (IOError, pickle.PickleError, EOFError) as e:
            print(f"Deserialization error: {e}")
            return None
