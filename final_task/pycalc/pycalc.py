from argparse import ArgumentParser

from pycalc.constants_and_operations import (CONSTANTS, FUNCTIONS)
from pycalc.expression_calculator import calculate_expression
from pycalc.expression_parser import parse_expression
from pycalc.module_appender import import_all_modules
from pycalc.valid_checks import (check_expression, check_result)


def parse_arguments() -> str:
    argument_parser = ArgumentParser(description='Pure-python command-line calculator.',
                                     usage='%(prog)s [-h] EXPRESSION [-m MODULE [MODULE ...]]',
                                     prog='pycalc')
    argument_parser.add_argument('expression', metavar='EXPRESSION', type=str, help='expression string to evaluate')
    argument_parser.add_argument('-m', '--use-modules', metavar='MODULE', nargs='+',
                                 dest='modules', help="additional modules to use")
    args = argument_parser.parse_args()
    if args.modules:
        import_all_modules(args.modules, CONSTANTS, FUNCTIONS)
    return args.expression


def main():
    try:
        expression = check_expression(parse_arguments())
        expression = parse_expression(expression, CONSTANTS)
        print(check_result(calculate_expression(expression)))
    except Exception as e:
        print(f"ERROR: {e}")
