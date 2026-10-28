"""
This module contains a collection of trigonometric functions to be used with degrees.
"""
 #* 📝 File type: Python type stub (.pyi)
 #* 📝 Purpose: Describes the module's interface for documentation,
 #* 📝         editor support, and static type checking.
 #* 📝 Runtime: Contains no implementation; see the corresponding
 #* 📝         .py file for executable code.

import numbers as num  # noqa: I001


#* 📝 Type for any real number
type RealType = float | int | num.Real


def sine(angle: RealType) -> RealType:
    """
    Calculates the sine of a given angle.

    >>> sine(0)
    0

    :param angle: value required in degrees

    :return: sine value
    """


def cosine(angle: RealType) -> RealType:
    """
    Calculates the cosine of a given angle.

    >>> cosine(0)
    1

    :param angle: value required in degrees

    :return: cosine value
    """


def tangent(angle: RealType) -> RealType:
    """
    Calculates the tangent of a given angle.

    >>> tangent(0)
    0

    :param angle: value required in degrees

    :return: tangent value
    """


def asine(value: RealType) -> RealType:
    """
    Calculates the asine of a given angle.

    >>> asine(0)
    0

    :param value: real value

    :return: asine value
    """