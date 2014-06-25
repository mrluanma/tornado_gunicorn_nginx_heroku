import os
import multiprocessing


bind = 'unix:/tmp/hello.socket'
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'tornado'


def when_ready(server):
    os.system('touch /tmp/app-initialized')
