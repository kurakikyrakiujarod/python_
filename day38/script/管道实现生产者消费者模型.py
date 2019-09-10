import time
import random
from multiprocessing import Process, Pipe


def producer(pipe1, pipe2, name, food):
    pipe1.close()
    for i in range(10):
        time.sleep(random.random())
        f = '{}{}{}'.format(name, food, i)
        print('\033[1;31m%s\033[0m' % f)
        pipe2.send(f)
    pipe2.close()


def consumer(pipe1, pipe2, name):
    pipe2.close()
    while True:
        try:
            f = pipe1.recv()
            print('\033[1;32m%s消费了%s\033[0m' % (name, f))
            time.sleep(random.random())
        except EOFError:
            pipe1.close()
            break


if __name__ == '__main__':
    pipe1, pipe2 = Pipe()
    p = Process(target=producer, args=(pipe1, pipe2, 'alex', '泔水'))
    xxx = Process(target=consumer, args=(pipe1, pipe2, 'egon'))
    p.start()
    xxx.start()
    pipe1.close()
    pipe2.close()
