import unittest
from pycalc.expression_parser import (parse_expression)
from pycalc.constants_and_operations import constants
from math import (pi, e, tau)


class ExpressionParserTestCase(unittest.TestCase):

    def test_parse_expression(self):
        self.assertEqual(parse_expression("1", constants), ['1'])
        self.assertEqual(parse_expression("1+1", constants), ['1', '+', '1'])
        self.assertEqual(parse_expression("-1*2", constants), ['-', '1', '*', '2'])
        self.assertEqual(parse_expression("2*-(-3+1)^3", constants),
                         ['2', '*', '-', '(', '-', '3', '+', '1', ')', '^', '3'])
        self.assertEqual(parse_expression("-(-(-1)+45*(2+2)*24)", constants),
                         ['-', '(', '-', '(', '-', '1', ')', '+', '45', '*', '(', '2', '+', '2', ')', '*', '24', ')'])
        self.assertEqual(parse_expression("pi*2", constants), [pi, '*', '2'])
        self.assertEqual(parse_expression("sin(pi/2)", constants), ['sin', '(', pi, '/', '2', ')'])
        self.assertEqual(parse_expression("e+pi+tau", constants), [e, '+', pi, '+', tau])
        self.assertEqual(parse_expression("cos(sin(tan(e)))", constants),
                         ['cos', '(', 'sin', '(', 'tan', '(', e, ')', ')', ')'])
