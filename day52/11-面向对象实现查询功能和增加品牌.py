from pymysql import connect


class JD(object):
    def __init__(self):
        self.conn = connect(host='localhost', port=3306, user='root',
                            password='123456', database='jing_dong', charset='utf8')
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def execute_sql(self, sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)

    def show_all_items(self):
        sql = 'select * from goods;'
        self.execute_sql(sql)

    def show_all_cates(self):
        sql = 'select name from goods_cates;'
        self.execute_sql(sql)

    def show_all_brands(self):
        sql = 'select name from goods_brands;'
        self.execute_sql(sql)

    def adds_brands(self):
        name = input("请输入品牌名:")
        sql = """insert into goods_brands (name) values ("%s")""" % name
        self.cursor.execute(sql)
        self.conn.commit()

    @staticmethod
    def print_menu():
        print('-----京东-----')
        print('1:所有的商品')
        print('2:所有的商品分类')
        print('3:所有的商品品牌')
        print('4:增加品牌')
        return input('请输入功能序号:')

    def run(self):
        while True:
            num = self.print_menu()
            if num == '1':
                self.show_all_items()
            elif num == '2':
                self.show_all_cates()
            elif num == '3':
                self.show_all_brands()
            elif num == "4":
                self.adds_brands()
            else:
                print('输入有误')


def main():
    JD().run()



if __name__ == '__main__':
    main()
