import os
import hashlib
import time


# 把时间戳转化为时间字符串
def time_stamp_2_time(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)


def md5_size_time(directory, name):
    # 拼接成文件绝对路径
    path = os.path.join(directory, name)
    size = os.path.getsize(path)  # 获取文件的大小（字节）
    m_time = os.path.getmtime(path)  # 获取文件的修改时间
    c_time = os.path.getctime(path)  # 获取文件的创建时间
    a_time = os.path.getatime(path)  # 获取文件的访问时间
    # 计算md5值
    md5_obj = hashlib.md5()
    with open(path, mode='rb') as f:
        while True:
            data = f.read(1024)
            if data:
                md5_obj.update(data)
            else:
                break
    """
    os模块返回的是时间字符串，调用前面定义的函数把时间转换成制定格式时间字符串
    拼接成字典返回
    """
    return {
        '文件': path,
        '大小': str(size) + '字节',
        '创建时间': time_stamp_2_time(c_time),
        '修改时间': time_stamp_2_time(m_time),
        '访问时间': time_stamp_2_time(a_time),
        'MD5': md5_obj.hexdigest()
    }


if __name__ == '__main__':
    # 文件路径
    directory = 'D:\Program files\JiJiDown\Download\CROSSANGE 天使与龙的轮舞'
    # 文件名
    name = '天使与龙的轮舞05.mp4'
    info = md5_size_time(directory, name)
    # 迭代取出字典的键值
    # 一行显示一对键值
    for k in info:
        print('\033[34m{}: {}\033[0m'.format(k, info[k]))


# 文件: D:\Program files\JiJiDown\Download\CROSSANGE 天使与龙的轮舞\天使与龙的轮舞05.mp4
# 大小: 277376815字节
# 创建时间: 2018-10-21 12:43:54
# 修改时间: 2018-10-21 12:43:54
# 访问时间: 2018-10-21 23:48:26
# MD5: a6b6d5bd1b506299b4dffdc118903282