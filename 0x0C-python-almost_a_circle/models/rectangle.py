#!/usr/bin/python3
"""
Module: square
Class: Square
"""

from models.base import Base


class Rectangle(Base):
    """
    Square class that inherits from Rectangle.
    Attributes:
    Inherits all attributes from Rectangle class.
    size (int): Private instance attribute
    representing the size of the square.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Square instance.
        Args:
        size (int): Size of the square.
        x (int): x-coordinate of the square (default is 0).
        y (int): y-coordinate of the square (default is 0).
        id (int): If provided, sets the id attribute to the given value.
        Otherwise, the id will be automatically assigned by the
        Base class constructor.
        """
        Base.__init__(self, id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.y = y

    def update(self, *args, **kwargs):
        """update the object's dimensions"""
        if len(args) == 5:
            self.__y = args[4]
        if len(args) >= 4:
            self.__x = args[3]
        if len(args) >= 3:
            self.__height = args[2]
        if len(args) >= 2:
            self.__width = args[1]
        if len(args) >= 1:
            self.id = args[0]

        if "id" in kwargs:
            self.id = kwargs["id"]
        if "width" in kwargs:
            self.__width = kwargs["width"]
        if "height" in kwargs:
            self.__height = kwargs["height"]
        if "x" in kwargs:
            self.__x = kwargs["x"]
        if "y" in kwargs:
            self.__y = kwargs["y"]

    @property
    def width(self):
        """get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get the x of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the x of the rectangle"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get the y of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the y of the rectangle"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """print the Rectangle"""
        for i in range(self.__y):
            print()

        for i in range(self.__height):
            for k in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """representation of Rectangle"""
        ret = "[Rectangle] ({})".format(self.id)
        ret += " {}/{}".format(self.__x, self.__y)
        ret += " - {}/{}".format(self.__width, self.__height)
        return ret

    def to_dictionary(self):
        """return dictionary representation"""
        return {'x': self.__x,
                'y': self.__y,
                'id': self.id,
                'height': self.height,
                'width': self.width}
