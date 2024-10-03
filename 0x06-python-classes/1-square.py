#!/usr/bin/python3
"""
This module defines a class `Square` that represents a square.
"""


class Square:
    """
    This class represents a square with a private instance attribute `size`.
    """

    def __init__(self, size):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (no type/value verification).
        """
        self.__size = size
