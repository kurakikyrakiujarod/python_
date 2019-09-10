import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            # print(self.request)
            print(self.client_address[0])
            msg = self.request.recv(1024).decode('utf-8')
            print(msg)
            self.request.send(msg.upper().encode('utf-8'))


if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    server = socketserver.TCPServer(('127.0.0.1', 9999), MyServer)
    server.serve_forever()
