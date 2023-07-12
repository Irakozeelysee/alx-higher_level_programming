#!/usr/bin/python3
"""
Same class or inherit from
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of,
    or if the object is an instance
    of a class that inherited from, the specified class.
    Args:
    obj: The object to be checked.
    a_class: The class to compare against.
    Returns:
    True if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class;
    False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
