#!/usr/bin/python3
"""
A module composed a function which adds two numbers
"""

def add_integer(a, b=98):
    """ Function adds two integer 
    Args:
        a: first number
        b: second number
    Returns:
        Addition of two numbers
    Raises:
        TypeError: If the a or b aren't integer
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
