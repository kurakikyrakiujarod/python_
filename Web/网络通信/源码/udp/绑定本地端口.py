from socket import *

s = socket(AF_INET, SOCK_DGRAM)  # 创建套接字
s.bind(('', 8788))  # 绑定一个端口，ip地址和端⼝号
addr = ('192.168.189.1', 8080)  # 准备接收方地址
data = input("请输入：")
s.sendto(data.encode(), addr)
redata = s.recvfrom(1024)  # 1024表示本次接收的最⼤字节数
print(redata)
s.close()
