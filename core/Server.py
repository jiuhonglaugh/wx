# -*- coding: utf-8 -*-
# @Time    : 2022/11/5 17:03
# @Author  : zhu
# @File    : Server.py
# @Software: PyCharm
import core
from core import app


class Server:
    def __init__(self):
        app_conf = core.context_conf.get('app', {})
        self.app_host = app_conf.get('host', '127.0.0.1')
        self.port = app_conf.get('port', 80)

    def start(self):
        app.run(self.app_host, self.port)
