#!/usr/bin/python3
def magic_calculation(a, b):
    sumud = 0
    for m in range(1, 3):
        try:
            if (m > a):
                raise Exception("Too far")
            else:
                sumud += (a ** b) / m
        except:
            sumud = b + a
            break
    return (sumud)
