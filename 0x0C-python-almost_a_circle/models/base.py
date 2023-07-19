#!/usr/bin/python3
"""
Module: base
Class: Base
"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances that inherit from Base.
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            json_str = cls.to_json_string([obj.to_dictionary()
                                          for obj in list_objs])
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: List represented by json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        Args:
            **dictionary: Double pointer to
            a dictionary representing an instance.

        Returns:
            object: An instance with all attributes set.
        """
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)
        else:
            dummy_instance = None

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a JSON file.
        Returns:
        list: List of instances from the JSON file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_data = file.read()
        except FileNotFoundError:
            return []
        list_dicts = cls.from_json_string(json_data)
        instances = [cls.create(**dictionary) for dictionary in list_dicts]
        return instances
