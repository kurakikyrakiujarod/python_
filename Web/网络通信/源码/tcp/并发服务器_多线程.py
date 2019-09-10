from socket import *
from threading import Thread


def dealWithClient(newSocket, destAddr):
    print('与{}建立链接'.format(destAddr))
    while True:
        recvData = newSocket.recv(1024)
        if len(recvData) > 0:
            print(destAddr, recvData.decode('gb2312'))
        else:
            print("客户端{}关闭".format(destAddr))
            newSocket.close()
            break


def main():
    serSocket = socket(AF_INET, SOCK_STREAM)
    serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    localAddr = ("", 7788)
    serSocket.bind(localAddr)
    serSocket.listen(5)
    try:
        while True:
            print("主进程等待连接")
            newSocket, destAddr = serSocket.accept()
            client = Thread(target=dealWithClient, args=(newSocket, destAddr))
            client.start()
    finally:
        serSocket.close()


if __name__ == "__main__":
    main()
