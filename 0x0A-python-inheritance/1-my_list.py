#!/usr/bin/python3
"""
MyList class
"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Prints the list in sorted order (ascending sort).

        Returns:
            None.
        """
        sorted_list = sorted(self)
        print(sorted_list)
