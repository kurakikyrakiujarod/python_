# 内建属性


# 常用专有属性	                 说明	                        触发方式
# __init__	                构造初始化函数	            创建实例后,赋值时使用,在__new__后
# __new__	                生成实例所需属性	        创建实例时
# __class__	                实例所在的类	            实例.__class__
# __str__	                实例字符串表示,可读性	    print(类实例),如没实现，使用repr结果
# __repr__	                实例字符串表示,准确性	    类实例 回车 或者 print(repr(类实例))
# _del__	                析构	                    del删除实例
# __getattribute__	        属性访问拦截器	            访问实例属性时
# __bases__	                类的所有父类构成元素	    类名.__bases__

# __getattribute__例子:


class Itcast(object):
    def __init__(self, subject1):
        self.subject1 = subject1
        self.subject2 = 'cpp'

    def __getattribute__(self, obj):
        if obj == 'subject1':
            print('log subject1')
            return 'redirect python'
        else:  # 测试时注释掉这2行，将找不到subject2
            return object.__getattribute__(self, obj)

    def show(self):
        print('this is Itcast')


s = Itcast("python")

# print(s.subject1)
# print(s.subject2)
# s.show()

# 输出
# log subject1
# redirect python
# cpp
# this is Itcast


# __getattribute__的坑


class Person(object):
    def __getattribute__(self, obj):
        print("---test---")
        if obj.startswith("a"):
            return "hahha"
        else:
            return self.test

    def test(self):
        print("heihei")


t = Person()

# 返回hahha
# t.a

# t.b

# 当t.b执行时，会调用Person类中定义的__getattribute__方法，但是在这个方法的执行过程中
# if条件不满足，所以 程序执行else里面的代码，即return self.test
# 问题就在这，因为return需要把 self.test的值返回，那么首先要获取self.test的值
# 因为self此时就是t这个对象，所以self.test就是t.test
# 此时要获取t这个对象的test属性，那么就会跳转到__getattribute__方法去执行，即此时产生了递归调用

# 由于这个递归过程中 没有判断什么时候推出，所以这个程序会永无休止的运行下去
# 每次调用函数，就需要保存一些数据，那么随着调用的次数越来越多，最终内存吃光，所以程序崩溃

# 注意：以后不要在__getattribute__方法中调用self.xxxx
