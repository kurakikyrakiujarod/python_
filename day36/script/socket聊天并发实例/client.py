import socket

sk = socket.socket()
ip_port = ('127.0.0.1', 9999)
sk.connect(ip_port)

while True:
    inp = input('>>>').strip()
    if not inp:continue
    sk.send(inp.encode('utf-8'))
    data = sk.recv(1024)
    print(data.decode('utf-8'))

sk.close()
