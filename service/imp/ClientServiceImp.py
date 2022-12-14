# -*- coding: utf-8 -*-
# @Time    : 2022/11/5 19:17
# @Author  : zhu
# @File    : __init__.py.py
# @Software: PyCharm
import threading
from core import CLIENT_MGR, NTCHAT_CONF
from service.ClientService import ClientService
from utils.common import screenshot, close_process
from utils.exception import ClientLoginAuth
from utils.fileUtil import repair_path, remove_file
from utils.timeUtil import get_time_stamp_ms


class ClientServiceImp(ClientService):
    def create_client(self) -> (int, dict, str):
        create_time = int(get_time_stamp_ms())
        guid = CLIENT_MGR.create_client(create_time)
        data = {"guid": guid, 'client_is_open': False, 'login_status': False, 'create_time': create_time}
        return 200, data, ''

    def open_client(self, guid: str, smart: bool = False, show_login_qrcode: bool = True) -> (int, dict, str):

        client = CLIENT_MGR.get_client(guid)
        data = {'guid': guid, 'login_status': client.login_status}
        if client.is_open:
            data['client_is_open'] = client.is_open
            return 200, data, ''

        client.is_open = client.open(smart, show_login_qrcode)
        client.qrcode_event = threading.Event()
        client.qrcode_event.wait(timeout=10)
        client.qrcode_path = f"{repair_path(NTCHAT_CONF.get('qrcode_img_path', '../qrcodes'))}{guid}.jpg"

        ret,msg = screenshot(client.qrcode_path)
        data['client_is_open'] = client.is_open
        return 200 if ret and client.is_open else 500, data, msg

    @ClientLoginAuth()
    def logout_client(self, guid: str) -> (int, dict, str):
        ret = CLIENT_MGR.remove_client(guid)
        return 200 if ret else 500, {"guid": guid, 'client_is_open': False}, ''

    def status_client(self, guid: str) -> (int, dict, str):
        client = CLIENT_MGR.get_client(guid)
        return 200, {'guid': guid, 'client_is_open': client.is_open, 'login_status': client.login_status}, ''
