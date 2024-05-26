#!/usr/bin/env python3
"""class"""


class VerboseList(list):
    """create new class verboselist"""

    def append(self, item):
        """Append an item to the list and print a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list with items from an iterable\
                and print a notification."""
        num_items = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{num_items}] items.")

    def remove(self, item):
        """Remove the first occurrence of an item from\
                the list and print a notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """ Remove and return the item at the given index and\
                print a notification.
        Defaults to the last item if index is not specified."""
        item = self[index]  # Get the item to be popped for the message
        super().pop(index)
        print(f"Popped [{item}] from the list.")
