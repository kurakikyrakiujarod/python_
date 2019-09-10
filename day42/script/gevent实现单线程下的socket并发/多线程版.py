import socket
import threading
from threading import Thread


def client(server_ip, server_port):
    c = socket.socket()
    # 套接字对象一定要加到函数内，即局部名称空间内，
    # 放在函数外则被所有线程共享，则大家公用一个套接字对象，
    # 那么客户端端口永远一样了
    c.connect((server_ip, server_port))
    count = 0
    while True:
        c.send(('%s say hello %s' % (threading.current_thread().getName(), count)).encode('utf-8'))
        msg = c.recv(1024)
        print(msg.decode('utf-8'))
        count += 1


if __name__ == '__main__':
    for i in range(500):
        t = Thread(target=client, args=('127.0.0.1', 9999))
        t.start()
