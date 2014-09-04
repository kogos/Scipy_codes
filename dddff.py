__author__ = 'stephen'

from dimension_validate import *
from numpy import *


def secant_method(f: callable, guess0: (int, float), guess1: (int, float), err: float) -> float:
    if dim_validate3(guess0) and dim_validate3(guess1) and dim_validate3(err):
        if dim_validate2(guess0) and dim_validate2(guess1) and dim_validate2(err):
            if dim_validate1(err):
                x0, x1 = guess0, guess1
                while abs(f(x1)) > err and f(x1) != f(x0):
                    x = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
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
                    sum += size * f(x)
                    x += size
                return sum
            else:
                raise ValueError("Argument(s) must be positive: ")
        raise TypeError('Argument(s) provided should not be string')
    raise AttributeError("Argument(s) not provided")


def trapezoidal(f: callable, start: (int, float), end: (int, float), partitions: int) -> float:
    if dim_validate3(start) and dim_validate3(end) and dim_validate3(partitions):
        if dim_validate2(start) and dim_validate2(end) and dim_validate2(partitions):
            if dim_validate1(partitions):
                x0, x1 = start, end
                width = (x1 - x0)/partitions
                sum = 0
                for i in range(0, partitions):
                    sum += (f(x0) + f(x0+width))*width/2
                    x0 += width
                return sum
            else:
                raise ValueError("Argument(s) must be positive: ")
        raise TypeError('Argument(s) provided should not be string')
    raise AttributeError("Argument(s) not provided")


def simpson(f: callable, start: (int, float), end: (int, float), partitions: int) -> float:
    if dim_validate3(start) and dim_validate3(end) and dim_validate3(partitions):
        if dim_validate2(start) and dim_validate2(end) and dim_validate2(partitions):
            if dim_validate1(partitions):
                    if dim_validate4(partitions):
                        x0, x1 = start, end
                        width = (x1-x0)/partitions
                        interval = int(partitions/2)
                        sum = f(x0)+f(x1)
                        x = x0 + width
                        for i in range(1, interval+1):
                            sum += 4*f(x)
                            x += 2*width
                        x = x0 + 2*width
                        for i in range(1, interval):
                            sum += 2*f(x)
                            x += 2*width
                        return width/3*sum
                    else:
                        raise TypeError("The argument must be even")
            raise ValueError("Argument(s) must be positive: ")
        raise TypeError('Argument(s) provided should not be string')
    raise AttributeError("Argument(s) not provided")


if __name__ == "__main__":
    def f(x):
        return cos(x) + sin(x)
    print("SECANT METHOD")
    print("a) ", secant_method(f, pi/2, 3*pi/2, 1e-6))
    print("b) ", secant_method(f, -pi/2, pi/2, 1e-6))

    def f(x):
        return x**3
    print("c) ", secant_method(f, 5, 6, 1e-9))

    def f(x):
        return x**2-2
    print("d)", secant_method(f, -3, 0, 0.00006))

    print("MIDPOINT METHOD")

    def f(x):
        return x**2-1
    print("a)", midpoint(f, -2, 2, 10))
    print("b)", midpoint(f, -2, 2, 10000))

    def f(x):
        return 1/x
    print("c)", midpoint(f, -0.1, 2.0, 100))

    def f(x):
            return sin(x)
    print("d)", midpoint(f, 0, pi/2, 1000))

    print("TRAPEZOID METHOD")

    def f(x):
        return x**2-1
    print("a)", trapezoidal(f, -2, 2, 10))
    print("b)", trapezoidal(f, -2, 2, 10000))

    def f(x):
        return 1/x
    print("c)", trapezoidal(f, -0.1, 2.0, 100))

    def f(x):
            return sin(x)
    print("d)", trapezoidal(f, 0, pi/2, 1000))

    print("SIMPSON METHOD")

    def f(x):
        return x**2-1
    print("a)", simpson(f, -2, 2, 10))
    print("b)", simpson(f, -2, 2, 10000))

    def f(x):
        return 1/x
    print("c)", simpson(f, -0.1, 2.0, 100))

    def f(x):
            return sin(x)
    print("d)", simpson(f, 0, pi/2, 1000))
    #print(trapezoidal(f, 1, 2, 6))
    #print(simpson(f, 0, 1, 11))
    #print(cos(0.75*pi)+sin(0.75*pi))