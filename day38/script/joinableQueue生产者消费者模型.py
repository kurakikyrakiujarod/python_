import time
import random
from multiprocessing import Process, JoinableQueue


def producer(name, food, q):
    for i in range(1, 11):
        time.sleep(random.random())
        print('\033[1;31m{}生产{}{}\033[0m'.format(name, food, i))
        q.put('{}{}{}'.format(name, food, i))
    q.join()


def consumer(name, q):
    while True:
        get_info = q.get()
        time.sleep(random.random())
        print('\033[1;32m{}消费{}\033[0m'.format(name, get_info))
        q.task_done()


if __name__ == '__main__':
    q = JoinableQueue()
    p1 = Process(target=producer, args=('alex', 'jiaozi', q))
    p2 = Process(target=producer, args=('egon', 'bread', q))
    p1.start()
    p2.start()
    c1 = Process(target=consumer, args=('aoa', q))
    c2 = Process(target=consumer, args=('kuraki', q))
    c1.daemon = True
    c2.daemon = True
    c1.start()
    c2.start()
    p1.join()
    p2.join()
# alex生产jiaozi1
# egon生产bread1
# aoa消费egonbread1
# alex生产jiaozi2
# kuraki消费alexjiaozi1
# aoa消费alexjiaozi2
# egon生产bread2
# kuraki消费egonbread2
# alex生产jiaozi3
# egon生产bread3
# egon生产bread4
# alex生产jiaozi4
# alex生产jiaozi5
# egon生产bread5
# aoa消费alexjiaozi3
# kuraki消费egonbread3
# kuraki消费alexjiaozi4
# alex生产jiaozi6
# egon生产bread6
# alex生产jiaozi7
# aoa消费egonbread4
# kuraki消费alexjiaozi5
# egon生产bread7
# kuraki消费alexjiaozi6
# alex生产jiaozi8
# kuraki消费egonbread6
# egon生产bread8
# aoa消费egonbread5
# alex生产jiaozi9
# egon生产bread9
# alex生产jiaozi10
# kuraki消费alexjiaozi7
# aoa消费egonbread7
# kuraki消费alexjiaozi8
# egon生产bread10
# kuraki消费alexjiaozi9
# aoa消费egonbread8
# kuraki消费egonbread9
# aoa消费alexjiaozi10
# kuraki消费egonbread10
