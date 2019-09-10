# 多继承以及MRO顺序

# 1. 单独调用父类的方法


class Parent(object):
    def __init__(self, name):
        print('parent的init开始被调用')
        self.name = name
        print('parent的init结束被调用')


class Son1(Parent):
    def __init__(self, name, age):
        print('Son1的init开始被调用')
        self.age = age
        Parent.__init__(self, name)
        print('Son1的init结束被调用')


class Son2(Parent):
    def __init__(self, name, gender):
        print('Son2的init开始被调用')
        self.gender = gender
        Parent.__init__(self, name)
        print('Son2的init结束被调用')


class Grandson(Son1, Son2):
    def __init__(self, name, age, gender):
        print('Grandson的init开始被调用')
        Son1.__init__(self, name, age)
        Son2.__init__(self, name, gender)
        print('Grandson的init结束被调用')


# gs = Grandson('grandson', 12, '男')
# print('姓名：', gs.name)
# print('年龄：', gs.age)
# print('性别：', gs.gender)

# 运行结果
# Grandson的init开始被调用
# Son1的init开始被调用
# parent的init开始被调用
# parent的init结束被调用
# Son1的init结束被调用
# Son2的init开始被调用
# parent的init开始被调用
# parent的init结束被调用
# Son2的init结束被调用
# Grandson的init结束被调用
# 姓名： grandson
# 年龄： 12
# 性别： 男


# 2. 多继承中super调用有所父类的被重写的方法


class Parent(object):
    def __init__(self, name, *args, **kwargs):  # 为避免多继承报错，使用不定长参数，接受参数
        print('parent的init开始被调用')
        self.name = name
        print('parent的init结束被调用')


class Son1(Parent):
    def __init__(self, name, age, *args, **kwargs):  # 为避免多继承报错，使用不定长参数，接受参数
        print('Son1的init开始被调用')
        self.age = age
        super().__init__(name, *args, **kwargs)  # 为避免多继承报错，使用不定长参数，接受参数
        print('Son1的init结束被调用')


class Son2(Parent):
    def __init__(self, name, gender, *args, **kwargs):  # 为避免多继承报错，使用不定长参数，接受参数
        print('Son2的init开始被调用')
        self.gender = gender
        super().__init__(name, *args, **kwargs)  # 为避免多继承报错，使用不定长参数，接受参数
        print('Son2的init结束被调用')


class Grandson(Son1, Son2):
    def __init__(self, name, age, gender):
        print('Grandson的init开始被调用')
        # 多继承时，相对于使用类名.__init__方法，要把每个父类全部写一遍
        # 而super只用一句话，执行了全部父类的方法，这也是为何多继承需要全部传参的一个原因
        # super(Grandson, self).__init__(name, age, gender)
        super().__init__(name, age, gender)
        print('Grandson的init结束被调用')


# print(Grandson.__mro__)
# gs = Grandson('grandson', 12, '男')
# print('姓名：', gs.name)
# print('年龄：', gs.age)
# print('性别：', gs.gender)

# 运行结果
# (<class '__main__.Grandson'>, <class '__main__.Son1'>,
#  <class '__main__.Son2'>, <class '__main__.Parent'>, <class 'object'>)
# Grandson的init开始被调用
# Son1的init开始被调用
# Son2的init开始被调用
# parent的init开始被调用
# parent的init结束被调用
# Son2的init结束被调用
# Son1的init结束被调用
# Grandson的init结束被调用
# 姓名： grandson
# 年龄： 12
# 性别： 男

# 注意
# 以上2个代码执行的结果不同
# 如果2个子类中都继承了父类，当在子类中通过父类名调用时，parent被执行了2次
# 如果2个子类中都继承了父类，当在子类中通过super调用时，parent被执行了1次

# 3. 单继承中super


class Parent(object):
    def __init__(self, name):
        print('parent的init开始被调用')
        self.name = name
        print('parent的init结束被调用')


class Son1(Parent):
    def __init__(self, name, age):
        print('Son1的init开始被调用')
        self.age = age
        super().__init__(name)  # 单继承不能提供全部参数
        print('Son1的init结束被调用')


class Grandson(Son1):
    def __init__(self, name, age, gender):
        print('Grandson的init开始被调用')
        super().__init__(name, age)  # 单继承不能提供全部参数
        print('Grandson的init结束被调用')


# gs = Grandson('grandson', 12, '男')
# print('姓名：', gs.name)
# print('年龄：', gs.age)
# print('性别：', gs.gender)

# 运行结果
# Grandson的init开始被调用
# Son1的init开始被调用
# parent的init开始被调用
# parent的init结束被调用
# Son1的init结束被调用
# Grandson的init结束被调用
# 姓名： grandson
# 年龄： 12


# 总结
# super().__init__相对于类名.__init__，在单继承上用法基本无差
# 但在多继承上有区别，super方法能保证每个父类的方法只会执行一次，而使用类名的方法会导致方法被执行多次，具体看前面的输出结果
# 多继承时，使用super方法，对父类的传参数，应该是由于python中super的算法导致的原因，必须把参数全部传递，否则会报错
# 单继承时，使用super方法，则不能全部传递，只能传父类方法所需的参数，否则会报错
# 多继承时，相对于使用类名.__init__方法，要把每个父类全部写一遍, 而使用super方法，只需写一句话便执行了全部父类的方法，这也是为何多继承需要全部传参的一个原因
