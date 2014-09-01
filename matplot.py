__author__ = 'stephen'
from pylab import *
from geom_formulae import *
#------------------------------Plot#1------------------------------------


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
#------------------------------Plot#2------------------------------------


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
#------------------------------Plot#3------------------------------------


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
#------------------------------Plot#4------------------------------------


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
#------------------------------Plot#5------------------------------------


def triangle_area_plot_props(start, end):
    """
    Plot the area of the triangle as a function of its base,
    with base from start to end. The height is fixed to 10 units.
    @param start: starting value.  should be less than end.
    @param end: end value.  should be greater than start.
    @return: None.  Produces a plot.
        """
    v_triangle_area = np.vectorize(triangle_area)
    base = np.linspace(start, end)  # base of triangle
    height = 10  # fixed height of triangle
    area = v_triangle_area(base=base, height=height)  # the areas
    plot(base, area, '-b', label="Area")
    xlabel('Triangle base, height=10')
    ylabel('geo values')
    title('Triangle Area Geo Properties')
    legend(loc='upper right')
    show()
    pass
#------------------------------Plot#6------------------------------------


def cuboid_volume_plot_props(start, end):
    """
    Plot the volume of the cuboid as a function of its length,
    with length from start to end. The width and height are fixed
    to 5 and 10 units respectively.
    @param start: starting value.  should be less than end.
    @param end: end value.  should be greater than start.
    @return: None.  Produces a plot.
        """
    v_cuboid_volume = np.vectorize(cuboid_volume)
    length = np.linspace(start, end)  # length of cuboid
    width = 5  # fixed width of the cuboid
    height = 10  # fixed height of the cuboid
    volume = v_cuboid_volume(length, width, height)  # the volumes
    plot(length, volume, '-b', label="Volume")
    xlabel('Cuboid length, width=5, height=10')
    ylabel('geo values')
    title('Cuboid Volume Geo Properties')
    legend(loc='upper right')
    show()
    pass
#------------------------------Plot#7------------------------------------


def cube_surface_area_plot_props(start, end):
    """
    Plots the surface area of a cube as a function of side,
    with side from start to end.
    @param start: starting value.  should be less than end.
    @param end: end value.  should be greater than start.
    @return: None.  Produces a plot.
        """
    v_cube_surface_area = np.vectorize(cube_surface_area)
    side = np.linspace(start, end)  # length of the cube
    surface_area = v_cube_surface_area(side)  # the surface areas
    plot(side, surface_area, ':h', label="Surface area")
    xlabel('Side of the cube')
    ylabel('geo values')
    title('Cube Surface Area Geo Properties')
    legend(loc='upper right')
    show()
    pass
#------------------------------Plot#8------------------------------------


def semi_circle_perimeter_plot_props(start, end):
    """
    Plots the perimeter of a semi circle as a function of radius,
    with radius from start to end.
    @param start: starting value.  should be less than end.
    @param end: end value.  should be greater than start.
    @return: None.  Produces a plot.
        """
    v_semi_circle_perimeter = np.vectorize(semi_circle_perimeter)
    radius = np.linspace(start, end)  # radius of the semi circle
    perimeter = v_semi_circle_perimeter(radius)  # the perimeters
    plot(radius, perimeter, '-b', label="Perimeter")
    xlabel('Radius of the semi circle')
    ylabel('geo values')
    title('Semi Circle Perimeter Geo Properties')
    legend(loc='upper right')
    show()
    pass
#------------------------------Plot#9------------------------------------


def trapezium_area_plot_props(start, end):
    """
    Plot the area of a trapezium as a function of its height,
    with height from start to end. The parallel_sides are fixed to 20
    and 10 units respectively.
    @param start: starting value.  should be less than end.
    @param end: end value.  should be greater than start.
    @return: None.  Produces a plot.
    """
    v_trapezium_area = np.vectorize(trapezium_area)
    height = np.linspace(start, end)  # height of a trapezium
    parallel_side_1 = 20  # parallel side of a trapezium
    parallel_side_2 = 10  # parallel side of a trapezium
    area = v_trapezium_area(parallel_side_1, parallel_side_2, height)  # the areas
    plot(height, area, '-b', label="Area")
    xlabel('Trapezium height, parallel_side_1=20, parallel_side_2=10')
    ylabel('geo values')
    title('Trapezium area Geo Properties')
    legend(loc='upper right')
    show()
    pass
#------------------------------Plot#10-----------------------------------


def regular_pyramid_volume_plot_props(start, end):
    """
    Plot the volume of a regular pyramid as a function of its height,
    with height from start to end. The base_length and base_width are fixed
    to 20 and 10 units respectively.
    @param start: starting value.  should be less than end.
    @param end: end value.  should be greater than start.
    @return: None.  Produces a plot.
        """
    v_regular_pyramid_volume = np.vectorize(regular_pyramid_volume)
    height = np.linspace(start, end)  # height of the pyramid
    base_length = 20  # fixed base length of the pyramid
    base_width = 10  # fixed base width of the pyramid
    volume = v_regular_pyramid_volume(base_length, base_width, height)  # the volumes
    plot(height, volume, '-b', label="Volume")
    xlabel('Regular pyramid height, base length=20, base_width=10')
    ylabel('geo values')
    title('Regular Pyramid Volume Geo Properties')
    legend(loc='upper right')
    show()
    pass
#------------------------------Plot#11-----------------------------------


def ellipsoid_volume_plot_props(start, end):
    """
    Plot the volume of an ellipsoid as a function of its vertical_axis,
    with vertical_axis from start to end. The major_axis and minor_axis are fixed
    to 20 and 10 units respectively.
    @param start: starting value.  should be less than end.
    @param end: end value.  should be greater than start.
    @return: None.  Produces a plot.
        """
    v_ellipsoid_volume = np.vectorize(ellipsoid_volume)
    vertical_axis = np.linspace(start, end)  # height of the pyramid
    major_axis = 20  # fixed base length of the pyramid
    minor_axis = 10  # fixed base width of the pyramid
    volume = v_ellipsoid_volume(major_axis, minor_axis, vertical_axis)  # the volumes
    plot(vertical_axis, volume, '-h', label="Volume")
    xlabel('Ellipsoid vertical_axis, major_axis=20, minor_axis=10')
    ylabel('geo values')
    title('Ellipsoid Volume Geo Properties')
    legend(loc='upper right')
    show()
    pass
#=========================================================================


if __name__ == "__main__":
    rectangle_area_plot_props(0, 10)
    solid_cone_surface_area_plot_props(0, 10)
    sphere_volume_plot_props(0, 10)
    circle_area_plot_props(0, 10)
    triangle_area_plot_props(0, 10)
    cuboid_volume_plot_props(0, 10)
    cube_surface_area_plot_props(0, 10)
    semi_circle_perimeter_plot_props(0, 10)
    trapezium_area_plot_props(0, 10)
    regular_pyramid_volume_plot_props(0, 10)
    ellipsoid_volume_plot_props(0, 10)
#========================================END=================================