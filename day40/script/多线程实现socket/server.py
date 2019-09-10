import socket
from threading import Thread


def talk(con):
    while True:
        rec_msg = con.recv(1024)
        if not rec_msg: break
        print(rec_msg.decode('utf-8'))
        con.send(rec_msg.upper())


if __name__ == '__main__':
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    HOST, PORT = '127.0.0.1', 9999
    server.bind((HOST, PORT))
    server.listen()
    while True:
        con, adr = server.accept()
        Thread(target=talk, args=(con,)).start()
