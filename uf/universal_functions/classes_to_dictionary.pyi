"""
This module contains a function that takes all functions in a class and make a dictionary with them.
"""

import collections.abc as cabc


def classes_to_dict(*classes: type) -> dict[str, cabc.Callable]:
    """
    Extracts callable objects from the given classes and returns them
    as a dictionary mapping their names to the corresponding objects

    >>> class RandomClass:
    ...     def get_item(self):
    ...         pass
    >>> result = classes_to_dict(RandomClass)
    >>> list(result)
    ['get_item']

    :param classes: Classes from which the callables are extracted
    :return: Dictionary of callable names and their objects
    """