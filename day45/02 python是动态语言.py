# 1. 动态语言的定义
# 动态编程语言是高级程序设计语言的一个类别，在计算机科学领域已被广泛应用它是一类在运行时可以改变其结构的语言
# 例如新的函数、对象、甚至代码可以被引进，已有的函数可以被删除或是其他结构上的变化
# 例如JavaScript便是一个动态语言，除此之外如PHP 、Ruby 、Python 等也都属于动态语言，而 C 、 C++ 等语言则不属于动态语言

# 动态语言 可以在运行的过程中，修改代码
# 静态语言 编译时已经确定好代码，运行过程中不能修改

# 2. 运行的过程中给对象绑定(添加)属性


class Person(object):
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age


p = Person("小明", "24")
p.sex = "male"
# print(p.sex)
# 输出
# male

# 这里实际上就是动态给实例绑定属性！
# 定义的类里面没有sex这个属性

# 3. 运行的过程中给类绑定(添加)属性
p1 = Person("小丽", "25")
# print(p1.sex)
# 输出
# AttributeError: 'Person' object has no attribute 'sex'

# 给p这个实例绑定属性对p1这个实例不起作用

# 给所有的Person的实例加上 sex属性
# 直接给Person绑定属性！
# 给类Person添加一个属性
Person.sex = None
p1 = Person("小丽", "25")
# print(p1.sex)
# 输出
# None

# 4. 运行的过程中给类绑定(添加)方法


class Person(object):
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def eat(self):
        print("eat food")


def run(self, speed):
    print("%s在移动, 速度是 %d km/h" % (self.name, speed))


p = Person("老王", 24)
# P.eat()
# 输出
# eat food
# P.run()
# 输出
# AttributeError: 'Person' object has no attribute 'run'
import types
p.run = types.MethodType(run, p)
# p.run(180)
# 输出
# 老王在移动, 速度是 180 km/h

# 完整的代码如下
# 定义了一个类


class Person(object):
    num = 0

    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def eat(self):
        print("eat food")


# 定义一个实例方法
def run(self, speed):
    print("%s在移动, 速度是 %d km/h" % (self.name, speed))


# 定义一个类方法
@classmethod
def testClass(cls):
    cls.num = 100


# 定义一个静态方法
@staticmethod
def testStatic():
    print("---static method----")


# 创建一个实例对象
p = Person("老王", 24)
# 调用在class中的方法
# p.eat()
# 输出
# eat food

# 给这个对象添加实例方法
p.run = types.MethodType(run, p)
# 调用实例方法
# p.run(180)
# 输出
# 老王在移动, 速度是 180 km/h

# 给Person类绑定类方法
Person.testClass = testClass
# 调用类方法
# print(Person.num)
Person.testClass()
# print(Person.num)
# 输出
# 0
# 100

# 给Person类绑定静态方法
Person.testStatic = testStatic
# 调用静态方法
# Person.testStatic()
# 输出
# ---static method----


# 5. 运行的过程中删除属性、方法
# del 对象.属性名
# delattr(对象, "属性名")