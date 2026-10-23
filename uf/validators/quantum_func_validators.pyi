"""
This module contains a validator and decorator from the QTM Dimension.
"""

import collections.abc as cabc


def qtm_func_validator(func: cabc.Callable, *args, **kwargs) -> cabc.Callable:
   """
   Takes a function and compares the entered value with the expected type.

   :param func: given function

   :param args: arguments

   :param kwargs: keyword arguments

   :return: given function if the provided argument matches the expected type, raises an error if not
   """


def qtm_validation_decorator(func: cabc.Callable) -> cabc.Callable:
   """
   QUANTUM DECORATOR!

   Decorates a function with the quantum function validator and returns the function.

   :param func: provided function
   
   :return: validated function
   """