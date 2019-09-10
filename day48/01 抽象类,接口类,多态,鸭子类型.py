# 编程原则
# python
# 开放封闭原则 对扩展是开放的 对修改是封闭的
# 依赖倒置原则
# 接口隔离原则

# 一、抽象类

# 与java一样，python也有抽象类的概念但是同样需要借助模块实现，抽象类是一个特殊的类，它的特殊之处在于只能被继承，不能被实例化

# 如果说类是从一堆对象中抽取相同的内容而来的，那么抽象类就是从一堆类中抽取相同的内容而来的，内容包括数据属性和函数属性

# 从设计角度去看，如果类是从现实对象抽象而来的，那么抽象类就是基于类抽象而来的

# 从实现角度来看，抽象类与普通类的不同之处在于
# 抽象类中有抽象方法，该类不能被实例化，只能被继承，且子类必须实现抽象方法

# 归一化设计：不管是哪一个类的对象，都调用同一个函数去完成相似的功能
# 归一化使得高层的外部使用者可以不加区分的处理所有接口兼容的对象集合

# 比如python的len方法，它可以接收很多参数类型，返回对象（字符、列表、元组等）长度或项目个数
# 只有一个类中实现了__len__()方法，才能使用len()方法

from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self): pass


class Alipay(Payment):
    def pay(self, money):
        print('使用支付宝支付了%s元' % money)


class QQpay(Payment):
    def pay(self, money):
        print('使用qq支付了%s元' % money)


class Wechatpay(Payment):
    def fuqian(self, money):
        print('使用微信支付了%s元' % money)


# 实例化
# w = Wechatpay()
# 报错
# TypeError: Can't instantiate abstract class Wechatpay with abstract methods pay

# 继承了Payment类，就必须去实现被abstractmethod装饰的方法

# 抽象类和接口类做的事情 ：建立规范

# 制定一个类的metaclass是ABCMeta，那么这个类就变成了一个抽象类(接口类)，这个类的主要功能就是建立一个规范
# 抽象类中所有被abstractmethod装饰的方法都必须被继承的子类实现 如果不实现，那么在实例化阶段将会报错
# 无论是抽象类还是接口类,都不可以被实例化

# p = Payment()
# 报错
# TypeError: Can't instantiate abstract class Payment with abstract methods pay

# 把fuqian改成pay就可以实例化Wechatpay了

# 依赖倒置原则

# 高层模块不应该依赖低层模块，二者都应该依赖其抽象;抽象不应该应该依赖细节,细节应该依赖抽象
# 换言之，要针对接口编程，而不是针对实现编程

# Payment是高层模块，Wechatpay是底层类
# Wechatpay只能依赖Payment，Payment不能依赖Wechatpay，因为它是底层模块
# Payment是抽象类，它定义了pay方法，具体实现的逻辑，它不需要写，由子类来完成
# 写代码并不是为了实现功能，而是在实现功能的前提下，规划化代码


# 二、接口类


# python里面没有接口的概念，那接口是哪儿来的概念呢？从java里面来的

# 接口类：定义一个接口对继承类进行约束，接口里有什么方法，继承类就必须有什么方法，接口中不能有任何功能代码


# 定义一个抽象类A
from abc import ABCMeta, abstractmethod


class A(metaclass=ABCMeta):
    @abstractmethod
    def fly(self): pass

    @abstractmethod
    def cal_flying_seeed(self): pass

    @abstractmethod
    def cal_flying_height(self): pass


class Tiger(object):  # 老虎
    def walk(self): pass  # 走路

    def swim(self): pass  # 游泳


class Monkey(object):  # 猴子
    def walk(self): pass  # 走路

    def climb(self): pass  # 爬树


class Swan(A):  # 天鹅
    def walk(self): pass

    def swim(self): pass

    def fly(self): pass  # 飞行

    def cal_flying_seeed(self): pass  # 计算飞行速度

    def cal_flying_height(self): pass  # 计算飞行高度


class Parrot(A):
    def fly(self): pass

    def cal_flying_speed(self): pass


# Parrot()
# 报错
# TypeError: Can't instantiate abstract class Parrot with abstract methods cal_flying_height, cal_flying_seeed

# 鹦鹉实例化时，报错，找不到方法cal_flying_height cal_flying_seeed,这样就约束了飞行动物的方法

from abc import ABCMeta, abstractmethod


class FlyAnimal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self): pass

    @abstractmethod
    def cal_flying_speed(self): pass

    @abstractmethod
    def cal_flying_height(self): pass


class WalkAnimal(metaclass=ABCMeta):  # 走路
    @abstractmethod
    def walk(self): pass


class SwimAnimal(metaclass=ABCMeta):  # 游泳
    @abstractmethod
    def swim(self): pass


