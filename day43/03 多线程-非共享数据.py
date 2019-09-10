# import threading
# import time
#
#
# class MyThread(threading.Thread):
#     # 重写 构造方法
#     def __init__(self, num, sleepTime):
#         threading.Thread.__init__(self)
#         self.num = num
#         self.sleepTime = sleepTime
#
#     def run(self):
#         self.num += 1
#         time.sleep(self.sleepTime)
#         print('线程(%s),num=%d' % (self.name, self.num))
#
#
# if __name__ == '__main__':
#     mutex = threading.Lock()
#     t1 = MyThread(100, 5)
#     t1.start()
#     t2 = MyThread(200, 1)
#     t2.start()

# 执行输出
# 线程(Thread-2),num=201
# 线程(Thread-1),num=101

# import threading
# from time import sleep
#
#
# def test(sleepTime):
#     num = 1
#     sleep(sleepTime)
#     num += 1
#     print('---(%s)--num=%d' % (threading.current_thread(), num))
#
#
# t1 = threading.Thread(target=test, args=(5,))
# t2 = threading.Thread(target=test, args=(1,))
#
# t1.start()
# t2.start()
# 执行输出
# ---(<Thread(Thread-2, started 3388)>)--num=2
# ---(<Thread(Thread-1, started 4004)>)--num=2

# 在多线程开发中，全局变量是多个线程都共享的数据，而局部变量等是各自线程的，是非共享的

