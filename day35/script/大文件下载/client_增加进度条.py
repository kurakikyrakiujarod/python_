import socket
import struct
import json
import sys
import time


# 进度条
def process_bar(num, total):
    rate = num / total  # 小数
    rate_num = int(rate * 100)  # 整数
    # 整除10
    if not rate_num % 10:
        # 100%进度
        if rate_num == 100:  # 控制等于号的输出
            # 输出末尾没有\n换行符
            r = '\r\033[31m%s>%d%%\n' % ('=' * int(rate_num / 5), rate_num)
        else:
            r = '\r\033[33m%s>%d%%' % ('=' * int(rate_num / 5), rate_num)
        sys.stdout.write(r)
        sys.stdout.flush
    else:
        pass


# 记录开始的时间
start_time = time.time()
sk = socket.socket()
ip_port = ('127.0.0.1', 9999)
sk.connect(ip_port)

len_dic = sk.recv(4)
len_dic = struct.unpack('i', len_dic)[0]
dic = sk.recv(len_dic)
dic = json.loads(dic.decode('utf-8'))

with open(dic['file_name'], mode='wb') as f:
    # 初始化
    data_size = 0
    while True:
        # 每次读4096字节数据
        data = sk.recv(4096)
        f.write(data)
        # 记录总共读取的数据
        data_size += len(data)
        # 调用进度条函数打印进度条，传参 1 读取的数据， 文件的总大小
        process_bar(data_size, dic['file_size'])
        if data_size == dic['file_size']:
            break
sk.close()
print('本次下载花费了{}秒'.format(time.time() - start_time))
# 执行最终输出
# ====================>100%
# 本次下载花费了1.9845898151397705秒

# 注
# 计算MD5值和循环打印进度条会拖慢程序
