# 加锁解决管道数据的不安全
import time
import random
from multiprocessing import Process, Pipe, Lock


def producer(con, pro, n, name, food):
    con.close()
    for i in range(1, n + 1):
        time.sleep(random.random())
        f = '{}{}'.format(food, i)
        print('\033[1;31m%s生产了%s\033[0m' % (name, f))
        pro.send(f)
    pro.send(None)
    pro.send(None)
    pro.close()


def consumer(con, pro, name, lo):
    pro.close()
    while True:
        lo.acquire()
        f = con.recv()
        lo.release()
        if f:
            time.sleep(random.random())
            print('\033[1;32m%s消费了%s\033[0m' % (name, f))
        else:
            con.close()
            break


if __name__ == '__main__':
    con, pro = Pipe()
    lo = Lock()
    c1 = Process(target=consumer, args=(con, pro, 'c1', lo))
    c2 = Process(target=consumer, args=(con, pro, 'c2', lo))
    p1 = Process(target=producer, args=(con, pro, 30, 'p1', '泔水'))
    c2.start()
    c1.start()
    p1.start()

    con.close()
    pro.close()

    c2.join()
    c1.join()
    p1.join()
