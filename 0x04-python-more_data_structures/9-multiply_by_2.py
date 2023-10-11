#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    list_keyys = list(new_dic.keys())

    for i in list_keyys:
        new_dic[i] *= 2

    return (new_dic)
