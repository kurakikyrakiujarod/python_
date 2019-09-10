# 同步调用就是你 喊 你朋友吃饭 ，你朋友在忙 ，你就一直在那等，等你朋友忙完了 ，你们一起去
# 异步调用就是你 喊 你朋友吃饭 ，你朋友说知道了 ，待会忙完去找你 ，你就去做别的了
from multiprocessing import Pool
import time
import os


def test():
    print("---进程池中的进程---pid=%d,ppid=%d--" % (os.getpid(), os.getppid()))
    for i in range(3):
        print("----%d---" % i)
        time.sleep(1)
    return "hahah"


def test2(args):
    print("---callback func--pid=%d" % os.getpid())
    print("---callback func--args=%s" % args)


if __name__ == '__main__':
    pool = Pool(3)
    pool.apply_async(func=test, callback=test2)

    time.sleep(5)

    print("----主进程-pid=%d----" % os.getpid())

# 执行输出
# ---进程池中的进程---pid=12364,ppid=3656--
# ----0---
# ----1---
# ----2---
# ---callback func--pid=3656
# ---callback func--args=hahah
# ----主进程-pid=3656----
