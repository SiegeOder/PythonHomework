from pycalc.expression_calculator import convert
from re import search


def check_expression(expression: str) -> str:
    if expression.count('(') != expression.count(')'):
        raise Exception('unbalanced brackets')
    if len(expression) == 0:
        raise Exception('empty expression')
    if search(r'^[-/*+<=>]+$', expression) \
            or search(r'[!=<>*/]+\s+[!=<>*/]', expression) \
            or search(r'\d+\s+\d', expression) or search(r'^[<!=>*/]', expression) \
            or search(r'[<!=>*/\+-]$', expression):
        raise Exception(f"invalid expression \"{expression}\"")
    expression = expression.replace(' ', '')
    while '+-' in expression or '-+' in expression or '--' in expression or '++' in expression:
        expression = expression.replace('+-', '-').replace('-+', '-').replace('--', '+').replace('++', '')
    return expression


def check_result(expression):
    if type(expression) == bool:
        return expression
    return convert(expression)
