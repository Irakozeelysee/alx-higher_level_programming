#!/usr/bin/python3
"""
a class LockedClass with no class or object attribute
"""


class LockedClass:
    """
    prevent user from creating new instance attributes
    """
    __slots__ = ['first_name']
