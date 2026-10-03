from typing import Any
from numbers import Real


class TypeValidate:
    """Makes sure the entered value is of correct type"""
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
    def __call__(self, value: Any, name: str | None = None) -> bool:
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
        return True

def int_validate() -> TypeValidate:
    """Makes sure the entered value is an integer with TypeValidate"""
    return TypeValidate(int)

def str_validate() -> TypeValidate:
    """Makes sure the entered value is a string with TypeValidate"""
    return TypeValidate(str)

def real_validate() -> TypeValidate:
    """Makes sure the entered value is a real number with TypeValidate"""
    return TypeValidate(Real)

class RealValidationParent:
    def __init__(self, expected: Real) -> None:
        self._validator = real_validate()
        self._validator(expected)
        self.expected = expected

class Positive:
    """Makes sure the entered value is positive"""
    def __call__(self, value: Real, name: str|None = None) -> bool:
        """Validates the entered value, expected to be positive (0 included)"""
        if name is not None:
            real_validate()(value, name)
        else:
            real_validate()(value)
        if value <= 0:
            raise ValueError(f"Entered value is expected to be greater than 0!")
        return True

class LessThan(RealValidationParent):
    """Makes sure the entered value is less than expected value"""
    def __call__(self, value: Real, name: str|None = None) -> bool:
        """Validates the entered value, expected to be less than expected value"""
        self._validator(value)
        if name is not None:
            str_validate()(name, "name")
        if value >= self.expected:
            raise ValueError(f"Entered value ({name}) is expected to be less than {self.expected!r}!")
        return True

class LessOrEqual(RealValidationParent):
    """Makes sure the entered value is less than or equal to expected value"""
    def __call__(self, value: Real, name: str|None = None) -> bool:
        """Validates the entered value, expected to be less than or equal to expected value"""
        self._validator(value)
        if name is not None:
            str_validate()(name, "name")
        if value > self.expected:
            raise ValueError(f"Entered value ({name}) is expected to be less than or equal to {self.expected!r}!")
        return True


class GreaterThan(RealValidationParent):
    """Makes sure the entered value is greater than expected value"""
    def __call__(self, value: Real, name: str|None = None) -> bool:
        """Validates the entered value, expected to be greater than expected value"""
        self._validator(value)
        if name is not None:
            str_validate()(name, "name")
        if self.expected >= value:
            raise ValueError(f"Entered value ({name}) is expected to be greater than {self.expected!r}!")
        return True

class GreaterOrEqual(RealValidationParent):
    """Makes sure the entered value is greater than or equal to expected value"""
    def __call__(self, value: Real, name: str|None = None) -> bool:
        """Validates the entered value, expected to be greater than or equal to expected value"""
        self._validator(value)
        if name is not None:
            str_validate()(name, "name")
        if self.expected > value:
            raise ValueError(f"Entered value ({name}) is expected to be greater than or equal to {self.expected!r}!")
        return True

class TupleValidate:
    """Makes sure the entered value is a tuple of any value"""
    def __init__(self, *expected: type) -> None:
        """Validates and sets the tuple to a variable"""
        for item in expected:
            TypeValidate(type)(item)
        self.expected = expected

    def __call__(self, value: tuple, name: str|None = None) -> bool:
        """Validates the entered value, expected to be a tuple of expected value/s"""
        TypeValidate(tuple)(value)
        if name is not None:
            str_validate()(name, "name")
        if len(self.expected) != len(value):
            raise ValueError(f"Entered value ({name}) must have the same number of elements as the provided expected tuple!")
        for expected_type, actual_value in zip(self.expected, value):
            TypeValidate(expected_type)(actual_value)
        return True