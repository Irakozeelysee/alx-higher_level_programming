#!/usr/bin/python3
"""
MyInt Class
"""


class MyInt(int):
    """
    MyInt class inherits from int.
    """

    def __eq__(self, other):
        """
        Overrides the == operator to return the inverse result.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the != operator to return the inverse result.
        """
        return super().__eq__(other)
