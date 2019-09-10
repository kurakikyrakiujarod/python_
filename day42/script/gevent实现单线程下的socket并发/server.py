from gevent import monkey;monkey.patch_all()
import socket
import gevent


def server(server_ip, server_port):
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((server_ip, server_port))
    s.listen()
    while True:
        con, adr = s.accept()
        gevent.spawn(talk, con, adr)


def talk(con, adr):
    try:
        while True:
            res = con.recv(1024)
            print('client {}:{} \nmsg:{}'.format(adr[0], adr[1], res.decode('utf-8')))
            con.send(res.upper())
    except Exception as e:
        print(e)
    finally:
        con.close()


if __name__ == '__main__':
    server('127.0.0.1', 9999)
