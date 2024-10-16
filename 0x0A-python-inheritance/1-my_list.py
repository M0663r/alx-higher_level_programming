#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list class
and includes a method to print the list in sorted order.
"""


class MyList(list):
    """
    A subclass of the built-in list class with an additional method.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order without modifying the original list.
        """
        print(sorted(self))
