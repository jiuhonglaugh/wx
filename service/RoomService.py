# -*- coding: utf-8 -*-
# @Time    : 2022/11/6 15:37
# @Author  : zhu
# @File    : __init__.py.py
# @Software: PyCharm
from typing import List


class RoomService:

    def get_all_rooms(self, guid: str) -> (int, dict, str):
        """
        # TODO 获取所有群成员
        :param guid:
        :return:
        """
        pass

    def create_room(self, guid: str, member_list: List[str]) -> (int, dict, str):
        """
        # TODO 创建群
        :param guid:
        :param member_list:
        :return:
        """
        pass

    def get_room_detail(self, guid: str, room_wxid: str) -> (int, dict):
        """
        # TODO 获取群详情
        :param guid:
        :param room_wxid:
        :return:
        """
        pass

    def send_room_at_msg(self, guid: str, to_room_wxid: str, content: str, at_list: List[str]) -> int:
        """
         # TODO 发送群消息 @ 成员
        :param guid:
        :param to_room_wxid:
        :param content:
        :param at_list:
        :return:
        """
        pass

    def del_room_member(self, guid: str, room_wxid: str, member_list: List[str]) -> (int, dict):
        """
        # TODO 删除群成员
        :param guid:
        :param room_wxid:
        :param member_list:
        :return:
        """
        pass

    def add_room_member(self, guid: str, room_wxid: str, member_list: List[str]) -> (int, dict):
        """
        # TODO 添加群成员
        :param guid:
        :param room_wxid:
        :param member_list:
        :return:
        """
        pass

    def add_room_friend(self, guid: str, room_wxid: str, wxid: str, verify: str) -> int:
        """
        # TODO 添加群成员为好友
        :param guid:
        :param room_wxid:
        :param wxid:
        :param verify:
        :return:
        """
        pass

    def quit_room(self, guid: str, room_wxid: str) -> int:
        """
        # TODO 退出群
        :param guid:
        :param room_wxid:
        :return:
        """
        pass

    def get_room_members(self, guid: str, room_wxid: str) -> (int, dict):
        """
        # TODO 获取群成员
        :param guid:
        :param room_wxid:
        :return:
        """
        pass

    def get_room_name(self, guid: str, room_wxid: str) -> (int, dict):
        """
        # TODO 获取群名称
        :param guid:
        :param room_wxid:
        :return:
        """
        pass

    def invite_room_member(self, guid, room_wxid, members_list):
        """
        # TODO 邀请好友入群
        :param guid:
        :param room_wxid:
        :param members_list:
        :return:
        """
        pass

    def modify_room_name(self, guid, room_wxid, name):
        """
        # TODO 修改群名称
        :param guid:
        :param room_wxid:
        :param name:
        :return:
        """
        pass

    def modify_room_notice(self, guid, room_wxid, notice):
        """
        # TODO 修改群公告
        :param guid:
        :param room_wxid:
        :param notice:
        :return:
        """
        pass
