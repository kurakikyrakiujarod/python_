# 1、模块被导入后，import module不能重新导入模块 重新导入需用reload

# 测试模块内容
# reload_test.py
# def test():
#     print('----1----')

import reload_test
reload_test.test()

# 修改测试模块
# def test():
#     print('----2---')

# 再次导入
import reload_test
reload_test.test()

# 使用reload函数函数
# 重新加载模块
from importlib import reload
reload(reload_test)
reload_test.test()

# 在Ipython中测试，PyCharm可能已经做了优化
# In [1]: import reload_test
#    ...: reload_test.test()
#    ...:
#    ...:
# ----1----
#
# In [2]: import reload_test
#    ...: reload_test.test()
#    ...:
#    ...:
# ----1----
#
# In [3]: from importlib import reload
#    ...: reload(reload_test)
#    ...: reload_test.test()
#    ...:
#    ...:
# ----2----


# 2、循环导入


# a.py 内容
# from b import b
#
# print('---------this is module a.py----------')
# def a():
#     print("hello, a")
#     b()
#
# a()

# b.py 内容
# from a import a
#
# print('----------this is module b.py----------')
# def b():
#     print("hello, b")
#
# def c():
#     a()
# c()

# 运行python a.py
# 输出
# ImportError: cannot import name 'b'