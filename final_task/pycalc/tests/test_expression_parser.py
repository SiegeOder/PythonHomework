import unittest
from pycalc.expression_parser import (parse_expression)
from pycalc.constants_and_operations import CONSTANTS
from math import (pi, e, tau)


class ExpressionParserTestCase(unittest.TestCase):

    def test_parse_expression(self):
        self.assertEqual(parse_expression("1", CONSTANTS), ['1'])
        self.assertEqual(parse_expression("1+1", CONSTANTS), ['1', '+', '1'])
        self.assertEqual(parse_expression("-1*2", CONSTANTS), ['-', '1', '*', '2'])
        self.assertEqual(parse_expression("2*-(-3+1)^3", CONSTANTS),
                         ['2', '*', '-', '(', '-', '3', '+', '1', ')', '^', '3'])
        self.assertEqual(parse_expression("-(-(-1)+45*(2+2)*24)", CONSTANTS),
                         ['-', '(', '-', '(', '-', '1', ')', '+', '45', '*', '(', '2', '+', '2', ')', '*', '24', ')'])
        self.assertEqual(parse_expression("pi*2", CONSTANTS), [pi, '*', '2'])
        self.assertEqual(parse_expression("sin(pi/2)", CONSTANTS), ['sin', '(', pi, '/', '2', ')'])
        self.assertEqual(parse_expression("e+pi+tau", CONSTANTS), [e, '+', pi, '+', tau])
        self.assertEqual(parse_expression("cos(sin(tan(e)))", CONSTANTS),
                         ['cos', '(', 'sin', '(', 'tan', '(', e, ')', ')', ')'])
