"""
文件上传和下载 客户端
"""
# 导入模块
import socket
import struct
import json
import hashlib
import time

# 记录开始的时间
st_time = time.time()
ip_port = ("127.0.0.1", 9999)
# 创建套接字连接服务器
sk = socket.socket()
sk.connect(ip_port)
# 接收4个字节数据
len_dic = sk.recv(4)
# 反解struct得到元组，获取元组第一个元素
len_dic = struct.unpack("i", len_dic)[0]
# 接收指定长度,获取完整的字典,并解码
dic = sk.recv(len_dic).decode("utf-8")
# 反序列化得到真正的字典
dic = json.loads(dic)
# print(dic)
# 创建MD5对象
md5 = hashlib.md5()
# 根据字典得到文件名
# 创建文件，读数据写数据，计算md5值
with open(dic["file_name"], mode="wb") as f:
    while True:
        data = sk.recv(dic["buff"])
        if data:
            f.write(data)
            md5.update(data)
        else:
            break
# 返回md5值
md5_value = md5.hexdigest()
# 跟服务器发送过来的md5值进行比对
if md5_value == dic["md5_value"]:
    print("md5校验成功")
else:
    print("md5校验失败")
# 打印总共花费的时间
print("本次下载共花费{}秒".format(time.time()-st_time))