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

from .ClassToDict import classes_to_dict
from .DecoratorArchive import deco_superposition, cls_deco_superposition
from .GetVariable import get_num
from .HelperFunctions import (
    helper,
    HelperFunctions,
    range_f,
)
from .StringCheck import get_str
from .Trigonometry import sine, cosine, asine
from .Validators import *

from . import ClassToDict
from . import DecoratorArchive
from . import GetVariable
from . import HelperFunctions as HelperFunctionsModule
from . import StringCheck
from . import Trigonometry
from . import Validators

__all__ = [
    "classes_to_dict",
    "deco_superposition",
    "cls_deco_superposition",
    "get_num",
    "helper",
    "HelperFunctions",
    "sine",
    "cosine",
    "asine",
    "range_f",
    "get_str",
    "TypeValidate",
    "Positive",
    "int_validate",
    "str_validate",
    "real_validate",
    "LessThan",
    "LessOrEqual",
    "GreaterThan",
    "GreaterOrEqual",
    "SequenceValidate",
    "qtm_validation_decorator",
    "qtm_func_validator",
    "qtm_constr_validator",
    "qtm_lt_validator",

    "ClassToDict",
    "DecoratorArchive",
    "GetVariable",
    "HelperFunctionsModule",
    "StringCheck",
    "Trigonometry",
    "Validators",
]