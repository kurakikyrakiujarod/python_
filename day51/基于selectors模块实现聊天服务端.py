from socket import *
import selectors


def accept(server_fileobj, mask):
    conn, addr = server_fileobj.accept()
    sel.register(conn, selectors.EVENT_READ, read)


def read(conn, mask):
    try:
        data = conn.recv(1024)
        if not data:
            print('closing', conn)
            sel.unregister(conn)
            conn.close()
            return
        conn.send(data.upper() + b'_SB')
    except Exception:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()


sel = selectors.DefaultSelector()
sk = socket(AF_INET, SOCK_STREAM)
sk.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sk.bind(('127.0.0.1', 8088))
sk.listen(5)
sk.setblocking(False)  # 设置socket的接口为非阻塞
sel.register(sk, selectors.EVENT_READ,
             accept)  # 相当于网select的读列表里append了一个sk对象,并且绑定了一个回调函数accept

while True:
    events = sel.select()  # 检测所有的fileobj，是否有完成wait data的
    for sel_obj, mask in events:
        callback = sel_obj.data  # 拿到回调函数
        callback(sel_obj.fileobj, mask)  # accpet(sk,1)/read(conn,)
