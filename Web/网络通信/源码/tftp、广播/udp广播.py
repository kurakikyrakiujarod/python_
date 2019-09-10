import socket

dest = ('<broadcast>', 7788)  # <broadcast>自动识别当前网络的广播地址
# 创建udp套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 对这个需要发送广播数据的套接字进行修改设置，否则不能发送广播数据
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # 允许s发送广播数据
# setsocketopt 设置套接字选项
# 以广播形式发送数据到本网络的所有电脑中
s.sendto(b'Hi', dest)
print("等待回复")
while True:
    (buf, address) = s.recvfrom(2048)
    print(address, buf.decode('GB2312'))
