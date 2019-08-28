import unittest
import math
import cmath
import time

from pycalc.module_appender import (append_module,
                                    append_module_by_name,
                                    import_all_modules)


class ModuleAppenderTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.constants = {}
        self.functions = {}

    def test_append_module(self):
        append_module(math, self.constants, self.functions)
        self.assertEqual(math.pi in self.constants.values(), True)
        self.assertEqual(math.asinh in self.functions.values(), True)

    def test_append_module_by_name(self):
        append_module_by_name("cmath", self.constants, self.functions)
        self.assertEqual(cmath.e in self.constants.values(), True)
        self.assertEqual(cmath.log10 in self.functions.values(), True)

    def test_import_all_modules(self):
        import_all_modules(['math', 'time', 'cmath'], self.constants, self.functions)
        self.assertEqual(time.time in self.functions.values(), True)
        self.assertEqual(math.cosh in self.functions.values(), False)
        self.assertEqual(cmath.cosh in self.functions.values(), True)
        self.assertEqual(cmath.tau in self.constants.values(), True)
