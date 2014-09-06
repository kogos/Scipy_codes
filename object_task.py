__author__ = 'stephen'
import math
import turtle
from numpy import *
from matplotlib.patches import Wedge
import matplotlib.pyplot as plt
# from pylab import *


def dim_checker(**kwargs):  # Original idea from Carl Pearson
    errmsg = "All given arguments must be positive numbers; provided :" \
             + \
             str({k: v for k, v in kwargs.items() if v is not None})
    for name, arg in kwargs.items():
        if arg is None:
            pass  # ignore nones, only checking provided arguments here
        elif not isinstance(arg, (int, float)):
            raise TypeError(errmsg)
        elif not arg >= 0:
            raise ValueError(errmsg)


class Shape(object):
    shapes_created = 0

    def __init__(self, **kwargs):
        dim_checker(**kwargs)
        self.shapes_created += 1

    def __str__(self):
        return self.__class__.__name__ + \
               "; area: " + str(self.area) + \
               "; perimeter: " + str(self.perimeter)


class Solid(object):
    solids_created = 0

    def __init__(self, **kwargs):
        dim_checker(**kwargs)
        self.solids_created += 1

    def __str__(self):
        return self.__class__.__name__ + \
               "; surface_area: " + str(self.surface_area) + \
               "; volume: " + str(self.volume)


#====================================CIRCLE=================================


class Circle(Shape):
    """a class representation of circles"""
    circles_created = 0

    def __init__(self, radius: (int, float)):
        super(Circle, self).__init__(radius=radius)
        self.circles_created += 1
        self.radius = radius
        self.pi = pi
        self.area = self.pi * radius ** 2
        self.perimeter = self.pi * radius * 2

    def __str__(self):
        return super(Circle, self).__str__() + \
               "; radius: " + str(self.radius)

    def __cmp__(self, other):
        if not isinstance(other, Circle):
            raise TypeError
        else:
            return self.radius - other.radius

    def draw(self):
        turtle.circle(self.radius)
        turtle.done()


#====================================RECTANGLE=================================


class Rectangle(Shape):
    """a class representation of circles"""
    rectangles_created = 0

    def __init__(self, length: (int, float), width: (int, float)):
        super(Rectangle, self).__init__(length=length, width=width)
        self.rectangles_created += 1
        self.length = length
        self.width = width
        self.area = self.length * self.width
        self.perimeter = self.length * 2 + self.width * 2

    def __str__(self):
        return super(Rectangle, self).__str__() + \
               "; length: " + str(self.length) + "; width: " + str(self.width)

    def __cmp__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError
        else:
            return self.length - other.length, self.width - other.width

    def draw(self):
        i = 0
        while i < 2:
            turtle.forward(self.length)
            turtle.left(90)
            turtle.forward(self.width)
            turtle.left(90)
            i = i + 1
        turtle.done()


#====================================TRIANGLE=================================


class Triangle(Shape):
    """a class representation of triangles"""
    triangles_created = 0

    def __init__(self, side_a: (int, float), side_b: (int, float), side_c: (int, float)):
        super(Triangle, self).__init__(side_a=side_a, side_b=side_b, side_c=side_c)
        self.triangles_created += 1
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.sqrt = sqrt
        self.s = (self.side_a + self.side_b + self.side_c) / 2
        self.area = self.sqrt(self.s * (self.s - self.side_a) * (self.s - self.side_b) * (self.s - self.side_c))
        self.perimeter = self.side_a + self.side_b + self.side_c
        self.cos = cos
        self.pi = pi
        self.acos = math.acos
        self.cosC = (((self.side_c ** 2) - ((self.side_a ** 2) + (self.side_b ** 2))) / ((-2) * self.side_a * self.side_b))
        self.angleC = self.acos(self.cosC) * 180 / self.pi
        self.cosB = (((self.side_b ** 2) - ((self.side_a ** 2) + (self.side_c ** 2))) / ((-2) * self.side_a * self.side_c))
        self.angleB = self.acos(self.cosB) * 180 / self.pi
        self.cosA = (((self.side_a ** 2) - ((self.side_c ** 2) + (self.side_b ** 2))) / ((-2) * self.side_c * self.side_b))
        self.angleA = self.acos(self.cosA) * 180 / self.pi

    def __str__(self):
        return super(Triangle, self).__str__() + \
               "; side_a: " + str(self.side_a) + "; side_b: " + str(self.side_b) + "; side_c: " + str(self.side_c)

    def __cmp__(self, other):
        if not isinstance(other, Triangle):
            raise TypeError
        else:
            return self.side_a - other.side_a, self.side_b - other.side_b, self.side_b - other.side_b

    def draw(self):
        turtle.forward(self.side_c)
        turtle.left(180 - self.angleB)
        turtle.forward(self.side_a)
        turtle.left(180 - self.angleC)
        turtle.forward(self.side_b)
        turtle.left(180 - self.angleA)
        turtle.done()


