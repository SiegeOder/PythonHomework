import unittest

from math import *
from pycalc.expression_parser import parse_expression
from pycalc.constants_and_operations import CONSTANTS
from pycalc.expression_calculator import (has_brackets,
                                          remove_brackets,
                                          calculate_expression,
                                          calculate_logical_expression,
                                          convert)


class ExpressionCalculatorTestCase(unittest.TestCase):

    def test_has_brackets(self):
        self.assertEqual(has_brackets([]), False)
        self.assertEqual(has_brackets(")"), False)
        self.assertEqual(has_brackets(")0)"), False)
        self.assertEqual(has_brackets("("), False)
        self.assertEqual(has_brackets("(9("), False)

    def test_remove_brackets(self):
        test_list1 = ['sin', '(', '3', ')']
        test_list2 = ['(', '7', ')']
        test_list3 = ['(', '2', '+', '2', ')', '-', '4']
        test_list4 = ['-', '7', '+', '(', '-', '(', '2', '+', '3', ')', '*', '4', ')', '*', '-', '1']
        test_lists = [test_list1,
                      test_list2,
                      test_list3,
                      test_list4,
                      ]
        for test_list in test_lists:
            remove_brackets(test_list)
        self.assertEqual(test_list1, [sin(3)])
        self.assertEqual(test_list2, [7])
        self.assertEqual(test_list3, [4, '-', '4'])
        self.assertEqual(test_list4, ['-', '7', '+', '(', '-', 5, '*', '4', ')', '*', '-', '1'])

    def test_calculate_expression(self):
        self.assertEqual(calculate_expression(parse_expression("1", CONSTANTS)), '1')
        self.assertEqual(calculate_expression(parse_expression("-1", CONSTANTS)), -1)
        self.assertEqual(calculate_expression(parse_expression("1+1", CONSTANTS)), 2)
        self.assertEqual(calculate_expression(parse_expression("1-1", CONSTANTS)), 0)
        self.assertEqual(calculate_expression(parse_expression("2*2", CONSTANTS)), 4)
        self.assertEqual(calculate_expression(parse_expression("3/2", CONSTANTS)), 1.5)
        self.assertEqual(calculate_expression(parse_expression("7//3", CONSTANTS)), 2)
        self.assertEqual(calculate_expression(parse_expression("7%3", CONSTANTS)), 1)
        self.assertEqual(calculate_expression(parse_expression("5^3", CONSTANTS)), 125)
        self.assertEqual(calculate_expression(parse_expression("2^3^4", CONSTANTS)), 2 ** 3 ** 4)
        self.assertEqual(calculate_expression(parse_expression("5^3", CONSTANTS)), 125)
        self.assertEqual(calculate_expression(parse_expression("5^6/7//8%9*10", CONSTANTS)), 5 ** 6 / 7 // 8 % 9 * 10)
        self.assertEqual(calculate_expression(parse_expression("(1)", CONSTANTS)), 1)
        self.assertEqual(calculate_expression(parse_expression("(-1)", CONSTANTS)), -1)
        self.assertEqual(calculate_expression(parse_expression("-(-1)", CONSTANTS)), 1)
        self.assertEqual(calculate_expression(parse_expression("-(-(1))", CONSTANTS)), 1)
        self.assertEqual(calculate_expression(parse_expression("-(-(-1))", CONSTANTS)), -1)
        self.assertEqual(calculate_expression(parse_expression("-(-(-(1)))", CONSTANTS)), -1)

    def test_calculate_logical_expression(self):
        self.assertEqual(calculate_logical_expression([2, '>', -2]), True)
        self.assertEqual(calculate_logical_expression([229, '>', 227]), True)
        self.assertEqual(calculate_logical_expression([512, '<', 1024]), True)
        self.assertEqual(calculate_logical_expression([1100, '==', 1100]), True)
        self.assertEqual(calculate_logical_expression([1100, '!=', 11]), True)
        self.assertEqual(calculate_logical_expression([8800, '==', 5553535]), False)
        self.assertEqual(calculate_logical_expression([88, '<=', 555]), True)
        self.assertEqual(calculate_logical_expression([555, '<=', 555]), True)
        self.assertEqual(calculate_logical_expression([888, '<=', 555]), False)
        self.assertEqual(calculate_logical_expression([456, '>=', 123]), True)
        self.assertEqual(calculate_logical_expression([123, '>=', 123]), True)
        self.assertEqual(calculate_logical_expression([123, '>=', 456]), False)

    def test_convert(self):
        self.assertEqual(convert(4), 4)
        self.assertEqual(convert('5'), 5)
        self.assertEqual(convert('23.6'), 23.6)
        self.assertEqual(convert('-70.5'), -70.5)
        self.assertEqual(convert(-54), -54)
        self.assertEqual(convert(-4.5), -4.5)