class Tiger(WalkAnimal, SwimAnimal):  # 老虎,继承走路和游泳
    def walk(self): pass  # 走路

    def swim(self): pass  # 游泳


class Monkey(WalkAnimal):  # 猴子
    def walk(self): pass

    def climb(self): pass  # 爬树


class Swan(FlyAnimal, WalkAnimal, SwimAnimal):  # 天鹅,继承飞行,走路,游泳
    def walk(self): pass

    def swim(self): pass

    def fly(self): pass  # 飞行

    def cal_flying_speed(self): pass  # 计算飞行速度

    def cal_flying_height(self): pass  # 计算飞行高度


class Parrot(FlyAnimal):  # 鹦鹉,继承飞行
    def fly(self): pass

    def cal_flying_speed(self): pass

    def cal_flying_height(self): pass


# 实例化
Tiger()
Monkey()
Swan()
Parrot()


# 执行输出，就没有报错了

# 接口隔离原则：
# 使用多个专门的接口，而不使用单一的总接口。即客户端不应该依赖那些不需要的接口

# 总结：
# 接口类的作用：
# 在java中，能够满足接口隔离原则，且完成多继承的约束
# 而在python中，满足接口隔离原则，由于python本身支持多继承，所以就不需要接口的概念了

# 抽象类和接口类
# 在python中:
# 并没有什么不同，都是用来约束子类中的方法的
# 只要是抽象类和接口类中被abstractmethod装饰的方法，都需要被子类实现
# 需要注意的是，当多个类之间有相同的功能也有不同的功能的时候，应该采用多个接口类来进行分别的约束

# 在java中
# 抽象类和接口截然不同
# 抽象类的本质还是一个类 是类就必须遵循单继承的规则，所以一个子类如果被抽象类约束，那么它只能被一个父类控制
# 当多个类之间有相同的功能也有不同的功能的时候 java只能用接口来解决问题

# 面试的时候
# 他可能会问：什么是抽象类？什么是接口类？
# 抽象类 是python中定义类的一种规范，用来约束子类中的方法的。被abstractmethod装饰的方法，子类必须实现，否则实例化时报错
# 接口类 满足接口隔离原则，且完成多继承的约束。如果不按照规范，在调用方法时，报错


# 三、多态


# 多态指的是一类事物有多种形态
# Python原生是多态的


class Payment:
    @staticmethod
    def pay(pay_obj, money):  # 静态方法.需要通过类名+方法名来调用这个方法
        '''
        统一支付方法
        :param pay_obj: 实例化对象
        :param money: 金钱
        :return: 使用xx支付了xx元
        '''
        pay_obj.pay(money)


class QQpay(Payment):
    def pay(self, money):
        print('使用qq支付了%s元' % money)


class Wechatpay(Payment):
    def pay(self, money):
        print('使用微信支付了%s元' % money)


qq = QQpay()
we = Wechatpay()


# Payment.pay(qq, 100)
# Payment.pay(we, 200)
# 输出
# 使用qq支付了100元
# 使用微信支付了200元

# 传入不同的参数返回不同的结果，这就是多态
# 一种接口，多种实现


# 四、鸭子类型


# Python崇尚鸭子类型，即‘如果看起来像、叫声像而且走起路来像鸭子，那么它就是鸭子

# python程序员通常根据这种行为来编写程序
# 例如，如果想编写现有对象的自定义版本，可以继承该对象,也可以创建一个外观和行为像，但与它无任何关系的全新对象，后者通常用于保存程序组件的松耦合度

# 二者看起来都像文件,因而就可以当文件一样去用


class TxtFile:
    def read(self):
        pass

    def write(self):
        pass


class DiskFile:
    def read(self):
        pass

    def write(self):
        pass


# Python不崇尚通过继承来约束


# 总结：

# 多态和鸭子类型

# 多态
# java在一个类之下发展出来的多个类的对象都可以作为参数传入一个函数或者方法
# 在python中不需要刻意实现多态，因为python本身自带多态效果

# 鸭子类型
# 不是通过具体的继承关系来约束某些类中必须有哪些方法名
# 是通过一种约定俗成的概念来保证在多个类中相似的功能叫相同的名字


class Cat(object):
    def say(self):
        print("i am a cat")


class Dog(object):
    def say(self):
        print("i am a fish")


class Duck(object):
    def say(self):
        print("i am a duck")


animal_list = [Cat, Dog, Duck]

# for animal in animal_list:
#     animal().say()

# 输出
# i am a cat
# i am a fish
# i am a duck


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)


company = Company(["tom", "bob", "jane"])
a = ["bobby1", "bobby2"]
b = ["bobby3", "bobby4"]
a.extend(b)
a.extend(company)
# print(a)

# 输出
# ['bobby1', 'bobby2', 'bobby3', 'bobby4', 'tom', 'bob', 'jane']