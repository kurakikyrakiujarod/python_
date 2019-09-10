import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()

conn, adr = sk.accept()

while True:
    cmd = input('>>>').strip()
    conn.send(cmd.encode('utf-8'))  # 先把cmd发送过去 不可直接break
    if cmd == 'q': break
    ret1 = conn.recv(1024)
    print(ret1.decode('gbk'))
    ret2 = conn.recv(1024)
    print(ret2.decode('gbk'))
conn.close()
sk.close()
