#!/usr/bin/python3
"""
a class Square that defines a square
"""


class Square:
    """
    The square
    """

    def __init__(self, size=0):
        """
        calls the square and the size
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
