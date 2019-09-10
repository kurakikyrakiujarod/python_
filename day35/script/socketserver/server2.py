import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.request)
        self.request.send(b'hello')  # 跟所有的client打招呼
        print(self.request.recv(1024))  # 接收客户端的信息


server = socketserver.ThreadingTCPServer(('127.0.0.1', 9987), MyServer)
server.serve_forever()
