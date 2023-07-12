#!/usr/bin/python3
"""This Module lists all available
attributes and methods of an object
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    Args:
    obj (object): The object to inspect.
    Returns:
    list: A list of strings representing the available attributes and methods.
    """
    return dir(obj)
