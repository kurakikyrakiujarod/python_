# 一个列表l=['a','b','c','d','e']，取列表中的内容
# 用索引取值和for循环取值
# 用索引取值，你可以取到任意位置的值，前提是你要知道这个值在什么位置
# for循环来取值，我们把每一个值都取到，不需要关心每一个值的位置，因为只能顺序的取值，并不能跳过任何一个直接去取其他位置的值

# 1、迭代器

# python中的for循环
# for i in 1234:
#     print(i)
# 输出
# TypeError: 'int' object is not iterable

# 迭代就是将某个数据集内的数据“一个挨着一个的取出来”

# for怎么知道谁是可迭代--->可迭代协议
# 可迭代协议的定义非常简单，就是内部实现了__iter__方法

# print('__iter__' in dir([]))
# print('__iter__' in dir((x * 2 for x in range(10))))
# 输出
# True
# True

X = [1, 2].__iter__()
# print(X)
# 输出
# <list_iterator object at 0x00000264E2CD87F0
# 执行了list([1,2])的__iter__方法，得到一个list_iterator

A = set(dir([1, 2].__iter__())) - set(dir([1, 2]))
# print(A)
# 输出
# {'__setstate__', '__length_hint__', '__next__'}

iter_l = [1, 2, 3, 4, 5, 6].__iter__()

# 获取迭代器中元素的长度
# print(iter_l.__length_hint__())
# 输出
# 6

# 根据索引值指定从哪里开始迭代
# print('*', iter_l.__setstate__(4))
# 输出
# * None

# 一个一个的取值
# print('**', iter_l.__next__())
# print('***', iter_l.__next__())
# 输出
# ** 5
# *** 6

# 在for循环中，就是在内部调用了__next__方法才能取到一个一个的值
# 用迭代器的next方法来写一个不依赖for的遍历

l = [1, 2, 3, 4]
l_iter = l.__iter__()
while True:
    try:
        item = l_iter.__next__()
        # print(item)
    except StopIteration:
        break


# 输出
# 1
# 2
# 3
# 4

# 迭代器遵循迭代器协议：必须拥有__iter__方法和__next__方法

# for循环就是基于迭代器协议提供了一个统一的可以遍历所有对象的方法
# 即在遍历之前，先调用对象的__iter__方法将其转换成一个迭代器
# 然后使用迭代器协议去实现循环访问，这样所有的对象就都可以通过for循环来遍历了

# 2、生成器

# 本质：迭代器(所以自带了__iter__方法和__next__方法，不需要我们去实现)
# 特点：惰性运算,开发者自定

# 初识生成器一

def genrator_fun1():
    a = 1
    print('现在定义了a变量')
    yield a
    b = 2
    print('现在又定义了b变量')
    yield b


g1 = genrator_fun1()


# print('g1 : ', g1)  # 打印g1可以发现g1就是一个生成器
# print('-' * 20)  # 我是华丽的分割线
# print(next(g1))
# print(next(g1))
# 输出
# g1 :  <generator object genrator_fun1 at 0x000002574AC4DE08>
# --------------------
# 现在定义了a变量
# 1
# 现在又定义了b变量
# 2

# 初识生成器二

def produce():
    """生产衣服"""
    for i in range(2000000):
        yield "生产了第%s件衣服" % i


product_g = produce()
# print(product_g.__next__())  # 要一件衣服
# print(product_g.__next__())  # 再要一件衣服
# print(product_g.__next__())  # 再要一件衣服
num = 0
for i in product_g:  # 要一批衣服，比如5件
    # print(i)
    num += 1
    if num == 5:
        break


# 输出
# 生产了第0件衣服
# 生产了第1件衣服
# 生产了第2件衣服
# 生产了第3件衣服
# 生产了第4件衣服
# 生产了第5件衣服
# 生产了第6件衣服
# 生产了第7件衣服


# 3、send

def generator():
    print(123)
    content = yield 1
    print('=======', content)
    print(456)
    yield 2


g = generator()


# ret = g.__next__()
# print('***', ret)
# ret = g.send('hello')  # send的效果和next一样
# print('***', ret)
# 输出
# 123
# *** 1
# ======= hello
# 456
# *** 2

# send获取下一个值的效果和next基本一致 只是在获取下一个值的时候，给上一yield的位置传递一个数据
# 使用send的注意事项
# 第一次使用生成器的时候 是用next获取下一个值
# 最后一个yield不能接受外部的值

# 4、计算移动平均值

def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        temp = yield average
        total += temp
        count += 1
        average = total / count


g_avg = averager()
next(g_avg)


# print(g_avg.send(10))
# print(g_avg.send(30))
# print(g_avg.send(5))
# 输出
# 10.0
# 20.0
# 15.0


# 预激协程的装饰器

# 在调用被装饰生成器函数的时候首先用next激活生成器
def init(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g

    return inner


@init
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        temp = yield average
        total += temp
        count += 1
        average = total / count


g_avg = averager()


# print(g_avg.send(10))
# print(g_avg.send(30))
# print(g_avg.send(5))
# 输出
# 10.0
# 20.0
# 15.0

# 5、yield from
def gen1():
    for c in 'AB':
        yield c
    for i in range(3):
        yield i


# print(list(gen1()))
# 输出
# ['A', 'B', 0, 1, 2]


def gen2():
    yield from 'AB'
    yield from range(3)


# print(list(gen2()))
# 输出
# ['A', 'B', 0, 1, 2]

# 6、小结

# 可迭代对象：拥有__iter__方法
# 特点：惰性运算
# 例如:range(),str,list,tuple,dict,set

# 迭代器Iterator：拥有__iter__方法和__next__方法
# 例如 iter(range()),iter(str),iter(list),reversed(list_o),map(func,list_o),filter(func,list_o)

# 生成器Generator：本质 迭代器，所以拥有__iter__方法和__next__方法
# 特点：惰性运算,开发者自定义

# 生成器的优点
# 1.延迟计算，一次返回一个结果。也就是说，它不会一次生成所有的结果，这对于大数据量处理，将会非常有用
# 2.提高代码可读性

# 列表解析
# 内存占用大,机器容易卡死
# sum([i for i in range(100000000)])

# 生成器表达式
# 几乎不占内存
# sum(i for i in range(100000000))

# 7、生成器相关的面试题

# 一、

def demo():
    for i in range(4):
        yield i


g = demo()

g1 = (i for i in g)
g2 = (i for i in g1)


# print(list(g1))
# print(list(g2))
# 输出
# [0, 1, 2, 3]
# []

# 二、

def add(n, i):
    return n + i


def test():
    for i in range(4):
        yield i


g = test()
for n in [1, 10]:
    g = (add(n, i) for i in g)

# print(list(g))
# 输出
# [20, 21, 22, 23]

# 执行逻辑
# n = 10
# print(add(n, i) for i in add(n, i) for i in test())
# [0 + 10 + 10, 1 + 10 + 10, 2 + 10 + 10, 3 + 10 + 10]
