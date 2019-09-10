# 时间同步服务
import socket
import time

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 9999))

while True:
    time_string_format, client_address = sk.recvfrom(1024)
    time_string_format = time_string_format.decode('utf-8')
    sk.sendto(time.strftime(time_string_format).encode('utf-8'), client_address)
sk.close()