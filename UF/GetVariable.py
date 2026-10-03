"""
This module contains an extremely important function: get_num, which takes a numerical value from the user.
"""

from time import sleep as rest
from typing import overload, Literal
from numbers import Real
from .Validators.ValidationClasses import LessThan, str_validate, real_validate, TypeValidate, GreaterOrEqual, LessOrEqual


type int_type = type[int]
type float_type = type[float]

@overload
def get_num(TYPE: int_type, entry: str, **options) -> int: ...

@overload
def get_num(TYPE: float_type, entry: str, **options) -> float: ...

def get_num(TYPE: float_type|int_type, entry: str, **options) -> Real:
    """
    Gets a real numerical value from the user

    :param TYPE: float or int;  which type of value to check for
    :param entry: str; input string
    :param options: MAX, MIN, store
    :return: float or int
    """
    if TYPE not in (int, float):
        raise TypeError("TYPE must be type float or int")

    str_validate()(entry, name="entry")

    for item in ("MAX", "MIN"):
        if item in options:
            real_validate()(options[item], name=item)

    if "MIN" in options and "MAX" in options:
        LessThan(options["MAX"])(options["MIN"])

    if "store" in options:
        TypeValidate((Real, type(None)))(options["store"], name="store")

    if (
        "store" in options
        and "MIN" in options
        and "MAX" in options
        and options["store"] is not None
        and (options["MIN"] > options["store"] or options["MAX"] < options["store"])
    ):
        raise ValueError("Stored value must be between MIN and MAX!")

    while True:
        try:
            if "store" in options:
                reserve: str = input(entry)
                if reserve == "ans":
                    if isinstance(options["store"], Real):
                        value: Real = options["store"]
                    else:
                        print("\nThere is no value stored yet!")
                        continue
                else:
                    value: Real = TYPE(reserve)
            else:
                value: Real = TYPE(input(entry))
            value_name: Literal["value"] = "value"

            if "MIN" in options and "MAX" in options:
                GreaterOrEqual(options["MIN"])(value, name=value_name)
                LessOrEqual(options["MAX"])(value, name=value_name)

            elif "MIN" in options:
                GreaterOrEqual(options["MIN"])(value, name=value_name)

            elif "MAX" in options:
                LessOrEqual(options["MAX"])(value, name=value_name)

            elif "store" in options:
                options["store"] = value
            return value
        except ValueError as error:
            print(error)
            rest(1.5)