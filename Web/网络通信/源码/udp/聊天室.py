from socket import *
import time

# 1创建套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)
bindAddr = ("", 7088)
udpSocket.bind(bindAddr)  # 绑定
while True:
    # 接收对方发送的数据
    recvData = udpSocket.recvfrom(1024)
    print('【%s】 %s.%s' % (time.ctime(), recvData[1], recvData[0].decode("GB2312")))
    a = input("请输入：")
    udpSocket.sendto(a.encode('GB2312'), recvData[1])
# 5关闭套接字
udpSocket.close()
