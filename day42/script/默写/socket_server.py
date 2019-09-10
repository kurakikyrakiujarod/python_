from gevent import monkey;monkey.patch_all()
import socket
import gevent


def async_talk(conn):
    try:
        while True:
            conn.send(b'hello')
            ret = conn.recv(1024)
            print(ret)
    finally:
        conn.close()


sk = socket.socket()
sk.bind(('127.0.0.1', 9999))
sk.listen()
while True:
    con, adr = sk.accept()
    gevent.spawn(async_talk, con)
sk.close()
