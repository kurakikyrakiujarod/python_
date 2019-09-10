# coding=utf-8

import tornado.web
import tornado.ioloop

UAS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36']


class AccessHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        UA = self.request.headers['User-Agent']
        # < class 'tornado.httputil.HTTPHeaders'>
        # print type(UA)

        if UA not in UAS:
            self.send_error(403)
        else:
            self.write('正常访问！')


ipcount = {}  # ipcount放到数据库（redis），读取最近一小时的访问次数


class SecondHandler(tornado.web.RequestHandler):
    def get(self):
        # HTTPServerRequest().remote_ip
        # 获取客户端访问地址
        ip = self.request.remote_ip
        # 每次访问增加1
        value = ipcount.get(ip, 0) + 1
        # 将访问次数存放在字典中
        ipcount[ip] = value

        print(ip, value)
        # 判断是否超过20次访问
        if ipcount.get(ip) > 20:
            self.send_error(403)
        else:
            self.write('访问成功')


app = tornado.web.Application([
    (r'/', AccessHandler),
    (r'^/login/$', SecondHandler)
])

app.listen(8000)

tornado.ioloop.IOLoop.instance().start()
