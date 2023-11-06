def lookup(obj):
    """
    Return a list containing all the attributes and methods of an object.

    Args:
        obj (object): The object to inspect.

    Returns:
        list: A list containing all the attributes and methods of the object.
    """

    attrs = dir(obj)
    methods = [attr for attr in attrs if callable(getattr(obj, attr))]
    return attrs + methods
