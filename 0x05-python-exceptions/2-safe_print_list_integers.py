#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    coniunt = 0

    for nm in range(x):
        try:
            print("{:d}".format(my_list[nm]), end='')
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            coniunt += 1

    print()
    return (coniunt)
