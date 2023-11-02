#!/usr/bin/python3
"""

Module is composed by function which prints square having hash #

"""

def print_square(size):
    """ Function which prints square with hash #
    Args:
        size: size of squared
    Returns:
        No return
    Raises:
        TypeError: If size is not integer
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
