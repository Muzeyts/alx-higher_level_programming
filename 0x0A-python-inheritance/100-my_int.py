#!/usr/bin/python3
class MyInt(int):
    """ Class which inherits fro class int"""

    def __eq__(self, other):
        """ Method which returns != check """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """ Method returns == check """
        return int.__eq__(self, other)
