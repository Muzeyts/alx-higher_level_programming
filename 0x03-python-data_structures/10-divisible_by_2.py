#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    check_divs = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            check_divs.append(True)
        else:
            check_divs.append(False)
    return (check_divs)
