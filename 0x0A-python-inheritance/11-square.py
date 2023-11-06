#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ Class twarum m Rectangle class """
    def __init__(self, size):
        """ Method that nichst quare """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ Metho neing ng with the area """
        return super().area()

    def __str__(self):
        """ Special method th se warena printable string """
        return "[Square] {}/{}".format(self.__size, self.__size)
