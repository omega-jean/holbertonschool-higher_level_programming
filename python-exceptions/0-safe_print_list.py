#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    idx = 0
    while True:
        try:
            if count >= x:
                break
            print(my_list[idx], end="")
            count += 1
            idx += 1
        except IndexError:
            break
    print(" ")
    return count
