#!/usr/bin/python3

def magic_string():
    """
    Returns a string "BestSchool" concatenated with itself a
    number of times equal to the current iteration count.
    Each time the function is called,
    the iteration count is incremented, starting from 0.
    Returns:
    str: A string representing the magic string.
    """
    magic_string.count = getattr(magic_string, 'count', -1) + 1
    return "BestSchool" + (", BestSchool" * magic_string.count)
