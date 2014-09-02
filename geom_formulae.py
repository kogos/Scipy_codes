__author__ = 'stephen'
from numpy import *
from numbers import Number
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

#print("Area of a rectangle length=10 units and width=5 units\n", rectangle_area(), " square units")
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

#print("Surface area of solid cone radius=4 units and slant_height=9 units\n", solid_cone_surface_area("t","dd"), " square units")

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
#print("Volume of sphere radius=7 units\n", sphere_volume(-8), " cubic units")
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
#print("Area of circle radius=7 units\n", circle_area(-8), " square units")
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
    if dim_validate3(length) and dim_validate3(width) and dim_validate3(height):
        if dim_validate2(length) and dim_validate2(width) and dim_validate2(height):
            if dim_validate1(length) and dim_validate1(width) and dim_validate1(height):
                return length * width *height
            else:
                raise ValueError("side must be positive: ")
        raise TypeError('value is a string')
    raise AttributeError("The dimension is not provided")

#print("Volume of a cuboid sides(3,4,6) units\n", cuboid_volume(3, 4, None), " cubic units")
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
#print("Surface area of a cube side=3 units\n", cube_surface_area(-9), " square units")
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
#print("Perimeter of semi circle diameter=7 units\n", semi_circle_perimeter(diameter=-7), " units")
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
#print("Area of semi circle radius=7 units\n", semi_circle_area(diameter=5), " square units")
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
#(trapezium_area(5,2,None))
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
#print("Volume of a regular pyramid base_length= 3 units, base_width=4 units, height=7 units\n", regular_pyramid_volume(3, 4, -4), " cubic units")
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
#print("Volume of an ellipsoid with dimensions (8,5,3) units\n", ellipsoid_volume(8, 5, -9), " cubic units")
#==============================END===============================================

#if __name__ == "__main__":
    #print("Area of a rectangle length=10 units and width=5 units\n", rectangle_area(5, 5), " square units")
    #print("Surface area of solid cone radius=4 units and slant_height=9 units\n", solid_cone_surface_area(4, 9),
    #      " square units")
    #print("Volume of sphere radius=7 units\n", sphere_volume(7), " cubic units")
    #print("Area of circle radius=7 units\n", circle_area(7), " square units")
    #print("Area of triangle sides(4,3,5) units\n", triangle_area(side_a=1, side_b=2, side_c=3), " square units")
    #print("Volume of a cuboid sides(3,4,6) units\n", cuboid_volume(3, 4, 5), " cubic units")
    #print("Surface area of a cube side=3 units\n", cube_surface_area(3), " square units")
    #print("Perimeter of semi circle diameter=7 units\n", semi_circle_perimeter(diameter=7), " units")
    #print("Area of semi circle radius=7 units\n", semi_circle_area(radius=7), " square units")
    #print("Area of trapezium parallel_side_1=5 units, parallel_side_2=10 units, height=6 units\n",
    #      trapezium_area(5, 10, 6), " square units")
    #print("Volume of a regular pyramid base_length= 3 units, base_width=4 units, height=7 units\n",
    #     regular_pyramid_volume(3, 4, 7), " cubic units")
    #print("Volume of an ellipsoid with dimensions (8,5,3) units\n", ellipsoid_volume(8, 5, 3), " cubic units")