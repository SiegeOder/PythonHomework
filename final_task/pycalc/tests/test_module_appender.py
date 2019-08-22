import unittest
import test_appending_1
from test_appending_1 import ca as c_a
from test_appending_1 import cb as c_b
from test_appending_1 import cc as c_c
from test_appending_1 import fa as f_a
from test_appending_1 import fb as f_b
from test_appending_1 import fc as f_c
from test_appending_2 import cd as c_d
from test_appending_2 import ce as c_e
from test_appending_2 import cf as c_f
from test_appending_2 import fd as f_d
from test_appending_2 import fe as f_e
from test_appending_2 import ff as f_f
from pycalc.module_appender import (append_module,
                                    append_module_by_name,
                                    import_all_modules)


class ModuleAppenderTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.constants = {}
        self.functions = {}

    def test_append_module(self):
        append_module(test_appending_1, self.constants, self.functions)
        self.assertEqual(self.constants, {'ca': c_a, 'cb': c_b, 'cc': c_c})
        self.assertEqual(self.functions, {'fa': f_a, 'fb': f_b, 'fc': f_c})

    def test_append_module_by_name(self):
        append_module_by_name('test_appending_2', self.constants, self.functions)
        self.assertEqual(self.constants, {'cd': c_d, 'ce': c_e, 'cf': c_f})
        self.assertEqual(self.functions, {'fd': f_d, 'fe': f_e, 'ff': f_f})

    def test_import_all_modules(self):
        import_all_modules(['test_appending_1', 'test_appending_2'], self.constants, self.functions)
        self.assertEqual(self.constants, {'ca': c_a, 'cb': c_b, 'cc': c_c, 'cd': c_d, 'ce': c_e, 'cf': c_f})
        self.assertEqual(self.functions, {'fa': f_a, 'fb': f_b, 'fc': f_c, 'fd': f_d, 'fe': f_e, 'ff': f_f})


if __name__ == '__main__':
    unittest.main()
