__author__ = 'stephen'
from pylab import *

from geom_formulae import *

v_rectangle_area = np.vectorize(rectangle_area)
#v_square_perimeter = np.vectorize(rectangle_area)

S = np.linspace(0, 10)  # length of rectangle
B = 5  # fixed width of rectangle

A = v_rectangle_area(S, B)  # the areas
#P = v_square_perimeter(S)  # the perimeters

plot(S, A, '-r', label="Area")
#plot(S, P, ':b', label="Perimeter")

xlabel('rectangle length, width=5')
ylabel('geo values')
title('Rectangle Geo Properties')
legend(loc='upper right')
show()
"""


from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
v_rectangle_area = np.vectorize(rectangle_area)
# An array of radii
# Does not include radius r=0, this is to eliminate duplicate points
L = np.linspace(0, 10)

# An array of angles
B = np.linspace(0, 10)

B = np.repeat(B, 10, axis=1)
A = v_rectangle_area(L, B)


fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot_trisurf(L, B, A, cmap=cm.jet, linewidth=0.2)

plt.show()


show()

v_solid_cone_surface_area = np.vectorize(solid_cone_surface_area)
#v_square_perimeter = np.vectorize(square_perimeter)

S = np.linspace(0,10) # our side lengths

A = v_solid_cone_surface_area(S,S)  # the areas
#P = v_square_perimeter(S)  # the perimeters

plot(S, A, '-r', label="Area")
#plot(S, P, ':b', label="Perimeter")

xlabel('side length')
ylabel('geo values')
title('Square Geo Properties')
legend(loc='upper right')

show()
"""
