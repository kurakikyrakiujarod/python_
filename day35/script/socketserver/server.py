import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.request)


server = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), MyServer)
server.serve_forever()

#  执行输出
# <socket.socket fd=488, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 9000), raddr=('127.0.0.1', 59419)>
# <socket.socket fd=504, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 9000), raddr=('127.0.0.1', 59434)>
