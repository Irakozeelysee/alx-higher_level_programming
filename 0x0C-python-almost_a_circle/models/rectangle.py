#!/usr/bin/python3
"""
Module: rectangle
Class: Rectangle
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base.

    Attributes:
        __width (int): Private instance attribute representing the width.
        __height (int): Private instance attribute representing the height.
        __x (int): Private instance attribute representing the x-coordinate.
        __y (int): Private instance attribute representing the y-coordinate.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): x-coordinate of the rectangle (default is 0).
            y (int): y-coordinate of the rectangle (default is 0).
            id (int): If provided, sets the id attribute to the given value.
                      Otherwise, the id will be automatically assigned by the
                      Base class constructor.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method for the x-coordinate attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for the x-coordinate attribute."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method for the y-coordinate attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for the y-coordinate attribute."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Prints the rectangle using '#' character to stdout."""
        for i in range(self.__y):
            print()

        for i in range(self.__height):
            for k in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns a string representation of the rectangle."""
        ret = "[Rectangle] ({})".format(self.id)
        ret += " {}/{}".format(self.__x, self.__y)
        ret += " - {}/{}".format(self.__width, self.__height)
        return ret
    def update(self, *args, **kwargs):
        """Assigns arguments to attributes in the order: id, width, height, x, y."""
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]

        if len(args) == 0 and len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
