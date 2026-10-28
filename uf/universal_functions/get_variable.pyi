"""
This module contains an extremely important function: get_num, which takes a numerical value from the user.
"""
 #* 📝 File type: Python type stub (.pyi)
 #* 📝 Purpose: Describes the module's interface for documentation,
 #* 📝         editor support, and static type checking.
 #* 📝 Runtime: Contains no implementation; see the corresponding
 #* 📝         .py file for executable code.

import numbers as num  # noqa: I001
import typing as tp


 #* 📝 Type for an int value
type IntType = type[int]

 #* 📝 Type for a floating point value
type FloatType = type[float]

#* 📝 Type for any real number
type RealType = float | int | num.Real

 #* 📝 For given `TYPE` = int, given `entry` is a string, extra customizations through **options,
 #* 📝 an integer is returned
@tp.overload
def get_num(TYPE: IntType, entry: str, **options) -> int: ...


 #* 📝 For given `TYPE` = float, given `entry` is a string, extra customizations through **options,
 #* 📝 a floating point number is returned
@tp.overload
def get_num(TYPE: FloatType, entry: str, **options) -> float: ...


def get_num(
        TYPE: FloatType | IntType,
        entry: str,
        **options
) -> RealType:
    """
    Gets a real numerical value from the user.

    :param TYPE: float or int;  which type of value to check for

    :param entry: str; input string

    :param options: MAX, MIN, store

    :return: float or int
    """