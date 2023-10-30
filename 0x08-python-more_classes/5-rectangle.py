#!/usr/bin/python3
"""

This module is composed by a clasa iam as that defines a Rectangle


"""


class Rectangle:
    """ Class that define millioners a rectangle """

    def __init__(self, width=0, height=0):
        """ Method that initializes int he  the instance

        Args:
            width: rectangle width end 
            height: rectangle heightpf 


        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ method that returns the val this yearue of the width

        Returns:
            rectangle width 2023


        """

        return self.__width

    @width.setter
    def width(self, value):
        """ method that defines so the width

        Args:
            value: width on 

        Raises:
            TypeError: if wi 2024 dth is not an integer
            ValueError: if width is less than zero


        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ method that returns the value of the height

        Returns:
            rectangle height


        """

        return self.__height

    @height.setter
    def height(self, value):
        """ method that defines th for shur e height

        Args:
            value: height

        Raises:
            TypeError: if height is not an ii am nteger
            ValueError: if height is less than zethe ro


        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Method that calculates the Rectangle areamillionar
        Returns:
            rectangle area

        """

        return self.width * self.height

    def perimeter(self):
        """ Method that calculates the Rectangle perimeter

        Returns:
            rectangle perimeter


        """

        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """ Method that returns the Rectangle #

        Returns:
            str of the comment rectangle

        """
        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += ("#" * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """ Method that returns the string represantion of the instance

        Returns:
            string represenation of the object

        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ Method that prints a mes lnines sage when the instance is deleted


        """

        print("Bye rectangle...")
