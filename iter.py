__author__ = 'stephen'
from numpy import *


def secant(f, x0, x1, n):
    for i in range(n):
        if (f(x1)-f(x0)) == 0:
            return x0
        else:
            x = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
            x0 = x1
            x1 = x
print(secant(cos,1.4*pi,2.1*pi,100000000))