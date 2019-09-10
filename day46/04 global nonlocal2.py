# 示例8


def add_b():
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

# 示例9


# def add_b():
#     # global b
#     # b = 42
#     def do_global():
#         nonlocal b
#         b = 10
#         print(b)
#
#     do_global()
#     print(b)


# add_b()
# 报错 SyntaxError: no binding for nonlocal 'b' found

# nonlocal要绑定一个局部变量b, 不存在或者b是全局变量就会报错

# 示例10


# def add_b():
#     def do_global():
#         global b
#         b = 10
#         print(b)
#
#     do_global()
#     b = b + 20
#     print(b)
#
#
# add_b()
# 输出
# 10
# UnboundLocalError: local variable 'b' referenced before assignment

# 不理解 需要在add_b加global b才不会报错

# 示例11


def add_b():
    b = 42

    def do_global():
        global b
        b = 10
        print(b)

    do_global()
    b = b + 5
    print(b)


# add_b()
# b = b + 30
# print("b = %s " % b)
# 输出
# 10
# 47
# b = 40

# 示例12


def add_b():
    global b
    b = 42

    def do_global():
        global b
        b = 10
        print(b)

    do_global()
    b = b + 5
    print(b)


# add_b()
# b = b + 30
# print("b = %s " % b)
# 输出
# 10
# 15
# b = 45


