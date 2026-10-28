# ⚓ Anchor for this module: [[quantum-validators-anchor|quantum_validators.py]] 
# 🔗 Parent package: [[#validators-anchor|validators]] 

import typing as tp

from . import validation_classes as vcls
from .errors import type_error


# ⚓ qtm_lt_validator anchor: [[qtm-lt-validator-anchor|qtm_lt_validator()]] 
#* 📝 Takes a given value and validates its contents with given `TYPE` 
#* and the value's name -> `name`
def qtm_lt_validator(value, TYPE, name):
    
    func_name: tp.Final[str] = "qtm_lt_validator"
    origin = tp.get_origin(TYPE)
    
    if origin not in (list, tuple):
        raise type_error()(text=
            f"""
            Validator: {func_name}
            Parameter TYPE must be a list/tuple of elements!
            Expected: type object
            Received: {TYPE}
            """)

    vcls.TypeValidate(expected=origin)(value=value, name="value")

    element_types = tp.get_args(TYPE)

    return vcls.SequenceValidate(*element_types)(value=value, name=name)


# ⚓ qtm_constr_validator anchor: [[qtm-constr-validator-anchor|qtm_constr_validator()]] 
#* Validates a value using its given annotation and name 
def qtm_constr_validator(value, annotation, name):

    func_name: tp.Final[str] = "qtm_constr_validator"

    if tp.get_origin(annotation) is not tp.Annotated:

        raise type_error()(text=
            f"""
            Validator: {func_name}
            Parameter annotation is not an Annotated type!
            Expected: Annotated object
            Received: {annotation}
            """)

    type_obj, *constraints = tp.get_args(annotation)

    vcls.TypeValidate(expected=str)(value=name, name="name")
    vcls.TypeValidate(expected=type_obj)(value=value, name=name)

    for constraint in constraints:
        constraint(value)

    return value