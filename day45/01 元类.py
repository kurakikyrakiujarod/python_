# ********************    1.类也是对象
# 在大多数编程语言中，类就是一组用来描述如何生成一个对象的代码段
# Python中的类还远不止如此,类同样也是一种对象
# 只要你使用关键字class，Python解释器在执行的时候就会创建一个对象


class ObjectCreator(object):
    pass


my_object = ObjectCreator()
# print(my_object)
# 执行输出
# <__main__.ObjectCreator object at 0x00000284C1D48748>

# 下面的代码段：
# class ObjectCreator(object):
#     pass

# 将在内存中创建一个对象，名字就是ObjectCreator。
# 这个对象（类对象ObjectCreator）拥有创建对象（实例对象）的能力。
# 但是，它的本质仍然是一个对象，于是乎你可以对它做如下的操作
# 1、你可以将它赋值给一个变量
# 2、你可以拷贝它
# 3、你可以为它增加属性
# 4、你可以将它作为函数参数进行传递

# --------------------你可以打印一个类，因为它其实也是一个对象
# print(ObjectCreator)
# 执行输出
# <class '__main__.ObjectCreator'>

# --------------------你可以将类做为参数传给函数


def echo(o):
    print(o)


# echo(ObjectCreator)
# 执行输出
# <class '__main__.ObjectCreator'>

# --------------------你可以为类增加属性
# print(hasattr(ObjectCreator, 'new_attribute'))
# 执行输出
# False
# ObjectCreator.new_attribute = 'foo'
# print(hasattr(ObjectCreator, 'new_attribute'))
# 执行输出
# True
# print(ObjectCreator.new_attribute)
# 执行输出
# foo

# --------------------你可以将类赋值给一个变量
# ObjectCreatorMirror = ObjectCreator
# print(ObjectCreatorMirror)
# 执行输出
# <class '__main__.ObjectCreator'>


# ********************      2.动态地创建类
# 因为类也是对象，你可以在运行时动态的创建它们，就像其他任何对象一样。
# 你可以在函数中创建类，使用class关键字即可。
def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass
        return Foo
    else:
        class Bar(object):
            pass
        return Bar


MyClass = choose_class('foo')
# 函数返回的是类，不是类的实例
# print(MyClass)
# 执行输出
# <class '__main__.choose_class.<locals>.Foo'>
# print(MyClass())
#  你可以通过这个类创建类实例，也就是对象
# 执行输出
# <__main__.choose_class.<locals>.Foo object at 0x00000149746EA0B8>


# 由于类也是对象，所以它们必须是通过什么东西来生成的才对。
# 当你使用class关键字时，Python解释器自动创建这个对象。

# 内建函数type
# print(type(1))
#  数值的类型
# <class 'int'>
# print(type('1'))
#  字符串的类型
# <class 'str'>
# print(type(ObjectCreator()))
# 实例对象的类型
# <class '__main__.ObjectCreator'>
# print(type(ObjectCreator))
# 类的类型
# <class 'type'>

# 使用type对ObjectCreator查看类型是，答案为type


# ********************    3. 使用type创建类
# type还有一种完全不同的功能，动态的创建类。type可以接受一个类的描述作为参数，然后返回一个类。
# type(类名, 由父类名称组成的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)

class Test:
    pass


# print(Test())
# 执行输出
# <__main__.Test object at 0x000001ECE9E812E8>

# 可以手动像这样创建
Test2 = type('Test2', (), {})
# print(Test2())
# 创建了一个Test2类的实例对象
# 执行输出
# <__main__.Test2 object at 0x000001A9CA590390>

# 我们使用"Test2"作为类名，并且也可以把它当做一个变量来作为类的引用。
MyDogClass = type('MyDog', (), {})
# print(MyDogClass)
# 执行输出
# <class '__main__.MyDog'>


# ********************     4. 使用type创建带有属性的类
# type 接受一个字典来为类定义属性
Foo = type('Foo', (), {'bar': True})
# 相当于
# class Foo(object):
#     bar = True
# print(Foo)
# 执行输出
# <class '__main__.Foo'>
# print(Foo.bar)
# 执行输出
# True
f = Foo()
# print(f)
# 执行输出
# <__main__.Foo object at 0x00000241DFE63CF8>

# 继承
# class FooChild(Foo):
#     pass
FooChild = type('FooChild', (Foo,), {})
# print(FooChild)
# 执行输出
# <class '__main__.FooChild'>
# print(FooChild.bar)
# 执行输出
# True

# 注意
# type的第2个参数，元组中是父类的名字，而不是字符串
# 添加的属性是类属性，并不是实例属性


# ********************     5. 使用type创建带有方法的类
# 添加实例方法
# 定义了一个普通的函数
def echo_bar(self):
    print(self.bar)


FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})
# 让FooChild类中的echo_bar属性，指向了上面定义的函数
# print(hasattr(Foo, 'echo_bar') )
# 判断Foo类中，是否有echo_bar这个属性
# 执行输出
# False
# print(hasattr(FooChild, 'echo_bar'))
# 判断FooChild类中，是否有echo_bar这个属性
# 执行输出
# True
my_foo = FooChild()
# my_foo.echo_bar()
# 执行输出
# True

# 添加静态方法
@staticmethod
def testStatic():
    print("static method ....")


