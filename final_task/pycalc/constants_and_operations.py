from pycalc.module_appender import (append_module_by_name)

operations = {'^': lambda arg1, arg2: arg1 ** arg2,
              '/': lambda arg1, arg2: arg1 / arg2 if arg2 != 0 else exit("ERROR: division by zero"),
              '//': lambda arg1, arg2: arg1 // arg2 if arg2 != 0 else exit("ERROR: division by zero"),
              '%': lambda arg1, arg2: arg1 % arg2 if arg2 != 0 else exit("ERROR: division by zero"),
              '*': lambda arg1, arg2: arg1 * arg2,
              '-': lambda arg1, arg2: arg1 - arg2,
              '+': lambda arg1, arg2: arg1 + arg2,
              }

logical_operations = {'==': lambda arg1, arg2: arg1 == arg2,
                      '!=': lambda arg1, arg2: arg1 != arg2,
                      '>=': lambda arg1, arg2: arg1 >= arg2,
                      '<=': lambda arg1, arg2: arg1 <= arg2,
                      '>': lambda arg1, arg2: arg1 > arg2,
                      '<': lambda arg1, arg2: arg1 < arg2,
                      }

constants = {}
functions = {'abs': abs,
             'round': round
             }

append_module_by_name("math", constants, functions)
