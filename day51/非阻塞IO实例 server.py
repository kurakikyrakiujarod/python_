from socket import *
import time

s = socket(AF_INET, SOCK_STREAM)
s.bind(('127.0.0.1', 8080))
s.listen(5)
s.setblocking(False)  # 设置socket的接口为非阻塞
conn_l = []
del_l = []

while True:
    try:
        conn, addr = s.accept()
        conn_l.append(conn)
    except BlockingIOError:
        # print(conn_l)
        for conn in conn_l:
            try:
                data = conn.recv(1024)
                if not data:
                    del_l.append(conn)
                    continue
                conn.send(data.upper())
            except BlockingIOError:
                pass
            except ConnectionResetError:
                del_l.append(conn)

        for conn in del_l:
            conn_l.remove(conn)
            conn.close()
        del_l = []


# 将套接字设置为非堵塞状态
# while True 死循环
# try 语句执行以下逻辑 监听套接字接受客户端连接，并把新套接字添加到conn_l列表中
# except 捕获到异常 即 没有客户端的连接 执行两个for循环
# 第一个for循环收发数据 并把要关闭的套接字添加到del_l列表中
# 最后一个for循环，关闭套接字并从conn_l列表中移除和清空del_l列表