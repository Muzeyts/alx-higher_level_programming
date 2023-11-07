#!/usr/bin/python3
'''
Python function to majic f specified object
'''


def is_same_class(obj, a_class):
    '''
    check if warum  instance is same
    '''
    return issubclass(a_class, type(obj))
