#!/usr/bin/python3
"""
This module defines a class `Square` that represents a square with size validation.
"""


class Square:
    """
    This class represents a square with a private instance attribute `size`.

    The size must be an integer and greater than or equal to 0.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (must be an integer >= 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # Private attribute to store the size
