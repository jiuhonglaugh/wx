# -*- coding: utf-8 -*-
# @Time    : 2022/11/6 15:37
# @Author  : zhu
# @File    : __init__.py.py
# @Software: PyCharm
from typing import List


class RoomService:
    def get_all_rooms(self, guid: str) -> (int, dict, str):
        pass

    def create_room(self, guid: str, member_list: List[str]) -> (int, dict, str):
        pass

    def get_room_detail(self, guid: str, room_wxid: str) -> (int, dict, str):
        pass

    def send_room_at_msg(self, guid: str, to_room_wxid: str, content: str, at_list: List[str]) -> (int, dict, str):
        pass

    def del_room_member(self, guid: str, room_wxid: str, member_list: List[str]) -> (int, dict, str):
        pass

    def add_room_member(self, guid: str, room_wxid: str, member_list: List[str]) -> (int, dict, str):
        pass

    def add_room_friend(self, guid: str, room_wxid: str, wxid: str, verify: str, ):
        pass

    def quit_room(self, guid: str, room_wxid: str):
        pass

    def get_room_members(self, guid: str, room_wxid: str):
        pass

    def get_room_name(self, guid: str, room_wxid: str):
        pass
