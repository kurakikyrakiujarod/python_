# coding=utf-8

import tornado.web
import tornado.ioloop
import pymysql


def _getConn():
    return pymysql.connect(host='127.0.0.1', user='root', passwd='', db='tornaod2019', port=3306)


class RegisterHandler(tornado.web.RequestHandler):
    def initialize(self, conn):
        self.conn = conn

    def get(self, *args, **kwargs):
        self.render('templates/register.html')

    def post(self, *args, **kwargs):
        # 获取请求参数
        uname = self.get_argument('uname')
        pwd = self.get_argument('pwd')

        # 将数据插入到数据库中
        try:
            cursor = self.conn.cursor()
            cursor.execute('insert into t_user values(null,"%s","%s",now())' % (uname, pwd))
            self.conn.commit()
            self.write('注册成功！')
        except:
            print('self.conn.rollback')
            self.conn.rollback()
            self.redirect('/register/')


app = tornado.web.Application([
    (r'^/register/$', RegisterHandler, {'conn': _getConn()})
])

app.listen(8888)

tornado.ioloop.IOLoop.instance().start()
