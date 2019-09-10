import socket

BUFSIZE = 1024
ip_port = ('127.0.0.1', 8080)

s = socket.socket()
res = s.connect(ip_port)  # 功能与connect(address)相同，但是成功返回0，失败返回errno的值
lenth = str(len('hello')).encode('utf-8')  # 获取hello的字符的长度,并转化为str,最后编码
s.send(lenth)  # 发送数字5
s.send('hello'.encode('utf-8'))  # 发送hello
lenth = str(len('egg')).encode('utf-8')  # 获取长度，结果为3
s.send(lenth)  # 发送3
s.send('egg'.encode('utf-8'))  # 发送egg

s.close()
