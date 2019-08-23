from pycalc.expression_calculator import (convert)
from re import (search)


def check_expression(expression: str) -> str:
    if expression.count('(') != expression.count(')'):
        print("ERROR: unbalanced brackets")
        raise Exception
    if len(expression) == 0:
        print('ERROR: empty expression')
        raise Exception
    if search(r'^[-/*+<=>]+$', expression) \
            or search(r'[!=<>*/]+\s+[!=<>*/]', expression) \
            or search(r'\d+\s+\d', expression) or search(r'^[<!=>*/]', expression) \
            or search(r'[<!=>*/\+-]$', expression):
        print(f"ERROR: invalid expression \"{expression}\"")
        raise Exception
    expression = expression.replace(' ', '')
    while '+-' in expression or '-+' in expression or '--' in expression or '++' in expression:
        expression = expression.replace('+-', '-').replace('-+', '-').replace('--', '+').replace('++', '')
    return expression


def check_result(expression):
    if type(expression) == bool:
        return expression
    return convert(expression)
