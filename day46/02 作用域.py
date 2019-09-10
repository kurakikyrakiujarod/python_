A = 100
B = 200


def test():
    a = 11
    b = 22
    print(locals())


# test()
# 输出
# {'b': 22, 'a': 11}

# print(globals())
# 输出
# {'__name__': '__main__', '__doc__': None, '__package__': None,
# '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001F57F298780>,
#  '__spec__': None, '__annotations__': {},
# '__builtins__': <module 'builtins' (built-in)>, '__file__': 'E:/code/github_python/day46/02 作用域.py',
# '__cached__': None, 'A': 100, 'B': 200, 'test': <function test at 0x000001F57F1A2E18>}

# LEGB 规则

# Python 使用 LEGB 的顺序来查找一个符号对应的对象
# locals -> enclosing function -> globals -> builtins

# 1、locals，当前所在命名空间（如函数、模块），函数的参数也属于命名空间内的变量
# 2、enclosing，外部嵌套函数的命名空间（闭包中常见）
# a位于外部嵌套函数的命名空间


def fun1():
    a = 10

    def fun2():
        print(a)


# 3、globals，全局变量，函数定义所在模块的命名空间
# a 全局变量
# fun函数修改全局变量a，需要通过global指令来声明全局变量，而不是创建一个新的local变量
a = 1


def fun():
    global a
    a = 2


# 4、builtins，内建模块的命名空间
# Python在启动的时候会自动为我们载入很多内建的函数、类
# 比如 dict，list，type，print，这些都位于 __builtin__ 模块中 可以使用 dir(__builtin__) 来查看

# Ipython3 测试
# In[1]: print(dir(__builtin__))
# ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError',
#  'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
#  'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError',
#  'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit',
#  'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError',
#  'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None',
#  'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError',
# 'PendingDeprecationWarning','PermissionError'
#  , 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError',
#  'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit',
#  'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
#  'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError',
#  'ZeroDivisionError', '__IPYTHON__', '__build_class__', '__debug__', '__doc__', '__import__',
#  '__loader__', '__name__','__package__', '__spec__',
#   'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr',
#  'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'display', 'divmod',
#  'enumerate', 'eval', 'exec', 'filter', 'float', 'format', 'frozenset', 'get_ipython', 'getattr',
# 'globals', 'hasattr','hash', 'help',
#   'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals',
#  'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow',
# 'print', 'property', 'range', 'repr','reversed', 'round', 'set',
#   'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type',
#  'vars', 'zip']


# 在Python中，有一个内建模块，该模块中有一些常用函数，在Python启动后，且没有执行程序员所写的任何代码前，Python会首先加载该内建函数到内存。
# 另外，该内建模块中的功能可以直接使用，不用在其前添加内建模块前缀，其原因是对函数、变量、类等标识符的查找是按LEGB法则，其中B即代表内建模块
# 比如：内建模块中有一个abs()函数，其功能求绝对值，如abs(-20)将返回20。