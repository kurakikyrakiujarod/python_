from socket import *

serSocket = socket(AF_INET, SOCK_STREAM)
localAddr = ('', 7788)
serSocket.bind(localAddr)
serSocket.listen(5)
while True:
    print("主进程等待新客户端")
    newSocket, destAddr = serSocket.accept()
    print("主进程接下来负责处理", str(destAddr))
    try:
        while True:
            recvData = newSocket.recv(1024)
            if len(recvData) > 0:  # 如果收到的客户端数据长度为0，代表客户端已经调用close下线
                print("接收到", recvData.decode('gb2312'))
            else:
                print("%s-客户端已关闭" % str(destAddr))
                break
    finally:
        newSocket.close()
serSocket.close()
