#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dictionary = {}
    for key, value in a_dictionary.items():
        dictionary[key] = value * 2
    return dictionary
