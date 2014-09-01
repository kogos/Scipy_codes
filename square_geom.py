__author__ = 'stephen'
from numbers import Number
from numpy import *


def square_perimeter(side: Number) -> Number:
    """
    Calculate perimeter of a square from side length.

    @param side: the side length
    @return: the perimeter (same units as side length)

    >>> square_perimeter(4)
    16
    """
    return 4*side


def square_area(side):
    """
    Calculate area of a square from side length.
    @param side: the side length
    @return: the area (units^2 from side)
    >>> square_area(4)
    16
    """
    return side*side


def solid_cone_surface_area(radius: Number, slant_height: Number) -> Number:
    """"
    It calculates the area of a rectangle given length and width
    @param radius: base radius of the cone
    @param slant_height: slant height of the cone
    @return: the surface area of the solid cone (in square units of input variables)
    >>> solid_cone_surface_area(4,9)
    163.36281798666926
    """
    return pi * (radius**2) + pi * radius * slant_height