#!/usr/bin/python3
def add_attribute(obj, name, value):
    """ Function  to an object

    Args:
        obj: object real
        name: name of attribute 
        value: attribute value

    Raises:
        TypeError: if attribute can't be added

    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
