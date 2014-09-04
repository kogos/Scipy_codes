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


def dim_validate1(param):
    """
    Tests if param>=0
    >>> dim_validate1(5)
    True
    >>> dim_validate1(-5)
    False
    """
    return param >= 0

def dim_validate4(param):
    """
    Tests if the number of partitions is even
    >>> dim_validate4(5)
    False
    >>> dim_validate4(6)
    True
    """
    return param % 2 == 0



def dim_validate2(param):
    """
    Tests that param is not a string
    >>>dim_validate2(4)
    True
    """
    return isinstance(param, Number)


def dim_validate3(param):
    """
    Tests that dim is provided

    >>> dim_validate3(1)
    True
    """
    if param is not None:
        return True