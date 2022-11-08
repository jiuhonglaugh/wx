# -*- coding: utf-8 -*-
# @Time    : 2022/11/5 17:13
# @Author  : zhu
# @File    : ClientService.py
# @Software: PyCharm
import ntchat

from core import client_mgr
from utils.fileUtil import remove_file


def callback(callback_data):
    msg = callback_data['message']
    type = msg['type']
    data = msg['data']
    guid = callback_data['guid']
    wechat_client = client_mgr.get_client(guid)
    if type == ntchat.MT_USER_LOGOUT_MSG:
        remove_file(wechat_client.qrcode_path)
        client_mgr.remove_client(callback_data['guid'])
