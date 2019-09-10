import socket

udp_client = socket.socket(type=socket.SOCK_DGRAM)
ip_port = ('127.0.0.1', 9000)

while True:
    cmd = input('>>>').strip()
    udp_client.sendto(cmd.encode('utf-8'), ip_port)
    out, server_adr = udp_client.recvfrom(1024)
    err, server_adr = udp_client.recvfrom(1024)
    if err:
        print('error : %s' % err.decode('gbk'), end='')
    if out:
        print(out.decode('gbk'), end='')
