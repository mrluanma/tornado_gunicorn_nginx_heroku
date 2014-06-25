from __future__ import unicode_literals, print_function
import os

import tornado.web


pid = os.getpid()


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print('Hello, world!', file=self)
        print('Process ID: %s' % pid, file=self)


application = tornado.web.Application([
    (r'/', MainHandler),
])
