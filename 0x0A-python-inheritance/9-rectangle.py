#!/usr/bin/python3
"""
Rectangle class
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class represents a rectangle shape.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        area of the rectangle
        Returns:
        rectangle's area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        Returns:
        str: The rectangle description in the format
        [Rectangle] <width>/<height>.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def __repr__(self):
        """
        represent the rectangle
        """
        print("[Rectangle] {}/{}".format(self.__width, self.__height))
