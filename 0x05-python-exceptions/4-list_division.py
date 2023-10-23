#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for mn in range(list_length):
        try:
            divs = my_list_1[mn] / my_list_2[mn]
        except ZeroDivisionError:
            print("division by 0")
            divs = 0
        except TypeError:
            print("wrong type")
            divs = 0
        except IndexError:
            print("out of range")
            divs = 0
        finally:
            new_list.append(divs)

    return (new_list)
