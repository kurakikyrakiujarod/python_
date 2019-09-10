# Python的类可以继承多个类，Java和C#中则只能继承一个类
# Python的类如果继承了多个类，如果继承了多个类，那么其寻找方法的方式有两种，分别是：深度优先和广度优先
# 当类是经典类时，多继承情况下，会按照深度优先方式查找
# 当类是新式类时，多继承情况下，会按照广度优先方式查找


# 继承查找顺序


class A(object):
    def test(self):
        print('from A')


class B(A):
    def test(self):
        print('from B')


class C(A):
    def test(self):
        print('from C')


class D(B):
    def test(self):
        print('from D')


class E(C):
    def test(self):
        print('from E')


class F(D, E):
    # def test(self):
    #     print('from F')
    pass


f1 = F()
# f1.test()
# print(F.__mro__)

# 输出
# from D
# (<class '__main__.F'>, <class '__main__.D'>, <class '__main__.B'>,
# <class '__main__.E'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# python3中统一都是新式类，新式类继承顺序:F->D->B->E->C->A
# #pyhon2中才分新式类与经典类，经典类继承顺序:F->D->B->A->E->C

# 继承原理

# python到底是如何实现继承的?
# 对于你定义的每一个类，python会计算出一个方法解析顺序(MRO)列表，这个MRO列表就是一个简单的所有基类的线性顺序列表
# 为了实现继承,python会在MRO列表上从左到右开始查找基类,直到找到第一个匹配这个属性的类为止，MRO列表的构造是通过一个C3算法来实现的
# 它实际上就是合并所有父类的MRO列表并遵循如下三条准则
# 1.子类会先于父类被检查
# 2.多个父类会根据它们在列表中的顺序被检查
# 3.如果对下一个类存在两个合法的选择,选择第一个父类

# 经典面试题


class A:
    def func(self):
        print('A')


class B(A):
    def func(self):
        super().func()
        print('B')


class C(A):
    def func(self):
        super().func()
        print('C')


class D(B, C):
    def func(self):
        super().func()
        print('D')


d = D()
# d.func()

# 输出
# A
# C
# B
# D

# super()
# 在单继承中就是单纯的寻找父类
# 在多继承中就是根据子节点 所在图的mro循环找寻下一个类