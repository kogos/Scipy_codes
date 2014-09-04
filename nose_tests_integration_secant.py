__author__ = 'stephen'
from integration import *
from nose.tools import *


eps = 1e-6


@raises(TypeError)
def test_midpoint_type():
        midpoint(f, -2, 2, "ssr")


@raises(ValueError)
def test_midpoint_type():
        midpoint(f, 0, 2, -4)

@raises(ValueError)
def test_midpoint_attr():
        midpoint(f, None, 2, -4)