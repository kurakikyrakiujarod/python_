# coding=utf-8

from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
import os


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html', uname='UNAME', PWD='PWD2')


app = Application([
    (r'^/$', IndexHandler)
], template_path=os.path.join(os.getcwd(), 'templates'))

app.listen(8000)

IOLoop.instance().start()
