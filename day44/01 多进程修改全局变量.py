# coding=utf-8
import os
import time

num = 0

# 注意，fork函数，只在Unix/Linux/Mac上运行，windows不可以
pid = os.fork()

if pid == 0:
    num += 1
    print('哈哈1---num=%d' % num)
else:
    time.sleep(1)
    num += 1
    print('哈哈2---num=%d' % num)

# 进程中，每个进程中所有数据（包括全局变量）都各有拥有一份，互不影响