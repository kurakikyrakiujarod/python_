import gevent


def A():
    while True:
        print(".........A.........")
        gevent.sleep(1)  # 用来模拟一个耗时操作
        # gevent中：当一个协程遇到耗时操作会自动交出控制权给其他协程


def B():
    while True:
        print(".........B.........")
        gevent.sleep(1)  # 每当遇到耗时操作，会自用转到其他协程


g1 = gevent.spawn(A)  # 创建一个gevent对象（创建了一个协程），此时就已经开始执行A
g2 = gevent.spawn(B)
g1.join()  # 等待协程执行结束
g2.join()  # 会等待协程运行结束后再退出
