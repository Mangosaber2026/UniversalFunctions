# ⚓ Anchor for this module: [[uf-anchor|uf.__init__.py]]  

"""
Welcome to the bridge between the Quantum Dimension and Python

Here you will be able to explore the lower floors of the upper software!

Nevertheless, be aware, even though you may use the reusable functions as much as you want,
not only do you have to credit the author, but also make sure you DO NOT change anything unless you
have become an official contributor.

As for the links in this package, if you decide to check out the source code, you can just click
on the links to go the source code.

__________ Quantum Dimension __________

Quantum Turtle Mechanics:  an extremely specialized sector where the author decided to implement
functions such as qtm_validation_decorator. This is a decorator which one can apply to a function to
make sure the Wave Function of each entered variable collapses into one.

Classical Turtle Mechanics: also a specialized sector, where the functions are closer to 'normal' Python
functions. These are still extremely important to the rest of the main package and must therefore
not be changed!
"""

#* 📝 Imports the contributions package containing CONTRIBUTIONS.md
#* 📝 which contains information regarding external contributions to this software
from . import contributions

#* 📝 Imports the editor_configs package containing a README.md and vscode-settings.json
#* 📝 which contains the configurations I used to develop this software
from . import editor_configs

#* 📝 Imports functions and classes from the [[#mathematics-anchor|mathematics package]] 
from .mathematics import (
    Percent,  
    # 🔗 Link to source code: [[#Percent-anchor|class Percent]] 

    pct10,
    # 🔗 Link to source code: [[#pct10-anchor|pct10()]] 

    pct20,
    # 🔗 Link to source code: [[#pct20-anchor|pct20()]] 

    pct25,
    # 🔗 Link to source code: [[#pct25-anchor|pct25()]] 

    pct30,
    # 🔗 Link to source code: [[#pct30-anchor|pct30()]] 

    pct40,
    # 🔗 Link to source code: [[#pct40-anchor|pct40()]] 

    pct50,
    # 🔗 Link to source code: [[#pct50-anchor|pct50()]] 

    pct60,
    # 🔗 Link to source code: [[#pct60-anchor|pct60()]] 

    pct70,
    # 🔗 Link to source code: [[#pct70-anchor|pct70()]] 

    pct75,
    # 🔗 Link to source code: [[#pct75-anchor|pct75()]] 

    pct80,
    # 🔗 Link to source code: [[#pct80-anchor|pct80()]] 

    pct90,
    # 🔗 Link to source code: [[#pct90-anchor|pct90()]] 

    sine,
    # 🔗 Link to source code: [[#sine-anchor|sine()]] 

    cosine,
    # 🔗 Link to source code: [[#cosine-anchor|cosine()]] 

    asine,
    # 🔗 Link to source code: [[#asine-anchor|asine()]] 
)

#* 📝 Imports functions, classes and aliases from the [[#universal-functions-anchor|universal_functions package]] 
from .universal_functions import (
   classes_to_dict,
   # 🔗 Link to source code: [[#classes-to-dict-anchor|classes_to_dict()]] 

   cls_deco_superposition,
   # 🔗 Link to source code: [[#cls-deco-superposition-anchor|cls_deco_superposition()]] 
   
   deco_superposition,
   # 🔗 Link to source code: [[#deco-superposition-anchor|deco_superposition()]] 

   get_str,
   # 🔗 Link to source code: [[#get-str-anchor|get_str()]] 

   get_num,
   # 🔗 Link to source code: [[#get-num-anchor|get_num()]] 

   HelperFunctions,
   # 🔗 Link to source code: [[#HelperFunctions-anchor|class HelperFunctions]] 
   
   helper,
   # 🔗 Link to source code: [[#helper-anchor|alias helper]] 
   
   range_f,
   # 🔗 Link to source code: [[#range-f-anchor|range_f()]] 
)

#* 📝 Imports classes and functions from the [[#validators-anchor|validators package]] 
from .validators import (
   ComboValidate,
   # 🔗 Link to source code: [[#ComboValidate-anchor|class ComboValidate]] 

   ConstraintError,
   # 🔗 Link to source code: [[#ConstraintError-anchor|error class ConstraintError]] 

   ErrorDedent,
   # 🔗 Link to source code: [[#ErrorDedent-anchor|class ErrorDedent]] 

   GreaterOrEqual,
   # 🔗 Link to source code: [[#GreaterOrEqual-anchor|class GreaterOrEqual]] 

   GreaterThan,
   # 🔗 Link to source code: [[#GreaterThan-anchor|class GreaterThan]] 

   ItemCountError,
   # 🔗 Link to source code: [[#ItemCountError-anchor|error class ItemCountError]] 

   LessOrEqual,
   # 🔗 Link to source code: [[#LessOrEqual-anchor|class LessOrEqual]] 

   LessThan,
   # 🔗 Link to source code: [[#LessThan-anchor|class LessThan]] 

   Positive,
   # 🔗 Link to source code: [[#Positive-anchor|class Positive]] 

   RealValidationParent,
   # 🔗 Link to source code: [[#RealValidationParent-anchor|class RealValidationParent]] 

   SequenceValidate,
   # 🔗 Link to source code: [[#SequenceValidate-anchor|class SequenceValidate]] 

   TypeValidate,
   # 🔗 Link to source code: [[#TypeValidate-anchor|class TypeValidate]] 

   attribute_error,
   # 🔗 Link to source code: [[#attribute-error-anchor|attribute_error()]] 

   constraint_error,
   # 🔗 Link to source code: [[#constraint-error-anchor|constraint_error()]] 

   int_validate,
   # 🔗 Link to source code: [[#int-validate-anchor|int_validate()]] 

   item_count_error,
   # 🔗 Link to source code: [[#item-count-error-anchor|item_count_error()]] 

   qtm_constr_validator,
   # 🔗 Link to source code: [[#qtm-constr-validator-anchor|qtm_constr_validator()]] 

   qtm_func_validator,
   # 🔗 Link to source code: [[#qtm-func-validator-anchor|qtm_func_validator]] 

   qtm_lt_validator,
   # 🔗 Link to source code: [[#qtm-lt-validator-anchor|qtm_lt_validator()]] 

   qtm_validation_decorator,
   # 🔗 Link to source code: [[#qtm-validation-decorator-anchor|qtm_validation_decorator()]] 

   real_validate,
   # 🔗 Link to source code: [[#real-validate-anchor|real_validate()]] 

   str_validate,
   # 🔗 Link to source code: [[#str-validate-anchor|str_validate()]] 

   type_error,
   # 🔗 Link to source code: [[#type-error-anchor|type_error()]] 

   value_error,
   # 🔗 Link to source code: [[#value-error-anchor|value_error()]] 
)


#* 📝 Specifies all available classes, functionsand constants through wildcard import
__all__ = [
   "contributions",
   "editor_configs",
    
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
   "cls_deco_superposition",
   "deco_superposition",
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