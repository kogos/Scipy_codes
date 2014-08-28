__author__ = 'stephen'
print("Hello world")
#print("This is not what i needed")
print("Hello Ghana")
print("This is not easy")
#---------Declaring Variables-------
text=("Student name")
#---------List--------

#---------DeclaringFunctions--------
def prime(a,b):
    for x in range(a,b):
        if all(x%i!=0 for i in range(2,x)):
            print(x)
#---------Printing variables--------
print(text)
#---------Calling functions--------
prime(2,100)
