import socket
import subprocess

ip_port = ('127.0.0.1', 9000)
udp_server = socket.socket(type=socket.SOCK_DGRAM)
udp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
udp_server.bind(ip_port)

while True:
    cli_msg, cli_adr = udp_server.recvfrom(1024)
    cmd = cli_msg.decode('utf-8')
    print('用户命令----->', cmd)

    ret = subprocess.Popen(cmd, shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    stdout = ret.stdout.read()
    stderr = ret.stderr.read()

    udp_server.sendto(stdout, cli_adr)
    udp_server.sendto(stderr, cli_adr)

udp_server.close()
