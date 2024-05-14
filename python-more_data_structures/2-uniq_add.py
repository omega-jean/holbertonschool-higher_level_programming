#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbers = []
    for i in my_list:
        if i not in unique_numbers:
            unique_numbers.append(i)
    result = sum(unique_numbers)
    return result
