# 迭代是访问集合元素的一种方式
# 迭代器一个可以记住遍历的位置的对象，从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退

# 1、 可迭代对象

# 可以直接作用于for循环的数据类型

# 一类是集合数据类型，如 list、tuple、dict、set、str等
# 一类是generator，包括生成器和带yield的generator function
# 这些可以直接作用于for循环的对象统称为可迭代对象(Iterable)

# 2、判断是否可以迭代
# 可以使用isinstance() 判断一个对象是否是 Iterable 对象
# from collections import Iterable
# print(isinstance([], Iterable))
# 输出
# True
# print(isinstance((x for x in range(10)), Iterable))
# 输出
# True
# print(isinstance(100, Iterable))
# 输出
# False

# 3、迭代器

# 凡是可作用于next()函数的对象都是Iterator类型

# 可以使用isinstance()判断一个对象是否是Iterator对象
# from collections import Iterator
# print(isinstance((x for x in range(10)), Iterator))
# 输出
# True
# print(isinstance([], Iterator))
# 输出
# False
# print(isinstance('abc', Iterator))
# 输出
# False

# 4、iter()函数

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数

# from collections import Iterator
# print(isinstance('abc', Iterator))
# print(isinstance(iter('abc'), Iterator))
# 输出
# False
# True