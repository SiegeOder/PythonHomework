def parse_expression(string: str, constants: dict) -> list:
    for i in ['(', ')', '^', '//', '/', '%', '*', '+', '-', ',', '==', '!=', '>=', '<=', '>', '<']:
        tmp = ' ' + i + ' '
        string = string.replace(i, tmp)
    return [x for x in constants_to_values(string  # returns parsed list without spaces
                                           .replace(' /  / ', '//')
                                           .replace(" < =", "<=")
                                           .replace(" > =", ">=")
                                           .split(' '), constants) if x != '']


def constants_to_values(expression: list, constants: dict) -> list:
    """ changes constants to their values """
    for i, v in enumerate(expression):
        if v in constants:
            expression[i] = constants[v]
    return expression
