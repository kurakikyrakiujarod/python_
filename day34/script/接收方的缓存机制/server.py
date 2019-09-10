from socket import *

ip_port = ('127.0.0.1', 8080)

tcp_socket_server = socket(AF_INET, SOCK_STREAM)
tcp_socket_server.bind(ip_port)
tcp_socket_server.listen(5)

conn, addr = tcp_socket_server.accept()

data1 = conn.recv(2)  # 一次没有收完整
data2 = conn.recv(10)  # 下次收的时候,会先取旧的数据,然后取新的

print('----->', data1.decode('utf-8'))
print('----->', data2.decode('utf-8'))

conn.close()
