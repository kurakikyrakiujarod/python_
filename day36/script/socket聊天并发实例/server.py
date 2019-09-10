import socket
from multiprocessing import Process


def com(con, cl_adr):
    while True:
        try:
            msg = con.recv(1024).decode('utf-8')
            print(msg)
            # print(client_adr)
            if not msg: break
            con.send(msg.upper().encode('utf-8'))
        except Exception as e:
            print(e)
            break


if __name__ == '__main__':
    sk = socket.socket()
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sk.bind(('127.0.0.1', 9999))
    sk.listen()
    while True:
        conn, client_adr = sk.accept()
        Process(target=com, args=(conn, client_adr)).start()
