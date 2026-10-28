"""
This module contains decorators which take any number of decorators and apply them to the function they are assigned to.
"""
 #* 📝 File type: Python type stub (.pyi)
 #* 📝 Purpose: Describes the module's interface for documentation,
 #* 📝         editor support, and static type checking.
 #* 📝 Runtime: Contains no implementation; see the corresponding
 #* 📝         .py file for executable code.

import collections.abc as cabc  # noqa: I001


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