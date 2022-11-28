# -*- coding: utf-8 -*-
# @Time    : 2022/11/5 17:03
# @Author  : zhu
# @File    : Server.py
# @Software: PyCharm
from aioflask import Flask
from flask_apscheduler import APScheduler
from flask_cors import CORS
from core import APP_CONF
from scheduler.CleanUpInvalidClients import add_clean_client_scheduler
from views.client import client_blue
from views.down import download_blue
from views.room import room_blue

app = Flask(__name__)
scheduler = APScheduler()
scheduler.init_app(app)
app.register_blueprint(client_blue)
app.register_blueprint(download_blue)
app.register_blueprint(room_blue)


class Server:
    def __init__(self):
        app.debug = APP_CONF.get('debug', False)
        if APP_CONF.get('cors', False):
            CORS(app, supports_credentials=True)
        self.app_host = APP_CONF.get('host', '127.0.0.1')
        self.port = APP_CONF.get('port', 80)

    def start(self):
        app.run(self.app_host, self.port)

    def init_scheduler(self):
        add_clean_client_scheduler(scheduler)
        scheduler.start()
        return self
