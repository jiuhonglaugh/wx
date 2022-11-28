# -*- coding: utf-8 -*-
# @Time    : 2022/11/5 19:17
# @Author  : zhu
# @File    : __init__.py.py
# @Software: PyCharm
from core.mgr import ClientManager
from utils.confUtil import get_conf_by_name

CONTEXT_CONF = get_conf_by_name('app.yml')
APP_CONF = CONTEXT_CONF.get('app', {})
LOG_CONF = CONTEXT_CONF.get('log', {})
NTCHAT_CONF = CONTEXT_CONF.get('ntchat', {})
CLIENT_MGR = ClientManager(NTCHAT_CONF.get("callback_url"))
