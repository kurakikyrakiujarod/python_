# https://blog.csdn.net/youngbit007/article/details/64905070


# 示例1


def scope_test():

    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignmane:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


# scope_test()
# print("In global scope:", spam)
# 输出
# After local assignmane: test spam
# After nonlocal assignment: nonlocal spam
# After global assignment: nonlocal spam
# In global scope: global spam

# do_local函数定义了另外的一个spam字符串变量，并且生命周期只在此函数内。此处的spam和外层的spam是两个变量，如果写出spam = spam + “local spam” 会报错
# do_nonlocal函数使用外层的spam变量


# 示例2

# global定义的变量，表明其作用域在局部以外，即局部函数执行完之后，不销毁函数内部以global定义的变量


def add_a():
    global a
    a = 3


# add_a()
# print(a)
# 输出
# 3


# 示例3

# 在函数add_b内global定义的变量b，能在函数do_global内被引用,但要在do_global内修改,必须在do_global函数里面声明global b


def add_b():
    global b
    b = 42

    def do_global():
        global b
        b = b + 10
        print(b)

    do_global()
    print(b)


# add_b()
# 输出
# 52
# 52


# 示例4


def add_b():
    # global b
    b = 42

    def do_global():
        nonlocal b
        b = 10
        print(b)

    do_global()
    print(b)


# add_b()
# 输出
# 10
# 10

# 如果在最后加上print(" b = %s " % b)，则会报错NameError: name 'b' is not defined
# nonlocal适用于在局部函数中的局部函数，把最内层的局部变量设置成外层局部可用，但是还不是全局的
# 将add_b函数加上global  b声明，会报错SyntaxError: no binding for nonlocal 'b' found
# nonlocal要绑定一个局部变量
# nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量

# 示例5


def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


def make_counter_test():
    mc = make_counter()
    print(mc())
    print(mc())
    print(mc())


# make_counter_test()
# 输出
# 1
# 2
# 3

# 示例6


def add_b():
    global b
    b = 42

    def do_global():
        global b
        b = b + 10
        print(b)

    do_global()
    print(b)


# add_b()
# print(b)
# 输出
# 52
# 52
# 52


# 示例7


def add_b():
    b = 42

    def do_global():
        global b
        b = 10
        print(b)

    do_global()
    print(b)


# add_b()
# print("b = %s " % b)
# 输出
# 10
# 42
#  b = 10

# 为什么do_global函数打印的全局变量b而不是外层变量b