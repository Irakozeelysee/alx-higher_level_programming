#!/usr/bin/python3
"""
This a square module.
"""


class Square:
    """
    represents a Square.
    """

    def __init__(self, size=0):
        """
        Initialize a Square.

        Args:
            length (int): size of the square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        the area of the square.

        Return:
            the square area.
        """
        return self.__size * self.__size
