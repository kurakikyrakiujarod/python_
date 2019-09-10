# 限制实例的属性
# Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性


class Person(object):
    __slots__ = ("name", "age")


p = Person()
p.name = "老王"
p.age = 20
# p.score = 100
# 输出
# AttributeError: 'Person' object has no attribute 'score'

# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的


class Test(Person):
    pass


t = Test()
t.score = 100
# 正常执行