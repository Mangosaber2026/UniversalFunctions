# ⚓ Anchor for this module: [[get-string-anchor|get_string.py]] 
# 🔗 Parent package: [[#universal-functions-anchor|universal_functions]] 

from time import sleep as rest

from .. import validators as vls


# ⚓ get_str anchor: [[get-str-anchor|get_str()]] 
 #* 📝 Gets a string from the user with provided string input and
 #* 📝 verifies the entered value against given check values
def get_str(str_input, *check_values):
    
    vls.str_validate()(value=str_input, name="str_input")

    while True:
        value: str = input(str_input).lower()

        for check in check_values:

            vls.TypeValidate(expected=(str, dict, list, tuple))(value=check, name="check")

            if (
                  isinstance(check, str) and check == value
                  or isinstance(check, (dict, list, tuple)) and value in check
            ):
                return value
            
        print("Enter something VALID!")
        rest(1.5)