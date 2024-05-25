#!/usr/bin/python3
"""my_list generation modul"""

class MyList(list):
    """class mylist"""

    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
