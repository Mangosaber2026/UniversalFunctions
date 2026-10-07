"""
This module contains an extremely important function: get_num, which takes a numerical value from the user.
"""

from time import sleep as rest
from typing import overload, Literal, Final
from numbers import Real
from .Validators import (
    LessThan,
    str_validate,
    real_validate,
    TypeValidate,
    GreaterOrEqual,
    LessOrEqual,
    type_error,
    GreaterThan,
)


type int_type = type[int]
type float_type = type[float]

@overload
def get_num(TYPE: int_type, entry: str, **options) -> int: ...

@overload
def get_num(TYPE: float_type, entry: str, **options) -> float: ...

def get_num(
        TYPE: float_type|int_type,
        entry: str,
        **options
) -> Real:
    """
    Gets a real numerical value from the user

    :param TYPE: float or int;  which type of value to check for
    :param entry: str; input string
    :param options: MAX, MIN, store
    :return: float or int
    """
    func_name: Final[Literal["get_num"]] = "get_num"
    type_obj_name: Final[Literal["TYPE"]] = "TYPE"

    store_var: Final[Literal["store"]] = "store"
    store_value = options[store_var]

    min_var: Final[Literal["MIN"]] = "MIN"
    min_value = options[min_var]

    max_var: Final[Literal["MAX"]] = "MAX"
    max_value = options[max_var]

    if TYPE not in (int, float):
        raise type_error()(f"""
            TypeError
            
            Function: {func_name}
            Parameter {type_obj_name} must be type float or int!
            Expected: int or float object
            Received:
                Name: {type_obj_name}
                Value: {TYPE}
            """)

    str_validate()(entry, name="entry")

    real_validate()(max_value, name=max_var)
    real_validate()(min_value, name=min_var)

    if min_var in options and max_var in options:
        LessThan(max_value)(min_value, name=min_var)

    if store_var in options:
        TypeValidate((Real, type(None)))(store_value, name=store_var)

    if (
        store_var in options
        and min_var in options
        and max_var in options
        and store_value is not None
    ):
        GreaterThan(min_value)(store_value, name=store_var)

    while True:
        try:
            if store_var in options:
                reserve: str = input(entry)
                if reserve == "ans":
                    if isinstance(store_value, Real):
                        value: Real = store_value
                    else:
                        print("\nThere is no value stored yet!")
                        continue
                else:
                    value: Real = TYPE(reserve)
            else:
                value: Real = TYPE(input(entry))
            value_name: Literal["value"] = "value"

            if min_var in options and max_var in options:
                GreaterOrEqual(min_value)(value, name=value_name)
                LessOrEqual(max_value)(value, name=value_name)

            elif min_var in options:
                GreaterOrEqual(min_value)(value, name=value_name)

            elif max_var in options:
                LessOrEqual(max_value)(value, name=value_name)

            elif store_var in options:
                options["store"] = value
            return value
        except ValueError as error:
            print(error)
            rest(1.5)