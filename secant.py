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