__author__ = 'stephen'
from numpy import *
from numbers import Number
#-----------------------------Function 1-----------------------------------------


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
#-----------------------------Function 2-----------------------------------------


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
#-----------------------------Function 3-----------------------------------------


def sphere_volume(radius: Number) -> Number:
    """
    Calculates the volume of a sphere.
    @param radius: radius of the sphere
    @return: the volume of the sphere (in cubic units of the radius)
    >>> sphere_volume (7)
    1436.755040241732

    """
    return 4 * pi * (radius**3) / 3
#-----------------------------Function 4-----------------------------------------


def circle_area(radius: Number) -> Number:
    """
    Calculates the area of a circle.
    @param radius: radius of the circle
    @return: area of the circle(in square units of it's radius)
    >>> circle_area(7)
    153.93804002589985

    """
    return pi * (radius ** 2)
#-----------------------------Function 5-----------------------------------------


def triangle_area(side_a=None, side_b=None, side_c=None, height=None, angle_theta=None, base=None) -> Number:
    """
    Calculates the area of a triangle given adequate arguments
    @param side_a: dimension of first side of the triangle
    @param side_b: dimension of second side of the triangle
    @param side_c: dimension of third side of the triangle
    @param height: height of the triangle
    @param angle_theta: angle given in triangle (in radians)
    @param base: base of the triangle
    @return: The area of the triangle (in square units of the sides)
    >>> triangle_area(side_a=4, side_b=3,side_c=5)
    6.0

    >>> triangle_area(side_a=4, side_b=3,angle_theta=pi/2)
    6.0

    >>> triangle_area(base=4, height=3)
    6.0

    """
    if (side_a is not None) & (side_b is not None) & (side_c is not None):
        if ((side_a + side_b) > side_c) & ((side_a + side_c) > side_b) & ((side_b + side_c) > side_a):
            s = (side_a + side_b + side_c) / 2
            area = (s * (s - side_a) * (s - side_b) * (s - side_c))**(1/2)
            return area
        else:
            return "The sum of two sides of a triangle must be greater that the third side"
    elif (side_a is not None) & (side_b is not None) & (angle_theta is not None):
        area = 0.5*side_a*side_b*sin(angle_theta)
        return area
    elif (base is not None) & (height is not None):
        area = base * height / 2
        return area
    else:
        return "The arguments given are inadequate to compute the area"
#-----------------------------Function 6-----------------------------------------


def cuboid_volume(length: float, width: float, height: float) ->Number:
    """
    Calculates the volume of cuboid
    @param length: the length of a cuboid
    @param width: the width of a cuboid
    @param height: the height of a cuboid
    @return:the volume of a cuboid (in cubic units of the dimensions)
    >>> cuboid_volume(5, 4, 3)
    60

    """
    return length*width*height
#-----------------------------Function 7-----------------------------------------


def cube_surface_area(side: Number) ->Number:
    """
    Calculates the surface area of cube given side dimension
    @param side: dimension of the side of cube
    @return: the surface area of the cube (in square units of side)
     >>> cube_surface_area(3)
     54

    """
    return 6*side**2
#-----------------------------Function 8-----------------------------------------


def semi_circle_perimeter(radius=None, diameter=None):
    """
    Calculates the perimeter of semicircle given either radius or diameter
    @param radius: radius of the semi circle
    @param diameter: diameter of the semi circle
    @return: the perimeter of the circle (in units of input parameter)
    >>> semi_circle_perimeter(radius=7)
    35.99114857512855

    >>> semi_circle_perimeter(diameter=7)
    17.995574287564274

    """
    if radius is not None:
        perimeter = pi*radius+2*radius
    else:
        perimeter = pi*diameter/2+diameter
    return perimeter
#-----------------------------Function 9-----------------------------------------


def semi_circle_area(radius=None, diameter=None):
    """
    Calculates the area of semicircle given either radius or diameter
    @param radius: radius of the semi circle
    @param diameter: diameter of the semi circle
    @return: the perimeter of the circle (in square units of input parameter)
    >>> semi_circle_area(radius=7)
    76.96902001294993

    >>> semi_circle_area(diameter=7)
    38.48451000647496

    """
    if radius is not None:
        area = pi*(radius**2)/2
    else:
        area = pi*((diameter/2)**2)
    return area
#-----------------------------Function 10-----------------------------------------


def trapezium_area(parallel_side_1: float, parallel_side_2: float, height: float) ->Number:
    """
    Calculates the area of  trapezium
    @param parallel_side_1: length of the first parallel side
    @param parallel_side_2: length of the second parallel side
    @param height: the height of the trapezium
    @return: the area of the trapezium (in square units of the input parameters)
    >>> trapezium_area(5,10,6)
    45.0

    """
    return 0.5*(parallel_side_1+parallel_side_2)*height
#-----------------------------Function 11-----------------------------------------


def regular_pyramid_volume(base_length: float, base_width: float, height: float) ->Number:
    """
    Calculates the volume of a regular pyramid
    @param base_length: base length of the pyramid
    @param base_width: base width of the pyramid
    @param height: height of the pyramid
    @return: area of the pyramid (in cubic units of the input parameters)
    >>> regular_pyramid_volume(3,4,7)
    28.0

    """
    return base_length*base_width*height/3
#-----------------------------Function 12-----------------------------------------


def ellipsoid_volume(major_axis: float, minor_axis: float, vertical_axis: float) ->Number:
    """
    Calculates the volume of an ellipsoid
    @param major_axis: the major axis of the ellipsoid
    @param minor_axis: the minor axis of the ellipsoid
    @param vertical_axis:the vertical axis of the ellipsoid
    @return: The area of the ellipsoid (in cubic units of input parameters)
    >>> ellipsoid_volume(8,5,3)
    502.65482457436684

    """
    return 4*pi*major_axis*minor_axis*vertical_axis/3
#==============================END===============================================