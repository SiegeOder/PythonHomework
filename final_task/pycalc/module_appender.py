def append_module(module, constants: dict, functions: dict):
    """ appends module's constants and functions to dicts """
    for attribute in dir(module):
        if not attribute.startswith('__'):
            if callable(getattr(module, attribute)):
                functions[attribute] = getattr(module, attribute)
            else:
                constants[attribute] = getattr(module, attribute)


def append_module_by_name(module_name: str, constants: dict, functions: dict):
    try:
        module = __import__(module_name)
        append_module(module, constants, functions)
    except Exception as e:
        raise Exception(f"{e} | MODULE IMPORTING FAILED")


def import_all_modules(modules: list, constants: dict, functions: dict):
    if modules:
        for module in modules:
            append_module_by_name(module, constants, functions)
