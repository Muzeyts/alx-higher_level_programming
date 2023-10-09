#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_ta = len(tuple_a)
    len_tb = len(tuple_b)

    if len_ta == 0:
        a11 = 0
        a22 = 0
    elif len_ta == 1:
        a11 = tuple_a[0]
        a22 = 0
    else:
        a11 = tuple_a[0]
        a22 = tuple_a[1]

    if len_tb == 0:
        b11 = 0
        b22 = 0
    elif len_tb == 1:
        b11 = tuple_b[0]
        b22 = 0
    else:
        b11 = tuple_b[0]
        b22 = tuple_b[1]

    new_tuple = (a11 + b11, a22 + b22)

    return (new_tuple)
