"""
This module contains validation classes which are expected to be used as callable objects.

The classes themselves not only validate the given value against the expected type, but also
validate the parameters. After the entered value has passed the validation, it is simply returned, though
if it does not pass validation, an error is raised.
"""
 #* 📝 File type: Python type stub (.pyi)
 #* 📝 Purpose: Describes the module's interface for documentation,
 #* 📝         editor support, and static type checking.
 #* 📝 Runtime: Contains no implementation; see the corresponding
 #* 📝         .py file for executable code.

import collections.abc as cabc  # noqa: I001
import numbers as num
import types as tps
import typing as tp


#* 📝 Type for any real number
type RealType = float | int | num.Real

#* 📝 Type for any sequence
type SequenceType = tuple | list 

#* 📝 Type for the name of a given variable
type NameType = str | None


class TypeValidate:
    """
    Makes sure the entered value is of correct type.

    >>> TypeValidate(float)(-30.9)
    -30.9
    >>> TypeValidate(str)('Hello World')
    'Hello World'
    >>> TypeValidate(int)(-10)
    -10
    >>> TypeValidate((list, int))([1, "2"])
    [1, '2']
    """
    name: tp.Final[str]

    def __init__(self, expected: type | tuple[type, ...]) -> None:
            """
            Makes sure the entered value is a type object.
    
            :param expected: type object or tuple of type objects
    
            :return: None
            """

    def __call__(self, value: tp.Any, name: NameType = None) -> tp.Any:
            """
            Validates the entered value, expected to be of expected type.
    
            :param value: any object of any type.
    
            :param name: the name of the value.
    
            :return: validated value.
            """

def int_validate() -> TypeValidate:
    """
    Makes sure the entered value is an integer with TypeValidate.

    >>> int_validate()(-39)
    -39

    :return: TypeValidate object with int as expected type.
    """


def str_validate() -> TypeValidate:
    """
    Makes sure the entered value is a string with TypeValidate.

    >>> str_validate()('Hello World')
    'Hello World'

    :return: TypeValidate object with str as expected type.
    """


def real_validate() -> TypeValidate:
    """
    Makes sure the entered value is a real number with TypeValidate.

    >>> real_validate()(-10.5)
    -10.5

    :return: TypeValidate object with numbers.Real as expected type.
    """


class RealValidationParent:
    """
    Parent class for classes which require an expected real number value when an instance is made of them.
    """
    def __init__(self, expected: RealType) -> None:
        """
        Makes sure the entered expected value is a real number.

        :param expected: expected real number value.

        :return: None
        """


class Positive:
    """
    Makes sure the entered value is positive.

    >>> Positive()(50)
    50
    """
    name: tp.Final

    def __call__(self, value: RealType, name: NameType = None) -> RealType:
        """
        Validates the entered value, expected to be positive (above 0).

        :param value: any real number.

        :param name: the name of the value.

        :return: validated value.
        """


class LessThan(RealValidationParent):
    """
    Makes sure the entered value is less than expected value.

    >>> LessThan(75)(10)
    10
    """
    name: tp.Final

    def __call__(self, value: RealType, name: NameType = None) -> RealType:
        """
        Validates the entered value, expected to be less than expected value.

        :param value: any real number.

        :param name: the name of the value.

        :return: validated value.
        """


class LessOrEqual(RealValidationParent):
    """
    Makes sure the entered value is less than or equal to expected value.

    >>> LessOrEqual(100)(90)
    90
    >>> LessOrEqual(50)(50)
    50
    """
    name: tp.Final

    def __call__(self, value: RealType, name: NameType = None) -> RealType:
        """
        Validates the entered value, expected to be less than or equal to expected value.

        :param value: any real number.

        :param name: the name of the value.

        :return: validated value.
        """


class GreaterThan(RealValidationParent):
    """
    Makes sure the entered value is greater than expected value.

    >>> GreaterThan(5)(10)
    10
    """
    name: tp.Final

    def __call__(self, value: RealType, name: NameType = None) -> RealType:
        """
        Validates the entered value, expected to be greater than expected value.

        :param value: any real number.

        :param name: the name of the value.

        :return: validated value.
        """


class GreaterOrEqual(RealValidationParent):
    """
    Makes sure the entered value is greater than or equal to expected value.

    >>> GreaterOrEqual(5)(10)
    10
    >>> GreaterOrEqual(5)(5)
    5
    """
    name: tp.Final

    def __call__(self, value: RealType, name: NameType = None) -> RealType:
        """
        Validates the entered value, expected to be greater than or equal to expected value.

        :param value: any real number.

        :param name: the name of the value.

        :return: validated value.
        """


class SequenceValidate:
    """
    Makes sure the entered value is a sequence of any value.

    >>> validator = SequenceValidate(
    ...     list,
    ...     list,
    ...     callable_items=(SequenceValidate(Real, ...),)
    ... )
    >>> validator([[1, 2], [3, 4]])
    [[1, 2], [3, 4]]
    """
    name: tp.Final[str]
    
    def __init__(self, *expected: type | tps.EllipsisType, **kwargs) -> None:
        """
        Makes sure the entered expected value is a sequence of any value.

        :param expected: type object or tuple of type objects

        :return: None
        """

    def __call__(self, value: SequenceType, name: NameType = None) -> SequenceType:
        """
        Validates the entered value, expected to be a sequence of any value.

        :param value: any sequence of any type.

        :param name: the name of the value.

        :return: validated value.
        """

class ComboValidate:
    """
    This class takes a value (and name if provided) and uses the given validators to validate it.
    """
    def __init__(self, value: tp.Any, name: NameType = None) -> None:
        """
        This initiates the validator class with a given value and if desired, it's name.
            
        :param value: any object of any type.

        :param name: the name of the value.

        :return: None
        """

    def __call__(self, *validation_funcs: cabc.Callable) -> tp.Any:
        """
        This executes all the validators given for validation_funcs by using the provided value and it's name if given.
        
        :param validation_funcs: validator functions.
        
        :return: validated value.
        """