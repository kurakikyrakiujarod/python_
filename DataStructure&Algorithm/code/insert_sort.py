#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def insert_sort(alist):
    # 从第二个位置，即下标为1的元素开始向前插入
    for i in range(1, len(alist)):
        # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i, 0, -1):
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]


# def insert_sort(li):
#     for i in range(1, len(li)):
#         tmp = li[i]
#         j = i - 1
#         while j >= 0 and li[j] > tmp:
#             li[j + 1] = li[j]
#             j = j - 1
#         li[j + 1] = tmp


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insert_sort(alist)
print(alist)
