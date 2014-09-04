__author__ = 'stephen'
import turtle
from numpy import *


def dim_checker(**kwargs):  # Original idea from Carl Pearson
    errmsg = "All given arguments must be positive numbers; provided :"\
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
        return self.__class__.__name__ +\
               "; area: "+str(self.area)+\
               "; perimeter: "+str(self.perimeter)
#====================================CIRCLE=================================


class Circle(Shape):
    """a class representation of circles"""
    circles_created = 0

    def __init__(self, radius: (int, float)):
        super(Circle, self).__init__(radius=radius)
        self.circles_created += 1
        self.radius = radius
        self.pi = pi
        self.area = self.pi*radius**2
        self.perimeter = self.pi*radius*2

    def __str__(self):
        return super(Circle, self).__str__()+\
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
        self.area = self.length*self.width
        self.perimeter = self.length*2+self.width*2

    def __str__(self):
        return super(Rectangle, self).__str__()+\
               "; length: " + str(self.length)+"; width: "+str(self.width)

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
            i = i+1
        turtle.done()
#====================================END=================================

if __name__ == "__main__":
    circ = Circle(50)
    print(circ)
    circ.draw()
    rect = Rectangle(50, 70)
    print(rect)
    rect.draw()
