# 多态

# 面向对象三大特性

# 封装 根据职责将属性和方法封装到一个抽象的类中
#      定义类的准则
# 继承 实现代码的重用，相同的代码不需要重复的编写
#      设计类的技巧
#      子类针对自己特有的需求，编写特定的代码
# 多态 不同的子类对象调用相同的父类方法，产生不同的执行结果
#      多态可以增加代码的灵活度
#      以继承和重写父类方法为前提
#      是调用方法的技巧，不会影响到类的内部设计

# 多态案例演练


class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍..." % self.name)


class XiaoTianDog(Dog):
    def game(self):
        print("%s 飞到天上去玩耍..." % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和 %s 快乐的玩耍..." % (self.name, dog.name))

        # 让狗玩耍
        dog.game()


# 1. 创建一个狗对象
wangcai1 = Dog("旺财")
wangcai2 = XiaoTianDog("飞天旺财")

# 2. 创建一个小明对象
xiaoming = Person("小明")

# 3. 让小明调用和狗玩的方法
xiaoming.game_with_dog(wangcai1)
xiaoming.game_with_dog(wangcai2)

# 运行结果
# 小明 和 旺财 快乐的玩耍...
# 旺财 蹦蹦跳跳的玩耍...
# 小明 和 飞天旺财 快乐的玩耍...
# 飞天旺财 飞到天上去玩耍...

# Person类中只需要让狗对象调用game方法，而不关心具体是什么狗 game方法是在Dog父类中定义的
# 在程序执行时，传入不同的狗对象实参，就会产生不同的执行效果

# 多态 更容易编写出出通用的代码，做出通用的编程，以适应需求的不断变化