__author__ = 'stephen'
from geom_formulae import *
from nose.tools import *


eps = 1e-6


@raises(TypeError)
def test_rectangle_area_type():
    rectangle_area("a string")


@raises(ValueError)
def test_rectangle_area_value():
    rectangle_area(6, -9)


@raises(TypeError)
def test_solid_cone_surface_area_type():
    solid_cone_surface_area("fds")


@raises(ValueError)
def test_solid_cone_surface_area_value():
    solid_cone_surface_area(-8, 3)


@raises(ValueError)
def test_sphere_volume_value():
    sphere_volume(-9)


@raises(TypeError)
def test_sphere_volume_value():
    sphere_volume("ddr")


@raises(ValueError)
def test_circle_area_value():
    circle_area(-89)


@raises(TypeError)
def test_circle_area_value():
    circle_area("jh")


@raises(ValueError)
def test_triangle_area_int():
    assert triangle_area(base=10, height=3) == 15
    triangle_area(-9, 5)


@raises(TypeError)
def test_triangle_area_value():
    triangle_area("dd", "ggh")


@raises(AttributeError)
def test_triangle_area_attr():
    triangle_area(None, 4)


@raises(ValueError)
def test_cuboid_volume_int():
    assert cuboid_volume(5, 6, 10) == 300
    cuboid_volume(5, 6, -10)


@raises(TypeError)
def test_cuboid_volume_type():
    cuboid_volume(5, 6, "dds")


@raises(AttributeError)
def test_cuboid_volume_attr():
    cuboid_volume(5, 6, None)


@raises(ValueError)
def test_cube_surface_area_int():
    assert cube_surface_area(5) == 150
    cube_surface_area(-8)


@raises(TypeError)
def test_cube_surface_area_type():
    cube_surface_area("kl")


@raises(ValueError)
def test_semi_circle_perimeter_int():
    assert semi_circle_perimeter(radius=7) == semi_circle_perimeter(diameter=14)
    assert semi_circle_area(radius=7) > semi_circle_perimeter(radius=7)
    semi_circle_perimeter(radius=-8)
    semi_circle_area(radius=-15)


@raises(TypeError)
def test_semi_circle_perimeter_type():
    semi_circle_perimeter(radius="hgfg")
    semi_circle_area(radius="hghh")


@raises(ValueError)
def test_trapezium_area_value():
    assert 400.0-eps < trapezium_area(30, 10, 20) < 400.0 + eps
    trapezium_area(45, -5, -98)


@raises(TypeError)
def test_trapezium_area_type():
    trapezium_area("hjkd", -5, "khjkd")


@raises(AttributeError)
def test_trapezium_area_attr():
    trapezium_area(None, 5, None)


@raises(ValueError)
def test_regular_pyramid_volume_int():
    assert regular_pyramid_volume(3, 4, 7) == 28
    regular_pyramid_volume(9, 4, -10)


@raises(TypeError)
def test_regular_pyramid_volume_type():
    regular_pyramid_volume(9, 4, "jkhds")


@raises(AttributeError)
def test_regular_pyramid_volume_attr():
    regular_pyramid_volume(9, 4, None)


@raises(ValueError)
def test_ellipsoid_volume_value():
    assert ellipsoid_volume(8, 5, 3) == 502.65482457436684
    ellipsoid_volume(5, 4, -8)


@raises(TypeError)
def test_ellipsoid_volume_type():
    ellipsoid_volume(5, 4, "jhads")


@raises(AttributeError)
def test_ellipsoid_volume_attr():
    ellipsoid_volume(None, 4, None)