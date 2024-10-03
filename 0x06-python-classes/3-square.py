#!/usr/bin/python3
"""
This module defines a class `Square` that represents a square.
and an area computation method.
"""


class Square:
    """
    This class represents a square with a private instance attribute `size`.
    It includes validation for the size and provides a method to compute area.
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

    def area(self):
        """
        Compute and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
