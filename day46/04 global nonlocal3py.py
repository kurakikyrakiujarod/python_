# https://blog.csdn.net/qq_36346262/article/details/79291305

# 一   global是标记此变量是全局变量

# b = 12
#
#
# def get():
#     b = b + 2
#     return b
#
#
# print(get())
# 报错
# UnboundLocalError: local variable 'b' referenced before assignment

# 这是因为python3里面对全局变量只能引用不能修改，如果修改需要加上global声明。
# 将上面这段代码改一下就可以得到正确的结果

b = 12


def get():
    global b
    b = b + 2
    return b


# print(get())
# 输出
# 14

# 如果函数外面没有声明变量，直接在函数里面用global声明一个变量，当调用了这个函数后，在外面也可以用这个变量了


def get():
    global b
    b = 4
    b = b + 2
    return b


# print(get())
# print(b)
# 输出
# 6
# 6

L = [1, 2]


def get():
    L.append(3)
    return L


# print(get())
# print(L)
# 输出
# [1, 2, 3]
# [1, 2, 3]

# 这段代码没有用global声明
# 本质上说get()函数并没有修改L，对于list这类可变变量来说，对其删除和添加元素并不能算是修改该变量
# 对于L来说其指向的对象并没有改变，只是对象本身变了而已

L = [1, 2]


def get():
    L = 2
    return L


# print(get())
# print(L)
# 输出
# 2
# [1, 2]

# 这段代码并没有报错，因为get()函数内部的L看成了初始化了一个局部变量的操作，而全局的L并没有改变

L = [1, 2]


def get():
    global L
    L = 2
    return L


# print(get())
# print(L)
# 输出
# 2
# 2

# 以上代码就会修改外部的全局变量

# 二     nonlocalb声明的变量，会从当前作用域的外层(该外层不能包括全局变量)寻找该变量


# b = 1
#
#
# def get():
#     nonlocal b
#     b = b + 10
#     return b


# print(get())
# print(b)
# 报错
# SyntaxError: no binding for nonlocal 'b' found

# 以上代码会报错，这个就是（该外层不包括全局）的意思

# b = 10
#
#
# def get():
#     b = 20
#
#     def f():
#         b = b + 1
#         return b
#
#     print(f())
#     return b
#
#
# print(get())
# print(b)
# 报错
# UnboundLocalError: local variable 'b' referenced before assignment

# 这段代码会报错，但是如果在f函数内部加上nonlocal声明的话，就可以正常运行了输出是：21 21 10
# 如果把f函数内的加上global申明的话，输出就会变成：11 20 11
# 可以看出虽然变量名字一样，但只要加上global声明就会和最外层的全局变量绑定

b = 10


def get():
    b = 20

    def f():
        b = 11

        def w():
            nonlocal b
            b = -1
            return b

        print('w -> %d' % w())
        return b

    print('f -> %d' % f())
    return b


# print('get -> %d' % get())
# print('b -> %d' % b)
# 输出
# w -> -1
# f -> -1
# get -> 20
# b -> 10

# 上面这个函数和输出结果说明，nonlocal会绑定和当前作用域最近的那个变量

b = 10


def get():
    b = 20

    def f():
        def w():
            nonlocal b
            b = -1
            return b

        print('w -> %d' % w())
        return None

    f()
    return b


# print('get -> %d' % get())
# print('b -> %d' % b)
# 输出
# w -> -1
# get -> -1
# b -> 10

# 这里发现即使相隔两层，但是仍然可以绑定到所需要的变量

# b = 10
#
#
# def get():
#     def g():
#         b = 1
#         return 1
#
#     def f():
#         nonlocal b
#         b = 20
#         return b
#
#     print('g -> %d' % g())
#     print('f -> %d' % f())
#     return b
#
#
# print('get -> %d' % get())
# print('b -> %d' % b)
# 报错
# SyntaxError: no binding for nonlocal 'b' found

# 上面这段代码会报错，这个说明，对于并行的两个函数的变量，无法相互绑定。只有包含关系才可以

# In [1]: b = 12
#    ...:
#    ...:
#    ...: def get():
#    ...:     nonlocal b
#    ...:     b = 2
#    ...:     return b
#    ...:
#   File "<ipython-input-1-c91122657aa3>", line 5
#     nonlocal b
#     ^
# SyntaxError: no binding for nonlocal 'b' found

# 这个函数不被调用也会报错
