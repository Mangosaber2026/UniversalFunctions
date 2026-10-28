"""
This module contains type validators for list and tuple which belong to the QTM Dimension.
"""
 #* 📝 File type: Python type stub (.pyi)
 #* 📝 Purpose: Describes the module's interface for documentation,
 #* 📝         editor support, and static type checking.
 #* 📝 Runtime: Contains no implementation; see the corresponding
 #* 📝         .py file for executable code.

import typing as tp  # noqa: I001


def qtm_lt_validator(
      value: list[tp.Any] | tuple[tp.Any, ...],
      TYPE: tp.Any,
      name: str
) -> tuple | list:
   """
   Takes a list/tuple of specific elements and validates its contents against the expected type.

   >>> qtm_lt_validator([1, 2, 3], list[int, ...], "random list")
   [1, 2, 3]

   :param value: list/tuple of elements

   :param TYPE: list[expected type] for example

   :param name: name of value

   :return: validated list/tuple of elements
   """


def qtm_constr_validator(value: tp.Any, annotation, name: str) -> tp.Any:
   """
   Takes a value and its annotation and compares it against the expected type.

   :param value: given value

   :param annotation: given annotation

   :param name: name of value
   
   :return: True, if validation succeeds
   """