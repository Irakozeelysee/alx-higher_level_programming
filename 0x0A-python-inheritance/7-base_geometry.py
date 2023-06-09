#!/usr/bin/python3
"""
Integer validator
"""


class BaseGeometry:
    """
    BaseGeometry class represents the base geometry object.
    """

    def area(self):
        """
        Calculates the area of the geometry object.
        Raises:
            Exception: If the area() method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value as an integer.
        Args:
            name (str): The name of the value.
            value (int): The value to be validated.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
