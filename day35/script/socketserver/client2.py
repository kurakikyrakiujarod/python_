import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 9987))
print(sk.recv(1024))
inp = input('>>>').encode('utf-8')
sk.send(inp)
sk.close()
