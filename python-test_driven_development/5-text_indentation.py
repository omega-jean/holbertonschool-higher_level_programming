#!/usr/bin/python3
def text_indentation(text):
    chars = [":", "?", "."]
    if type(text) != str:
        raise TypeError("text must be a string")

    length = len(text)
    i = 0

    while i < length:
        print(text[i], end="")
        if text[i] in chars:
            print("\n")
            i += 1
            while i < length and text[i] == " ":
                i += 1
            continue
        i += 1