#====================================SEMI CIRCLE=================================


class Semicircle(Shape):
    """a class representation of semi circles"""
    semicircles_created = 0

    def __init__(self, radius: (int, float)):
        super(Semicircle, self).__init__(radius=radius)
        self.semicircles_created += 1
        self.radius = radius
        self.pi = pi
        self.area = self.pi * ((self.radius) ** 2) / 2
        self.perimeter = self.pi * self.radius + 2 * self.radius

    def __str__(self):
        return super(Semicircle, self).__str__() + \
               "; radius: " + str(self.radius)

    def __cmp__(self, other):
        if not isinstance(other, Semicircle):
            raise TypeError
        else:
            return self.radius - other.radius

    def draw(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        paths = Wedge((0, 0), self.radius, 0, 180)
        ax.add_artist(paths)
        plt.axis([-self.radius, self.radius, 0, self.radius])
        plt.show()


#====================================TRAPEZIUM=================================


class Trapezium(Shape):
    """a class representation of trapeziums"""
    trapeziums_created = 0

    def __init__(self, parallel_side1: (int, float), parallel_side2: (int, float), slant_height1: (int, float),
                 slant_height2: (int, float), height: (int, float)):
        super(Trapezium, self).__init__(parallel_side1=parallel_side1, parallel_side2=parallel_side2,
                                        slant_height1=slant_height1, slant_height2=slant_height2, height=height)
        self.trapeziums_created += 1
        self.parallel_side1 = parallel_side1
        self.parallel_side2 = parallel_side2
        self.slant_height1 = slant_height1
        self.slant_height2 = slant_height2
        self.height = height
        self.area = (self.parallel_side1 + self.parallel_side2 / 2) * self.height
        self.perimeter = self.parallel_side1 + self.parallel_side2 + self.slant_height1 + self.slant_height2

    def __str__(self):
        return super(Trapezium, self).__str__() + \
               "; parallel_side1: " + str(self.parallel_side1)+"; parallel_side2: " + str(self.parallel_side2)\
               +"; slant_height1: " + str(self.slant_height1)+"; slant_height2: " + str(self.slant_height2)\
               +"; height: " + str(self.height)

    def __cmp__(self, other):
        if not isinstance(other, Trapezium):
            raise TypeError
        else:
            return self.parallel_side1 - other.parallel_side1, self.parallel_side2 - other.parallel_side2, \
                   self.slant_height1 - other.slant_height1, self.height - other.height

    def draw(self):
        turtle.forward(self.parallel_side1)
        turtle.left(135)
        turtle.forward(self.slant_height1)
        turtle.left(45)
        turtle.forward(self.parallel_side2)
        turtle.left(45)
        turtle.forward(self.slant_height2)
        turtle.left(135)
        turtle.done()

#====================================CUBE=================================


class Cube(Solid):
    """a class representation of cubes"""
    cubes_created = 0

    def __init__(self, side: (int, float)):
        super(Cube, self).__init__(side=side)
        self.cubes_created += 1
        self.side = side
        self.surface_area = (self.side ** 2)*6
        self.volume = self.side ** 3

    def __str__(self):
        return super(Cube, self).__str__() + \
               "; side: " + str(self.side)

    def __cmp__(self, other):
        if not isinstance(other, Cube):
            raise TypeError
        else:
            return self.side - other.side

#====================================CUBOID=================================


class Cuboid(Solid):
    """a class representation of cuboids"""
    cuboids_created = 0

    def __init__(self, length: (int, float), width: (int, float), height: (int, float)):
        super(Cuboid, self).__init__(length=length, width=width, height=height)
        self.cuboids_created += 1
        self.length = length
        self.width = width
        self.height = height
        self.surface_area = ((self.length * self.width)*2)+((self.length * self.height)*2)+\
                            ((self.height * self.width)*2)
        self.volume = self.length * self.width * self.height

    def __str__(self):
        return super(Cuboid, self).__str__() + \
               "; length: " + str(self.length)+"; width: " + str(self.width)+"; height: " + str(self.height)

    def __cmp__(self, other):
        if not isinstance(other, Cuboid):
            raise TypeError
        else:
            return self.length - other.length, self.width - other.width, self.height - other.height

#====================================END=================================

if __name__ == "__main__":
    circle = Circle(50)
    print(circle)
    circle.draw()
    rectangle = Rectangle(50, 70)
    print(rectangle)
    rectangle.draw()
    triangle = Triangle(300, 400, 500)
    print(triangle)
    triangle.draw()
    semicircle = Semicircle(100)
    print(semicircle)
    semicircle.draw()
    trapezium = Trapezium(200, 100, sqrt(5000), sqrt(5000), 50)
    print(trapezium)
    trapezium.draw()
    cube = Cube(100)
    print(cube)
    cuboid = Cuboid(100, 200, 500)
    print(cuboid)


