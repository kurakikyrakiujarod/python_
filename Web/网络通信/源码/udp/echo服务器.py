from socket import *

# 1创建套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)
# 2绑定本地信息，不使用随机分配的端口
bindAddr = ("", 7088)
udpSocket.bind(bindAddr)  # 绑定
num = 0
while True:
    # 接收对方发送的数据
    recvData = udpSocket.recvfrom(1024)
    print(recvData[0].decode('gb2312'), recvData[1])
    # 将接收到的数据回发给对方
    udpSocket.sendto(recvData[0], recvData[1])
    num += 1
    print("已将接收到的第%d个数据返回给对方，" % num)
udpSocket.close()
