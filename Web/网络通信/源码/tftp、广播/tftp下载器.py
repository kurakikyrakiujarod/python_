import struct
from socket import *

filename = 'test1.jpg'
server_ip = '192.168.189.1'
send_data = struct.pack('!H%dsb5sb' % len(filename), 1, filename.encode(), 0, 'octet'.encode(), 0)
s = socket(AF_INET, SOCK_DGRAM)
s.sendto(send_data, (server_ip, 69))  # 第一次发送, 连接服务器69端口
f = open(filename, 'ab')  # a:以追加模式打开（必要时可以创建）append;b:表示二进制
while True:
    recv_data = s.recvfrom(1024)  # 接收数据
    caozuoma, ack_num = struct.unpack('!HH', recv_data[0][:4])  # 获取数据块编号
    rand_port = recv_data[1][1]  # 获取服务器的随机端口

    if int(caozuoma) == 5:
        print('文件不存在...')
        break
    print("操作码：%d,ACK：%d,服务器随机端口：%d,数据长度：%d" % (caozuoma, ack_num, rand_port, len(recv_data[0])))
    f.write(recv_data[0][4:])  # 将数据写入
    if len(recv_data[0]) < 516:
        break
    ack_data = struct.pack("!HH", 4, ack_num)
    s.sendto(ack_data, (server_ip, rand_port))  # 回复ACK确认包
