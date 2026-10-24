# This is the anchor of this module: [[trigonometry-anchor|trigonometry.py]]

import math

from .. import validators as vls


# Sine function anchor: [[sine-anchor|sine]]
#* Calculates the sine of an angle in degrees
def sine(angle):
    
    vls.real_validate()(angle, name="angle")
    return math.sin(math.radians(angle))

# Cosine function anchor: [[cosine-anchor|cosine]]
#* Calculates the cosine of an angle in degrees
def cosine(angle):
    
    vls.real_validate()(angle, name="angle")
    return math.cos(math.radians(angle))

# Asine function anchor [[asine-anchor|asine]]
#* Calculates the asine of a value
def asine(value):
    
    vls.real_validate()(value, name="value")
    return math.degrees(math.asin(value))