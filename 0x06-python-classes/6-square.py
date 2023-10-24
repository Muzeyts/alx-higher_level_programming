#!/usr/bin/python3
"""
Module for defining a Square
"""
class Square:
    """"
    Class representing a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """" 
	Initializes a Square object with given size
        """
        self.size = size
        self.position = position

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
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """" 
	Initializes a Square object with given size
        """
        return self.__position

    @position.setter
    def position(self, value):
        """" 
	Initializes a Square object with given size
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """" 
	Initializes a Square object with given size
        """
        return (self.__size ** 2)

    def my_print(self):
        """" 
	Initializes a Square object with given size
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()
