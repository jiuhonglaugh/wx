# -*- coding: utf-8 -*-
# @Time    : 2022/11/5 19:17
# @Author  : zhu
# @File    : __init__.py.py
# @Software: PyCharm
from aioflask import Flask
from core.mgr import ClientManager
from utils.confUtil import get_conf_by_name

app = Flask(__name__)
context_conf = get_conf_by_name('app.yml')
log_conf = context_conf.get('log', {})
ntchat_conf = context_conf.get('ntchat', {})
wechat_client_list = {}
client_mgr = ClientManager()
client_mgr.callback_url = ntchat_conf.get("callback_url")