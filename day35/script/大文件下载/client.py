import json
import struct
import socket

# 创建套接字连接服务端
ip_port = ('127.0.0.1', 9999)
sk = socket.socket()
sk.connect(ip_port)

# 先接收4个字节
len_dic = sk.recv(4)
# 反struct返回字典的长度
len_dic = struct.unpack('i', len_dic)[0]
# 按指定长度收数据
dic = sk.recv(len_dic)
# 解码和反序列化返回字典
dic = dic.decode('utf-8')
dic = json.loads(dic)
# print(dic)

# 创建文件，读数据写数据
with open(dic['file_name'], mode='wb') as f:
    while dic['file_size']:
        data = sk.recv(4096)
        dic['file_size'] -= len(data)
        f.write(data)
sk.close()
