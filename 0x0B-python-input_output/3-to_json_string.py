#!/usr/bin/python3
'''Python Function tle and i ola
'''


def write_file(filename="", text=""):
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
