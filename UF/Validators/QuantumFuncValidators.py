"""
This module contains a validator and decorator from the QTM Dimension.
"""

from collections.abc import Callable
from inspect import signature
from typing import get_origin, Annotated
from .QuantumValidators import qtm_lt_validator, qtm_constr_validator
from functools import wraps
from .ValidationClasses import TypeValidate


def qtm_func_validator(func: Callable, *args, **kwargs) -> bool:
    """
    Takes a function and compares the entered value with the expected type
    :param func: given function
    :param args: arguments
    :param kwargs: keyword arguments
    :return: True if the provided argument matches the expected type, raises an error if not
    """
    TypeValidate(Callable)(func, name=func.__name__)
    sig = signature(func)
    bound = sig.bind(*args, **kwargs)

    for name, value in bound.arguments.items():
        parameter = sig.parameters[name]
        type_ = parameter.annotation

        if type_ is parameter.empty:
            continue

        origin = get_origin(type_)

        if origin in (list, tuple):
            qtm_lt_validator(value, type_, name)

        elif origin is Annotated:
            qtm_constr_validator(value, type_, name)

        else:
            TypeValidate(type_)(value, name=name)

    return True

def qtm_validation_decorator(func: Callable) -> Callable:
    """
    DECORATOR!

    Decorates a function with the quantum function validator and returns the function
    :param func: provided function
    :return: validated function
    """
    TypeValidate(Callable)(func, name=func.__name__)

    @wraps(func)
    def wrapper(*args, **kwargs):
        qtm_func_validator(func, *args, **kwargs)
        return func(*args, **kwargs)
    return wrapper
