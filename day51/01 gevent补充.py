# 小问题
import gevent


def func():
    print('eating')


# 协程任务开启
# gevent.spawn(func)
# 执行程序，没有输出结果

# 加上join
import gevent


def func():
    print('eating')


# g = gevent.spawn(func)
# g.join()  # 阻塞,等待协程执行完毕
# 执行输出
# eating


# 加上睡眠
import time
import gevent


def func():
    print('eating')


# g = gevent.spawn(func)
# time.sleep(1)
# 执行程序，没有输出结果


# 使用gevent.sleep()
import gevent


def func():
    print('eating')


# g = gevent.spawn(func)
# gevent.sleep(1)
# 执行输出
# eating


# 导入monkey模块，再使用内置的time.sleep()
from gevent import monkey;

monkey.patch_all()
import time
import gevent


def func():
    print('eating')


# g = gevent.spawn(func)
# time.sleep(1)
# 执行输出
# eating


# 修改为sleep(0)
from gevent import monkey;

monkey.patch_all()
import time
import gevent


def func():
    print('eating')


# g = gevent.spawn(func)
# time.sleep(0)
# 执行输出
# eating

# time.sleep(0) 虽然时间为0，它也是阻塞，gevent检测到了IO

# 总结：

# 协程任务开启，不会立即执行，它需要IO才能执行


from gevent import monkey;

monkey.patch_all()
import time
import gevent


def func():
    print('eating1')  # 执行
    time.sleep(0.1)  # 遇到IO
    print('eating2')
    time.sleep(0.1)
    print('eating3')
    time.sleep(0.1)


# g = gevent.spawn(func)  # 协程任务开启
# time.sleep(0)  # 阻塞遇到IO
# 执行输出
# eating1

from gevent import monkey;

monkey.patch_all()
import time
import gevent


def func():
    print('eating1')  # 执行
    time.sleep(0.1)  # 遇到IO
    print('eating2')
    time.sleep(0.1)
    print('eating3')
    time.sleep(0.1)


# g = gevent.spawn(func)  # 协程任务开启
# g.join()  # 等待协程结束

# 执行输出
# eating1
# eating2
# eating3

# 总结：
# 内部执行switch时，必须保证协程不结束之前，主线程不结束