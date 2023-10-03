#!/usr/bin/python3
for combnum in range(0, 90):
        if combnum % 10 > combnum / 10:
                if combnum != 89:
                        print("{:02d}, ".format(combnum), end='')
                else:
                        print("{:02d}".format(combnum))
