from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)

serAddr = ('192.168.189.1', 7788)
# 链接服务器
clientSocket.connect(serAddr)

clientSocket.send(b"hello")
recvData = clientSocket.recv(1024)
print("接收到的数据为：", recvData)
clientSocket.close()
