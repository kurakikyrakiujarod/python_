# 1、装饰器的形成过程
import time


def func1():
    print('in func1')


def timer(func):
    def inner():
        start = time.time()
        time.sleep(0.1)
        func()
        print(time.time() - start)

    return inner


# func1 = timer(func1)
# func1()
# 输出
# in func1
# 0.10046505928039551

# 语法糖
import time


def timer(func):
    def inner():
        start = time.time()
        time.sleep(0.1)
        func()
        print(time.time() - start)

    return inner


# @timer
def func1():
    print('in func1')


# func1()
# 输出
# in func1
# 0.10090351104736328

# 语法糖@timer相当于func1 = timer(func1)

# 装饰器的本质：一个闭包函数
# 装饰器的功能：在不修改原函数及其调用方式的情况下对原函数功能进行扩展


# 2、装饰器进阶

# Python装饰器（decorator）在实现的时候，被装饰后的函数其实已经是另外一个函数了（函数名等函数属性会发生改变）
# Python的functools包中提供了一个叫wraps的decorator来消除这样的副作用
# 写一个decorator的时候，最好在实现之前加上functools的wrap，它能保留原有函数的名称和docstring

# 查看函数信息的一些方法
def index():
    '''这是一个主页信息'''
    print('from index')


# 查看函数注释、 函数名
# print(index.__doc__)
# print(index.__name__)
# 输出
# 这是一个主页信息
# index

# 不加wraps
def my_decorator(func):
    def wrapper(*args, **kwargs):
        '''decorator'''
        print('Calling decorated function...')
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def example():
    """Docstring"""
    print('Called example function')


# print(example.__name__, example.__doc__)
# 输出
# wrapper decorator

# 加wraps
# @wraps(func) 加在最内层函数正上方
# -*- coding=utf-8 -*-
from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        '''decorator'''
        print('Calling decorated function...')
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def example():
    """Docstring"""
    print('Called example function')


# print(example.__name__, example.__doc__)
# 输出
# example Docstring

# 开放封闭原则
# 1.对扩展是开放的
# 2.对修改是封闭的


# 装饰器的固定格式
def timer(func):
    def inner(*args, **kwargs):
        '''执行函数之前要做的'''
        ret = func(*args, **kwargs)
        '''执行函数之后要做的'''
        return ret

    return inner


# 装饰器的固定格式——wraps版
from functools import wraps


def deco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


# 带参数的装饰器
flag = True


def outer(flag):
    def timer(func):
        def inner(*args, **kwargs):
            if flag:
                print('''执行函数之前要做的''')
                re = func(*args, **kwargs)
                print('''执行函数之后要做的''')
            else:
                re = func(*args, **kwargs)
            return re

        return inner

    return timer


@outer(flag)
def func(a):
    print(111, a)
    return 333


# ret = func(222)
# print(ret)
# 输出
# 执行函数之前要做的
# 111 222
# 执行函数之后要做的
# 333

