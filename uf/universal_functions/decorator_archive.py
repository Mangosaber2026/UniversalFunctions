# ⚓ Anchor for this module: [[decorator-archive-anchor|decorator_archive.py]] 
# 🔗 Parent package: [[#universal-functions-anchor|universal_functions]] 

import collections.abc as cabc

from .. import validators as vls


# ⚓ cls_deco_superposition anchor: [[cls-deco-superposition-anchor|cls_deco_superposition()]] 
 #* 📝 Decorates all functions of a class with provided decorators
def cls_deco_superposition(*decorators):

    vls.SequenceValidate(cabc.Callable, ...)(value=decorators, name="decorators")     # pyright: ignore[reportArgumentType]
    deco_composer = deco_superposition(*decorators)

    def inner(cls):

        for name, func in vars(cls).items():
            if callable(func) and not name.startswith("_"):
                setattr(cls, name, deco_composer(func))

        return cls
    
    return inner


# ⚓ deco_superposition anchor: [[deco-superposition-anc 
 #* 📝 Decorates a function with provided decorators
def deco_superposition(*decorators):

    vls.SequenceValidate(cabc.Callable, ...)(value=decorators, name="decorators")     # pyright: ignore[reportArgumentType]

    def inner_deco(func):

        for decorator in reversed(decorators):
            func = decorator(func)

        return func
    
    return inner_deco