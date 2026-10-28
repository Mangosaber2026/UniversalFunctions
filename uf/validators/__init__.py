# ⚓ Anchor for this module: [[validators-anchor|validators.__init__.py]] 

"""
Welcome to the Quantum/Classical Dimension!

Here you will find some of the most sensitive pieces of code, however you may gladly use the validators,
no matter quantum or classic.
But whatever you do, DO NOT change the actual functions, otherwise, the entire
software will cease to function.
Almost every single other module in this software relies on the quantum validation centers, if anything is changed
inappropriately, the user shall face serious consequences.

Abbreviations:
    qtm = Quantum Turtle Mechanics
    ctm = Classical Turtle Mechanics

All functions with qtm belong to the Quantum Dimension whereas all functions with ctm belong to the Classical Dimension
"""

 #* 📝 Imports error classes and functions from [[#errors-anchor|errors.py]] 
from .errors import (
 ConstraintError,
 # 🔗 Link to source code: [[#ConstraintError-anchor|class ConstraintError]] 
 ErrorDedent,
 # 🔗 Link to source code: [[#ErrorDedent-anchor|class ErrorDedent]] 
 ItemCountError,
 # 🔗 Link to source code: [[#ItemCountError-anchor|class ItemCountError]] 
 attribute_error,
 # 🔗 Link to source code: [[#attribute-error-anchor|attribute_error()]] 
 constraint_error,
 # 🔗 Link to source code: [[#constraint-error-anchor|constraint_error()]] 
 item_count_error,
 # 🔗 Link to source code: [[#item-count-error-anchor|item_count_error()]] 
 type_error,
 # 🔗 Link to source code: [[#type-error-anchor|type_error()]] 
 value_error,
 # 🔗 Link to source code: [[#value-error-anchor|value_error()]] 
)

#* Imports functions from [[#quantum-func-validators-anchor|quantum_func_validators.py]] 
from .quantum_func_validators import (
 qtm_func_validator,
 # 🔗 Link to source code: [[#qtm-func-validator-anchor|qtm_func_validator()]] 
 qtm_validation_decorator,
 # 🔗 Link to source code: [[#qtm-validation-decorator-anchor|qtm_validation_decorator()]] 
)

#* Imports functions from [[#quantum-validators-anchor|quantum_validators.py]] 
from .quantum_validators import (
 qtm_constr_validator,
 # 🔗 Link to source code: [[#qtm-constr-validator-anchor|qtm_constr_validator()]] 
 qtm_lt_validator,
 # 🔗 Link to source code: [[#qtm-lt-validator-anchor|qtm_lt_validator()]] 
)

#* Imports classes and functions from [[#validation-classes-anchor|validation_classes.py]] 
from .validation_classes import (
 ComboValidate,
 # 🔗 Link to source code: [[#ComboValidate-anchor|class ComboValidate]] 
 GreaterOrEqual,
 # 🔗 Link to source code: [[#GreaterOrEqual-anchor|class GreaterOrEqual]] 
 GreaterThan,
 # 🔗 Link to source code: [[#GreaterThan-anchor|class GreaterThan]] 
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
 int_validate,
 # 🔗 Link to source code: [[#int-validate-anchor|int_validate()]] 
 real_validate,
 # 🔗 Link to source code: [[#real-validate-anchor|real_validate()]]
 str_validate,
 # 🔗 Link to source code: [[#str-validate-anchor|str_validate()]] 
)

#* 📝 Specifies all available classes and functions through wildcard import
__all__ = [
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