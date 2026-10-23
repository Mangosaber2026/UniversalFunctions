import math

from .. import validators as vls


def sine(angle):
    
    vls.real_validate()(angle, name="angle")
    return math.sin(math.radians(angle))

def cosine(angle):
    
    vls.real_validate()(angle, name="angle")
    return math.cos(math.radians(angle))

def asine(value):
    
    vls.real_validate()(value, name="value")
    return math.degrees(math.asin(value))