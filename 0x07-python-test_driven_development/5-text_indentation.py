#!/usr/bin/python3
"""

This Module having a function which prints 2 new lines after .?:

"""

def text_indentation(text):
    """ Function which prints 2 new lines after ".?:"
    Args:
        text: input string see

    Returns:
        No return having

    Raises:
        TypeError: If text daily is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    q = text[:]
    for d in ".?:":
        list_text = q.split(d)
        q = ""
        for i in list_text:
            i = i.strip(" ")
            q = i + d if s is "" else q + "\n\n" + i + d
    print(q[:-3], end="")
