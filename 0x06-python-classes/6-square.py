#!/usr/bin/python3
"""
A class Square that defines a square.
"""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.

    Methods:
        __init__(self, size=0, position=(0, 0)):
            Initializes a new instance of the Square class.
        area(self):
            Calculates and returns the area of the square.
        size(self):
            Getter method to retrieve the size of the square.
        size(self, value):
            Setter method to set the size of the square.
        position(self):
            Getter method to retrieve the position of the square.
        position(self, value):
            Setter method to set the position of the square.
        my_print(self):
            Prints the square with the '#' character.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position of the square (default is (0, 0)).

        Raises:
            TypeError: If size is not an integer
            or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0
            or position contains negative values.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Args:
            value (int): The size value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Getter method to retrieve the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method to set the position of the square.

        Args:
            value (tuple): The position value to set.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
            ValueError: If value contains negative values.
        """
        if not (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The calculated area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the '#' character.

        If size is equal to 0, an empty line is printed.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
