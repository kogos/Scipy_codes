__author__ = 'stephen'
import turtle
from matplotlib.patches import Wedge
import matplotlib.pyplot as plt
from numpy import *
#------------------------------CIRCLE------------------------


def draw_circle(radius):
    turtle.circle(radius)
    turtle.done()
#------------------------------RECTANGLE----------------------


def draw_rectangle(width, length):
    i = 0
    while i < 2:
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)
        i = i+1
    turtle.done()
#------------------------------TRAPEZIUM----------------------


def draw_trapezium(parallel_side_1, parallel_side_2, slant_height_1, slant_height_2):
    turtle.forward(parallel_side_1)
    turtle.left(135)
    turtle.forward(slant_height_1)
    turtle.left(45)
    turtle.forward(parallel_side_2)
    turtle.left(45)
    turtle.forward(slant_height_2)
    turtle.left(135)
    turtle.done()
#------------------------------TRIANGLE------------------------


def draw_triangle(side):
    i = 0
    while i < 3:
        turtle.forward(side)
        turtle.left(120)
        i = i+1
    turtle.done()
#------------------------------SEMI CIRCLE----------------------


def draw_semi_circle(radius):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    paths = Wedge((0.5, 0), radius, 0, 180)
    ax.add_artist(paths)
    plt.show()
#===============================================================


if __name__ == "__main__":
    draw_circle(50)
    draw_rectangle(50, 100)
    draw_trapezium(200, 100, sqrt(5000), sqrt(5000))
    draw_triangle(70)
    draw_semi_circle(0.5)
#============================END================================