#!/usr/bin/env python3
"""a basic serialization module that adds the functionality\
    to serialize a Python dictionary to a JSON file and\
    deserialize the JSON file to recreate the Python Dictionary."""


import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to a JSON file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load and deserialize a JSON file to recreate a Python dictionary."""
    with open(filename, 'r') as file:
        read_file = json.load(file)
        return read_file
