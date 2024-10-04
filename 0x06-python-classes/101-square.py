#!/usr/bin/python3
"""
This module defines a class Square that represents a square.
"""


class Square:
    """
    This class represents a square.

    Attributes:
        size (int): The size of one side of the square.
        position (tuple): A tuple of 2 positive integers.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square.

        Args:
            size (int): The size of one side of the square.
            position (tuple): A tuple of 2 positive integers.

        Raises:
            TypeError: If size is not an integer or position is not a tuple.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size of one side of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): A tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the character # according to the size.

        If size is equal to 0, print an empty line.
        """
        if self.__size == 0:
            print("")
            return

        print("\n" * self.__position[1], end="")

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Return a string representation of the square.

        This method mimics the behavior of my_print when printing a square.
        """
        if self.__size == 0:
            return ""

        square_str = "\n" * self.__position[1]

        for i in range(self.__size):
            square_str += " " * self.__position[0] + "#" * self.__size
            if i != self.__size - 1:
                square_str += "\n"

        return square_str
