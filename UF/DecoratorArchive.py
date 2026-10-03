"""
This module contains decorators which take any number of decorators and apply them to the function they are assigned to.
"""

from collections.abc import Callable
from .Validators.QuantumFuncValidators import qtm_validation_decorator


@qtm_validation_decorator
def cls_deco_superposition(*decorators: tuple[Callable, ...]) -> Callable:
    """
    DECORATOR!!   Creates a class decorator that applies the given decorator to every user defined function
    :param decorator: provided decorator function
    :return: a class decorator that transforms the class (& it's functions) and returns it
    """
    deco_composer = deco_superposition(*decorators)

    def inner(cls):
        for name, func in vars(cls).items():
            if callable(func) and not name.startswith("_"):
                setattr(cls, name, deco_composer(func))
        return cls
    return inner

@qtm_validation_decorator
def deco_superposition(*decorators: tuple[Callable, ...]) -> Callable:
    """
    DECORATOR! this decorator takes multiple decorators and applies them to the given function the same way python would naturally
    :param decorators: decorator functions
    :return: supplied function
    """
    def inner_deco(func):
        for decorator in reversed(decorators):
            func = decorator(func)

        return func
    return inner_deco