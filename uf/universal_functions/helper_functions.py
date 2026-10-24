# Anchor for this module: [[helper-functions-anchor|helper_functions.py]]

import math
import numbers as num

from .. import validators as vls
from . import classes_to_dictionary as cls_to_dict
from . import decorator_archive as dec_arc
from . import get_variable as gv


# HelperFunctions anchor: [[HelperFunctions-anchor|HelperFunctions]]
#* Contains helper functions which make getting certain values easier for the user
@dec_arc.cls_deco_superposition(staticmethod)
class HelperFunctions:

    def intervals_f():

        interval_num: float = gv.get_num(float, "Enter intervals(ℚ>0): ", MIN=0)
        return interval_num

    def length_float():

        length: float = gv.get_num(float, "Enter side length(ℚ>0): ", MIN=0)
        return length

    def radius_float():

        radius: float = gv.get_num(float, "Enter radius(ℚ>0): ", MIN=0)
        return radius

    def object_num():

        object_count: int = gv.get_num(int, "Enter object count(ℕ≥1): ", MIN=1)
        return object_count

    def sides_num():
        
        sides: int = gv.get_num(int, "Enter sides count(ℕ≥3): ", MIN=3)
        return sides

    def row_num():
        
        row_count: int = gv.get_num(int, "Enter row count(ℕ≥1): ", MIN=1)
        return row_count

    def row_pair():
        
        row_count: int = gv.get_num(int, "Enter row pairs count(ℕ≥1): ", MIN=1)
        return row_count

    def diameter_sq(length):
        
        vls.ComboValidate(length, name="length")(
            vls.real_validate(),
            vls.Positive()
        )

        diameter: float = length*math.sqrt(2); d_half: num.Real = diameter / 2
        return diameter, d_half

    def x_ft():
        
        x_val: float = gv.get_num(float, "Enter x value: ")
        return x_val

    def y_ft():
        
        y_val: float = gv.get_num(float, "Enter y value: ")
        return y_val

    def list_helperfunctions():

        return cls_to_dict.classes_to_dict(HelperFunctions)

# helper anchor: [[helper-anchor|helper]]
#* Another name for [[#HelperFunctions-anchor|HelperFunctions]] to make it shorter
helper = HelperFunctions

# range_f anchor: [[range-f-anchor|range_f]]
#* Similar to Pythons range function, but with real number inputs functionality
def range_f(start, stop, step):
    
    items = (start, stop, step)

    for item in items:
        vls.real_validate()(item)

    vls.Positive()(step, name="step")
    vls.LessThan(stop)(start)

    while start < stop:
        yield start
        start += step