#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argc = len(argv)

    if argc < 2:
        print("0 arguments.")
    else:
        if argc == 2:
            print("1 argument:")
        else:
            print(f"{argc - 1} arguments:")

        for n in range(1, argc):
            print(f"{n}: {argv[n]}")
