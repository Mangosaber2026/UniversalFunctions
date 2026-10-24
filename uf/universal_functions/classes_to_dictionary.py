# Anchor for this module: [[classes-to-dictionary-anchor|classes_to_dictionary.py]]

from .. import validators as vls


# classes_to_dict anchor: [[classes-to-dict-anchor|classes_to_dict]]
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