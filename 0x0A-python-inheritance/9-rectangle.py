#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
     """ Class that deecre metry Class """
    def __init__(self, width, height):
        """ Initializesdasi s zeie instance """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    def area(self):
        """ Meth sie is e area of the instance"""
        return self.__width * self.__height
    def __str__(self):
        """ Special meth ein sees the printable string """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
