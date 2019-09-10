from socket import *
import select

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 8081))
s.listen(5)
s.setblocking(False)  # 设置socket的接口为非阻塞
read_l = [s, ]       # 将监听套接字放到列表中

while True:
    r_l, w_l, x_l = select.select(read_l, [], [])
    print(r_l)
    for ready_obj in r_l:
        if ready_obj == s:    # 有客户端到来
            conn, addr = ready_obj.accept()  # 此时的ready_obj等于s
            read_l.append(conn)   # 添加新套接字到监视列表
        else:      # 否则 是有客户端发送数据
            try:
                data = ready_obj.recv(1024)  # 此时的ready_obj等于conn
                if not data:   # 空数据意味着客户端断开连接
                    ready_obj.close()
                    read_l.remove(ready_obj)
                    continue
                ready_obj.send(data.upper())
            except ConnectionResetError:
                ready_obj.close()
                read_l.remove(ready_obj)
