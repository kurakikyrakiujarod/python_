import time
import random
import os
from multiprocessing import Queue, Process


def consumer(q):
    while True:
        bao_zi = q.get()
        if bao_zi is None: break
        # if not bao_zi: break
        time.sleep(random.random())
        print('\033[1;32m{}消费了{}\033[0m'.format(os.getpid(), bao_zi))


def producer(q):
    for i in range(1, 11):
        time.sleep(random.random())
        bao_zi = '{}{}'.format('包子', i)
        q.put(bao_zi)
        print('\033[1;31m{}生产了{}'.format(os.getpid(), bao_zi))
    q.put(None)


if __name__ == '__main__':
    q = Queue()
    p = Process(target=producer, args=(q,))
    xxx = Process(target=consumer, args=(q,))
    p.start()
    xxx.start()

# 1172生产了包子1
# 1172生产了包子2
# 4720消费了包子1
# 1172生产了包子3
# 4720消费了包子2
# 4720消费了包子3
# 1172生产了包子4
# 1172生产了包子5
# 4720消费了包子4
# 1172生产了包子6
# 4720消费了包子5
# 1172生产了包子7
# 4720消费了包子6
# 1172生产了包子8
# 1172生产了包子9
# 4720消费了包子7
# 1172生产了包子10
# 4720消费了包子8
# 4720消费了包子9
# 4720消费了包子10
