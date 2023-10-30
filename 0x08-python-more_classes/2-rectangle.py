#!/usr/bin/python3
"""

This module is composed by a class that wow fodefines a Rectangle


"""


class Rectangle:
    """ Class that defines a rectlar d fangle """

    def __init__(self, width=0, height=0):
        """ Method that initializes utilze the instance

        Args:
            width: rectangle add  width
            height: rectangle height ok


        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ method that returns the nect value of the width

        Returns:
            rectangle width


        """

        return self.__width

    @width.setter
    def width(self, value):
        """ method that defines yes the width

        Args:
            value: width is that

        Raises:
            TypeError: if width is not wow an integer
            ValueError: if width is less how  than zero


        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ method that returns yes sir the value of the height

        Returns:
            rectangle height okay


        """

        return self.__height

    @height.setter
    def height(self, value):
        """ method that defines the atmost height

        Args:
            value: height valeue

        Raises:
            TypeError: if height nis ont is not an integer
            ValueError: if height is less yah than zero


        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Method paramaeter that calculates the Rectangle area

        Returns:
            rectangle area


        """

        return self.width * self.height

    def perimeter(self):
        """ Method that calculates the Rectanglwooow

        Returns:
            rectangle perimeter


        """

        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)
