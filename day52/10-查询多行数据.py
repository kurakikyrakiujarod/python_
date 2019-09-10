from pymysql import *


def main():
    # 创建Connection连接
    conn = connect(host='localhost', port=3306, user='root', password='123456', database='jing_dong', charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()
    # 执行select语句，并返回受影响的行数：查询一条数据
    count = cs1.execute('select id,name from goods where id>=4')
    # 打印受影响的行数
    print("查询到%d条数据:" % count)

    result = cs1.fetchall()
    print(result)

    # 关闭Cursor对象
    cs1.close()
    conn.close()


if __name__ == '__main__':
    main()
