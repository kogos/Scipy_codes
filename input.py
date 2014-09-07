__author__ = 'stephen'
from object_task import *
"""
#def f(shape, length, width):
#=['rectangle', '5', '4']
a = ['', '', '']

a[0] = input("Enter the shape")
a[1] = input("Enter the length")
a[2] = input("Enter the width")
a[0] = str.capitalize(a[0])
a[1] = float(a[1])
a[2] = float(a[2])
c = 'a[1], a[2]'
#b = {'a[0]': c}
#print(type(b))
#print(a[0])
#print(b['a[0]'])

#print(a[1]+a[2])

#length = int(a[1])
#width = int(a[2])
#area = length * width
#print(area)
"""
#print(dic[a[0]])
if __name__ == "__main__":
    a = ['', '', '']
    a[0] = input("Enter the shape")
    a[1] = input("Enter the length")
    a[2] = input("Enter the width")
    a[0] = str.capitalize(a[0])
    a[1] = float(a[1])
    a[2] = float(a[2])
    c = 'a[1], a[2]'
    rectangle = a[0](a[1], a[2])
    print(rectangle)
    rectangle.draw()