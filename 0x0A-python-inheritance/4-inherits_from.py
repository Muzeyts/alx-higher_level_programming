#!/usr/bin/python3
def inherits_from(obj, a_class):
    """ Fus True/False if obj  yah
    Args:
        obj: object df
        a_class: classdf type
    Returns:
        True if obj is a artn instance of a_class
        False, otherwise
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
