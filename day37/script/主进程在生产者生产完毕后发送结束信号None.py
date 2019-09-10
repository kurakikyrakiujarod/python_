import time
import random
import os
from multiprocessing import Queue, Process


def consumer(q):
    while True:
        bao_zi = q.get()
        if bao_zi is None: break
        time.sleep(random.random())
        print('\033[1;32m{}消费了{}\033[0m'.format(os.getpid(), bao_zi))


def producer(q):
    for i in range(1, 11):
        time.sleep(random.random())
        bao_zi = '{}{}'.format('包子', i)
        q.put(bao_zi)
        print('\033[1;31m{}生产了{}'.format(os.getpid(), bao_zi))


if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=producer, args=(q,))
    c1 = Process(target=consumer, args=(q,))
    c2 = Process(target=consumer, args=(q,))
    p1.start()
    p2.start()
    c1.start()
    c2.start()

    # 等待两个生产者全部生产完毕
    p1.join()
    p2.join()
    # 发送结束信号 队列最后
    # 有几个消费者就应该发送几次结束信号None
    q.put(None)
    q.put(None)

# 执行输出
# 10200生产了包子1
# 9280生产了包子1
# 2476消费了包子1
# 4820消费了包子1
# 9280生产了包子2
# 9280生产了包子3
# 10200生产了包子2
# 10200生产了包子3
# 9280生产了包子4
# 4820消费了包子3
# 10200生产了包子4
# 2476消费了包子2
# 10200生产了包子5
# 9280生产了包子5
# 2476消费了包子3
# 4820消费了包子2
# 2476消费了包子4
# 2476消费了包子5
# 9280生产了包子6
# 10200生产了包子6
# 10200生产了包子7
# 9280生产了包子7
# 2476消费了包子5
# 4820消费了包子4
# 2476消费了包子6
# 10200生产了包子8
# 4820消费了包子6
# 9280生产了包子8
# 10200生产了包子9
# 9280生产了包子9
# 10200生产了包子10
# 4820消费了包子7
# 4820消费了包子8
# 9280生产了包子10
# 2476消费了包子7
# 2476消费了包子9
# 4820消费了包子8
# 4820消费了包子10
# 2476消费了包子9
# 4820消费了包子10
