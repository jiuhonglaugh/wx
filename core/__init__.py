# -*- coding: utf-8 -*-
# @Time    : 2022/11/5 19:17
# @Author  : zhu
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Flask

from utils.confUtil import get_conf_by_name

app = Flask(__name__)
context_conf = get_conf_by_name('app.yml')
log_conf = context_conf.get('log', {})
wechat_client_list = {}
