"""
This module contains a function that takes all functions in a class and make a dictionary with them.
"""

from collections.abc import Callable
from .Validators.QuantumFuncValidators import qtm_validation_decorator


@qtm_validation_decorator
def classes_to_dict(*classes: tuple[type, ...]) -> dict[str, Callable]:
    """
    Extracts callable objects from the given classes and returns them
    as a dictionary mapping their names to the corresponding objects
    :param classes: Classes from which the callables are extracted
    :return: Dictionary of callable names and their objects
    """
    dictionary = {}
    for cls in classes:
        dictionary.update({
            name: obj
            for name, obj in vars(cls).items()
            if callable(obj)
        })
    return dictionary