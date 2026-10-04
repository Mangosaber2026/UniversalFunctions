from typing import Any
from numbers import Real
from types import EllipsisType
from itertools import cycle
from collections.abc import Callable


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
    def __init__(self, expected: type | tuple[type, ...]):
        """Makes sure the entered value is a type object"""
        if isinstance(expected, tuple):
            for item in expected:
                if not isinstance(item, type):
                    raise TypeError(f"Entered value {item!r} is not a type object!")
            self.expected = expected

        elif isinstance(expected, type):
            self.expected = expected

        else:
            raise TypeError(f"Parameter 'expected' MUST be a type object or a tuple of type objects!")
    def __call__(self, value: Any, name: str | None = None) -> Any:
        """Validates the entered value, expected to be of expected type"""
        if name is not None and not isinstance(name, str):
            raise TypeError(f"Parameter 'name' MUST be a string object!")

        if not isinstance(value, self.expected):
            if type(self.expected) is type:
                if name is not None:
                    raise TypeError(f"{name} is not of expected type {self.expected.__name__!r}!")
                raise TypeError(f"{value!r} is not of expected type {self.expected.__name__!r}!")
            elif type(self.expected) is tuple:
                if name is not None:
                    raise TypeError(f"{name} is not of expected type {self.expected!r}!")
                raise TypeError(f"{value!r} is not of expected type {self.expected!r}!")
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
        self._validator(expected)
        self.expected = expected

class Positive:
    """
    Makes sure the entered value is positive.

    >>> Positive()(50)
    50
    """
    def __call__(self, value: Real, name: str|None = None) -> Real:
        """Validates the entered value, expected to be positive (above 0)"""
        if name is not None:
            real_validate()(value, name)
        else:
            real_validate()(value)
        if value <= 0:
            raise ValueError(f"Entered value is expected to be greater than 0!")
        return value

class LessThan(RealValidationParent):
    """
    Makes sure the entered value is less than expected value.

    >>> LessThan(75)(10)
    10
    """
    def __call__(self, value: Real, name: str|None = None) -> Real:
        """Validates the entered value, expected to be less than expected value"""
        self._validator(value)
        if name is not None:
            str_validate()(name, "name")
        if value >= self.expected:
            raise ValueError(f"Entered value ({name}) is expected to be less than {self.expected!r}!")
        return value

class LessOrEqual(RealValidationParent):
    """
    Makes sure the entered value is less than or equal to expected value.

    >>> LessOrEqual(100)(90)
    90
    >>> LessOrEqual(50)(50)
    50
    """
    def __call__(self, value: Real, name: str|None = None) -> Real:
        """Validates the entered value, expected to be less than or equal to expected value"""
        self._validator(value)
        if name is not None:
            str_validate()(name, "name")
        if value > self.expected:
            raise ValueError(f"Entered value ({name}) is expected to be less than or equal to {self.expected!r}!")
        return value


class GreaterThan(RealValidationParent):
    """
    Makes sure the entered value is greater than expected value.

    >>> GreaterThan(5)(10)
    10
    """
    def __call__(self, value: Real, name: str|None = None) -> Real:
        """Validates the entered value, expected to be greater than expected value"""
        self._validator(value)
        if name is not None:
            str_validate()(name, "name")
        if self.expected >= value:
            raise ValueError(f"Entered value ({name}) is expected to be greater than {self.expected!r}!")
        return value

class GreaterOrEqual(RealValidationParent):
    """
    Makes sure the entered value is greater than or equal to expected value.

    >>> GreaterOrEqual(5)(10)
    10
    >>> GreaterOrEqual(5)(5)
    5
    """
    def __call__(self, value: Real, name: str|None = None) -> Real:
        """Validates the entered value, expected to be greater than or equal to expected value"""
        self._validator(value)
        if name is not None:
            str_validate()(name, "name")
        if self.expected > value:
            raise ValueError(f"Entered value ({name}) is expected to be greater than or equal to {self.expected!r}!")
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
    def __init__(self, *expected: type | EllipsisType, **kwargs) -> None:
        """Validates and sets the tuple to a variable"""
        for item in expected:
            if item is not Ellipsis:
                TypeValidate(type)(item)
            else:
                if expected[-1] is not Ellipsis:
                    raise ValueError(f"Entered value ({expected[-1]}) is expected to be an ellipsis type!")

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
        if not isinstance(value, (tuple, list)):
            raise TypeError(f"Entered value ({name}) is expected to be a tuple or list!")

        if name is not None:
            str_validate()(name, "name")
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
                raise ValueError(f"Entered value ({name}) must have the same number of elements as the provided expected tuple!")
            for expected_type, actual_value in zip(self.expected, value):
                TypeValidate(expected_type)(actual_value)
                for func in self.callables:
                    func(actual_value)
        return value