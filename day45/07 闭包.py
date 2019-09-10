# 一、函数名的本质

# 函数名本质上就是函数的内存地址

# 1.可以被引用


def func():
    print('in func')


f = func


# print(f)
# 输出
# <function func at 0x0000027DF0EF2E18>

# 2.可以被当作容器类型的元素


def f1():
    print('f1')


def f2():
    print('f2')


def f3():
    print('f3')


L = [f1, f2, f3]
d = {'f1': f1, 'f2': f2, 'f3': f3}
# 调用
# L[0]()
# d['f2']()
# 输出
# f1
# f2

# 3.可以当作函数的参数和返回值

# 当普通变量用

# 第一类对象（first-class object）指
# 1.可在运行期创建
# 2.可用作函数参数或返回值
# 3.可存入变量的实体


# 函数引用


def test1():
    print("--- in test1 func----")


# 调用函数
# test1()
# 输出
# --- in test1 func----

# 引用函数
ret = test1
# print(id(ret))
# print(id(test1))
# 输出
# 2288330812952
# 2288330812952

# 通过引用调用函数
# ret()
# 输出
# --- in test1 func----

# 二、 什么是闭包


# 定义一个函数
def test(number):
    # 在函数内部再定义一个函数，并且这个函数用到了外边函数的变量
    # 那么将这个函数以及用到的一些变量称之为闭包
    def test_in(number_in):
        print("in test_in 函数, number_in is %d" % number_in)
        return number + number_in

    # 其实这里返回的就是闭包的结果
    return test_in


# 给test函数赋值，这个20就是给参数number
ret = test(20)


# 注意这里的100其实给参数number_in
# print(ret(100))
# 输出
# in test_in 函数, number_in is 100
# 120


# 三、 闭包再理解

# 内部函数对外部函数作用域里变量的引用（非全局变量），则称内部函数为闭包
# 函数内部定义的函数称为内部函数

# 由于闭包引用了外部函数的局部变量，则外部函数的局部变量没有及时释放

def fun_2():
    a = list()

    def fun(num):
        a.append(num)
        # print(num)
        return a

    return fun


g1 = fun_2()
g2 = g1(2)
# print('****', g2)
g3 = g1(3)
# print('*****', g3)
# 输出
# 2
# **** [2]
# 3
# ***** [2, 3]

# 当执行fun_2函数时，变量a被创建。执行g1(2)时，列表a添加一个值2。执行g2(3)时，列表a又添加了一个值。
# 我们知道一个函数内的局部变量的生命周期是从执行函数开始到到结束。
# 而现在我们函数已经执行完了，按道理来讲局部变量a应该清除才对。
# 这就是因为闭包的原因，闭包使用了外部函数的局部变量，这就导致局部变量a一直在内存中无法释放，占用内存。


# nonlocal修改外部函数的局部变量(python3)
def counter(start=0):
    def incr():
        nonlocal start
        start += 1
        return start

    return incr


c1 = counter(5)
# print(c1())
# print(c1())
# 输出
# 6
# 7

# 四、 闭包实例


def line_conf(a, b):
    def line(x):
        return a * x + b

    return line


line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
# print(line1(5))
# print(line2(5))
# 输出
# 6
# 25

# 这个例子中，函数line与变量a,b构成闭包
# 在创建闭包的时候，我们通过line_conf的参数a,b说明了这两个变量的取值，这样，我们就确定了函数的最终形式(y = x + 1和y = 4x + 5)
# 我们只需要变换参数a,b，就可以获得不同的直线表达函数 ----> 闭包具有提高代码可复用性的作用
# 如果没有闭包，我们需要每次创建直线函数的时候同时说明a,b,x。这样，我们就需要更多的参数传递，也减少了代码的可移植性

# 闭包思考
# 1.闭包优化了变量，原来需要类对象完成的工作，闭包也可以完成
# 2.由于闭包引用了外部函数的局部变量，则外部函数的局部变量没有及时释放，消耗内存

# 闭包就是为了不动原函数的代码，还要给它增加新功能的一个手段
# 通过外面的一层层函数传递的参数，让最内层函数直接调用外层函数的代码，增加了新的功能