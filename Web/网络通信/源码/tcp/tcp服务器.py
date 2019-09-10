from socket import *

tcpSerSocket = socket(AF_INET, SOCK_STREAM)
address = ("", 7788)
tcpSerSocket.bind(address)
tcpSerSocket.listen(5)  # 设置最大连接数
newSocket, clientAddr = tcpSerSocket.accept()
# 如果有新的客户端来链接服务器， 那么就产⽣⼀个新的套接字
#  newSocket⽤来为这个客户端服务（10086小妹）
#  tcpSerSocket就可以省下来等待其他新客户端的链接 
#  接收对⽅发送过来的数据， 最⼤接收1024个字节
recvData = newSocket.recv(1024)
print(recvData)
newSocket.send(b"thank you!")
newSocket.close()
tcpSerSocket.close()
