"""
This module contains type validators for list and tuple which belong to the QTM Dimension.
"""

from typing import Any, get_args, get_origin, Annotated
from .ValidationClasses import TypeValidate, SequenceValidate

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
    origin = get_origin(TYPE)
    if origin not in (list, tuple):
        raise TypeError(f"{TYPE} must be a list or tuple for a specific type! e.g. list[int]")

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

    if get_origin(annotation) is not Annotated:
        raise TypeError(f"{annotation} is not an Annotated type!")

    type_obj, *constraints = get_args(annotation)

    TypeValidate(str)(name, name="name")
    TypeValidate(type_obj)(value, name=name)

    for constraint in constraints:
        constraint(value)

    return value