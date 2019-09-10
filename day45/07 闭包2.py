# 判断闭包函数的方法__closure__


# 输出的__closure__有cell元素 ：是闭包函数
def func():
    name = 'eva'

    def inner():
        print(name)

    # print(inner.__closure__)
    return inner


f = func()
# f()
# 输出
# (<cell at 0x000001BC28417078: str object at 0x000001BC28308730>,)
# eva


# 输出的__closure__为None ：不是闭包函数
name = 'egon'


def func2():
    def inner():
        print(name)

    # print(inner.__closure__)
    return inner


f2 = func2()


# f2()
# 输出
# None
# egon

# 闭包嵌套


def wrapper():
    money = 1000

    def func():
        name = 'eva'

        def inner():
            print(name, money)

        return inner

    return func


f = wrapper()
i = f()
# i()
# 输出
# eva 1000
