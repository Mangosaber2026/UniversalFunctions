from textwrap import dedent
from typing import Callable


class ErrorDedent:
    def __init__(self, error_func) -> None:
        if not isinstance(error_func, type) or not issubclass(error_func, Exception):
            raise TypeError(dedent(f"""
                ErrorDedent:
                Parameter 'error_func' MUST be an error class!
                expected: Exception subclass
                received: {error_func}
                """).strip())
        self.error_func = error_func

    def __call__(self, text: str) -> Exception:
        if not isinstance(text, str):
            raise TypeError(dedent(f"""
                Parameter 'text' MUST be a string object!
                expected: str
                received: {text}
                """).strip())
        return self.error_func(dedent(text).strip())

def type_error() -> Callable:
    return ErrorDedent(TypeError)

def value_error() -> Callable:
    return ErrorDedent(ValueError)

class ItemCountError(Exception):
    """
    This exception is raised when an item count does not match the expected count.
    """

class ConstraintError(Exception):
    """
    This exception is raised when an item does not pass the expected constraint.
    """