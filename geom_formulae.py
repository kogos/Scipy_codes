__author__ = 'stephen'
from numpy import *
from numbers import Number


def rectangle_area(length: int, width: int) -> Number:
    """
    It calculates the area of a rectangle given length and width
    :param length: the length of a rectangle
    :param width: the width of a rectangle
    :return: the area of a rectangle (in square units of input variables)
    >>> rectangle_area(10,5)
    50
    """
    return length * width


print(rectangle_area(10, 5))


def solid_cone_surface_area(radius: Number, slant_height: Number) -> Number:
    """"
    It calculates the area of a rectangle given length and width
    :param radius: base radius of the cone
    :param slant_height: slant height of the cone
    :return: the surface area of the solid cone (in square units of input variables)
    >>> solid_cone_surface_area(4,9)
    163.36281798666926
    """
    return pi * radius * radius + pi * radius * slant_height


print(solid_cone_surface_area(4.9, 9.))


def sphere_volume(radius: Number) -> Number:
    """
    Calculates the volume of a sphere.
    :param radius: radius of the sphere
    :return: the volume of the sphere (in cubic units of the radius)
    >>> sphere_volume (7)
    1436.7550402417319
    """
    return 4 * pi * radius * radius * radius / 3


print(sphere_volume(7))


def circle_area(radius: Number) -> Number:
    """
    Calculates the area of a circle.
    :param radius: radius of the circle
    :return: area of the circle(in units of it's radius)
    >>> circle_area(7)
    153.93804002589985
    """
    return pi * radius ** 2


print(circle_area(7))


def triangle_area(side_a=None, side_b=None, side_c=None, height=None, theta=None) -> Number:
    """
    Calculates the area of a triangle given three sides
    :rtype : object
    :param side_a: dimension of first side of the triangle
    :param side_b: dimension of second side of the triangle
    :param side_c: dimension of third side of the triangle
    :param height: height of the triangle
    :param theta: angle given in triangle
    :return: The area of the triangle (in square units of the sides)
    """
    if (side_a is not None) & (side_b is not None) & (side_c is not None):
        s = (side_a + side_b + side_c) / 2
        area = (s * (s - side_a) * (s - side_b) * (s - side_c))**(1/2)
    elif (side_a is not None) & (side_b is not None) & (theta is not None):
        area = 0.5*side_a*side_b*sin(theta)
    else:
        #height != None & side_a != None:
        area = side_a * height / 2
    return area
print (triangle_area(side_a=3, side_b=4, theta=pi/2))
