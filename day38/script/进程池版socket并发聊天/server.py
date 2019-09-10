from socket import *
from multiprocessing import Pool
import os


def talk(conn):
    print('进程pid: %s' % os.getpid())
    while True:
        try:
            msg = conn.recv(1024)
            if not msg: break
            conn.send(msg.upper())
        except Exception as e:
            print(e)
            break


if __name__ == '__main__':
    server = socket(AF_INET, SOCK_STREAM)
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.bind(('127.0.0.1', 8080))
    server.listen(5)
    p = Pool(4)
    while True:
        conn, adr = server.accept()
        p.apply_async(talk, args=(conn,))
