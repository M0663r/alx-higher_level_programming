#!/usr/bin/python3
"""
This module defines a class Student, which includes attributes for
first name, last name, and age, along with a method to return a dictionary
representation of the instance. It allows retrieving specific attributes
based on a provided list.
"""


class Student:
    """
    A class that defines a student by their first name, last name, and age.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

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
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only those attributes are retrieved.
        Otherwise, all attributes are retrieved.

        Args:
            attrs (list): A list of attribute names (strings) to retrieve.

        Returns:
            dict: The dictionary representation of the student.
        """
        if attrs is not None and isinstance(attrs, list):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__
