# ⚓ Anchor for this module: [[classes-to-dictionary-anchor|classes_to_dictionary.py]] 
# 🔗 Parent package: [[#universal-functions-anchor|universal_functions]] 

from .. import validators as vls


# ⚓ classes_to_dict anchor: [[classes-to-dict-anchor|classes_to_dict()]] 
#* 📝 Creates and returns a dictionary of provided class
#* 📝 mapping its function names with the function
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