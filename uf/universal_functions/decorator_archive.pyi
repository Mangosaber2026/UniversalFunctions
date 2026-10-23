"""
This module contains decorators which take any number of decorators and apply them to the function they are assigned to.
"""

import collections.abc as cabc


def cls_deco_superposition(*decorators: cabc.Callable) -> cabc.Callable:
    """
    DECORATOR!!   Creates a class decorator that applies the given decorator to every user defined function
    
    :param decorators: provided decorator functions
    
    :return: a class decorator that transforms the class (& it's functions) and returns it
    """

def deco_superposition(*decorators: cabc.Callable) -> cabc.Callable:
    """
    DECORATOR! this decorator takes multiple decorators and applies them to the given function the same way python would naturally
    
    :param decorators: decorator functions
    
    :return: supplied function
    """