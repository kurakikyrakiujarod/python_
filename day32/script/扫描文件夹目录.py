import os

# 设置为全局变量 方便修改
dic = {
    'sum_size': 0,
    'file_num': 0,
    'directory_num': 0
}


def get_size(path, txt):
    # 传入的路径
    items = os.listdir(path)
    # 文件
    files = []
    # 文件夹
    dirs = []
    # 总大小
    sum_size = 0
    for item in items:
        item = os.path.join(path, item)
        # 如果是文件夹添加到文件夹列表中
        if os.path.isdir(item):
            dirs.append(item)
        # 如果是文件添加到文件列表中
        elif os.path.isfile(item):
            files.append(item)

    for file in files:
        # 获取文件的大小
        size = os.path.getsize(file)
        # 累加
        sum_size += size
        # 打印文件和文件大小
        print(file, size)
        # 修改全局变量
        dic['file_num'] += 1
        dic['sum_size'] += size
        # 写入到txt文件中
        with open(txt, mode="a+", encoding='utf-8') as f:
            data = '{} {}\n'.format(file, size)
            f.write(data)
    # 遍历文件夹 递归调用
    for directory in dirs:
        dic['directory_num'] += 1
        # sum_size += get_size(directory,txt)
        get_size(directory, txt)
    # 返回最终总大小
    return dic['sum_size']


# 入口
if __name__ == '__main__':
    # 路径
    path = 'E:\IDMD'
    # 文件名
    txt = 'data.txt'
    # result = get_size(path,txt)
    # print(result)
    get_size(path, txt)
    # 最终结果
    data = '{}:{}:{}\n'.format(dic['directory_num'], dic['file_num'], dic['sum_size'])
    # print(data)
    # 写入到txt文件中
    with open(txt, mode="a+", encoding='utf-8') as f:
        f.write(data)
