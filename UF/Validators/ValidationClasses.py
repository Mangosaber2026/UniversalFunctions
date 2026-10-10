"""
This module contains validation classes which are expected to be used as callable objects.

The classes themselves not only validate the given value against the expected type, but also
validate the parameters. After the entered value has passed the validation, it is simply returned, though
if it does not pass validation, an error is raised.
"""

from typing import Any, Final, Literal
from numbers import Real
from types import EllipsisType
from itertools import cycle
from collections.abc import Callable
from .Errors import type_error, constraint_error, item_count_error


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
    name: Final[Literal["TypeValidate"]] = "TypeValidate"
    def __init__(self, expected: type | tuple[type, ...]) -> None:
        """Makes sure the entered value is a type object"""
        if isinstance(expected, tuple):
            for item in expected:
                if not isinstance(item, type):
                    raise type_error()(f"""
                        Validator: {self.name}
                        Entered value {item!r} is not a type object!
                        Expected: type object
                        Received: 
                            Item: {item}
                            Type: {type(item).__name__}
                        """)
            self.expected = expected

        elif isinstance(expected, type):
            self.expected = expected

        else:
            raise type_error()(f"""
                Validator: {self.name}
                Parameter 'expected' MUST be a type object or a tuple of type objects!
                Expected: type|tuple
                Received: 
                    Given value for expected: {expected}
                    Type: {type(expected).__name__}
                """)

    def __call__(self, value: Any, name: str | None = None) -> Any:
        """Validates the entered value, expected to be of expected type"""
        if name is not None and not isinstance(name, str):
            raise type_error()(f"""
            Validator: {self.name}
            Parameter 'name' MUST be a string object!
            Expected: str (name of value)
            Received: 
                Name: {name}
                Type: {type(name).__name__}
            """)

        if not isinstance(value, self.expected):
            value_type = type(value).__name__

            if type(self.expected) is type:
                expected_type: str = self.expected.__name__

                if name is not None:
                    raise type_error()(f"""
                        Validator: {self.name}
                        Parameter {name!r} is not of expected type {expected_type!r}!
                        Expected: {expected_type}
                        Received: 
                            Name: {name}
                            value: {value}
                            Type: {value_type}
                        """)
                raise type_error()(f"""
                    Validator: {self.name}
                    Parameter value is not of expected type {expected_type!r}!
                    Expected: {expected_type}
                    Received:
                        Value: {value}
                        Type: {value_type}
                    """)

            elif type(self.expected) is tuple:
                expected_type: tuple[type, ...] = self.expected

                if name is not None:
                    raise type_error()(f"""
                        Validator: {self.name}
                        Parameter {name!r} is not of expected type {expected_type!r}!
                        Expected: {expected_type}
                        Received:
                            Name: {name}
                            Value: {value}
                            Type: {value_type}
                        """)
                raise type_error()(f"""
                    Validator: {self.name}
                    Parameter value is not of expected type {expected_type!r}!
                    Expected: {expected_type}
                    Received:
                        Value: {value}
                        Type: {value_type}
                    """)
        return value

def int_validate() -> TypeValidate:
    """
    Makes sure the entered value is an integer with TypeValidate.

    >>> int_validate()(-39)
    -39
    """
    return TypeValidate(int)

def str_validate() -> TypeValidate:
    """
    Makes sure the entered value is a string with TypeValidate.

    >>> str_validate()('Hello World')
    'Hello World'
    """
    return TypeValidate(str)

def real_validate() -> TypeValidate:
    """
    Makes sure the entered value is a real number with TypeValidate.

    >>> real_validate()(-10.5)
    -10.5
    """
    return TypeValidate(Real)

class RealValidationParent:
    """
    Parent class for classes which require an expected real number value when an instance is made of them.
    """
    def __init__(self, expected: Real) -> None:
        self._validator = real_validate()
        real_validate()(expected, name="expected")
        self.expected = expected

class Positive:
    """
    Makes sure the entered value is positive.

    >>> Positive()(50)
    50
    """
    name: Final[Literal["Positive"]] = "Positive"
    def __call__(self, value: Real, name: str|None = None) -> Real:
        """Validates the entered value, expected to be positive (above 0)"""
        if name is not None:
            TypeValidate(str)(name, name="name")
            real_validate()(value, name)
            value_name = name
        else:
            value_name = "value"
            real_validate()(value, name=value_name)

        if value <= 0:
            raise constraint_error()(f"""
                Validator: {self.name}
                Parameter value is expected to be greater than 0!
                Expected: value > 0
                Received:
                    Name: {value_name}
                    Value: {value}
                """)
        return value

class LessThan(RealValidationParent):
    """
    Makes sure the entered value is less than expected value.

    >>> LessThan(75)(10)
    10
    """
    name: Final[Literal["LessThan"]] = "LessThan"
    def __call__(self, value: Real, name: str|None = None) -> Real:
        """Validates the entered value, expected to be less than expected value"""
        if name is not None:
            str_validate()(name, name="name")
            real_validate()(value, name=name)
            value_name = name
        else:
            value_name = "value"
            real_validate()(value, name=value_name)

        if value >= self.expected:
            raise constraint_error()(f"""
                Validator: {self.name}
                Parameter value is expected to be less than {self.expected!r}!
                Expected: {self.expected}
                Received:
                    Name: {value_name}
                    Value: {value}
                """)
        return value

