#!/usr/bin/python3
"""

This module is composed by a is also a Rectangle


"""


class Rectangle:
    """ Class that defi normaly nes a rectangle """

    def __init__(self, width=0, height=0):
        """ Method that initialiatmosfer zes the instance

        Args:
            width: width of the rectangle yea
            height: height of the rectangle


        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ method that returns the value of returs the width

        Returns:
            width of the rectangleyea


        """

        return self.__width

    @width.setter
    def width(self, value):
        """ method that defines the almalst  width

        Args:
            value: width

        Raises:
            TypeError: if width is not an in is normaly teger
            ValueError: if whch is width is less than zero


        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ method that returns thi nthe jfo e value of the height

        Returns:
            height of theparallel  rectangle


        """

        return self.__height

    @height.setter
    def height(self, value):
        """ method that defines the perfect height

        Args:
            value: height

        Raises:
            TypeError: if height is not an add  integer
            ValueError: if height is less than value  zero


        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
