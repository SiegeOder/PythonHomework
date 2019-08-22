from pycalc.constants_and_operations import (functions, operations, logical_operations)


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
        if expression[start_index - 1] in functions:
            try:
                expression[start_index] = functions[expression[start_index - 1]](*result)
            except TypeError as e:
                print(f"ERROR: {e}")
                exit(5)
            del expression[start_index - 1]


def get_operation_position(expression: list, set_expression: set):
    """ returns index of operation according priority """
    for operation in ({'^'}, {'//', '%', '/', '*'}, {'-', '+'}):
        intersection = operation & set_expression
        if intersection:
            if intersection == {'^'}:
                position = len(expression) - 1 - expression[::-1].index("^")
            else:
                position = min([expression.index(x) for x in intersection])
            return position


def calculate(expression: list) -> list:
    """ performs sequence of operations in expression """
    prepare_expression(expression)
    set_expression = set(expression)
    while {'^', '//', '%', '/', '*', '-', '+'} & set_expression:
        position = get_operation_position(expression, set_expression)
        operation = operations[expression[position]]

        expression[position + 1] = operation(  # position+1 because delete [pos-1:pos+1]
            convert(expression[position - 1]),  # arg1
            convert(expression[position + 1]))  # arg2
        del expression[position - 1: position + 1]
        set_expression = set(expression)

    return [calculate_logical_expression(expression)] if has_logical_operation(expression) else expression


def has_logical_operation(expression: list) -> bool:
    for logical_operation in logical_operations:
        if logical_operation in expression:
            return True
    return False


def calculate_logical_expression(expression: list) -> bool:
    for logical_operation in logical_operations.keys():
        if logical_operation in expression:
            return logical_operations[logical_operation](expression[0], expression[2])


def calculate_expression(expression: list) -> list:
    """ preforms full calculation """
    while has_brackets(expression):
        remove_brackets(expression)
    else:
        return calculate(expression).pop(0)


def prepare_expression(expression: list):
    if not expression:
        print(f"ERROR: empty expression")
        exit(6)
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
            print(f"ERROR: invalid expression \"{value}\" | {e}")
            exit(4)
    return value
