#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqq_list = set(my_list)
    numb = 0

    for i in uniqq_list:
        numb += i

    return (numb)
