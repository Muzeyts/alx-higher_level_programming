#!/usr/bin/python3
"""6. From JSON string to Object"""


def from_json_string(my_str):
    """returns an object (Python data structure)
    Args:
        my_str (str): representation of an object
    Returns:
        Object (Python data structure): based on my_str
    """
    import json
    return json.loads(my_str)
