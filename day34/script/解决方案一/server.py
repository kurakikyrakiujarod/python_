# _*_coding:utf-8_*_
from socket import *

ip_port = ('127.0.0.1', 8080)

tcp_socket_server = socket()
tcp_socket_server.bind(ip_port)
tcp_socket_server.listen(5)

conn, addr = tcp_socket_server.accept()
lenth = conn.recv(1)  # 接收1个字节，返回 b'5'
# print(lenth)
lenth = int(lenth.decode('utf-8'))  # 转化字符串,返回5

data1 = conn.recv(lenth)  # 接收5字节，返回 b'hello'
lenth2 = conn.recv(1)  # 接收1个字节
lenth2 = int(lenth2.decode('utf-8'))  # 转化字符串,返回3
data2 = conn.recv(lenth2)  # 接收3个字节,返回b'egg'

print('----->', data1.decode('utf-8'))
print('----->', data2.decode('utf-8'))

conn.close()
tcp_socket_server.close()
