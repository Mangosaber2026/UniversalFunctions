# ⚓ Anchor for this module: [[errors-anchor|errors.py]] 
# 🔗 Parent package: [[#validators-anchor|validators]] 

from textwrap import dedent


# ⚓ ErrorDedent anchor: [[ErrorDedent-anchor|class ErrorDedent]] 
 #* 📝 Prints an error message with given error function and text
class ErrorDedent:
    name = "ErrorDedent"

    #* 📝 Initializes [[#ErrorDedent-anchor|ErrorDedent]] with a given error function
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

    #* 📝 Creates and returns an error function with given text
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

# ⚓ type_error anchor: [[type-error-anchor|type_error()]] 
#* 📝🔗 Creates and returns an instance of [[#ErrorDedent-anchor|ErrorDedent]] with TypeError
def type_error():
    return ErrorDedent(TypeError)

# ⚓ value_error anchor: [[value-error-anchor|value_error()]] 
#* 📝🔗 Creates and returns an instance of [[#ErrorDedent-anchor|ErrorDedent]] with ValueError
def value_error():
    return ErrorDedent(ValueError)

# ⚓ item_count_error anchor: [[item-count-error-anchor|item_count_error()]] 
#* 📝🔗 Creates and returns an instance of [[#ErrorDedent-anchor|ErrorDedent]] with [[#ItemCountError-anchor|ItemCountError]]
def item_count_error():
    return ErrorDedent(ItemCountError)

# ⚓ constraint_error anchor: [[constraint-error-anchor|constraint_error()]] 
#* 📝🔗 Creates and returns an instance of [[#ErrorDedent-anchor|ErrorDedent]] with [[#ConstraintError-anchor|ConstraintError]]
def constraint_error():
    return ErrorDedent(ConstraintError)

# ⚓ attribute_error anchor: [[attribute-error-anchor|attribute_error()]] 
#* 📝🔗 Creates and returns an instance of [[#ErrorDedent-anchor|ErrorDedent]] with AttributeError
def attribute_error():
    return ErrorDedent(AttributeError)


# ⚓ ItemCountError anchor: [[ItemCountError-anchor|class ItemCountError]] 
 #* 🚨 Additional error class showing a failure to meet a specific item count
 #* alongside Python's built-in ones
class ItemCountError(Exception):
    pass

# ⚓ ConstraintError anchor: [[ConstraintError-anchor|class ConstraintError]] 
 #* 🚨 Additional error class showing a failure to meet the constraint
 #* alongside Python's built-in ones
class ConstraintError(Exception):
    pass