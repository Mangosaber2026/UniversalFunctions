"""
This module provides a collection of error message deliverers and separate errors created by the author which
are not normally provided with Python.

The custom errors in this module can be used just like any other conventional error provided by Python itself.
"""

import collections.abc as cabc
import typing as tp


class ErrorDedent:
   """
   This class is the error raiser for the other validators found in this package (uf).

   The use of this class is to make the error message be printed with some formatting instead of the conventional
   way it would be printed otherwise.

   >>> print(ErrorDedent(TypeError)("This is a TypeError!"))
   TypeError
   <BLANKLINE>
   This is a TypeError!
   """

   name: tp.Final[str]

   def __init__(self, error_func: cabc.Callable) -> None:
      """
      Takes an error (Exception) class and returns an error message with it.
      :param error_func: Exception subclass exception
      :return: None
      """

   def __call__(self, text: str) -> Exception:
      """
      Takes a text (str) and returns the error message with it.
      :param text: string
      :return: error message with given text
      """

def type_error() -> cabc.Callable:
   """
   This function returns a callable type error function.

   >>> print(type_error()("This is a TypeError!"))
   TypeError
   <BLANKLINE>
   This is a TypeError!

   :return: ErrorDedent function
   """

def value_error() -> cabc.Callable:
   """
   This function returns a callable value error function.

   >>> print(value_error()("This is a ValueError!"))
   ValueError
   <BLANKLINE>
   This is a ValueError!

   :return: ErrorDedent function
   """


def item_count_error() -> cabc.Callable:
   """
   This function returns a callable item count error function.

   >>> print(item_count_error()("This is an Item Count Error!"))
   ItemCountError
   <BLANKLINE>
   This is an Item Count Error!

   :return: ErrorDedent function
   """


def constraint_error() -> cabc.Callable:
   """
   This function returns a callable constraint error function.

   >>> print(constraint_error()("This is a Constraint Error!"))
   ConstraintError
   <BLANKLINE>
   This is a Constraint Error!

   :return: ErrorDedent function
   """


def attribute_error() -> cabc.Callable:
   """
   This function returns a callable attribute error function.

   >>> print(attribute_error()("This is an Attribute Error!"))
   AttributeError
   <BLANKLINE>
   This is an Attribute Error!

   :return: ErrorDedent function
   """

class ItemCountError(Exception):
   """
   This exception is raised when an item count does not match the expected count.

   >>> print(ItemCountError("This is an Item Count Error!"))
   This is an Item Count Error!
   """

class ConstraintError(Exception):
   """
   This exception is raised when an item does not pass the expected constraint.

   >>> print(ConstraintError("This is a Constraint Error!"))
   This is a Constraint Error!
   """