#!/usr/bin/python3
for i in range(100):
    if i < 99:
        print('{}, '.format(f"{i:02}"), end="")
    else:
        print('{}'.format(f"{i:02}"), end="")
print()
