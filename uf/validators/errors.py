from textwrap import dedent


class ErrorDedent:
    name = "ErrorDedent"

    def __init__(self, error_func):

        if not isinstance(error_func, type) or not issubclass(error_func, Exception):
            raise TypeError(dedent(f"""
                TypeError:
                
                Validator: ErrorDedent
                Parameter 'error_func' MUST be an error class!
                expected: Exception subclass
                received: {error_func}
                """).strip())

        self.error_func = error_func

    def __call__(self, text):

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

def type_error():
    return ErrorDedent(TypeError)

def value_error():
    return ErrorDedent(ValueError)

def item_count_error():
    return ErrorDedent(ItemCountError)

def constraint_error():
    return ErrorDedent(ConstraintError)

def attribute_error():
    return ErrorDedent(AttributeError)


class ItemCountError(Exception):
    pass

class ConstraintError(Exception):
    pass