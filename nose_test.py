__author__ = 'stephen'
from geom_formulae import *


eps = 1e-6


def test_rectangle_area_float():
    assert 100 - eps < rectangle_area(10, 10) < 100 + eps
    assert 20 - eps < rectangle_area(5, 4) < 20 + eps


def test_solid_cone_surface_area_int():
    assert solid_cone_surface_area(4, 9) == 163.36281798666926


def test_sphere_volume_int():
    assert sphere_volume(7) == 1436.755040241732


def test_circle_area_int():
    assert circle_area(14) == 615.7521601035994


def test_triangle_area_int():
    assert triangle_area(side_a=3, side_b=4, side_c=5) == 6
    assert triangle_area(base=10, height=3) == 15
    assert triangle_area(angle_theta=pi/2, side_a=4, side_b=3) == 6


def test_cuboid_volume_int():
    assert cuboid_volume(5, 6, 10) == 300


def test_cube_surface_area_int():
    assert cube_surface_area(5) == 150


def test_semi_circle_perimeter_int():
    assert semi_circle_perimeter(radius=7) == semi_circle_perimeter(diameter=14)
    assert semi_circle_area(radius=7) > semi_circle_perimeter(radius=7)


def test_trapezium_area_double():
    assert 400.0-eps < trapezium_area(30, 10, 20) < 400.0 + eps


def test_regular_pyramid_volume_int():
    assert regular_pyramid_volume(3, 4, 7) == 28


def test_ellipsoid_volume_int():
    assert ellipsoid_volume(8,5,3) == 502.65482457436684