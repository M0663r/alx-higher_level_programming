#!/usr/bin/python3
"""Base module to manage the id attribute in all future classes."""

class Base:
    """Base class to manage id attribute in future classes.

    Attributes:
        __nb_objects (int): Private class attribute to keep count of the objec.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes an instance of the Base class.

        Args:
            id (int): The id for the instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
