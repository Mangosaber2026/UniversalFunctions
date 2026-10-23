import collections.abc as cabc

from .. import validators as vls


def cls_deco_superposition(*decorators):

    vls.SequenceValidate(cabc.Callable, ...)(decorators, name="decorators")
    deco_composer = deco_superposition(*decorators)

    def inner(cls):
        for name, func in vars(cls).items():
            if callable(func) and not name.startswith("_"):
                setattr(cls, name, deco_composer(func))
        return cls
    return inner

def deco_superposition(*decorators):

    vls.SequenceValidate(cabc.Callable, ...)(decorators, name="decorators")
    def inner_deco(func):
        for decorator in reversed(decorators):
            func = decorator(func)

        return func
    return inner_deco