# ⚓ Anchor for this module: [[helper-functions-anchor|helper_functions.py]] 
# 🔗 Parent package: [[#universal-functions-anchor|universal_functions]] 

import math
import numbers as num

from .. import validators as vls
from . import classes_to_dictionary as cls_to_dict
from . import decorator_archive as dec_arc
from . import get_variable as gv


# ⚓ HelperFunctions anchor: [[HelperFunctions-anchor|class HelperFunctions]] 
 #* 📝 Contains helper functions which make getting certain values easier for the user
@dec_arc.cls_deco_superposition(staticmethod)
class HelperFunctions:

    # ⚓ intervals_f anchor: [[HelperFunctions-intervals-f-anchor|intervals_f()]] 
    #* 📝 Gets a floating point interval count with [[#get-num-anchor|get_num()]] 
    #* 📝 from the user and returns it
    def intervals_f():

        interval_num: float = gv.get_num(float, "Enter intervals(ℚ>0): ", MIN=0)
        return interval_num

    # ⚓ length_float anchor: [[HelperFunctions-length-float-anchor|length_float()]] 
    #* 📝 Gets a floating point length with [[#get-num-anchor|get_num()]] 
    #* 📝 from the user and returns it
    def length_float():

        length: float = gv.get_num(float, "Enter side length(ℚ>0): ", MIN=0)
        return length

    # ⚓ radius_float anchor: [[HelperFunctions-radius-float-anchor|radius_float()]] 
    #* 📝 Gets a floating point radius with [[#get-num-anchor|get_num()]] 
    #* 📝 from the user and returns it
    def radius_float():

        radius: float = gv.get_num(float, "Enter radius(ℚ>0): ", MIN=0)
        return radius

    # ⚓ object_num anchor: [[HelperFunctions-object-num-anchor|object_num()]] 
    #* 📝 Gets a natural object count with [[#get-num-anchor|get_num()]] 
    #* 📝 from the user and returns it
    def object_num():

        object_count: int = gv.get_num(int, "Enter object count(ℕ≥1): ", MIN=1)
        return object_count

    # ⚓ sides_num anchor: [[HelperFunctions-sides-num-anchor|sides_num()]] 
    #* 📝 Gets a natural sides count with [[#get-num-anchor|get_num()]] 
    #* 📝 from the user and returns it
    def sides_num():
        
        sides: int = gv.get_num(int, "Enter sides count(ℕ≥3): ", MIN=3)
        return sides

    # ⚓ row_num anchor: [[HelperFunctions-row-num-anchor|row_num()]] 
    #* 📝 Gets a natural row count with [[#get-num-anchor|get_num()]] 
    #* 📝 from the user and returns it
    def row_num():
        
        row_count: int = gv.get_num(int, "Enter row count(ℕ≥1): ", MIN=1)
        return row_count

    # ⚓ row_pair anchor: [[HelperFunctions-row-pair-anchor|row_pair()]] 
    #* 📝 Gets a natural row pair count with [[#get-num-anchor|get_num()]] 
    #* 📝 from the user and returns it
    def row_pair():
        
        row_count: int = gv.get_num(int, "Enter row pairs count(ℕ≥1): ", MIN=1)
        return row_count

    # ⚓ diameter_sq anchor: [[HelperFunctions-diameter-sq-anchor|diameter_sq()]] 
    #* 📝 Calculates the diameter and half of it of a square with given length
    def diameter_sq(length):
        
        vls.ComboValidate(length, name="length")(
            vls.real_validate(),
            vls.Positive()
        )

        diameter: float = length * math.sqrt(2)
        d_half: num.Real = diameter / 2

        return diameter, d_half

    # ⚓ x_ft anchor: [[HelperFunctions-x-ft-anchor|x_ft()]] 
    #* 📝 Gets a value for the x-coordinate with [[#get-num-anchor|get_num()]] 
    #* 📝 from the user and returns it
    def x_ft():
        
        x_val: float = gv.get_num(float, "Enter x value: ")
        return x_val

    # ⚓ y_ft anchor: [[HelperFunctions-y-ft-anchor|y_ft()]] 
    #* 📝 Gets a value for the y-coordinate with [[#get-num-anchor|get_num()]] 
    #* 📝 from the user and returns it
    def y_ft():
        
        y_val: float = gv.get_num(float, "Enter y value: ")
        return y_val

    # ⚓ list_helperfunctions anchor: [[HelperFunctions-list-helperfunctions-anchor|list_helperfunctions()]] 
    #* 📝 Creates and returns a dictionary mapping [[#HelperFunctions-anchor|HelperFunctions]] function names
    #* 📝 with the actual function with [[#classes-to-dict-anchor|classes_to_dict()]] 
    def list_helperfunctions():

        return cls_to_dict.classes_to_dict(HelperFunctions)

# ⚓ helper anchor: [[helper-anchor|alias helper]]
 #* 📝 Another name for [[#HelperFunctions-anchor|HelperFunctions]] to make it shorter
helper = HelperFunctions

# ⚓ range_f anchor: [[range-f-anchor|range_f()]]
 #* 📝 Similar to Pythons range function, but with real number inputs functionality
def range_f(start, stop, step):
    
    items = (start, stop, step)

    for item in items:
        vls.real_validate()(item)

    vls.Positive()(step, name="step")
    vls.LessThan(stop)(start)

    while start < stop:
        yield start
        start += step