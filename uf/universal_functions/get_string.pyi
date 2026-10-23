"""
This module contains an extremely important function: get_str, which takes a string input from the user.
"""

def get_str(str_input: str, *check_values) -> str:
    """
    Checks whether the input string matches the allowed values (*check_values).

    :param str_input: input string
    
    :param check_values: allowed string values (all lowercase), options: str, dict, list, tuple
    
    :return: the input string if it matches one of the allowed values
    """