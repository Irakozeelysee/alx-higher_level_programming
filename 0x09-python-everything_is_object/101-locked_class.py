class LockedClass:
    """
    Class that prevents the creationof new
    instance attributes, except 'first_name'.
    """

    __slots__ = ['first_name']
