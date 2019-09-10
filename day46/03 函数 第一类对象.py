# https://foofish.net/function-is-first-class-object.html

# 什么是“第一类”对象？

# 在计算机科学中指可以在执行期创造并作为参数传递给其他函数或存入一个变量的实体
# 将一个实体变为第一类对象的过程叫做“物件化”（Reification）

# 这意味着对对象的使用没有限制
# 第一类对象是一个实体，可以动态创建，销毁，传递给函数，作为值返回，并且具有作为编程语言中其他变量的所有权限

# 第一类对象不一定是面向对象程序设计所指的物件，而可以指任何程序中的实体

# 一般第一类对象所特有的特性为
# 1.可以被存入变量或其他结构
# 2.可以被作为参数传递给其他函数
# 3.可以被作为函数的返回值
# 4.可以在执行期创造，而无需完全在设计期全部写出
# 5.即使没有被系结至某一名称，也可以存在

# 在Python中函数是第一类对象
# C中的函数是第二类，因为它们不能被动态创建


def foo(text):
    return len(text)


# 函数身为一个对象，拥有对象模型的三个通用属性：id、类型、和值

# print(id(foo))
# print(type(foo))
# print(foo)
# 输出
# 1415600352792
# <class 'function'>
# <function foo at 0x00000149985B2E18>

# 1.作为对象，函数可以赋值给一个变量

# 赋值给另外一个变量时，函数并不会被调用，仅仅是在函数对象上绑定一个新的名字而已
# 可以把该函数赋值给更多的变量，唯一变化的是该函数对象的引用计数不断地增加，本质上这些变量最终指向的都是同一个函数对象

bar = foo
a = foo
b = foo
c = bar
# print(a is b is c)
# 输出
# True

# 2.函数可以存储在容器

funcs = [foo, str, len]


# print(funcs)
# 输出
# [<function foo at 0x000002295F7D2E18>, <class 'str'>, <built-in function len>]
# for f in funcs:
#     print(f("hello"))
# 输出
# 5
# hello
# 5

# 也可以使用列表的索引定位到元素来调用函数
# print(funcs[0]("Python之禅"))
# 输出
# 8

# 3.函数可以作为参数

# 函数还可以作为参数值传递给另外一个函数

def show(func):
    size = func("python 之禅")
    print("length of string is : %s" % size)


# show(foo)
# 输出
# length of string is : 9

# 4.函数可以作为返回值
# 函数作为另外一个函数的返回值
def nick():
    return foo


# print(nick()("python"))
# 输出
# 6

# 函数接受一个或多个函数作为输入或者函数输出（返回）的值是函数时，我们称这样的函数为高阶函数
# Python内置函数中，map函数就是典型的高阶函数
# map函数
# 接受一个函数和一个迭代对象作为参数，调用map时，依次迭代把迭代对象的元素作为参数调用该函数

lens = map(foo, ["the", "zen", "of", "python"])
# print(list(lens))
# 输出
# [3, 3, 2, 6]

# 相当于[foo(i) for i in ["the","zen","of","python"]]
# print([foo(i) for i in ["the","zen","of","python"]])
# 输出
# [3, 3, 2, 6]

# 5.函数可以嵌套

# 6.实现了 __call__ 的类也可以作为函数
# 对于一个自定义的类，如果实现了_call_方法，那么该类的实例对象的行为就是一个函数，是一个可以被调用（callable)的对象


class Add:
    def __init__(self, n):
         self.n = n

    def __call__(self, x):
        return self.n + x


add = Add(1)
ret = add(4)
# print(ret)
# 输出
# 5

# 执行add(4)相当于调用Add._call__(add, 4)，self就是实例对象add，self.n等于1，所以返回值为1+4

# 确定对象是否为可调用对象可以用内置函数callable来判断

# print(callable(foo))
# print(callable(1))
# print(callable(int))
# 输出
# True
# False
# True

# 7.函数在执行期创造

# exec('''def foo2():
#     print("haha")
# foo2()''')
# 输出
# haha

# 8.没有被系结至某一名称的匿名函数lambda
# print(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))