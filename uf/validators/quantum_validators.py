import typing as tp

from .errors import type_error
from . import validation_classes as vcls


def qtm_lt_validator(value, TYPE, name):
    
    func_name: tp.Final[str] = "qtm_lt_validator"
    origin = tp.get_origin(TYPE)
    if origin not in (list, tuple):
        raise type_error()(f"""
            Validator: {func_name}
            Parameter TYPE must be a list/tuple of elements!
            Expected: type object
            Received: {TYPE}
            """)

    vcls.TypeValidate(origin)(value)

    element_type = tp.get_args(TYPE)
    validator = vcls.SequenceValidate(*element_type)

    return validator(value, name=name)

def qtm_constr_validator(value, annotation, name):

    func_name: tp.Final[str] = "qtm_constr_validator"
    if tp.get_origin(annotation) is not tp.Annotated:
        raise type_error()(f"""
            Validator: {func_name}
            Parameter annotation is not an Annotated type!
            Expected: Annotated object
            Received: {annotation}
            """)

    type_obj, *constraints = tp.get_args(annotation)

    vcls.TypeValidate(str)(name, name="name")
    vcls.TypeValidate(type_obj)(value, name=name)

    for constraint in constraints:
        constraint(value)

    return value