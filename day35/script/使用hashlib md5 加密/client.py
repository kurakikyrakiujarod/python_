import socket
import hashlib

secret_key = '菜菜菜子'
sk = socket.socket()
ip_port = ('127.0.0.1', 9999)
sk.connect(ip_port)

urandom = sk.recv(32)
md5_obj = hashlib.md5(secret_key.encode('utf-8'))
md5_obj.update(urandom)
sk.send(md5_obj.hexdigest().encode('utf-8'))
print('-' * 10)
sk.close()
