# ⚓ Anchor for this module: [[helper-functions-anchor|helper_functions.py]] 
# 🔗 Parent package: [[#universal-functions-anchor|universal_functions]] 

import math

from .. import validators as vls
from . import classes_to_dictionary as cls_to_dict
from . import get_variable as gv


# ⚓ HelperFunctions anchor: [[HelperFunctions-anchor|class HelperFunctions]] 
 #* 📝 Contains helper functions which make getting certain values easier for the user
class HelperFunctions:

    # ⚓ intervals_f anchor: [[HelperFunctions-intervals-f-anchor|intervals_f()]] 
    #* 📝 Gets a floating point interval count with [[#get-num-anchor|get_num()]] 
    #* 📝 from the user and returns it
    @staticmethod
    def intervals_f():

        return gv.get_num(TYPE=float, entry="Enter intervals(ℚ>0): ", MIN=0)


    # ⚓ length_float anchor: [[HelperFunctions-length-float-anchor|length_float()]] 
    #* 📝 Gets a floating point length with [[#get-num-anchor|get_num()]] 
    #* 📝 from the user and returns it
    @staticmethod
    def length_float():

        return gv.get_num(TYPE=float, entry="Enter side length(ℚ>0): ", MIN=0)
    

    # ⚓ radius_float anchor: [[HelperFunctions-radius-float-anchor|radius_float()]] 
    #* 📝 Gets a floating point radius with [[#get-num-anchor|get_num()]] 
    #* 📝 from the user and returns it
    @staticmethod
    def radius_float():

        return gv.get_num(float, "Enter radius(ℚ>0): ", MIN=0)


    # ⚓ object_num anchor: [[HelperFunctions-object-num-anchor|object_num()]] 
    #* 📝 Gets a natural object count with [[#get-num-anchor|get_num()]] 
    #* 📝 from the user and returns it
    @staticmethod
    def object_num():

        return gv.get_num(int, "Enter object count(ℕ≥1): ", MIN=1)
    

    # ⚓ sides_num anchor: [[HelperFunctions-sides-num-anchor|sides_num()]] 
    #* 📝 Gets a natural sides count with [[#get-num-anchor|get_num()]] 
    #* 📝 from the user and returns it
    @staticmethod
    def sides_num():
        
        return gv.get_num(int, "Enter sides count(ℕ≥3): ", MIN=3)


    # ⚓ row_num anchor: [[HelperFunctions-row-num-anchor|row_num()]] 
    #* 📝 Gets a natural row count with [[#get-num-anchor|get_num()]] 
    #* 📝 from the user and returns it
    @staticmethod
    def row_num():
        
        return gv.get_num(int, "Enter row count(ℕ≥1): ", MIN=1)
    

    # ⚓ row_pair anchor: [[HelperFunctions-row-pair-anchor|row_pair()]] 
    #* 📝 Gets a natural row pair count with [[#get-num-anchor|get_num()]] 
    #* 📝 from the user and returns it
    @staticmethod
    def row_pair():
        
        return gv.get_num(int, "Enter row pairs count(ℕ≥1): ", MIN=1)


    # ⚓ diameter_sq anchor: [[HelperFunctions-diameter-sq-anchor|diameter_sq()]] 
    #* 📝 Calculates the diameter and half of it of a square with given length
    @staticmethod
    def diameter_sq(length):
        
        vls.ComboValidate(value=length, name="length")(
            vls.real_validate(),
            vls.Positive()
        )

        diameter = length * math.sqrt(2)
        d_half = diameter / 2

        return diameter, d_half


    # ⚓ x_ft anchor: [[HelperFunctions-x-ft-anchor|x_ft()]] 
    #* 📝 Gets a value for the x-coordinate with [[#get-num-anchor|get_num()]] 
    #* 📝 from the user and returns it
    @staticmethod
    def x_ft():
        
        return gv.get_num(float, "Enter x value: ")


    # ⚓ y_ft anchor: [[HelperFunctions-y-ft-anchor|y_ft()]] 
    #* 📝 Gets a value for the y-coordinate with [[#get-num-anchor|get_num()]] 
    #* 📝 from the user and returns it
    @staticmethod
    def y_ft():
        
        return gv.get_num(float, "Enter y value: ")
    

    # ⚓ list_helperfunctions anchor: [[HelperFunctions-list-helperfunctions-anchor|list_helperfunctions()]] 
    #* 📝 Creates and returns a dictionary mapping [[#HelperFunctions-anchor|HelperFunctions]] function names
    #* 📝 with the actual function with [[#classes-to-dict-anchor|classes_to_dict()]] 
    @staticmethod
    def list_helperfunctions():

        return cls_to_dict.classes_to_dict(HelperFunctions)


# ⚓ helper anchor: [[helper-anchor|alias helper]]
 #* 📝 Another name for [[#HelperFunctions-anchor|HelperFunctions]] to make it shorter
helper = HelperFunctions


# ⚓ range_f anchor: [[range-f-anchor|range_f()]]
 #* 📝 Similar to Pythons range function, but with real number inputs functionality
def range_f(start, stop, step):
    
    items = (start, stop, step)
    items_names = ("start", "stop", "step")

    for item, item_name in zip(items, items_names):
        vls.real_validate()(value=item, name=item_name)

    vls.Positive()(value=step, name="step")
    vls.LessThan(expected=stop)(value=start)

    while start < stop:
        yield start
        start += step