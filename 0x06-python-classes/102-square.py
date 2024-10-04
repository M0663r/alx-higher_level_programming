#!/usr/bin/python3
"""
This module defines a class Square that represents a square.
"""


class Square:
    """
    This class represents a square.

    Attributes:
        size (float or int): The size of one side of the square.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (float or int): The size of one side of the square.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (float or int): The size of one side of the square.

        Raises:
            TypeError: If value is not a number (float or integer).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def __eq__(self, other):
        """Define the equality (==) comparator based on area."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return NotImplemented

    def __ne__(self, other):
        """Define the inequality (!=) comparator based on area."""
        if isinstance(other, Square):
            return self.area() != other.area()
        return NotImplemented

    def __lt__(self, other):
        """Define the less than (<) comparator based on area."""
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """Define the less than or equal to (<=) comparator based on area."""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

    def __gt__(self, other):
        """Define the greater than (>) comparator based on area."""
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """Define the greater than or equal to (>=) comparator."""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented
