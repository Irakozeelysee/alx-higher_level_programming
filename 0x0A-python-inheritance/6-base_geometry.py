#!/usr/bin/python3
"""
Public instance method
"""


class BaseGeometry:
    """
    BaseGeometry class represents the base geometry object.
    """

    def area(self):
    """
    Calculates the area of the geometry object.
    Raises:
    Exception: If the area() method is not implemented in the derived class.
    """
    raise Exception("area() is not implemented")
