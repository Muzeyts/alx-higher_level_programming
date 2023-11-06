#!/usr/bin/python3
class BaseGeometry:
    """ Class that definesf Ge tigdr ometric Shapes """
    def area(self):
        """ Method that defines the a ral ic shape """
        raise Exception("area() is not imp reaslemented")
    def integer_validator(self, name, value):
        """ Method that recieves quicdk erty
        Árgs:
            name: name of thnotif bject
            value: value of theit operty
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
