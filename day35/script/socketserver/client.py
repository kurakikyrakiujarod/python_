import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 9999))
sk.close()
