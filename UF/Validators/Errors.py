"""
This module provides a collection of error message deliverers and separate errors created by the author which
are not normally provided with Python.

The custom errors in this module can be used just like any other conventional error provided by Python itself.
"""

from textwrap import dedent
from typing import Callable, Final, Literal


class ErrorDedent:
    """
    This class is the error raiser for the other validators found in this package (UF).

    The use of this class is to make the error message be printed with some formatting instead of the conventional
    way it would be printed otherwise.

    >>> print(ErrorDedent(TypeError)("This is a TypeError!"))
    TypeError
    <BLANKLINE>
    This is a TypeError!
    """
    name: Final[Literal["ErrorDedent"]] = "ErrorDedent"
    def __init__(self, error_func) -> None:
        if not isinstance(error_func, type) or not issubclass(error_func, Exception):
            raise TypeError(dedent(f"""
                TypeError:
                Validator: ErrorDedent
                Parameter 'error_func' MUST be an error class!
                expected: Exception subclass
                received: {error_func}
                """).strip())
        self.error_func = error_func

    def __call__(self, text: str) -> Exception:
        if not isinstance(text, str):
            raise TypeError(dedent(f"""
                TypeError:
                Validator: {self.name} 
                Parameter 'text' MUST be a string object!
                expected: str
                received: {text}
                """).strip())
        return self.error_func(dedent(f"""
            {self.error_func.__name__}
            
            {text}
            """).strip())

def type_error() -> Callable:
    """
    This function returns a callable type error function.

    >>> print(type_error()("This is a TypeError!"))
    TypeError
    <BLANKLINE>
    This is a TypeError!

    :return: ErrorDedent function
    """
    return ErrorDedent(TypeError)

def value_error() -> Callable:
    """
    This function returns a callable value error function.

    >>> print(value_error()("This is a ValueError!"))
    ValueError
    <BLANKLINE>
    This is a ValueError!

    :return: ErrorDedent function
    """
    return ErrorDedent(ValueError)

def item_count_error() -> Callable:
    """
    This function returns a callable item count error function.

    >>> print(item_count_error()("This is an Item Count Error!"))
    ItemCountError
    <BLANKLINE>
    This is an Item Count Error!

    :return: ErrorDedent function
    """
    return ErrorDedent(ItemCountError)

def constraint_error() -> Callable:
    """
    This function returns a callable constraint error function.

    >>> print(constraint_error()("This is a Constraint Error!"))
    ConstraintError
    <BLANKLINE>
    This is a Constraint Error!

    :return: ErrorDedent function
    """
    return ErrorDedent(ConstraintError)

def attribute_error() -> Callable:
    """
    This function returns a callable attribute error function.

    >>> print(attribute_error()("This is an Attribute Error!"))
    AttributeError
    <BLANKLINE>
    This is an Attribute Error!

    :return: ErrorDedent function
    """
    return ErrorDedent(AttributeError)

class ItemCountError(Exception):
    """
    This exception is raised when an item count does not match the expected count.

    >>> print(ItemCountError("This is an Item Count Error!"))
    This is an Item Count Error!
    """

class ConstraintError(Exception):
    """
    This exception is raised when an item does not pass the expected constraint.

    >>> print(ConstraintError("This is a Constraint Error!"))
    This is a Constraint Error!
    """