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

from .QuantumFuncValidators import qtm_validation_decorator, qtm_func_validator
from .QuantumValidators import qtm_lt_validator, qtm_constr_validator
from .ValidationClasses import (
    TypeValidate,
    int_validate,
    str_validate,
    real_validate,
    Positive,
    LessThan,
    LessOrEqual,
    GreaterThan,
    GreaterOrEqual,
    SequenceValidate,
    RealValidationParent,
)

from . import QuantumFuncValidators
from . import QuantumValidators
from . import ValidationClasses

__all__ = [
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

    "QuantumFuncValidators",
    "QuantumValidators",
    "ValidationClasses",
]