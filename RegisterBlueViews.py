# -*- coding: utf-8 -*-
# @Time    : 2022/11/5 17:11
# @Author  : zhu
# @File    : RegisterBlueViews.py
# @Software: PyCharm
from views.client import client_blue
from views.down import download_blue
from views.room import room_blue
from core import app

app.register_blueprint(client_blue)
app.register_blueprint(download_blue)
app.register_blueprint(room_blue)
