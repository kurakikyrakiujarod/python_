import os
import socket
import json
import struct

# 文件路径
file_path = r'D:\Program files\JiJiDown\Download\CROSSANGE 天使与龙的轮舞\天使与龙的轮舞05.mp4'

# 套接字 起服务端 接听 连接
sk = socket.socket()
ip_port = ('127.0.0.1', 9999)
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk.bind(ip_port)
sk.listen()
conn, adr = sk.accept()

# 文件相关信息 大小和文件名
file_name = os.path.basename(file_path)
file_size = os.path.getsize(file_path)
dic = {
    'file_name': file_name,
    'file_size': file_size
}
# 将字典序列化再编码 网络传输只能使用utf-8,gbk等
bytes_dic = json.dumps(dic).encode('utf-8')
# 字典大小
len_dic = struct.pack('i', len(bytes_dic))
# 先发字典的大小 再发字典
conn.send(len_dic)
conn.send(bytes_dic)

# 读文件发送内容
with open(file_path, mode='rb') as f:
    while file_size:
        data = f.read(4096)
        conn.send(data)
        file_size -= len(data)
conn.close()
sk.close()
