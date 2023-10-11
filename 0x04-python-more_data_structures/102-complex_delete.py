#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    liste_kiys = list(a_dictionary.keys())
    for value_dict in liste_kiys:
        if value == a_dictionary.get(value_dict):
            del a_dictionary[value_dict]
    return (a_dictionary)
