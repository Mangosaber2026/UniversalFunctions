# ⚓ Anchor for this module: [[quantum-func-validators-anchor|quantum_func_validators.py]] 
# 🔗 Parent package: [[#validators-anchor|validators]] 

import collections.abc as cabc
import functools as ft
import inspect as ins
import typing as tp

from . import quantum_validators as qtm_vls
from . import validation_classes as vcls


# ⚓ qtm_func_validator anchor: [[qtm-func-validator-anchor|qtm_func_validator()]] 
#* 📝 Validates a functions input values by using its annotations
def qtm_func_validator(func: cabc.Callable, *args, **kwargs):

    vcls.TypeValidate(expected=cabc.Callable)(value=func, name=func.__name__)     # pyright: ignore[reportArgumentType]
    sig = ins.signature(func)
    bound = sig.bind(*args, **kwargs)

    for name, value in bound.arguments.items():
        parameter = sig.parameters[name]
        type_ = parameter.annotation

        if type_ is parameter.empty:
            continue

        origin = tp.get_origin(type_)

        if origin in (list, tuple):
            qtm_vls.qtm_lt_validator(value=value, TYPE=type_, name=name)

        elif origin is tp.Annotated:
            qtm_vls.qtm_constr_validator(value=value, annotation=type_, name=name)

        else:
            vcls.TypeValidate(expected=type_)(value=value, name=name)

    return func


# ⚓ qtm_validation_decorator anchor: [[qtm-validation-decorator-anchor|qtm_validation_decorator()]] 
#* 📝 Decorates a function which then uses [[#qtm-func-validator-anchor|qtm_func_validator()]] to verify the inputs
def qtm_validation_decorator(func: cabc.Callable):

    vcls.TypeValidate(expected=cabc.Callable)(value=func, name=func.__name__)   # pyright: ignore[reportArgumentType]

    @ft.wraps(func)
    def wrapper(*args, **kwargs):

        qtm_func_validator(func, *args, **kwargs)
        
        return func(*args, **kwargs)
    
    return wrapper