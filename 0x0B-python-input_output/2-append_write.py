#!/usr/bin/python3
'''Python function how to do  and print ot stdout'''


def read_lines(filename="", nb_lines=0):
    cotunt = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            cotunt += 1
            print(line, end="")
            if nb_lines == cotunt:
                break
