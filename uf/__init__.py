"""
Welcome to the bridge between the Quantum Dimension and Python

Here you will be able to explore the lower floors of the upper software!

Nevertheless, be aware, even though you may use the reusable functions as much as you want,
not only do you have to credit the author, but also make sure you DO NOT change anything unless you
have become an official contributor.

__________ Quantum Dimension __________

Quantum Turtle Mechanics:  an extremely specialized sector where the author decided to implement
functions such as qtm_validation_decorator. This is a decorator which one can apply to a function to
make sure the Wave Function of each entered variable collapses into one.

Classical Turtle Mechanics: also a specialized sector, where the functions are closer to 'normal' Python
functions. These are still extremely important to the rest of the main package and must therefore
not be changed!
"""

from .mathematics import (
   Percent,
   pct10,
   pct20,
   pct25,
   pct30,
   pct40,
   pct50,
   pct60,
   pct70,
   pct75,
   pct80,
   pct90,

   sine,
   asine,
   cosine,
)

from .universal_functions import (
   HelperFunctions,
   classes_to_dict,
   cls_deco_superposition,
   deco_superposition,
   get_num,
   get_str,
   helper,
   range_f,
)

from .validators import (
   ComboValidate,
   ConstraintError,
   ErrorDedent,
   GreaterOrEqual,
   GreaterThan,
   ItemCountError,
   LessOrEqual,
   LessThan,
   Positive,
   RealValidationParent,
   SequenceValidate,
   TypeValidate,
   attribute_error,
   constraint_error,
   int_validate,
   item_count_error,
   qtm_constr_validator,
   qtm_func_validator,
   qtm_lt_validator,
   qtm_validation_decorator,
   real_validate,
   str_validate,
   type_error,
   value_error,
)

__all__ = [
   "Percent",
   "pct10",
   "pct20",
   "pct25",
   "pct30",
   "pct40",
   "pct50",
   "pct60",
   "pct70",
   "pct75",
   "pct80",
   "pct90",
   "sine",
   "cosine",
   "asine",

   "classes_to_dict",
   "deco_superposition",
   "cls_deco_superposition",
   "get_str",
   "get_num",
   "HelperFunctions",
   "helper",
   "range_f",

   "ErrorDedent",
   "type_error",
   "value_error",
   "item_count_error",
   "constraint_error",
   "attribute_error",
   "ItemCountError",
   "ConstraintError",

   "qtm_validation_decorator",
   "qtm_func_validator",

   "qtm_lt_validator",
   "qtm_constr_validator",

   "TypeValidate",
   "int_validate",
   "str_validate",
   "real_validate",
   "Positive",
   "LessThan",
   "LessOrEqual",
   "GreaterThan",
   "GreaterOrEqual",
   "SequenceValidate",
   "RealValidationParent",
   "ComboValidate",
]