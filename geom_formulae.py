__author__ = 'stephen'
from numpy import *
from dimension_validate import *
#-----------------------------Function 1-----------------------------------------


def rectangle_area(length: Number, width: Number) -> Number:
    """
    It calculates the area of a rectangle given length and width
    :param length: the length of a rectangle
    :param width: the width of a rectangle
    :return: the area of a rectangle (in square units of input variables)
    >>> rectangle_area(10,5)
    50

    """
    if dim_validate(length) and dim_validate(width):
        return length * width
    elif dim_validate(length):
        if not isinstance(width, Number):
            raise TypeError("The width should be a Number: "+str(width))
        else:
            raise ValueError("The width is less than 0: "+str(width))
    elif dim_validate(width):
        if not isinstance(length, Number):
            raise TypeError("The length should be a Number: "+str(length))
        else:
            raise ValueError("The length is less than 0: "+str(length))
    else:
        if not isinstance(length, Number) and not isinstance(width, Number):
            raise TypeError("Both length and width should be Numbers: "+str(length)+","+str(width))
        else:
            raise ValueError("Both length and width are less than 0: "+str(length)+","+str(width))
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
    if dim_validate(radius) and dim_validate(slant_height):
        return pi * (radius**2) + pi * radius * slant_height
    elif dim_validate(radius):
        if not isinstance(slant_height, Number):
            raise TypeError("The slant_height should be a Number: "+str(slant_height))
        else:
            raise ValueError("The slant_height is less than 0: "+str(slant_height))
    elif dim_validate(slant_height):
        if not isinstance(radius, Number):
            raise TypeError("The radius should be a Number: "+str(radius))
        else:
            raise ValueError("The radius is less than 0: "+str(radius))
    else:
        if not isinstance(radius, Number) and not isinstance(slant_height, Number):
            raise TypeError("Both radius and slant_height should be Numbers: "+str(radius)+","+str(slant_height))
        else:
            raise ValueError("Both radius and slant_height are less than 0: "+str(radius)+","+str(slant_height))
#-----------------------------Function 3-----------------------------------------


def sphere_volume(radius: Number) -> Number:
    """
    Calculates the volume of a sphere.
    @param radius: radius of the sphere
    @return: the volume of the sphere (in cubic units of the radius)
    >>> sphere_volume (7)
    1436.755040241732

    """
    if dim_validate(radius):
        return 4 * pi * (radius**3) / 3
    else:
        if not isinstance(radius, Number):
            raise TypeError("The radius should be a Number: "+str(radius))
        else:
            raise ValueError("The radius is less than 0: "+str(radius))
#-----------------------------Function 4-----------------------------------------


def circle_area(radius: Number) -> Number:
    """
    Calculates the area of a circle.
    @param radius: radius of the circle
    @return: area of the circle(in square units of it's radius)
    >>> circle_area(7)
    153.93804002589985

    """
    if dim_validate(radius):
        return pi * (radius**2)
    else:
        if not isinstance(radius, Number):
            raise TypeError("The radius should be a Number: "+str(radius))
        else:
            raise ValueError("The radius is less than 0: "+str(radius))
#-----------------------------Function 5-----------------------------------------


def triangle_area(height=None, base=None) -> Number:
    """
    Calculates the area of a triangle given adequate arguments
    @param height: height of the triangle
    @param base: base of the triangle
    @return: The area of the triangle (in square units of the sides)
    >>> triangle_area(base=4, height=3)
    6.0

    """
    if dim_validate3(base) and dim_validate3(height):
        if dim_validate2(base) and dim_validate2(height):
            if dim_validate1(base) and dim_validate1(height):
                return base * height / 2
            else:
                raise ValueError("side must be positive: ")
        raise TypeError('value is a string')
    raise AttributeError("The dimension is not provided")

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
    if dim_validate3(length) and dim_validate3(width) and dim_validate3(height):
        if dim_validate2(length) and dim_validate2(width) and dim_validate2(height):
            if dim_validate1(length) and dim_validate1(width) and dim_validate1(height):
                return length * width * height
            else:
                raise ValueError("side must be positive: ")
        raise TypeError('value is a string')
    raise AttributeError("The dimension is not provided")
#-----------------------------Function 7-----------------------------------------


def cube_surface_area(side: Number) ->Number:
    """
    Calculates the surface area of cube given side dimension
    @param side: dimension of the side of cube
    @return: the surface area of the cube (in square units of side)
     >>> cube_surface_area(3)
     54

    """
    if dim_validate(side):
        return 6*side**2
    else:
        if not isinstance(side, Number):
            raise TypeError("The side should be a Number: "+str(side))
        else:
            raise ValueError("The side should be positive: "+str(side))
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
        if dim_validate(radius):
            perimeter = pi*radius+2*radius
            return perimeter
        else:
            if not isinstance(radius, Number):
                raise TypeError("The radius should be a Number: "+str(radius))
            else:
                raise ValueError("The radius should be positive: "+str(radius))

    else:
        if dim_validate(diameter):
            perimeter = pi*diameter/2+diameter
            return perimeter
        else:
            if not isinstance(diameter, Number):
                raise TypeError("The diameter should be a Number: "+str(diameter))
            else:
                raise ValueError("The diameter should be positive: "+str(diameter))
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
        if dim_validate(radius):
            area = pi*(radius**2)/2
            return area
        else:
            if not isinstance(radius, Number):
                raise TypeError("The radius should be a Number: "+str(radius))
            else:
                raise ValueError("The radius should be positive: "+str(radius))

    else:
        if dim_validate(diameter):
            area = pi*((diameter/2)**2)
            return area
        else:
            if not isinstance(diameter, Number):
                raise TypeError("The diameter should be a Number: "+str(diameter))
            else:
                raise ValueError("The diameter should be positive: "+str(diameter))
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
    if dim_validate3(parallel_side_1) and dim_validate3(parallel_side_2) and dim_validate3(height):
        if dim_validate2(parallel_side_1) and dim_validate2(parallel_side_2) and dim_validate2(height):
            if dim_validate1(parallel_side_1) and dim_validate1(parallel_side_2) and dim_validate1(height):
                return 0.5*(parallel_side_1+parallel_side_2)*height
            else:
                raise ValueError("side must be positive: ")
        raise TypeError('value is a string')
    raise AttributeError("The dimension is not provided")
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
    if dim_validate3(base_length) and dim_validate3(base_width) and dim_validate3(height):
        if dim_validate2(base_length) and dim_validate2(base_width) and dim_validate2(height):
            if dim_validate1(base_length) and dim_validate1(base_width) and dim_validate1(height):
                return base_length*base_width*height/3
            else:
                raise ValueError("side must be positive: ")
        raise TypeError('value is a string')
    raise AttributeError("The dimension is not provided")
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
    if dim_validate3(major_axis) and dim_validate3(minor_axis) and dim_validate3(vertical_axis):
        if dim_validate2(major_axis) and dim_validate2(minor_axis) and dim_validate2(vertical_axis):
            if dim_validate1(major_axis) and dim_validate1(minor_axis) and dim_validate1(vertical_axis):
                return 4*pi*major_axis*minor_axis*vertical_axis/3
            else:
                raise ValueError("side must be positive: ")
        raise TypeError('value is a string')
    raise AttributeError("The dimension is not provided")
#==============================END===============================================
