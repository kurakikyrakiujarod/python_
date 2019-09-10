import os
import socket
import hashlib

secret_key = '菜菜菜子'
sk = socket.socket()
ip_port = ('127.0.0.1', 9999)
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk.bind(ip_port)
sk.listen()

while True:
    try:
        conn, address = sk.accept()
        random_bytes = os.urandom(32)  # 随机产生32个字节的字符串,返回bytes
        conn.send(random_bytes)
        md5_obj = hashlib.md5(secret_key.encode('utf-8'))  # 使用secret_key作为加密盐
        md5_obj.update(random_bytes)
        ret = md5_obj.hexdigest()
        msg = conn.recv(1024).decode('utf-8')
        if msg == ret:
            print('是合法的客户端')  # 如果接收的摘要和本机计算的摘要一致，就说明是合法的
        else:
            conn.close()
    finally:
        sk.close()
        break
