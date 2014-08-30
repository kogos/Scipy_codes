__author__ = 'stephen'
from numpy import *
from numbers import Number


def rectangle_area(length: float, width: float) -> Number:
    """
    It calculates the area of a rectangle given length and width
    :param length: the length of a rectangle
    :param width: the width of a rectangle
    :return: the area of a rectangle (in square units of input variables)
    >>> rectangle_area(10,5)
    50
    """
    return length * width


def solid_cone_surface_area(radius: Number, slant_height: Number) -> Number:
    """"
    It calculates the area of a rectangle given length and width
    @param radius: base radius of the cone
    @param slant_height: slant height of the cone
    @return: the surface area of the solid cone (in square units of input variables)
    >>> solid_cone_surface_area(4,9)
    163.36281798666926
    """
    return pi * radius * radius + pi * radius * slant_height


def sphere_volume(radius: Number) -> Number:
    """
    Calculates the volume of a sphere.
    @param radius: radius of the sphere
    @return: the volume of the sphere (in cubic units of the radius)
    >>> sphere_volume (7)
    1436.7550402417319
    """
    return 4 * pi * radius * radius * radius / 3


def circle_area(radius: Number) -> Number:
    """
    Calculates the area of a circle.
    @param radius: radius of the circle
    @return: area of the circle(in units of it's radius)
    >>> circle_area(7)
    153.93804002589985
    """
    return pi * radius ** 2


def triangle_area(side_a=None, side_b=None, side_c=None, height=None, angle_theta=None) -> Number:
    """
    Calculates the area of a triangle given adequate arguments
    @param side_a: dimension of first side of the triangle
    @param side_b: dimension of second side of the triangle
    @param side_c: dimension of third side of the triangle
    @param height: height of the triangle
    @param angle_theta: angle given in triangle (in radians)
    @return: The area of the triangle (in square units of the sides)
    >>>triangle_area(side_a=4, side_b=3,side_c=5)
    6.0
    >>>triangle_area(side_a=4, side_b=3,angle_theta=pi/2)
    6.0
    >>>triangle_area(side_a=4, height=3)
    6.0
    """
    if (side_a is not None) & (side_b is not None) & (side_c is not None):
        s = (side_a + side_b + side_c) / 2
        area = (s * (s - side_a) * (s - side_b) * (s - side_c))**(1/2)
        return area
    elif (side_a is not None) & (side_b is not None) & (angle_theta is not None):
        area = 0.5*side_a*side_b*sin(angle_theta)
        return area
    elif (side_a is not None) & (height is not None):
        area = side_a * height / 2
        return area
    else:
        return "The arguments given are inadequate to compute the area"


def cuboid_volume(length: float, width: float, height: float) ->Number:
    """
    Calculates the volume of cuboid
    @param length: the length of a cuboid
    @param width: the width of a cuboid
    @param height: the height of a cuboid
    @return:the volume of a cuboid (in cubic units of the dimensions)
    >>> cuboid_volume(3, 4, 5)
    60
    """
    return length*width*height


def cube_surface_area(side: Number) ->Number:
    """
    Calculates the surface area of cube given side dimension
    @param side: dimension of the side of cube
    @return: the surface area of the cube (in square units of side)
     >>> cube_surface_area(3)
     54
    """
    return 6*side**2


def semi_circle_perimeter(radius=None, diameter=None):
    """
    Calculates the perimeter of semicircle given either radius or diameter
    @param radius: radius of the semi circle
    @param diameter: diameter of the semi circle
    @return: the perimeter of the circle (in units of input parameter)
    >>>semi_circle_perimeter(radius=7)
    35.99114857512855
    >>>semi_circle_perimeter(diameter=7)
    17.995574287564274
    """
    if radius is not None:
        perimeter = pi*radius+2*radius
    else:
        perimeter = pi*diameter/2+diameter
    return perimeter


def trapezium_area(parallel_side_1: float, parallel_side_2: float, height: float) ->Number:
    """
    Calculates the area of  trapezium
    @param parallel_side_1: length of the first parallel side
    @param parallel_side_2: length of the second parallel side
    @param height: the height of the trapezium
    @return: the area of the trapezium (in square units of the input parameters)
    >>>trapezium_area(5,10,6)
    45.0
    """
    return 0.5*(parallel_side_1+parallel_side_2)*height


def regular_pyramid_volume(base_length: float, base_width: float, height: float) ->Number:
    """

    @param base_length: base length of the pyramid
    @param base_width: base width of the pyramid
    @param height: height of the pyramid
    @return: area of the pyramid (in cubic units of the input parameters)
    >>>regular_pyramid_volume(3,4,7)
    28.0
    """
    return base_length*base_width*height/3
print(rectangle_area(10, 5))
print(solid_cone_surface_area(4.9, 9.))
print(sphere_volume(7))
print(circle_area(7))
print(triangle_area(side_a=4, side_b=3, side_c=5))
print(cuboid_volume(3, 4, 5))
print(cube_surface_area(3))
print(semi_circle_perimeter(diameter=7))
print(trapezium_area(5, 10, 6))
print(regular_pyramid_volume(3, 4, 7))
