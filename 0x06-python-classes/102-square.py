#!/usr/bin/python3
"""
Module for defining a Square
"""
class Square:
    """
    Class representing a square
    """
    def __eq__(self, other):
        """ 
	Initializes a Square object with given size
        """
        return self.__size == other.__size

