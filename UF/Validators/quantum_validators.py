"""
This module contains type validators for list and tuple which belong to the QTM Dimension.
"""

from typing import Annotated, Any, Final, get_args, get_origin

from .errors import type_error
from .validation_classes import SequenceValidate, TypeValidate


def qtm_lt_validator(value: list[Any] | tuple[Any, ...], TYPE: Any, name: str) -> tuple | list:
    """
    Takes a list/tuple of specific elements and validates its contents against the expected type

    >>> qtm_lt_validator([1, 2, 3], list[int, ...], "random list")
    [1, 2, 3]

    :param value: list/tuple of elements
    :param TYPE: list[expected type] for example
    :param name: name of value
    :return: validated list/tuple of elements
    """
    func_name: Final = "qtm_lt_validator"
    origin = get_origin(TYPE)
    if origin not in (list, tuple):
        raise type_error()(f"""
            Validator: {func_name}
            Parameter TYPE must be a list/tuple of elements!
            Expected: type object
            Received: {TYPE}
            """)

    TypeValidate(origin)(value)

    element_type = get_args(TYPE)
    validator = SequenceValidate(*element_type)

    return validator(value, name=name)

def qtm_constr_validator(value: Any, annotation, name: str) -> Any:
    """
    Takes a value and its annotation and compares it against the expected type
    :param value: given value
    :param annotation: given annotation
    :param name: name of value
    :return: True, if validation succeeds
    """
    func_name: Final = "qtm_constr_validator"
    if get_origin(annotation) is not Annotated:
        raise type_error()(f"""
            Validator: {func_name}
            Parameter annotation is not an Annotated type!
            Expected: Annotated object
            Received: {annotation}
            """)

    type_obj, *constraints = get_args(annotation)

    TypeValidate(str)(name, name="name")
    TypeValidate(type_obj)(value, name=name)

    for constraint in constraints:
        constraint(value)

    return value