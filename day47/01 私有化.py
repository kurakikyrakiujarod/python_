# 私有化


# xx: 公有变量
# _x: 单前置下划线,私有化属性或方法，from somemodule import * 禁止导入，类对象和子类可以访问
# __xx：双前置下划线,避免与子类中的属性命名冲突，名字重整，无法在外部直接访问
# __xx__:双前后下划线,用户名字空间的魔法对象或属性。例如:__init__ ,不要自己发明这样的名字
# xx_:单后置下划线,用于避免与Python关键词的冲突

# coding=utf-8


class Person(object):
    def __init__(self, name, age, taste):
        self.name = name
        self._age = age
        self.__taste = taste

    def showperson(self):
        print(self.name)
        print(self._age)
        print(self.__taste)

    def dowork(self):
        self._work()
        self.__away()

    def _work(self):
        print('my _work')

    def __away(self):
        print('my __away')


class Student(Person):
    def construction(self, name, age, taste):
        self.name = name
        self._age = age
        self.__taste = taste

    def showstudent(self):
        print(self.name)
        print(self._age)
        print(self.__taste)

    @staticmethod
    def testbug():
        _Bug.showbug()


# 模块内可以访问，当from  cur_module import * 时，不导入


class _Bug(object):
    @staticmethod
    def showbug():
        print("showbug")


s1 = Student('jack', 25, 'football')

# print(s1.__dict__)
# {'name': 'jack', '_age': 25, '_Person__taste': 'football'}

# s1.showperson()
# jack
# 25
# football

# 无法访问__taste,导致报错
# s1.showstudent()
# 报错
# AttributeError: 'Student' object has no attribute '_Student__taste'

# print(s1._Person__taste)
# 输出
# football

s1.construction('rose', 30, 'basketball')
# print(s1.__dict__)
# {'name': 'rose', '_age': 30, '_Person__taste': 'football', '_Student__taste': 'basketball'}

# s1.showperson()
# rose
# 30
# football

# s1.showstudent()
# rose
# 30
# basketball

# Student.testbug()
# showbug


# 总结
# 属性名为__名字的，名字被重整，通过_Class__object机制就可以访问的属性，不建议
# 如果在子类中向__名字赋值，那么会在子类中定义的一个与父类相同名字的属性
# _名的变量、函数、类在使用from xxx import *时都不会被导入


# from private import *
# print(num)
# 输出
# 100
# print(_num2)
# NameError: name '_num2' is not defined
# print(__num3)
# NameError: name '__num3' is not defined

# printName()
# 输出
# sy

# _printName1()
# NameError: name '_printName1' is not defined

# __printName1()
# 输出
# NameError: name '__printName1' is not defined

# import private
# print(private.num)
# print(private._num2)
# print(private.__num3)
# private.printName()
# private._printName1()
# private.__printName1()
# 输出
# 100
# 150
# 300
# sy
# sy1
# sy2