from pycalc.module_appender import (append_module_by_name)
import operator

OPERATIONS = {'^': operator.pow,
              '/': operator.truediv,
              '//': operator.floordiv,
              '%': operator.mod,
              '*': operator.mul,
              '-': operator.sub,
              '+': operator.add,
              }

LOGICAL_OPERATIONS = {'==': operator.eq,
                      '!=': operator.ne,
                      '>=': operator.ge,
                      '<=': operator.le,
                      '>': operator.gt,
                      '<': operator.lt,
                      }

CONSTANTS = {}
FUNCTIONS = {'abs': abs,
             'round': round
             }

append_module_by_name("math", CONSTANTS, FUNCTIONS)
