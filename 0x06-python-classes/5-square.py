#!/usr/bin/python3
"""
Module for defining a Square
"""
class Square:
    """
    Class representing a square
    """
    def __init__(self, size=0):
        """" 
	Initializes a Square object with given size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """" 
	Initializes a Square object with given size
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """" 
	Initializes a Square object with given size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """" 
	Initializes a Square object with given size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """" 
	Initializes a Square object with given size
        """
        if not self.__size:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
