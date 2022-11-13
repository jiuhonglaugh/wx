# -*- coding: utf-8 -*-
# @Time    : 2022/11/5 17:03
# @Author  : zhu
# @File    : Server.py
# @Software: PyCharm
from aioflask import Flask
from flask_cors import CORS
import core
from views.client import client_blue
from views.down import download_blue
from views.room import room_blue

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.register_blueprint(client_blue)
app.register_blueprint(download_blue)
app.register_blueprint(room_blue)


class Server:
    def __init__(self):
        app_conf = core.APP_CONF.get('app', {})
        app.debug = app_conf.get('debug', False)
        self.app_host = app_conf.get('host', '127.0.0.1')
        self.port = app_conf.get('port', 80)

    def start(self):
        app.run(self.app_host, self.port)
