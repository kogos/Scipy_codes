__author__ = 'stephen'
import turtle
from numpy import *


def draw_square(side):
    i = 0
    while (i < 4):
        turtle.forward(side)
        turtle.left(90)
        i = i+1

side = 50
while side in range(50,101):
    draw_square(side)
    side = side + 10
turtle.done()


def draw_rectangle(length, width):
    i = 0
    while i < 5:
        if i == 0 | i == 2:
            turtle.forward(length)
        else:
            turtle.forward(width)
        turtle.left(90)
        i = i+1
length = 100
width = 40
draw_rectangle(length, width)
turtle.done()
"""
while length in range(50,101):
    draw_rectangle(length, width)
    length = length + 10
turtle.done()
"""