# 1. __doc__


# 输出文件开头注释的内容


class Foo:
    """ 描述类信息 """

    def func(self):
        pass


# print(Foo.__doc__)
# 输出
# 描述类信息


# 2. __module__ 和 __class__


# __module__ 表示当前操作的对象在那个模块
# __class__ 表示当前操作的对象的类是什么


class Person(object):
    def __init__(self):
        self.name = 'aoa'


obj = Person()


# print(obj.__module__)
# print(obj.__class__)

# 输出
# __main__
# <class '__main__.Person'>


# 3. __init__


# 初始化方法
# 通过类创建对象时，自动触发执行


# 4. __del__


# 析构方法
# 当对象在内存中被释放时，自动触发执行


# 5. __call__


# 对象后面加括号，触发执行


# 6. __dict__


# 类或对象中的所有属性


# 7. __str__


# 如果一个类中定义了__str__方法，那么在打印对象时，默认输出该方法的返回值


# 8、__getitem__、__setitem__、__delitem__


# 使用 [''] 的方式操作属性时被调用
# 以上分别表示获取、设置、删除数据


# -*- coding:utf-8 -*-


class Foo(object):
    def __getitem__(self, key):
        print('__getitem__', key)

    def __setitem__(self, key, value):
        print('__setitem__', key, value)

    def __delitem__(self, key):
        print('__delitem__', key)


obj = Foo()


# 自动触发执行 __getitem__
# result = obj['k1']

# 自动触发执行 __setitem__
# obj['k2'] = 'aoa'

# 自动触发执行 __delitem__
# del obj['k1']

# 输出
# __getitem__ k1
# __setitem__ k2 aoa
# __delitem__ k1

# 9、__getslice__、__setslice__、__delslice__


# 该三个方法用于分片操作，如：列表


# >>> class Foo(object):
# ...
# ...     def __getslice__(self, i, j):
# ...         print '__getslice__',i,j
# ...
# ...     def __setslice__(self, i, j, sequence):
# ...         print '__setslice__',i,j
# ...
# ...     def __delslice__(self, i, j):
# ...         print '__delslice__',i,j
# ...
# ... obj = Foo()
# ...
# ... obj[-1:1]                   # 自动触发执行 __getslice__
# ... obj[0:1] = [11,22,33,44]    # 自动触发执行 __setslice__
# ... del obj[0:2]                # 自动触发执行 __delslice__
# __getslice__ -1 1
# __setslice__ 0 1
# __delslice__ 0 2

# Python2中执行OK

