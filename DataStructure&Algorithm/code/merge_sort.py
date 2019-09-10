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


def merge(li, low, mid, high):
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    li[low:high + 1] = ltmp


def _mergesort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        _mergesort(li, low, mid)
        _mergesort(li, mid + 1, high)
        merge(li, low, mid, high)


@cal_time
def merge_sort(li):
    _mergesort(li, 0, len(li) - 1)


if __name__ == "__main__":
    data = list(range(10000))
    random.shuffle(data)
    print(data)
    merge_sort(data)
    print(data)
