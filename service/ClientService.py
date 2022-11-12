# -*- coding: utf-8 -*-
# @Time    : 2022/11/6 15:37
# @Author  : zhu
# @File    : __init__.py.py
# @Software: PyCharm

class ClientService:

    def create_client(self):
        pass

    def open_client(self, guid: str, smart: bool = False, show_login_qrcode: bool = True):
        pass

    def logout_client(self, guid: str):
        pass

    def status_client(self, guid: str):
        pass
