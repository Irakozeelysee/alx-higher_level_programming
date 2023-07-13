#!/usr/bin/python3
"""
This module contains the Student class.
"""


class Student:
    """
    Student class represents a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student object with
        the given first name, last name, and age.
        Args:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of a student object.
        Args:
        attrs (list): Optional list of attributes to
        include in the dictionary representation.
        Returns:
        dict: A dictionary representation of the student object.
        """
        if type(attrs) == list and all(type(ele) == str for ele in attrs):
            dicto = {}
            for element in attrs:
                if hasattr(self, element):
                    dicto.update({element: getattr(self, element)})
            return dicto
        return self.__dict__
