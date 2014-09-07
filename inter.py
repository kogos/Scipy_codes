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
        print("You can try 'solids', 'shapes', or 'Quit' to exit the system.")
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
                           perimeter = pi * radius * 2
                           print(str(option2)+", area: "+str(area)+"; perimeter: "+str(perimeter)+
                                 " ; radius: "+str(radius))
                       elif option2 == 'Semicircle':
                           radius = float(input("Enter radius: "))
                           area = pi * (radius**2) / 2
                           perimeter = (pi * radius) + 2 * radius
                           print(str(option2)+", area: "+str(area)+"; perimeter: "+str(perimeter)+
                                 " ; radius: "+str(radius))
                       elif option2 == 'Rectangle':
                           length = float(input("Enter the length: "))
                           width = float(input("Enter the width: "))
                           area = length * width
                           perimeter = (length + width) * 2
                           print(str(option2)+", area: "+str(area)+"; perimeter: "+str(perimeter)+" ; length: "
                                 +str(length)+" ; width: "+str(width))
                       elif option2 == 'Triangle':
                           side_a = float(input("Enter the side_a: "))
                           side_b = float(input("Enter the side_b: "))
                           side_c = float(input("Enter the side_c: "))
                           s = (side_a + side_b + side_c) / 2
                           area = sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))
                           perimeter = side_a + side_b + side_c
                           print(str(option2)+", area: "+str(area)+"; perimeter: "+str(perimeter)+" ; side_a: "
                                 +str(side_a)+" ; side_b: "+str(side_b)+" ; side_c: "+str(side_c))
                       elif option2 == 'Trapezium':
                           parallel_side1 = float(input("Enter the parallel_side1: "))
                           parallel_side2 = float(input("Enter the parallel_side2: "))
                           slant_height1 = float(input("Enter the slant_height1: "))
                           slant_height2 = float(input("Enter the slant_height2: "))
                           height = float(input("Enter the height: "))
                           area = (parallel_side1 + parallel_side2) * height/2
                           perimeter = parallel_side1 + parallel_side2 + slant_height1 + slant_height2
                           print(str(option2)+", area: "+str(area)+"; perimeter: "+str(perimeter)+" ; parallel_side1: "
                                 +str(parallel_side1)+" ; parallel_side2: "+str(parallel_side2)+" ; slant_height1: "
                                 +str(slant_height1)+" ; slant_height2: "+str(slant_height2)+" ; height: "+str(height))
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
                           surface_area = (side**2)*6
                           volume = side**3
                           print(str(option2)+", Surface area: "+str(surface_area)+" ;Volume: "+str(volume)
                                 +" : side: "+str(side))
                       elif option2 == 'Sphere':
                           radius = float(input("Enter radius: "))
                           surface_area = 4*pi*(radius**2)
                           volume = 4*pi*(radius**3)/3
                           print(str(option2)+", surface area: "+str(surface_area)+"; volume: "+str(volume)+
                                 " ; radius: "+str(radius))

                       elif option2 == 'Cone':
                           radius = float(input("Enter radius: "))
                           slant_height = float(input("Enter slant_height: "))
                           surface_area = pi * radius * (radius+slant_height)
                           volume = pi * (radius**2)*slant_height/3
                           print(str(option2)+", surface area: "+str(surface_area)+"; volume: "+str(volume)+
                                 " ; radius: "+str(radius)+" ; slant_height: "+str(slant_height))
                       elif option2 == 'Cuboid':
                           length = float(input("Enter length: "))
                           width = float(input("Enter width: "))
                           height = float(input("Enter height: "))
                           surface_area = ((length * width)*2)+((length * height)*2)+((height * width)*2)
                           volume = length * width * height
                           print(str(option2)+", Surface area: "+str(surface_area)+" ;Volume: "+str(volume)
                                 +" : length: "+str(length)+" : width: "+str(width)+" : height: "+str(height))
                       elif option2 == 'Ellipsoid':
                           major_axis = float(input("Enter major_axis: "))
                           minor_axis = float(input("Enter minor_axis: "))
                           vertical_axis = float(input("Enter vertical_axis: "))
                           surface_area = 4*pi*(((((major_axis * minor_axis)**1.6075)+
                                         ((major_axis * vertical_axis)**1.6075)+
                                         ((minor_axis * vertical_axis)**1.6075))/3)**(1/1.6075))
                           volume = major_axis * minor_axis * vertical_axis
                           print(str(option2)+", Surface area: "+str(surface_area)+" ;Volume: "+str(volume)
                                 +" : major_axis: "+str(major_axis)+" : minor_axis: "+str(minor_axis)+
                                 " : vertical_axis: "+str(vertical_axis))
                       elif option2 == 'Pyramid':
                           base_length = float(input("Enter base_length: "))
                           base_width = float(input("Enter base_width: "))
                           height = float(input("Enter height: "))
                           slant_height1 = sqrt((height**2)+((0.5*base_length)**2))
                           slant_height2 = sqrt((height**2)+((0.5*base_width)**2))
                           surface_area = (base_length * base_width) + (base_length * slant_height2) + \
                                          (base_width * slant_height1)
                           volume = base_length * base_width * height / 3
                           print(str(option2)+", Surface area: "+str(surface_area)+" ;Volume: "+str(volume)
                                 +" : base_length: "+str(base_length)+" : base_width: "+str(base_width)+
                                 " : height: "+str(height))
                       else:
                           print(str(option2)+" is not recognized as a solid, please try"+str(Solids))
                    except (TypeError, ValueError) as err:
                            print(err.args[0])
                    else:
                        option = 'sr'
            elif option == 'Quit':
                print("Thank you for trying shapes and solids")
            else:
                option = 'sr'

