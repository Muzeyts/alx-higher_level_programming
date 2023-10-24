#!/usr/bin/python3

"""
Module for defining a Square
"""

class Square:

    """
    Class representing a square
    """
    def __init__(self, size=0):
        """
        Initializes a Square object with given size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
