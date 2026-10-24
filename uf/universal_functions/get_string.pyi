"""
This module contains an extremely important function: get_str, which takes a string input from the user.
"""
#* File type: Python type stub (.pyi)
#* Purpose: Describes the module's interface for documentation,
#*          editor support, and static type checking.
#* Runtime: Contains no implementation; see the corresponding
#*          .py file for executable code.

def get_str(str_input: str, *check_values) -> str:
    """
    Checks whether the input string matches the allowed values (*check_values).

    :param str_input: input string
    
    :param check_values: allowed string values (all lowercase), options: str, dict, list, tuple
    
    :return: the input string if it matches one of the allowed values
    """