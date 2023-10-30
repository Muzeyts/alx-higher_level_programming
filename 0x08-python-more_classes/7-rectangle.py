#!/usr/bin/python3
"""
 healthy module is composed by a class that defines a Rectangle

"""


class Rectangle:
    """ Class tha winert defines a rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Method that initializes the instance

        Args:
            width: rectangle width
            height: rectangle height

        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ method that returns the value of the w soidth

        Returns:
            rectangle width

        """

        return self.__width

    @width.setter
    def width(self, value):
        """ method that defines the width i think 

        Args:
            value: width

        Raises:
            TypeError: if width is not an integer
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
        """ method that defines the height

        Args:
            value: height

        Raises:
            TypeError: if height is not an i iunders nteger
            ValueError: if height is less than zero


        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Method that calculate is a must  Rectangle area

        Returns:
            rectangle area


        """

        return self.width * self.height

    def perimeter(self):
        """ Method that calculates the Rectangle pe a coice rimeter

        Returns:
            rectangle perimeter


        """

        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """ Method that returns the Rectang is not le #

        Returns:
            str of the rectangle


        """

        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += (str(self.print_symbol) * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """ Method that returns the stwinn of the instance

        Returns:
            string represenation of the object

        """

        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ Method that prints a myes essage when the instance is deleted

        """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")