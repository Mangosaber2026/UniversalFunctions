# ⚓ Anchor for this module: [[quantum-func-validators-anchor|quantum_func_validators.py]] 
# 🔗 Parent package: [[#validators-anchor|validators]] 

import collections.abc as cabc
import functools as ft
import inspect as ins
import typing as tp

from . import quantum_func_validators as qtm_ft_vls
from . import validation_classes as vcls


# ⚓ qtm_func_validator anchor: [[qtm-func-validator-anchor|qtm_func_validator()]] 
#* 📝 Validates a functions input values by using its annotations
def qtm_func_validator(func, *args, **kwargs):

    vcls.TypeValidate(cabc.Callable)(func, name=func.__name__)
    sig = ins.signature(func)
    bound = sig.bind(*args, **kwargs)

    for name, value in bound.arguments.items():
        parameter = sig.parameters[name]
        type_ = parameter.annotation

        if type_ is parameter.empty:
            continue

        origin = tp.get_origin(type_)

        if origin in (list, tuple):
            qtm_ft_vls.qtm_lt_validator(value, type_, name)

        elif origin is tp.Annotated:
            qtm_ft_vls.qtm_constr_validator(value, type_, name)

        else:
            vcls.TypeValidate(type_)(value, name=name)

    return func

# ⚓ qtm_validation_decorator anchor: [[qtm-validation-decorator-anchor|qtm_validation_decorator()]] 
#* 📝 Decorates a function which then uses [[#qtm-func-validator-anchor|qtm_func_validator()]] to verify the inputs
def qtm_validation_decorator(func):

    vcls.TypeValidate(cabc.Callable)(func, name=func.__name__)

    @ft.wraps(func)
    def wrapper(*args, **kwargs):
        qtm_func_validator(func, *args, **kwargs)
        return func(*args, **kwargs)
    return wrapper