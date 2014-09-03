__author__ = 'stephen'
from numpy import *
#print(sin(pi/2))
#f = input("enter the function")
#guess1 = input("Enter first guess")
#guess2 = input("Enter second guess")
#err = input("Define your error")

def secant(f, guess1, guess2, err=1e-3):
    y0 = f(guess1)
    y1 = f(guess2)
    y=5
    while y > err:
        x = guess2-(guess2 - guess1)*y1/(y1-y0)
        y = f(x)
        #trial = (guess2-guess1)**2
        guess1 = guess2
        y0 = y1
        guess2 = x
        y1 = y
    return x
print(secant(sin, 0.1, (2*pi), 0.005))



"""
% makes the output more compact
% Solves f(x) = 0 by doing n steps of the secant method
% starting with x0 and x1.
% Inputs: f -- the function , input as an inline function
% x0 -- starting guess , a number
% x1 -- second starting geuss
% n -- the number of steps to do
% Output: x -- the approximate solution
y0 = f(x0);
y1 = f(x1);
for
i = 1:n
% Do n times
x = x1 - (x1-x0)*y1/(y1-y0)
% secant formula.
y=f(x)
% y value at the new approximate solution.
% Move numbers to get ready for the next step
x0=x1;
y0=y1;
x1=x;
y1=y;
end
"""