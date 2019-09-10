# 生成器generator
# 在Python中，这种一边循环一边计算的机制

# 1、创建生成器方法1

# 把一个列表生成式的 [ ] 改成 ( )

L = [x * 2 for x in range(5)]
# print(L)
G = (x * 2 for x in range(5))


# print(G)
# 输出
# [0, 2, 4, 6, 8]
# <generator object <genexpr> at 0x000002215E5456D0>

# print(next(G))
# 输出
# 0
# print(next(G))
# 输出
# 2
# print(next(G))
# 输出
# 4
# print(next(G))
# 输出
# 6
# print(next(G))
# 输出
# 8
# print(next(G))
# 输出
# StopIteration

# for x in G:
#     print(x)
# 输出
# 0
# 2
# 4
# 6
# 8

# 生成器保存的是算法
# 每次调用next(G)就计算出G的下一个元素的值
# 直到计算到最后一个元素，没有更多的元素时，抛出 StopIteration 的异常

# 2、 创建生成器方法2

# 生成器函数
# 一个包含yield关键字的函数就是一个生成器函数
# yield可以为我们从函数中返回值，但是yield又不同于return，return的执行意味着程序的结束
# 调用生成器函数不会得到返回的具体的值，而是得到一个可迭代的对象 每一次获取这个可迭代对象的值，就能推动函数的执行，获取新的返回值 直到函数执行结束

def fib(times):
    n = 0
    a, b = 0, 1
    while n < times:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


# for n in fib(5):
#     print(n)
# 输出
# 1
# 1
# 2
# 3
# 5

# for循环调用generator时，发现拿不到generator的return语句的返回值
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中

g = fib(5)
while True:
    try:
        x = next(g)
        # print("value:%d" % x)
    except StopIteration as e:
        # print("生成器返回值:%s" % e.value)
        break
# 输出
# value:1
# value:1
# value:2
# value:3
# value:5
# 生成器返回值:done

# 3、send


def gen():
    i = 0
    while i < 5:
        temp = yield i
        print('生成器打印%s' % temp)
        i += 1


# 使用__next__()方法
f = gen()
# print(f.__next__())
# 输出
# 0
# print(f.send('haha'))
# 输出
# 生成器打印haha
# 1
# print(f.__next__())
# 输出
# 生成器打印None
# 2
# print(f.send('haha'))
# 生成器打印haha
# 3

# 执行到yield时，gen函数作用暂时保存，返回i的值，temp接收下次send发送过来的值

