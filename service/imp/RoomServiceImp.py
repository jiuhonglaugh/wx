# -*- coding: utf-8 -*-
# @Time    : 2022/11/5 19:17
# @Author  : zhu
# @File    : __init__.py.py
# @Software: PyCharm
from typing import List

from core import client_mgr
from service.RoomService import RoomService
from utils.exception import ClientLoginAuth


class RoomServiceImp(RoomService):
    @ClientLoginAuth()
    def get_all_rooms(self, guid) -> (int, dict, str):
        client = client_mgr.get_client(guid)
        client.get_login_info()
        return 200, {'rooms': client.get_rooms()}

    @ClientLoginAuth()
    def create_room(self, guid, member_list: List[str]) -> (int, dict, str):
        client = client_mgr.get_client(guid)
        ret = client.create_room(member_list)
        return 200 if ret else 500, {}

    @ClientLoginAuth()
    def get_room_detail(self, guid, room_wxid: str) -> (int, dict, str):
        client = client_mgr.get_client(guid)
        room_detail = client.get_room_detail(room_wxid)
        return 200, {'room_detail': room_detail}

    def send_room_at_msg(self, guid, to_room_wxid: str, content: str, at_list: List[str]) -> (int, dict, str):
        client = client_mgr.get_client(guid)
        ret = client.send_room_at_msg(to_room_wxid, content, at_list)
        return 200 if ret else 500, {}

    def del_room_member(self, guid, room_wxid: str, member_list: List[str]) -> (int, dict, str):
        client = client_mgr.get_client(guid)
        ret = client.del_room_member(room_wxid, member_list)
        return 200 if ret else 500

    def add_room_member(self, guid, room_wxid: str, member_list: List[str]) -> (int, dict, str):
        client = client_mgr.get_client(guid)
        ret = client.add_room_member(room_wxid, member_list)
        return 200 if ret else 500, {}

    def add_room_friend(self, guid, room_wxid: str, wxid: str, verify: str):
        client = client_mgr.get_client(guid)
        ret = client.add_room_friend(room_wxid, wxid, verify)
        return 200 if ret else 500, {}

    def quit_room(self, guid, room_wxid: str):
        client = client_mgr.get_client(guid)
        ret = client.quit_room(room_wxid)
        return 200 if ret else 500, {}

    def get_room_members(self, guid, room_wxid: str):
        client = client_mgr.get_client(guid)
        room_members = client.get_room_members(room_wxid)
        return 200, {"room_members": room_members}

    def get_room_name(self, guid, room_wxid: str):
        client = client_mgr.get_client(guid)
        room_members = client.get_room_members(room_wxid)
        return 200, {"room_members": room_members}
