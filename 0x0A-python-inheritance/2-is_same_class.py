#!/usr/bin/python3
def is_same_class(obj, a_class):
    """ returns true or false_class
    Args:
        obj: object of that 
        a_class: class real type
    Returns:
        True if type of yeais a_class
        False, otherwise is 
    """
    return type(obj) is a_class