Foochild = type('Foochild', (Foo,), {"echo_bar": echo_bar, "testStatic": testStatic})
foochid = Foochild()
# print(fooclid.testStatic)
# 执行输出
# <function testStatic at 0x000001D76E1356A8>
# fooclid.testStatic()
# 执行输出
# static method ....
# fooclid.echo_bar()
# 执行输出
# True

# 添加类方法
@classmethod
def testClass(cls):
    print(cls.bar)


Foochild = type('Foochild', (Foo,), {"echo_bar": echo_bar, "testStatic": testStatic, "testClass": testClass})
# foochid = Foochild()
# foochid.testClass()
# 执行输出
# True

# 当你使用关键字class时Python在幕后做的事情，而这就是通过元类来实现的。

# ********************     6. 到底什么是元类
# 元类就是用来创建类的“东西”。元类就是用来创建这些类（对象）的，元类就是类的类
# 函数type实际上是一个元类, type就是Python在背后用来创建所有类的元类
# str是用来创建字符串对象的类，而int是用来创建整数对象的类。type就是创建类对象的类。
# 你可以通过检查__class__属性来看到这一点。
# Python中所有的东西,都是对象。
# 它们全部都是对象，而且它们都是从一个类创建而来，这个类就是type。

age = 35
# print(age.__class__)
# 执行输出
# <class 'int'>
name = 'bob'
# print(name.__class__)
# 执行输出
# <class 'str'>
def foo(): pass
# print(foo.__class__)
# 执行输出
# <class 'function'>
class Bar(object): pass
b = Bar()
# print(b.__class__)
# 执行输出
# <class '__main__.Bar'>

# 现在，对于任何一个__class__的__class__属性又是什么呢？
# print(age.__class__.__class__)
# 执行输出
# <class 'type'>
# print(foo.__class__.__class__)
# 执行输出
# <class 'type'>


# ********************     7. __metaclass__属性
# 你可以在定义一个类的时候为其添加__metaclass__属性
# class Foo(object):
#     __metaclass__ = something
# 如果你这么做了，Python就会用元类来创建类Foo。
# 你首先写下class Foo(object)，但是类Foo还没有在内存中创建。
# Python会在类的定义中寻找__metaclass__属性
# 如果找到了，Python就会用它来创建类Foo，如果没有找到，就会用内建的type来创建这个类。

class Foo(Bar):
    pass


# Python做了如下的操作
# Foo中有__metaclass__这个属性吗？如果有，Python会通过__metaclass__创建一个名字为Foo的类(对象)
# 如果Python没有找到__metaclass__，它会继续在Bar（父类）中寻找__metaclass__属性，并尝试做和前面同样的操作
# 如果Python在任何父类中都找不到__metaclass__，它就会在模块层次中去寻找__metaclass__，并尝试做同样的操作
# 如果还是找不到__metaclass__,Python就会用内置的type来创建这个类对象

# 你可以在__metaclass__中放置些什么代码呢？
# 可以创建一个类的东西。
# 那么什么可以用来创建一个类呢？
# type，或者任何使用到type或者子类化type的东东都可以。

# ********************     8. 自定义元类
# 模块里所有的类的属性都应该是大写形式
# 有好几种方法可以办到，但其中一种就是通过在模块级别设定__metaclass__
# 采用这种方法，这个模块中的所有类都会通过这个元类来创建
# 我们只需要告诉元类把所有的属性都改成大写形式就万事大吉了

# 所以，我们这里就先以一个简单的函数作为例子开始
# python3中
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    # 遍历属性字典，把不是__开头的属性名字变为大写
    newAttr = {}
    for name, value in future_class_attr.items():
        if not name.startswith("__"):
            newAttr[name.upper()] = value
            # 调用type来创建一个类
    return type(future_class_name, future_class_parents, newAttr)


class Foo(object, metaclass=upper_attr):
    bar = 'bip'


# print(hasattr(Foo, 'bar'))
# print(hasattr(Foo, 'BAR'))
# 执行输出
# False
# True
f = Foo()
# print(f.BAR)
# 执行输出
# bip

# 现在让我们再做一次，这一次用一个真正的class来当做元类。
# __new__ 是在__init__之前被调用的特殊方法 用来创建对象并返回之的方法
# 一般很少用到__new__，除非你希望能够控制对象的创建
# 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__


class UpperAttrMetaClass(type):
    def __new__(cls, future_class_name, future_class_parents, future_class_attr):
        # 遍历属性字典，把不是__开头的属性名字变为大写
        newAttr = {}
        for name, value in future_class_attr.items():
            if not name.startswith("__"):
                newAttr[name.upper()] = value

        # 方法1：通过'type'来做类对象的创建
        # return type(future_class_name, future_class_parents, newAttr)

        # 方法2：复用type.__new__方法
        # 这就是基本的OOP编程，没什么魔法
        # return type.__new__(cls, future_class_name, future_class_parents, newAttr)

        # 方法3：使用super方法
        return super(UpperAttrMetaClass, cls).__new__(cls, future_class_name, future_class_parents, newAttr)


# python3的用法
class Foo(object, metaclass = UpperAttrMetaClass):
    bar = 'bip'


# print(hasattr(Foo, 'bar'))
# 输出
# False
# print(hasattr(Foo, 'BAR'))
# 输出
# True

f = Foo()
# print(f.BAR)
# 输出
# 'bip'

# 元类
# 拦截类的创建
# 修改类
# 返回修改之后的类