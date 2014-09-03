__author__ = 'stephen'

from dimension_validate import *
from numpy import *


def secant_method(f: callable, guess0: (int, float), guess1: (int, float), err: float) -> float:
    if dim_validate3(guess0) and dim_validate3(guess1) and dim_validate3(err):
        if dim_validate2(guess0) and dim_validate2(guess1) and dim_validate2(err):
            if dim_validate1(err):
                x0, x1 = guess0, guess1
                y = 5
                while y > err:
                    x = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
                    y = (f(x))**2
                    x0 = x1
                    x1 = x
                return x1
            else:
                raise ValueError("Argument(s) must be positive: ")
        raise TypeError('Argument(s) must not be string')
    raise AttributeError("Argument(s) not provided")


def midpoint(f: callable, start: (int, float), end: (int, float), partitions: int) -> float:
    if dim_validate3(start) and dim_validate3(end) and dim_validate3(partitions):
        if dim_validate2(start) and dim_validate2(end) and dim_validate2(partitions):
            if dim_validate1(partitions):
                size = (end-start)/partitions
                sum = 0
                x = start+size/2
                for i in range(0, partitions):
                    sum += size *f(x)
                    x += size
                return sum
            else:
                raise ValueError("Argument(s) must be positive: ")
        raise TypeError('Argument(s) provided should not be string')
    raise AttributeError("Argument(s) not provided")


if __name__ == "__main__":
    def f(x):
        return x**2-2
    #print(secant_method(f, -3, 0, 0.00006))
    #print(midpoint(cos,"op",pi/2,10000))