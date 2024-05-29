#!/usr/bin/env python3
"""This script defines a function to convert CSV data to JSON format."""


import csv
import json


def convert_csv_to_json(csv_filename):
    """convert csv to json"""
    try:
        with open(csv_filename, mode='r', newline='') as file:
            csv_reader = csv.DictReader(file)
            data = [row for row in csv_reader]
            """Uses a list understanding to convert\
            the csv_reader object to a dictionary list"""
        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)
        return True
    except FileNotFoundError:
        return False
