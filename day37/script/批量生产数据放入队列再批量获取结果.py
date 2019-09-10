import os
import time
from multiprocessing import Queue, Process


# 输入
def inp_que(q):
    info = str(os.getpid())+'(put):'+time.asctime()
    q.put(info)
    print(info)


# 获取消息
def get_que(q):
    info = q.get()
    print('\033[32m{}(get):{}\033[0m'.format(os.getpid(), info))


if __name__ == '__main__':
    q = Queue(3)
    inp_list = []  # store input processes
    get_list = []  # store output processes

    # 输入进程
    for i in range(10):
        p = Process(target=inp_que, args=(q,))
        inp_list.append(p)
        p.start()

    # 输出进程
    for i in range(10):
        p = Process(target=get_que, args=(q,))
        get_list.append(p)
        p.start()

    for p in inp_list:
        p.join()
    for p in get_list:
        p.join()

# 11908(put):Fri Jan 25 13:26:42 2019
# 3264(get):11908(put):Fri Jan 25 13:26:42 2019
# 10448(put):Fri Jan 25 13:26:42 2019
# 11736(get):10448(put):Fri Jan 25 13:26:42 2019
# 2464(put):Fri Jan 25 13:26:42 2019
# 12220(get):2464(put):Fri Jan 25 13:26:42 2019
# 9360(put):Fri Jan 25 13:26:42 2019
# 4516(get):9360(put):Fri Jan 25 13:26:42 2019
# 11120(put):Fri Jan 25 13:26:42 2019
# 11592(get):11120(put):Fri Jan 25 13:26:42 2019
# 9876(put):Fri Jan 25 13:26:42 2019
# 9640(get):9876(put):Fri Jan 25 13:26:42 2019
# 3696(put):Fri Jan 25 13:26:42 2019
# 11036(get):3696(put):Fri Jan 25 13:26:42 2019
# 2584(put):Fri Jan 25 13:26:42 2019
# 11836(get):2584(put):Fri Jan 25 13:26:42 2019
# 3908(put):Fri Jan 25 13:26:42 2019
# 11912(get):3908(put):Fri Jan 25 13:26:42 2019
# 12076(put):Fri Jan 25 13:26:43 2019
# 6548(get):12076(put):Fri Jan 25 13:26:43 2019
