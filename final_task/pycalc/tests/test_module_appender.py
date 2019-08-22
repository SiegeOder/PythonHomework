import unittest
import test_appending_1
import test_appending_2
from test_appending_1 import ca
from test_appending_1 import cb
from test_appending_1 import cc
from test_appending_1 import fa
from test_appending_1 import fb
from test_appending_1 import fc
from test_appending_2 import cd
from test_appending_2 import ce
from test_appending_2 import cf
from test_appending_2 import fd
from test_appending_2 import fe
from test_appending_2 import ff
from pycalc.module_appender import (append_module,
                                    append_module_by_name,
                                    import_all_modules)


class ModuleAppenderTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.constants = {}
        self.functions = {}

    def test_append_module(self):
        append_module(test_appending_1, self.constants, self.functions)
        self.assertEqual(self.constants, {'ca': ca, 'cb': cb, 'cc': cc})
        self.assertEqual(self.functions, {'fa': fa, 'fb': fb, 'fc': fc})

    def test_append_module_by_name(self):
        append_module_by_name("test_appending_2", self.constants, self.functions)
        self.assertEqual(self.constants, {'cd': cd, 'ce': ce, 'cf': cf})
        compare_functions = {'fd': fd, 'fe': fe, 'ff': ff}
        for func in self.functions:
            self.assertEqual(self.functions[func](), compare_functions[func]())

    def test_import_all_modules(self):
        import_all_modules(['test_appending_1', 'test_appending_2'], self.constants, self.functions)
        self.assertEqual(self.constants, {'ca': ca, 'cb': cb, 'cc': cc, 'cd': cd, 'ce': ce, 'cf': cf})
        compare_functions = {'fa': fa, 'fb': fb, 'fc': fc, 'fd': fd, 'fe': fe, 'ff': ff}
        for func in self.functions:
            self.assertEqual(self.functions[func](), compare_functions[func]())
