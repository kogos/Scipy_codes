__author__ = 'stephen'
from numpy import *
from numbers import Number


def square_perimeter(side: Number) ->Number:
    """
    Calculate perimeter of a square from side length.
    @param side: the side length
    @return: the perimeter (same units as side length)
    >>> square_perimeter(4)
    16
    """
    return 4*side
print(square_perimeter(4))


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
print(rectangle_area(10.5, 5.2))


def solid_cone_surface_area(radius: Number, slant_height: Number) ->Number:
    """
    It calculates the area of a rectangle given length and width
    :param radius: base radius of the cone
    :param slant_height: slant height of the cone
    :return: the surface area of the solid cone (in square units of input variables)
    >>> solid_cone_surface_area(4,9)
    163.36281798666926
    """
    return pi*radius*radius+pi*radius*slant_height
print(solid_cone_surface_area(4, 9))


def sphere_volume(radius: Number) ->Number:
    """
    Calculates the volume of a sphere.
    :param radius: radius of the sphere
    :return: the volume of the sphere (in cubic units of the radius)
    >>> sphere_volume(7)
    1436.7550402417319
    """
    return 4*pi*radius*radius*radius/3
print(sphere_volume(7))

