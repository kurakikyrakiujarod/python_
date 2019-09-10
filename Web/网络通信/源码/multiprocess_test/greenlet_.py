from greenlet import greenlet
import time


def t1():
    while True:
        print("........a........")
        gr2.switch()
        time.sleep(1)


def t2():
    while True:
        print("........b........")
        gr1.switch()  # 调到上次执行的地方继续执行
        time.sleep(1)


gr1 = greenlet(t1)  # 创建一个greenlet对象
gr2 = greenlet(t2)
gr1.switch()  # 此时会执行1函数
