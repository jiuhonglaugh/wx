# -*- coding: utf-8 -*-
# @Time    : 2022/11/5 19:17
# @Author  : zhu
# @File    : __init__.py.py
# @Software: PyCharm
import threading
from core import client_mgr, ntchat_conf
from service import ClientServiceImp
from utils.common import screenshot, close_process
from utils.exception import ClientLoginAuth
from utils.fileUtil import repair_path, remove_file


class ClientService(ClientServiceImp):
    def create_client(self):
        guid = client_mgr.create_client()
        data = {"guid": guid, 'client_is_open': False, 'login_status': False}
        return 200, data, ''

    def open_client(self, guid: str, smart: bool = False, show_login_qrcode: bool = True):
        client = client_mgr.get_client(guid)
        data = {'guid': guid, 'login_status': client.login_status}
        if client.is_open:
            data['client_is_open'] = client.is_open
            return 200, data, ''

        client.is_open = client.open(smart, show_login_qrcode)
        client.qrcode_event = threading.Event()
        client.qrcode_event.wait(timeout=10)
        client.qrcode_path = f"{repair_path(ntchat_conf.get('qrcode_img_path', '../qrcodes'))}{guid}.jpg"
        ret = screenshot(client.qrcode_path)
        data['client_is_open'] = client.is_open
        return 200 if ret and client.is_open else 500, data, ''

    @ClientLoginAuth()
    def logout_client(self, guid: str):
        client = client_mgr.get_client(guid)
        remove_file(client.qrcode_path)
        close_process(client.pid)
        client_mgr.remove_client(guid)
        return 200, {"guid": guid, 'client_is_open': False}, ''

    def status_client(self, guid: str):
        client = client_mgr.get_client(guid)
        return 200, {'guid': guid, 'client_is_open': client.is_open, 'login_status': client.login_status}, ''
