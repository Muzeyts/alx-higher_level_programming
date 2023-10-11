#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    weigh = 0
    numpp = 0
    for tup in my_list:
        weigh += tup[0] * tup[1]
        numpp += tup[1]
    return (weigh / numpp)
