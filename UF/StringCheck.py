"""
This module contains an extremely important function: get_str, which takes a string input from the user.
"""

from time import sleep as rest
from .Validators.ValidationClasses import TypeValidate, str_validate


def get_str(str_input: str, *check_values) -> str:
    """
    Checks whether the input string matches the allowed values (*check_values)
    :param str_input: input string
    :param check_values: allowed string values (all lowercase), options: str, dict, list, tuple
    """
    str_validate()(str_input, name="str_input")
    while True:
        value: str = input(str_input).lower()
        for check in check_values:
            TypeValidate((str, dict, list, tuple))(check, name="check")
            if isinstance(check, str) and check == value:
                return value
            elif isinstance(check, (dict, list, tuple)) and value in check:
                return value
        print("Enter something VALID!")
        rest(1.5)