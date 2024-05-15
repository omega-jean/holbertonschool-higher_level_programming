#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    
    value_max = None
    best_key = None
    
    for key, value in a_dictionary.items():
        if value_max is None or value > value_max:
            value_max = value
            best_key = key

    return best_key
