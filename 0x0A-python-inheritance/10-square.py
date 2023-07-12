#!/usr/bin/python3
"""
Square Class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square object.
        Args:
            size (int): The size of the square.
        """
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculates the area of the square.
        Returns:
            The area of the square.
        """
        return self.__size * self.__size
