import os
from multiprocessing import Process


def func(exp):
    print(os.getpid(), os.getppid())
    result = eval(exp)
    with open('file', mode='w') as f:
        f.write(str(result))


if __name__ == '__main__':
    print(os.getpid(), os.getppid())
    p = Process(target=func, args=('3*6-1',))
    p.start()
    ret = 5 / 2
    p.join()
    with open('file') as f:
        result = f.read()
    ret += int(result)
    print(ret)

# 12984 6872
# 11600 12984
# 19.5
