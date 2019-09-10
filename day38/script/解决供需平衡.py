import time
import random
from multiprocessing import Process, Queue


def producer(q, name, food):
    for i in range(5):
        time.sleep(random.random())  # 模拟生产时间
        print('\033[1;31m{}生产了{}{}\033[0m'.format(name, food, i))
        q.put('{}{}'.format(food, i))  # 放入队列


def consumer(q, name):
    while True:
        food = q.get()  # 获取队列
        if food == 'done': break  # 当获取的值为done时,结束循环
        time.sleep(random.random())  # 模拟吃的时间
        print('\033[1;32m{}吃了{}\033[0m'.format(name, food))


if __name__ == '__main__':
    q = Queue()  # 创建队列对象，如果不提供maxsize，则队列数无限制
    p1 = Process(target=producer, args=(q, '康师傅', '红烧牛肉'))
    p2 = Process(target=producer, args=(q, '郑师傅', '红烧鱼块'))
    p1.start()  # 启动进程
    p2.start()
    Process(target=consumer, args=(q, 'xiao')).start()
    Process(target=consumer, args=(q, 'lin')).start()
    p1.join()  # 保证子进程结束后再向下执行
    p2.join()
    q.put('done')  # 向队列添加一个值done
    q.put('done')
