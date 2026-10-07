"""
This module contains a collection of trigonometric functions to be used with degrees.
"""

from math import (
    radians,
    degrees,
    sin,
    cos,
    asin,
)
from numbers import Real
from .Validators import real_validate


def sine(angle: Real) -> Real:
    """
    Calculates the sine of a given angle

    >>> sin(0)
    0

    :param angle: value required in degrees
    :return: sine value
    """
    real_validate()(angle, name="angle")
    return sin(radians(angle))

def cosine(angle: Real) -> Real:
    """
    Calculates the cosine of a given angle

    >>> cosine(0)
    1

    :param angle: value required in degrees
    :return: cosine value
    """
    real_validate()(angle, name="angle")
    return cos(radians(angle))

def asine(value: Real) -> Real:
    """
    Calculates the asine of a given angle

    >>> asine(0)
    0

    :param value: real value
    :return: asine value
    """
    real_validate()(value, name="value")
    return degrees(asin(value))