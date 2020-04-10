import numpy as np
import pandas
import importlib
import builtins

safe_builtins = {}

_safe_bi_names = [
    'None',
    'False',
    'True',
    'abs',
    'bool',
    'callable',
    'chr',
    'complex',
    'divmod',
    'float',
    'hash',
    'hex',
    'id',
    'int',
    'isinstance',
    'issubclass',
    'len',
    'oct',
    'ord',
    'pow',
    'range',
    'repr',
    'round',
    'slice',
    'str',
    'tuple',
    'zip',
]

_safe_bi_exceptions = [
    'ArithmeticError',
    'AssertionError',
    'AttributeError',
    'BaseException',
    'BufferError',
    'BytesWarning',
    'DeprecationWarning',
    'EOFError',
    'EnvironmentError',
    'Exception',
    'FloatingPointError',
    'FutureWarning',
    'GeneratorExit',
    'IOError',
    'ImportError',
    'ImportWarning',
    'IndentationError',
    'IndexError',
    'KeyError',
    'KeyboardInterrupt',
    'LookupError',
    'MemoryError',
    'NameError',
    'NotImplementedError',
    'OSError',
    'OverflowError',
    'PendingDeprecationWarning',
    'ReferenceError',
    'RuntimeError',
    'RuntimeWarning',
    'StopIteration',
    'SyntaxError',
    'SyntaxWarning',
    'SystemError',
    'SystemExit',
    'TabError',
    'TypeError',
    'UnboundLocalError',
    'UnicodeDecodeError',
    'UnicodeEncodeError',
    'UnicodeError',
    'UnicodeTranslateError',
    'UnicodeWarning',
    'UserWarning',
    'ValueError',
    'Warning',
    'ZeroDivisionError',
]

_safe_np_names = [
    'array',
    'ndarray',
    'arange',
    'vectorize',
    'dtype',
    'shape',
    'ndim',
    'reshape',
]

for name in _safe_bi_names:
    safe_builtins[name] = getattr(builtins, name)
for exception in _safe_bi_exceptions:
    safe_builtins[exception] = getattr(builtins, exception)
for name in _safe_np_names:
    safe_builtins[name] = np.__dict__[name]

safe_builtins.update(importlib.import_module(pandas.__name__).__dict__)
