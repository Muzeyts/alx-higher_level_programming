#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    conunt = 0
    for n in range(x):
        try:
            print("{}".format(my_list[n]), end='')
        except:
            break
        else:
            conunt += 1
    print()
    return (conunt)
