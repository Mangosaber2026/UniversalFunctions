from math import (
    radians,
    degrees,
    sin,
    cos,
    asin,
)
from numbers import Real
from .Validators.QuantumFuncValidators import qtm_validation_decorator


@qtm_validation_decorator
def sine(angle: Real) -> Real:
    """
    Calculates the sine of a given angle
    :param angle: value required in degrees
    :return: sine value
    """
    return sin(radians(angle))

@qtm_validation_decorator
def cosine(angle: Real) -> Real:
    """
    Calculates the cosine of a given angle
    :param angle: value required in degrees
    :return: cosine value
    """
    return cos(radians(angle))

@qtm_validation_decorator
def asine(angle: Real) -> Real:
    """
    Calculates the asine of a given angle
    :param angle: real value
    :return: asine value
    """
    return degrees(asin(angle))