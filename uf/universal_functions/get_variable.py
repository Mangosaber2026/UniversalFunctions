"""
This module contains an extremely important function: get_num, which takes a numerical value from the user.
"""

from numbers import Real
from time import sleep as rest
from typing import Final, Literal, overload

from .. import validators as vls

type IntType = type[int]
type FloatType = type[float]

@overload
def get_num(TYPE: IntType, entry: str, **options) -> int: ...

@overload
def get_num(TYPE: FloatType, entry: str, **options) -> float: ...

def get_num(
        TYPE: FloatType | IntType,
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
    func_name: Final = "get_num"
    type_obj_name: Final = "TYPE"
    type_item: Final = TYPE

    if type_item not in (int, float):
        raise vls.type_error()(f"""
            TypeError

            Function: {func_name}
            Parameter {type_obj_name} must be type float or int!
            Expected: int or float object
            Received:
                Name: {type_obj_name}
                Value: {TYPE}
            """)

    vls.str_validate()(entry, name="entry")

    store_var: Final = "store"
    if store_var in options:
        store_value = options[store_var]
        vls.TypeValidate((Real, type(None)))(store_value, name=store_var)

    min_var: Final = "MIN"
    if min_var in options:
        min_value = options[min_var]
        vls.real_validate()(min_value, name=min_var)

    max_var: Final = "MAX"
    if max_var in options:
        max_value = options[max_var]
        vls.real_validate()(max_value, name=max_var)

    if min_var in options and max_var in options:
        vls.LessThan(max_value)(min_value, name=min_var)

    if (
        store_var in options
        and min_var in options
        and max_var in options
        and store_value is not None
    ):
        vls.GreaterThan(min_value)(store_value, name=store_var)

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
                vls.GreaterOrEqual(min_value)(value, name=value_name)
                vls.LessOrEqual(max_value)(value, name=value_name)

            elif min_var in options:
                vls.GreaterOrEqual(min_value)(value, name=value_name)

            elif max_var in options:
                vls.LessOrEqual(max_value)(value, name=value_name)

            elif store_var in options:
                options["store"] = value
            return value
        except ValueError as error:
            print(error)
            rest(1.5)