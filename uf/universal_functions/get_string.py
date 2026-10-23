from time import sleep as rest

from .. import validators as vls


def get_str(str_input, *check_values):
    
    vls.str_validate()(str_input, name="str_input")
    while True:
        value: str = input(str_input).lower()
        for check in check_values:
            vls.TypeValidate((str, dict, list, tuple))(check, name="check")
            if (
                  isinstance(check, str) and check == value
                  or isinstance(check, (dict, list, tuple)) and value in check
            ):
                return value
        print("Enter something VALID!")
        rest(1.5)