#!/usr/bin/python3
def number_keys(a_dictionary):
    znum = 0
    nb_keys = list(a_dictionary.keys())
    for i in nb_keys:
        znum += 1
    return (znum)
