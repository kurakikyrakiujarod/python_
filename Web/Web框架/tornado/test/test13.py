# coding=utf-8

from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('templates/index.html', uname='UNAME', PWD='PWD')


app = Application([
    (r'^/$', IndexHandler)
])

app.listen(8000)

IOLoop.instance().start()
