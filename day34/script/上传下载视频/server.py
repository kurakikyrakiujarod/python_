"""
文件上传和下载 服务端
"""
# 导入模块
import socket
import struct
import os
import hashlib
import json

# 创建套接字
sk = socket.socket()
ip_port = ("127.0.0.1", 9999)
# 绑定套接字本地ip和端口
sk.bind(ip_port)
# 监听
sk.listen()
# 接受连接
conn, addr = sk.accept()
# 打印连接方信息
print(addr)
# 文件名称
file_name = "天使与龙的轮舞05.mp4"
# 文件路径
file_path = "D:\Program files\JiJiDown\Download\CROSSANGE 天使与龙的轮舞"
# 通过os模块拼成文件路径详细信息
abs_path = os.path.join(file_path, file_name)
# 一次读取的大小
buff = 1024 * 1024
# 创建一个md5对象
md5 = hashlib.md5()
# 以二进制读的方式打开文件
with open(abs_path, mode="rb") as f:
    while True:
        data = f.read(buff)
        # 把读到的数据给md5对象
        if data:
            md5.update(data)
        # 读不到数据则退出循环
        else:
            break

# 组成文件信息字典
file_dic = {
    # 文件名
    "file_name": file_name,
    # md5值
    "md5_value": str(md5.hexdigest()),
    # 一次发送的字节数值
    "buff": buff,
    # 文件大小
    "file_size": os.path.getsize(abs_path)
}
# 序列化
# 编码
bytes_dic = json.dumps(file_dic).encode("utf-8")
# 获取字典长度,转换为struct
len_dic = struct.pack("i", len(bytes_dic))

# 先发字典长度再发字典
conn.send(len_dic)
conn.send(bytes_dic)

# 以二进制只读的方式打开文件，读buff个字节数据，发buff个字节数据
with open(abs_path, mode="rb") as f:
    while True:
        data = f.read(buff)
        if data:
            conn.send(data)
        else:
            break
# 关闭连接、服务器
conn.close()
sk.close()