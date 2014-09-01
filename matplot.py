__author__ = 'stephen'
from pylab import *
from geom_formulae import *


def rectangle_area_plot_props(start, end):
    """
    Plot the area of the rectangle as a function of length,
    with length from start to end. The width is fixed to 5 units.
    @param start: starting value.  should be less than end.
    @param end: end value.  should be greater than start.
    @return: None.  Produces a plot.
        """
    v_rectangle_area = np.vectorize(rectangle_area)
    length = np.linspace(start, end)  # length of rectangle
    width = 5  # fixed width of rectangle
    area = v_rectangle_area(length, width)  # the areas
    plot(length, area, '-r', label="Area")
    xlabel('Rectangle length, width=5')
    ylabel('geo values')
    title('Rectangle Area Geo Properties')
    legend(loc='upper right')
    show()
    pass


def solid_cone_surface_area_plot_props(start, end):
    """
    Plots the surface area of a solid cone as a function of radius,
    with radius from start to end. The slant_height is fixed to 10 units.
    @param start: starting value.  should be less than end.
    @param end: end value.  should be greater than start.
    @return: None.  Produces a plot.
        """
    v_solid_cone_surface_area = np.vectorize(solid_cone_surface_area)
    radius = np.linspace(start, end)  # base radius of the cone
    slant_height = 10  # slant height of the cone
    surface_area = v_solid_cone_surface_area(radius, slant_height)  # the areas
    plot(radius, surface_area, '-b', label="Surface area")
    xlabel('Solid cone radius, slant_height=10')
    ylabel('geo values')
    title('Solid Cone Surface Area Geo Properties')
    legend(loc='upper right')
    show()
    pass


def sphere_volume_plot_props(start, end):
    """
    Plots the volume of a sphere as a function of radius,
    with radius from start to end.
    @param start: starting value.  should be less than end.
    @param end: end value.  should be greater than start.
    @return: None.  Produces a plot.
        """
    v_sphere_volume = np.vectorize(sphere_volume)
    radius = np.linspace(start, end)  # radius of the sphere
    volume = v_sphere_volume(radius)  # the volumes
    plot(radius, volume, '-b', label="Volume")
    xlabel('Radius of the sphere')
    ylabel('geo values')
    title('Sphere Volume Area Geo Properties')
    legend(loc='upper right')
    show()
    pass


def circle_area_plot_props(start, end):
    """
    Plots the area of a circle as a function of radius,
    with radius from start to end.
    @param start: starting value.  should be less than end.
    @param end: end value.  should be greater than start.
    @return: None.  Produces a plot.
        """
    v_circle_area = np.vectorize(circle_area)
    radius = np.linspace(start, end)  # radius of the circle
    area = v_circle_area(radius)  # the areas
    plot(radius, area, ':r', label="Area")
    xlabel('Radius of the circle')
    ylabel('geo values')
    title('Circle Area Geo Properties')
    legend(loc='upper right')
    show()
    pass


if __name__ == "__main__":
    rectangle_area_plot_props(0, 10)
    solid_cone_surface_area_plot_props(0, 10)
    sphere_volume_plot_props(0, 10)
    circle_area_plot_props(0, 10)