__author__ = 'stephen'
from numpy import *
print("Welcome to shapes and solids")
Shapes = ['Rectangle', 'Circle', 'Trapezium', 'Triangle', 'Semicircle']
Solids = ['Sphere', 'Cube', 'Cuboid', 'Cone', 'Ellipsoid', 'Pyramid']
Options = ['Solids', 'Shapes', 'Quit']
#print("Choose a class")
#option = input()
#option = str.capitalize(option)


try:
    option = 'sr'
except (TypeError, ValueError) as err:
        print(err.args[0])
else:
    while option not in Options:
        print("You can try 'solids', 'shapes', or Quit to exist the system")
        print("Choose a class")
        try:
           option = input()
           option = str.capitalize(option)
        except (TypeError, ValueError) as err:
            print(err.args[0])
        else:
            print("you have chosen: "+str(option))
            if option == 'Shapes':

                #print("Choose a shape")
                option2 = 'sav'
                option2 = str.capitalize(option2)
                while option2 not in Shapes:
                    print("Choose a shape")
                    try:
                       option2 = input()
                       option2 = str.capitalize(option2)
                       if option2 == 'Circle':
                           radius = float(input("Enter radius: "))
                           area = pi * (radius**2)
                           print("Area: "+str(area)+" ; radius: "+str(radius))
                       else:
                           print(str(option2)+" is not recognized as a shape, please try"+str(Shapes))
                    except (TypeError, ValueError) as err:
                        print(err.args[0])
                    else:
                        option = 'sr'
            elif option == 'Solids':
                option2 = 'sav'
                option2 = str.capitalize(option2)
                while option2 not in Solids:
                    print("Choose a solid")
                    try:
                       option2 = input()
                       option2 = str.capitalize(option2)
                       if option2 == 'Cube':
                           side = float(input("Enter side: "))
                           surface_area = side*side*6
                           print("Surface rea: "+str(surface_area)+" : side: "+str(side))
                       else:
                           print("Choose the correct solid")
                    except (TypeError, ValueError) as err:
                            print(err.args[0])
                    else:
                        option = 'sr'
            else:
                print("Thank you for trying shapes and solids")
