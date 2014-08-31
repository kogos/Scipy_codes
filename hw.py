__author__ = 'stephen'
from numpy import *
#---------DECLARING VARIABLES-------
text = "Student name" # string variable
star = "Hello Ghana"
y=50#Numeric variable
x=20
print(text)#printing contents of variables(text)
print(star)
print(x+y)
#---------DECLARING FUNCTIONS--------
#Prime numbers
def prime(a,b):
    print("The prime numbers between ",a," and ",b," are:")
    for x in range(a,b):
        if all(x%i!=0 for i in range(2,x)):
            print(x)
prime(2,50)#Calling the prime function
#Equation of a line
def straightline(x1,x2,y1,y2,c):
    m=((y2-y1)/(x2-x1))
    print("Equation: y=",m,"x +",c)
straightline(2.4,1,8,5,2.8)#Calling the straightline function
#Area of a triangle
def triangle(a,b,c):
    s=(a+b+c)/2
    area=sqrt(s*(s-a)*(s-b)*(s-c))
    print("The area of the triangle is: ",area,"sq. units")
triangle(5,12,13)
#Getting roots of a quadratic equation
def roots(a,b,c):
    root1=((-b+0j)+(sqrt((b+0j)*(b+0j)-4*(a+0j)*(c+0j))))/2*(a+0j)
    root2=((-b+0j)-(sqrt((b+0j)*(b+0j)-4*(a+0j)*(c+0j))))/2*(a+0j)
    print(("Root1= "),root1)
    print(("Root2= "),root2)
roots(1,3,2)
#---------LISTS-----------------------
listdata=["numbers","functions","variables"]
print(listdata[2]) #Indexing starts at zero, element[1] is in position 2.
#-------MATRICES----------------------
a=matrix('2,3;4,6')#Defining a matrix
b = matrix ( '3,7;4,8')
print(a)
print(b+a) # Adding matrices and printing the output
#============END===============
import geom_formulae
print(geom_formulae.circle_area(2))

import turtle

side = 50

i = 0;
while (i < 4):
    turtle.forward(side)
    turtle.left(90)
    i = i+1

turtle.done()