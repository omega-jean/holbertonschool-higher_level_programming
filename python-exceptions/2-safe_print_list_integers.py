#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for idx in range(x):
        try:
            if count >= x:
                break
            print("{:d}".format(my_list[idx]), end="")
            count += 1
        except (TypeError, ValueError):
            try:
                continue
            except IndexError:
                break
    print()
    return count
