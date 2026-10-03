"""
This module contains type validators for list and tuple which belong to the QTM Dimension.
"""

from typing import Any, get_args, get_origin, Annotated
from .ValidationClasses import TypeValidate

def qtm_lt_validator(value: list[Any] | tuple[Any, ...], TYPE: Any, name: str) -> bool:
    """
    Takes a list of ONE specific element and validates its contents against the expected type
    :param value: list of elements
    :param TYPE: list[expected type]
    :param name: name of value
    :return: True if the contents of value satisfy the expected type
    """
    origin = get_origin(TYPE)
    if origin not in (list, tuple):
        raise TypeError(f"{TYPE} must be a list or tuple for a specific type! e.g. list[int]")

    TypeValidate(origin)(value)

    element_type = get_args(TYPE)
    if origin is list:
        if len(element_type) != 1:
            raise TypeError("TYPE must contain only ONE type!")

    elif origin is tuple:
        if len(element_type) != 2 or element_type[1] is not Ellipsis:
            raise TypeError("tuple TYPE must contain only ONE type with the form tuple[T, ...]!")

    for index, element in enumerate(value):
        if not isinstance(element, element_type[0]):
            raise TypeError(f"{name}[{index}] must be of type {element_type[0].__name__!r}!")

    return True

def qtm_constr_validator(value, annotation, name) -> bool:
    """
    Takes a value and its annotation and compares it against the expected type
    :param value: given value
    :param annotation: given annotation
    :param name: name of value
    :return: True, if validation succeeds
    """

    if get_origin(annotation) is not Annotated:
        raise TypeError(f"{annotation} is not an Annotated type!")

    type_obj, *constraints = get_args(annotation)

    TypeValidate(type_obj)(value, name=name)

    for constraint in constraints:
        constraint(value)

    return True