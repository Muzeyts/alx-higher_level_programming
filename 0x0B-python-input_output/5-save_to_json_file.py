#!/usr/bin/python3
"""Save Object to a file"""


def save_to_json_file(my_obj, filename):
    """writes an Object to a texntation
    Args:
        my_obj (object): a python object needded
        filename (str): name of the json file 
    """
    import json

    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
