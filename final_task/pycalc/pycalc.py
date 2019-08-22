from pycalc.constants_and_operations import (constants, functions)
from pycalc.expression_calculator import (calculate_expression)
from pycalc.expression_parser import (parse_expression)
from pycalc.module_appender import (import_all_modules)
from pycalc.valid_checks import (check_expression, check_result)
from argparse import (ArgumentParser)


def parse_arguments():
    argument_parser = ArgumentParser(description='Pure-python command-line calculator.',
                                     usage='%(prog)s [-h] EXPRESSION [-m MODULE [MODULE ...]]',
                                     prog='pycalc')
    argument_parser.add_argument('expression', metavar='EXPRESSION', type=str, help='expression string to evaluate')
    argument_parser.add_argument('-m', '--use-modules', metavar='MODULE', nargs='+',
                                 dest='modules', help="additional modules to use")
    args = argument_parser.parse_args()
    if args.modules:
        import_all_modules(args.modules, constants, functions)
    return args.expression


def main():
    expression = check_expression(parse_arguments())
    expression = parse_expression(expression, constants)
    print(check_result(calculate_expression(expression)))
