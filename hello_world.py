import os

import tornado.web


pid = os.getpid()


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("Hello, world!", file=self)
        print("Process ID: %s" % pid, file=self)


application = tornado.web.Application([("/", MainHandler)])
