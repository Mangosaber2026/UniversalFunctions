"""
This module contains a collection of trigonometric functions to be used with degrees.
"""

from math import (
    asin,
    cos,
    degrees,
    radians,
    sin,
)
from numbers import Real

from .. import validators as vls


def sine(angle: Real) -> Real:
    """
    Calculates the sine of a given angle

    >>> sin(0)
    0

    :param angle: value required in degrees
    :return: sine value
    """
    vls.real_validate()(angle, name="angle")
    return sin(radians(angle))

def cosine(angle: Real) -> Real:
    """
    Calculates the cosine of a given angle

    >>> cosine(0)
    1

    :param angle: value required in degrees
    :return: cosine value
    """
    vls.real_validate()(angle, name="angle")
    return cos(radians(angle))

def asine(value: Real) -> Real:
    """
    Calculates the asine of a given angle

    >>> asine(0)
    0

    :param value: real value
    :return: asine value
    """
    vls.real_validate()(value, name="value")
    return degrees(asin(value))