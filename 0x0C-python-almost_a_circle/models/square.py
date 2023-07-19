#!/usr/bin/python3
"""
Module: square
Class: Square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    Attributes:
        Inherits all attributes from Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): Size of the square (both width and height).
            x (int): x-coordinate of the square (default is 0).
            y (int): y-coordinate of the square (default is 0).
            id (int): If provided, sets the id attribute to the given value.
                      Otherwise, the id will be automatically assigned by the
                      Base class constructor.
        """
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """Assigns attributes based on *args and **kwargs."""
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if i < len(attributes):
                    setattr(self, attributes[i], args[i])
                    if i == 1:
                        self.width = args[i]
                        self.height = args[i]
        elif kwargs:
            for key, value in kwargs.items():
                if key == 'size':
                    self.width = value
                    self.height = value
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Returns a string representation of the square."""
        ret = "[Square] ({})".format(self.id)
        ret += " {}/{}".format(self.x, self.y)
        ret += " - {}".format(self.width)
        return ret
