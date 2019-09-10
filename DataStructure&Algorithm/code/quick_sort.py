#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import random


def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__, t2 - t1))
        return result

    return wrapper


def partition(data, left, right):
    tmp = data[left]
    while left < right:
        while left < right and data[right] >= tmp:
            right -= 1
        data[left] = data[right]
        while left < right and data[left] <= tmp:
            left += 1
        data[right] = data[left]
    data[left] = tmp
    return left


def quick_sort_x(data, left, right):
    if left < right:
        mid = partition(data, left, right)
        quick_sort_x(data, left, mid - 1)
        quick_sort_x(data, mid + 1, right)


@cal_time
def quick_sort(data):
    return quick_sort_x(data, 0, len(data) - 1)


if __name__ == "__main__":
    data = list(range(10))
    random.shuffle(data)
    print(data)
    quick_sort(data)
    print(data)
