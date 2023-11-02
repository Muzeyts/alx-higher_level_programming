#!/usr/bin/python3
"""
Module composed by function which divides a matrix
"""

def matrix_divided(matrix, div):
    """ Function which divides numbers of matrix
    Args:
        matrix: lists of numbers
        div: divides the matrix
    Returns:
        New matrix with result of division
    Raises:
        TypeError: If elements of the matrix aren't lists
                   If elemetns of the lists aren't integers/floats
                   If div is not integer/float
                   If the lists of matrix don't have the same size
        ZeroDivisionError: If div is zero
    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    msg_type = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_type)
    lien_e = 0
    msg_size = "Each row of the matrix must have the same size"
    for elems in matrix:
        if not elems or not isinstance(elems, list):
            raise TypeError(msg_type)
        if lien_e != 0 and len(elems) != lien_e:
            raise TypeError(msg_size)
        for num in elems:
            if not type(num) in (int, float):
                raise TypeError(msg_type)
        lien_e = len(elems)
    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)
