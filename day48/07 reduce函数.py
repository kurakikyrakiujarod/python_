# 在 Python3 中，reduce() 函数已经被从全局名字空间里移除了，它现在被放置在 fucntools 模块里,用的话要先引入：

# def reduce(function, sequence, initial=None):  # real signature unknown; restored from __doc__
#     """
#     reduce(function, sequence[, initial]) -> value
#
#     Apply a function of two arguments cumulatively to the items of a sequence,
#     from left to right, so as to reduce the sequence to a single value.
#     For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
#     ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
#     of the sequence in the calculation, and serves as a default when the
#     sequence is empty.
#     """
#     pass
#

# function:该函数有两个参数
# sequence:序列可以是str，tuple，list
# initial:固定初始值


# reduce依次从sequence中取一个元素，和上一次调用function的结果做参数再次调用function
# 第一次调用function时，如果提供initial参数，会以sequence中的第一个元素和initial 作为参数调用function
# 否则会以序列sequence中的前两个元素做参数调用function
# 注意function函数不能为None
from functools import reduce

# print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))
# print(reduce(lambda x, y: x + y, [1, 2, 3, 4], 5))
# print(reduce(lambda x, y: x + y, ['aa', 'bb', 'cc'], 'dd'))

# 输出
# 10
# 15
# ddaabbcc

sentences = [
    'The Deep Learning textbook is a resource intended to help students and'
    ' practitioners enter the field of machine learning in general and deep learning in particular. '
]

word_count = reduce(lambda a, x: a + x.count("learning"), sentences, 0)

# print(word_count)
# 输出
# 2

# 0--> a + sentences[0].count("learning")