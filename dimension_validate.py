__author__ = 'stephen'
from numbers import Number


def dim_validate(param):
    """
    Test if dim is a Number and is >= 0.

    >>> dim_validate(5)
    True

    >>> dim_validate(-5)
    False

    >>> dim_validate("a string")
    False
    """
    return isinstance(param, Number) and param >= 0 and param is not str