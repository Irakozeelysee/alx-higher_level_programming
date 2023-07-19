#!/usr/bin/python3
"""
Module: base
Class: Base
"""


class Base:
    """
    Base class for managing id attributes in future classes.
    Attributes:
    __nb_objects (int): Private class attribute to keep track of instances.
    id (int): Public instance attribute representing the object's ID.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance.
        Args:
        id (int): If provided, sets the id attribute to the given value.
        Otherwise, increments the __nb_objects counter and
        assigns a new value to the id attribute.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
