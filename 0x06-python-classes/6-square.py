#!/usr/bin/python3
"""
This module defines a class `Square` that represents a square,
area computation, and methods to print the square using the `#` character and a
position.
"""


class Square:
    """
    This class represents a square with private instance attributes

    It includes validation for both size and position,
    methods to get and set these attributes,
    compute the area,
    and print the square with the character `#` according to the size and
    position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (must be an integer >= 0).
            position (tuple): A tuple of two integers representing the position

        Raises:
            TypeError: If size is not an integer
            or position is not a tuple of two positive integers.
            ValueError: If size is less than 0
            or the integers in position are not >= 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square, with validation for type and value.

        Args:
            value (int): The new size of the square (must be an integer >= 0).

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
        """
        Get the position of the square.

        Returns:
            tuple: A tuple of two positive integers representing the position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square,
        with validation for a tuple of two positive integers.

        Args:
            value (tuple): The new position of the square

        Raises:
            TypeError: If value is not a tuple of two positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Compute and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square using the character `#`.

        If size is 0, print an empty line.
        Position is used to control the leading spaces and
        the number of empty lines before printing the square.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print("")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
