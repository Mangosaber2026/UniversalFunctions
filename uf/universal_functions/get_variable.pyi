"""
This module contains an extremely important function: get_num, which takes a numerical value from the user.
"""

import numbers as num
import typing as tp


type IntType = type[int]
type FloatType = type[float]

@tp.overload
def get_num(TYPE: IntType, entry: str, **options) -> int: ...

@tp.overload
def get_num(TYPE: FloatType, entry: str, **options) -> float: ...


def get_num(
        TYPE: FloatType | IntType,
        entry: str,
        **options
) -> num.Real:
    """
    Gets a real numerical value from the user.

    :param TYPE: float or int;  which type of value to check for

    :param entry: str; input string

    :param options: MAX, MIN, store

    :return: float or int
    """