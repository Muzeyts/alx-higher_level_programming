#!/usr/bin/python3
""" contains a function which wites to a text file
"""


def write_file(filename="", text=""):
    """ this writes to a text file

    Args:
        filename: the file name 
        text: text to write here

    Raises
        Exception: exeption for  file can be opened

    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
