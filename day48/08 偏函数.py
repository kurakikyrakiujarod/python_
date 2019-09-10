import functools


# partial函数(偏函数)
# 把一个函数的某些参数设置默认值，返回一个新的函数，调用这个新函数会更简单


def showarg(*args, **kw):
    print(args)
    print(kw)


p1 = functools.partial(showarg, 1, 2, 3)
# p1()
# p1(4, 5, 6)
# p1(a='python', b='itcast')

p2 = functools.partial(showarg, a=3, b='linux')
# p2()
# p2(1, 2)
# p2(a='python', b='itcast')

# 输出
# (1, 2, 3)
# {}
# (1, 2, 3, 4, 5, 6)
# {}
# (1, 2, 3)
# {'a': 'python', 'b': 'itcast'}
# ()
# {'a': 3, 'b': 'linux'}
# (1, 2)
# {'a': 3, 'b': 'linux'}
# ()
# {'a': 'python', 'b': 'itcast'}
