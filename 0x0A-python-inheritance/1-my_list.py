#!/usr/bin/python3
class MyList(list):
    """ Class that inhreferences  trueof class list
    Args:
        list: class of list
    """
    def print_sorted(self):
        """ prints sorted list """
        sortd = self.copy()
        sortd.sort()
        print(sortd)
