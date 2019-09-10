from socket import *

s = socket(AF_INET, SOCK_DGRAM)  # 创建套接字
addr = ('192.168.189.1', 8080)  # 准备接收方地址
data = input("请输入：")
s.sendto(data.encode('gb2312'), addr)
# 等待接收数据
redata = s.recvfrom(1024)
# 1024表示本次接收的最大字节数
print(redata[0].decode('gb2312'), redata[1])
s.close()
