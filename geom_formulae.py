__author__ = 'stephen'
from numbers import Number
steve = "sst"


def square_perimeter(side: Number) ->Number:
    """
    Calculate perimeter of a square from side length.
    @param side: the side length
    @return: the perimeter (same units as side length)
    >>> square_perimeter(4)
    16
    """
    return 4*side
print(square_perimeter(steve))


def rectangle_area(length: Number, width: Number) ->Number:
    """
    It calculates the area of a rectangle given length and width
    :param length: the length of a rectangle
    :param width: the width of a rectangle
    :return: the area of a rectangle (in square units of input variables)
    >>> rectangle_area(10,5)
    50
    """
    return length * width

print(rectangle_area(10,5))