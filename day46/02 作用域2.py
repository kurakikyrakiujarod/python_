# 1、楔子


def my_max(x, y):
    m = x if x > y else y


my_max(10, 20)
# print(m)
# 输出
# NameError: name 'm' is not defined

# 错误提示：变量m没有被定义 ----> 变量m是在函数内部定义的

# python代码运行的时候遇到函数
# 从python解释器开始执行之后，就在内存中开辟了一个空间 每当遇到一个变量的时候，就把变量名和值之间的对应关系记录下来
# 但是当遇到函数定义的时候解释器只是象征性的将函数名读入内存，表示知道这个函数的存在，至于函数内部的变量和逻辑解释器根本不关心
# 等执行到函数调用的时候，python解释器会再开辟一块内存来存储这个函数里的内容
# 这个时候，才关注函数里面有哪些变量，而函数中的变量会存储在新开辟出来的内存中
# 函数中的变量只能在函数的内部使用，并且会随着函数执行完毕，这块内存中的所有内容也会被清空

# 我们给这个“存放名字与值的关系”的空间起了一个名字——叫做命名空间
# 在函数的运行中开辟的临时的空间叫做局部命名空间

# 2、命名空间和作用域


# 命名空间的本质：存放名字与值的绑定关系

# 命名空间一共分为三种：
# 内置命名空间
# 全局命名空间
# 局部命名空间

# 内置命名空间中存放了python解释器为我们提供的名字，它们都是我们熟悉的，拿过来就可以用的方法

# 三种命名空间之间的加载与取值顺序

# 加载顺序
# 内置命名空间(程序运行前加载)->全局命名空间(程序运行中，从上到下加载)->局部命名空间(程序运行中，调用时才加载)

# 取值
# 在局部调用：局部命名空间---->全局命名空间--->内置命名空间
# 在全局调用：全局命名空间->内置命名空间

# 在全局引用变量x
x = 1


def f(x):
    print(x)


# f(10)
# print(x)
# 输出
# 10
# 1

# 作用域就是作用范围，按照生效范围可以分为全局作用域和局部作用域
# 全局作用域：包含内置名称空间、全局名称空间，在整个文件的任意位置都能被引用、全局有效
# 局部作用域：局部名称空间，只能在局部范围内生效

# 在全局调用globals和locals
# print(globals())
# 输出
# {'__name__': '__main__', '__doc__': None, '__package__': None,
#  '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000018AE2A28780>,
# '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>,
# '__file__': 'E:/code/github_python/day46/02 作用域2.py', '__cached__': None,
#  'my_max': <function my_max at 0x0000018AE2932E18>, 'x': 1, 'f': <function f at 0x0000018AE2C95620>}

# print(locals())
# 输出
# {'__name__': '__main__', '__doc__': None, '__package__': None,
#  '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000018AE2A28780>,
# '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>,
# '__file__': 'E:/code/github_python/day46/02 作用域2.py', '__cached__': None,
#  'my_max': <function my_max at 0x0000018AE2932E18>, 'x': 1, 'f': <function f at 0x0000018AE2C95620>}

# 在局部调用globals和locals
def func():
    a = 12
    b = 20
    print(locals())
    print(globals())


# func()
# 输出
# {'b': 20, 'a': 12}
# {'__name__': '__main__', '__doc__': None, '__package__': None,
# '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000002758BA68780>,
# '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>,
# '__file__': 'E:/code/github_python/day46/02 作用域2.py',
# '__cached__': None, 'my_max': <function my_max at 0x000002758B972E18>,
#  'x': 1, 'f': <function f at 0x000002758BCD5620>, 'func': <function func at 0x000002758BCD56A8>}


# 3、函数的嵌套和作用域链


# 函数的嵌套调用

def f1():
    def f2():
        def f3():
            print("in f3")

        print("in f2")
        f3()

    print("in f1")
    f2()


# f1()
# 输出
# in f1
# in f2
# in f3

# 4、nonlocal关键字
# 1.外部必须有这个变量
# 2.在内部函数声明nonlocal变量之前不能再出现同名变量
# 3.内部修改这个变量如果想在外部有这个变量的第一层函数中生效

def f1():
    a = 1

    def f2():
        nonlocal a
        a = 2

    f2()
    print('a in f1 : ', a)


# f1()
# 输出
# a in f1 :  2
