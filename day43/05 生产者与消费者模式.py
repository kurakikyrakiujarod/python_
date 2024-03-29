# 队列 先进先出
# 栈 先进后出
# Python的Queue模块中提供了同步的、线程安全的队列类
# 包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列PriorityQueue
# 这些队列都实现了锁原语（可以理解为原子操作，即要么不做，要么就做完），能够在多线程中直接使用
# 可以使用队列来实现线程间的同步
# 用FIFO队列实现上述生产者与消费者问题的代码如下
import threading
import time

# python2中
# from Queue import Queue


# python3中
from queue import Queue


class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize() < 1000:
                for i in range(100):
                    count = count + 1
                    msg = '生成产品' + str(count)
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(3):
                    msg = self.name + '消费了 ' + queue.get()
                    print(msg)
            time.sleep(1)


if __name__ == '__main__':
    queue = Queue()

    for i in range(500):
        queue.put('初始产品' + str(i))
    for i in range(2):
        p = Producer()
        p.start()
    for i in range(5):
        xxx = Consumer()
        xxx.start()

# 3. Queue的说明
# 对于Queue，在多线程通信之间扮演重要的角色
# 添加数据到队列中，使用put()方法
# 从队列中取数据，使用get()方法

# 4. 生产者消费者模式的说明
# 为什么要使用生产者和消费者模式
# 在线程世界里，生产者就是生产数据的线程，消费者就是消费数据的线程。
# 在多线程开发当中，如果生产者处理速度很快，而消费者处理速度很慢，那么生产者就必须等待消费者处理完，才能继续生产数据。
# 同样的道理，如果消费者的处理能力大于生产者，那么消费者就必须等待生产者。
# 为了解决这个问题于是引入了生产者和消费者模式。

# 什么是生产者消费者模式
# 生产者消费者模式是通过一个容器来解决生产者和消费者的强耦合问题
# 生产者和消费者彼此之间不直接通讯，而通过阻塞队列来进行通讯
# 所以生产者生产完数据之后不用等待消费者处理，直接扔给阻塞队列
# 消费者不找生产者要数据，而是直接从阻塞队列里取
# 阻塞队列就相当于一个缓冲区，平衡了生产者和消费者的处理能力

# 这个阻塞队列就是用来给生产者和消费者解耦的。
# 纵观大多数设计模式，都会找一个第三者出来进行解耦，