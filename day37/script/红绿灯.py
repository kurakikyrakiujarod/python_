import time
import random
from multiprocessing import Process, Event


def traffic_light(e):
    count = 0
    while count < 6:
        print('\033[1;31m红灯亮\033[0m')
        time.sleep(2)
        if not e.is_set(): e.set()
        print('\033[1;32m绿灯亮\033[0m')
        time.sleep(2)
        if e.is_set(): e.clear()
        count += 1


def car(i, e):
    if not e.is_set():
        print('car%s正在等待' % i)
    e.wait()
    print('car%s通过路口' % i)


if __name__ == '__main__':
    e = Event()
    Process(target=traffic_light, args=(e,)).start()
    for i in range(1, 6):
        time.sleep(random.randint(1, 3))
        Process(target=car, args=(i, e)).start()

# 执行输出
# 红灯亮
# car1正在等待
# 绿灯亮
# car1通过路口
# car2通过路口
# 红灯亮
# 绿灯亮
# car3通过路口
# 红灯亮
# car4正在等待
# 绿灯亮
# car4通过路口
# car5通过路口
# 红灯亮
# 绿灯亮
# 红灯亮
# 绿灯亮
# 红灯亮
# 绿灯亮
