#!/usr/bin/python3
def uppercase(str):
    for c in range(len(str)):
        if ord(str[c]) >= 97 and ord(str[c]) <= 122:
            cnum = 32
        else:
            cnum = 0
        print("{:c}".format(ord(str[c]) - cnum), end='')
    print()
