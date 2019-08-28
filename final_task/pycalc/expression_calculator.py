from pycalc.constants_and_operations import (FUNCTIONS, OPERATIONS, LOGICAL_OPERATIONS)


def has_brackets(expression: list) -> bool:
    return '(' in expression and ')' in expression


def find_brackets(expression: list) -> tuple:
    end_index = expression.index(')')
    start_index = end_index - expression[end_index::-1].index('(')
    return start_index, end_index


def remove_brackets(expression: list):
    """ replaces brackets with the value inside them """
    start_index, end_index = find_brackets(expression)
    result = [convert(x) for x in calculate(expression[start_index + 1:end_index])]
    del expression[start_index:end_index]
    expression[start_index] = result[0]

    if start_index > 0:  # computes if there is a function before brackets
        if expression[start_index - 1] in FUNCTIONS:
            try:
                expression[start_index] = FUNCTIONS[expression[start_index - 1]](*result)
            except TypeError as e:
                raise Exception(e)
            del expression[start_index - 1]


def get_operation_position(expression: list, set_expression: set) -> int:
    """ returns index of operation according priority """
    for operation in ({'^'}, {'//', '%', '/', '*'}, {'-', '+'}):
        intersection = operation & set_expression
        if intersection:
            if intersection == {'^'}:
                position = len(expression) - 1 - expression[::-1].index("^")
            else:
                position = min([expression.index(x) for x in intersection])
            return position
    raise Exception("no operator found")


def calculate(expression: list) -> list:
    """ performs sequence of OPERATIONS in expression """
    prepare_expression(expression)
    set_expression = set(expression)
    while {'^', '//', '%', '/', '*', '-', '+'} & set_expression:
        position = get_operation_position(expression, set_expression)
        operation = OPERATIONS[expression[position]]

        expression[position + 1] = operation(  # position+1 because delete [pos-1:pos+1]
            convert(expression[position - 1]),  # arg1
            convert(expression[position + 1]))  # arg2
        del expression[position - 1: position + 1]
        set_expression = set(expression)
    return [calculate_logical_expression(expression)] if has_logical_operation(expression) else expression


def has_logical_operation(expression: list) -> bool:
    for logical_operation in LOGICAL_OPERATIONS:
        if logical_operation in expression:
            return True
    return False


def calculate_logical_expression(expression: list) -> bool:
    for logical_operation in LOGICAL_OPERATIONS.keys():
        if logical_operation in expression:
            return LOGICAL_OPERATIONS[logical_operation](expression[0], expression[2])
    raise Exception("no operation found")


def calculate_expression(expression: list) -> list:
    """ preforms full calculation """
    while has_brackets(expression):
        remove_brackets(expression)
    else:
        return calculate(expression).pop(0)


def prepare_expression(expression: list):
    if not expression:
        raise Exception("empty expression")
    if expression[0] == '-':
        expression[1] = -convert(expression[1])
        del expression[0]
    if expression[0] == '+':
        del expression[0]

    for index, value in enumerate(expression):  # changes ['2', '*', '-', '3']  to  ['2', '*', '-3']
        if value in ['^', '//', '/', '%', '*', '+', ',']:
            if expression[index + 1] == '-':
                expression[index + 2] = -convert(expression[index + 2])
                del expression[index + 1]
    while ',' in expression:
        expression.remove(',')


def convert(value):
    """ converts string to int or float """
    if type(value) == str:
        try:
            if '.' in value:
                return float(value)
            else:
                return int(value)
        except Exception as e:
            raise Exception(f"invalid expression \"{value}\" | {e}")
    return value
