from threading import Thread
import socket


def client():
    sk = socket.socket()
    sk.connect(('127.0.0.1',9999))
    while True:
        print(sk.recv(1024).decode('utf-8'))
        sk.send(b'bye')
    sk.close()


for i in range(500):
    Thread(target=client).start()