from socket import *

s = socket(AF_INET, SOCK_DGRAM)  # 创建套接字
addr = ('192.168.189.1', 8080)  # 准备接收方地址
data = input("请输入：")
s.sendto(data.encode('gb2312'), addr)
# 发送数据时，python3需要将字符串转成byte
# encode('utf-8')# 用utf-8对数据进行编码，获得bytes类型对象
# decode（）反过来
s.close()
