#!/usr/bin/env python3
def uppercase(str):
    result = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        result += i
    print('{}'.format(result))
