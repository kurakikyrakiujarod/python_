# 1、装饰器


def w1(func):
    def inner():
        # 验证1
        # 验证2
        # 验证3
        func()

    return inner


@w1
def f1():
    print('f1')


# python解释器就会从上到下解释代码，步骤如下
# 1.def w1(func): --->将w1函数加载到内存
# 2.@w1内部会执行以下操作
# 执行w1函数，即w1(f1)：
# func是参数，此时func等于f1
# 返回的inner，inner代表的是函数，非执行函数,其实就是将原来的f1函数塞进另外一个函数中
# 将w1的返回值再重新赋值给f1

# 2、 再议装饰器


# 定义函数：完成包裹数据
def makeBold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"

    return wrapped


# 定义函数：完成包裹数据
def makeItalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"

    return wrapped


@makeBold
def test1():
    return "hello world-1"


@makeItalic
def test2():
    return "hello world-2"


@makeBold
@makeItalic
def test3():
    return "hello world-3"


# print(test1())
# print(test2())
# print(test3())
# 输出
# <b>hello world-1</b>
# <i>hello world-2</i>
# <b><i>hello world-3</i></b>

# 3、装饰器示例


# 无参数的函数
from time import ctime


def timefun(func):
    def wrappedfunc():
        print("%s called at %s" % (func.__name__, ctime()))
        func()

    return wrappedfunc


@timefun
def foo():
    print("I am foo")


# foo()
# 输出
# foo called at Sun Nov  4 17:10:13 2018
# I am foo

# 被装饰的函数有不定长参数
from time import ctime


def timefun(func):
    def wrappedfunc(*args, **kwargs):
        print("%s called at %s" % (func.__name__, ctime()))
        func(*args, **kwargs)

    return wrappedfunc


@timefun
def foo(a, b, c):
    print(a + b + c)


# foo(3, 5, 7)
# 输出
# foo called at Sun Nov  4 17:14:36 2018
# 15

# 装饰器中的return
from time import ctime


def timefun(func):
    def wrappedfunc():
        print("%s called at %s" % (func.__name__, ctime()))
        return func()

    return wrappedfunc


@timefun
def getInfo():
    return '----hahah---'


# print(getInfo())
# 输出
# getInfo called at Sun Nov  4 17:18:14 2018
# ----hahah---


# 装饰器带参数,在原有装饰器的基础上，设置外部变量
from time import ctime


def timefun_arg(pre="hello"):
    def timefun(func):
        def wrappedfunc():
            print("%s called at %s %s" % (func.__name__, ctime(), pre))
            return func()

        return wrappedfunc

    return timefun


@timefun_arg("itcast")
def foo():
    print("I am foo")


# foo()
# 输出
# foo called at Sun Nov  4 17:22:09 2018 itcast
# I am foo

# 执行逻辑---->foo()==timefun_arg("itcast")(foo)()

# 4、类装饰器


# 装饰器函数其实是这样一个接口约束，它必须接受一个callable对象作为参数，然后返回一个callable对象
# 在Python中一般callable对象都是函数，只要某个对象重写了__call__()方法，那么这个对象就是callable的

# class Test():
#     def __call__(self):
#         print('call me!')
#
#
# t = Test()


# t()
# 输出
# call me!

# 类装饰器demo
class Test(object):
    def __init__(self, func):
        print("---初始化---")
        print("func name is %s" % func.__name__)
        self.__func = func

    def __call__(self):
        print("---装饰器中的功能---")
        self.__func()


# @Test
def test():
    print("----test---")


# test()
# 输出
# ---初始化---
# func name is test
# ---装饰器中的功能---
# ----test---


# 说明：
# 1.当用Test装饰器对test函数进行装饰的时候，首先会创建Test的实例对象
# 并且会把test这个函数名当做参数传递到__init__方法中 即在__init__方法中的func变量指向了test函数体
# 2.test函数相当于指向了用Test创建出来的实例对象
# 3.当在使用test()进行调用时，就相当于让这个对象()，因此会调用这个对象的__call__方法
# 4.为了能够在__call__方法中调用原来test指向的函数体，所以在__init__方法中就需要一个实例属性来保存这个函数体的引用
# 所以才有了self.__func = func这句代码，从而在调用__call__方法中能够调用到test之前的函数体