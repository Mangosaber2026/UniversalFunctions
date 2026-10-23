import collections.abc as cabc

from .. import validators as vls


def classes_to_dict(*classes):

    vls.SequenceValidate(type, ...)(classes, name="classes")
    dictionary = {}
    for cls in classes:
        dictionary.update({
            name: obj
            for name, obj in vars(cls).items()
            if callable(obj)
        })
    return dictionary