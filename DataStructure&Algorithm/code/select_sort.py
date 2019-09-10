#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import time


def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__, t2 - t1))
        return result

    return wrapper


@cal_time
def select_sort(li):
    for i in range(len(li) - 1):
        min_loc = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]


# def selection_sort(alist):
#     n = len(alist)
#     # 需要进行n-1次选择操作
#     for i in range(n - 1):
#         # 记录最小位置
#         min_index = i
#         # 从i+1位置到末尾选择出最小数据
#         for j in range(i + 1, n):
#             if alist[j] < alist[min_index]:
#                 min_index = j
#         # 如果选择出的数据不在正确位置，进行交换
#         if min_index != i:
#             alist[i], alist[min_index] = alist[min_index], alist[i]


# alist = [54, 226, 93, 17, 77, 31, 44, 55, 20]
# selection_sort(alist)
# print(alist)

if __name__ == "__main__":
    data = list(range(10))
    random.shuffle(data)
    print(data)
    select_sort(data)
    print(data)
