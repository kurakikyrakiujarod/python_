import socket

sk = socket.socket()
HOST, PORT = "127.0.0.1", 9999
sk.connect((HOST, PORT))

while True:
    inp = input('>>>').strip().encode('utf-8')
    sk.send(inp)
    print(sk.recv(1024).decode('utf-8'))
sk.close()
