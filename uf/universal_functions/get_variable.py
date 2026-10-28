# ⚓ Anchor for this module: [[get-variable-anchor|get_variable.py]] 
# 🔗 Parent package: [[#universal-functions-anchor|universal_functions]] 

import numbers as num
import typing as tp
from time import sleep as rest

from .. import validators as vls


# ⚓ get_num anchor: [[get-num-anchor|get_num()]] 
 #* 📝 Gets a numerical value from the user, validation depends on the customzation
def get_num(TYPE, entry, **options):

    func_name: tp.Final = "get_num"
    type_obj_name: tp.Final = "TYPE"
    type_item: tp.Final = TYPE

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

    vls.str_validate()(value=entry, name="entry")

    store_var: tp.Final = "store"

    if store_var in options:

        store_value = options[store_var]
        vls.TypeValidate((num.Real, type(None)))(store_value, name=store_var)

    min_var: tp.Final = "MIN"

    if min_var in options:

        min_value = options[min_var]
        vls.real_validate()(value=min_value, name=min_var)

    max_var: tp.Final = "MAX"

    if max_var in options:

        max_value = options[max_var]
        vls.real_validate()(value=max_value, name=max_var)

    if min_var in options and max_var in options:

        vls.LessThan(expected=max_value)(value=min_value, name=min_var)

    if (
        store_var in options
        and min_var in options
        and max_var in options
        and store_value is not None
    ):
        vls.GreaterThan(expected=min_value)(value=store_value, name=store_var)

    while True:
        try:

            if store_var in options:

                reserve: str = input(entry)
                if reserve == "ans":
                    if isinstance(store_value, num.Real):
                        value: num.Real = store_value
                    else:
                        print("\nThere is no value stored yet!")
                        continue
                else:
                    value: num.Real = TYPE(reserve)

            else:
                value: num.Real = TYPE(input(entry))
            value_name: tp.Literal["value"] = "value"

            if min_var in options and max_var in options:
                vls.GreaterOrEqual(expected=min_value)(value=value, name=value_name)
                vls.LessOrEqual(expected=max_value)(value=value, name=value_name)

            elif min_var in options:
                vls.GreaterOrEqual(expected=min_value)(value=value, name=value_name)

            elif max_var in options:
                vls.LessOrEqual(expected=max_value)(value=value, name=value_name)

            elif store_var in options:
                options["store"] = value
                
            return value
        
        except ValueError as error:
            print(error)
            rest(1.5)