class LessOrEqual(RealValidationParent):
    """
    Makes sure the entered value is less than or equal to expected value.

    >>> LessOrEqual(100)(90)
    90
    >>> LessOrEqual(50)(50)
    50
    """
    name: Final[Literal["LessOrEqual"]] = "LessOrEqual"
    def __call__(self, value: Real, name: str|None = None) -> Real:
        """Validates the entered value, expected to be less than or equal to expected value"""
        if name is not None:
            str_validate()(name, "name")
            real_validate()(value, name=name)
            value_name = name
        else:
            value_name = "value"
            real_validate()(value, name=value_name)

        if value > self.expected:
            raise constraint_error()(f"""
                Validator: {self.name}
                Parameter value is expected to be less than or equal to {self.expected!r}!
                Expected: {self.expected}
                Received:
                    Name: {value_name}
                    Value: {value}
                """)
        return value


class GreaterThan(RealValidationParent):
    """
    Makes sure the entered value is greater than expected value.

    >>> GreaterThan(5)(10)
    10
    """
    name: Final[Literal["GreaterThan"]] = "GreaterThan"
    def __call__(self, value: Real, name: str|None = None) -> Real:
        """Validates the entered value, expected to be greater than expected value"""
        if name is not None:
            str_validate()(name, "name")
            real_validate()(value, name=name)
            value_name = name
        else:
            value_name = "value"
            real_validate()(value, name=value_name)

        if self.expected >= value:
            raise constraint_error()(f"""
                Validator: {self.name}
                Parameter value is expected to be greater than {self.expected!r}!
                Expected: {self.expected}
                Received:
                    Name: {value_name}
                    Value: {value}
                """)
        return value

class GreaterOrEqual(RealValidationParent):
    """
    Makes sure the entered value is greater than or equal to expected value.

    >>> GreaterOrEqual(5)(10)
    10
    >>> GreaterOrEqual(5)(5)
    5
    """
    name: Final[Literal["GreaterOrEqual"]] = "GreaterOrEqual"
    def __call__(self, value: Real, name: str|None = None) -> Real:
        """Validates the entered value, expected to be greater than or equal to expected value"""
        if name is not None:
            str_validate()(name, "name")
            real_validate()(value, name=name)
            value_name = name
        else:
            value_name = "value"
            real_validate()(value, name=value_name)

        if self.expected > value:
            raise constraint_error()(f"""
                Validator: {self.name}
                Parameter value is expected to be greater than or equal to {self.expected!r}!
                Expected: {self.expected}
                Received:
                    Name: {value_name}
                    Value: {value}
                """)
        return value

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
    name: Final[Literal["SequenceValidate"]] = "SequenceValidate"
    def __init__(self, *expected: type | EllipsisType, **kwargs) -> None:
        """Validates and sets the tuple to a variable"""
        for item in expected:
            if item is not Ellipsis:
                TypeValidate(type)(item)
            else:
                if expected[-1] is not Ellipsis:
                    raise type_error()(f"""
                        Validator: {self.name}
                        The last item in 'expected' is expected to be an ellipsis type!
                        Expected: ellipsis type
                        Received:
                            name: {type(expected[-1]).__name__}
                            item: {expected[-1]}
                        """)

        self.expected = expected

        callable_name = "callable_items"
        self.callables = ()

        if callable_name in kwargs:
            TypeValidate(tuple)(kwargs[callable_name], callable_name)
            for func in kwargs[callable_name]:
                TypeValidate(Callable)(func)

            self.callables = kwargs[callable_name]

    def __call__(self, value: tuple|list, name: str|None = None) -> tuple|list:
        """Validates the entered value, expected to be a tuple of expected value/s"""
        if name is not None:
            str_validate()(name, "name")
            TypeValidate((tuple, list))(value, name=name)
        TypeValidate((tuple, list))(value)

        type_store = []
        if isinstance(self.expected[-1], EllipsisType):
            for item in self.expected:
                if not isinstance(item, EllipsisType):
                    type_store.append(item)

            for given_obj, expected_type in zip(value, cycle(type_store)):
                TypeValidate(expected_type)(given_obj)
                for func in self.callables:
                    func(given_obj)

        else:
            if len(self.expected) != len(value):
                raise item_count_error()(f"""
                    Validator: {self.name}
                    Parameter value ({name}) must have the same number of elements as the provided expected tuple!
                    Expected number of items: {len(self.expected)}
                    Received: 
                        Name: {name}
                        Value: {value}
                        Number of items in value: {len(value)}
                    """)
            for expected_type, actual_value in zip(self.expected, value):
                TypeValidate(expected_type)(actual_value)
                for func in self.callables:
                    func(actual_value)
        return value

class ComboValidate:
    """
    This class takes a value (and name if provided) and uses the given validators to validate it.
    """
    def __init__(self, value: Any, name: str | None = None) -> None:
        """
        This initiates the validator class with a given value and if desired, it's name.
        :param value: any object of any type.
        :param name: the name of the value.
        """
        if name is not None:
            str_validate()(name, name="name")

        self.value = value
        self.name = name

    def __call__(self, *validation_funcs: Callable) -> Any:
        """
        This executes all the validators given for validation_funcs by using the provided value and it's name if given.
        :param validation_funcs: validator functions.
        :return: validated value.
        """
        SequenceValidate(Callable, ...)(validation_funcs, name="validation_funcs")
        for validator in validation_funcs:
            if self.name is not None:
                validator(self.value, name=self.name)

            else:
                validator(self.value)

        return self.value