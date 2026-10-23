import collections.abc as cabc
import itertools as itls
import numbers as num
import types as tps
import typing as tp

from .errors import constraint_error, item_count_error, type_error


class TypeValidate:
    name = "TypeValidate"

    def __init__(self, expected):

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

    def __call__(self, value, name = None):

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

def int_validate():
    return TypeValidate(int)

def str_validate():
    return TypeValidate(str)

def real_validate():
    return TypeValidate(num.Real)

class RealValidationParent:

    def __init__(self, expected):
        self._validator = real_validate()
        real_validate()(expected, name="expected")
        self.expected = expected

class Positive:

    name = "Positive"

    def __call__(self, value, name = None):
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
    name = "LessThan"

    def __call__(self, value, name = None):

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
    name = "LessOrEqual"

    def __call__(self, value, name = None):

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
    name = "GreaterThan"

    def __call__(self, value, name = None):

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
    name = "GreaterOrEqual"

    def __call__(self, value, name = None):

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

    name = "SequenceValidate"
    def __init__(self, *expected, **kwargs):

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
                TypeValidate(cabc.Callable)(func)

            self.callables = kwargs[callable_name]

    def __call__(self, value, name = None):

        if name is not None:
            str_validate()(name, "name")
            TypeValidate((tuple, list))(value, name=name)
        TypeValidate((tuple, list))(value)

        type_store = []
        if isinstance(self.expected[-1], tps.EllipsisType):
            for item in self.expected:
                if not isinstance(item, tps.EllipsisType):
                    type_store.append(item)

            for given_obj, expected_type in zip(value, itls.cycle(type_store)):
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
    
    def __init__(self, value, name = None):

        if name is not None:
            str_validate()(name, name="name")

        self.value = value
        self.name = name

    def __call__(self, *validation_funcs):
        
        SequenceValidate(cabc.Callable, ...)(validation_funcs, name="validation_funcs")
        for validator in validation_funcs:
            if self.name is not None:
                validator(self.value, name=self.name)

            else:
                validator(self.value)

        return self.value