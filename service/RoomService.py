# -*- coding: utf-8 -*-
# @Time    : 2022/11/5 19:17
# @Author  : zhu
# @File    : __init__.py.py
# @Software: PyCharm
from core import client_mgr
from service import RoomServiceImp
from utils.exception import ClientLoginAuth


class RoomService(RoomServiceImp):
    @ClientLoginAuth()
    def get_all_rooms(self, guid):
        client = client_mgr.get_client(guid)
        return 200, {'rooms': client.get_rooms()}, ''

    @ClientLoginAuth()
    def create_room(self, guid, member_list: list):
        client = client_mgr.get_client(guid)
        ret = client.create_room(member_list)
        return 500 if ret else 200, {}, ''

    @ClientLoginAuth()
    def get_room_detail(self, guid, room_wxid: str):
        client = client_mgr.get_client(guid)
        room_detail = client.get_room_detail(room_wxid)
        return 200, {'room_detail': room_detail}, ''
