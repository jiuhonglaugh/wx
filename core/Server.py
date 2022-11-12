# -*- coding: utf-8 -*-
# @Time    : 2022/11/5 17:03
# @Author  : zhu
# @File    : Server.py
# @Software: PyCharm
import core


class Server:
    def __init__(self):
        app_conf = core.context_conf.get('app', {})
        self.debug = app_conf.get('debug', False)
        self.app_host = app_conf.get('host', '127.0.0.1')
        self.port = app_conf.get('port', 80)

    def start(self):
        core.app.debug = self.debug
        core.app.run(self.app_host, self.port)
