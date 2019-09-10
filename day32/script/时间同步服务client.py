# 时间同步服务客户端
import socket
import time
import os

sk = socket.socket(type=socket.SOCK_DGRAM)

while True:
    sk.sendto('%Y/%m/%d %H:%M:%S'.encode('utf-8'), ('127.0.0.1', 9999))
    rec_time_string, server_address = sk.recvfrom(1024)
    rec_time_string = rec_time_string.decode('utf-8')
    print(rec_time_string)
    time.sleep(1)
    os.system('cls')
sk.close()