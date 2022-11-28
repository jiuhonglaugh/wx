# -*- coding: utf-8 -*-
import ntchat
import requests
import threading
from typing import Dict, Union
from ntchat.utils.singleton import Singleton
from utils.common import generate_guid, close_process
from utils.exception import ClientNotExists
from utils.fileUtil import remove_file


class ClientWeChat(ntchat.WeChat):
    guid: str = ""
    qrcode_event: threading.Event = None
    qrcode: str = ""
    qrcode_path = ""
    is_open = False
    create_time = 0


class ClientManager(metaclass=Singleton):
    __client_map: Dict[str, ClientWeChat] = {}
    __callback_url: str = ""

    def get_all_clients(self):
        return self.__client_map.copy()

    def __init__(self, callback_url):
        self.__callback_url = callback_url

    def new_guid(self):
        """
        生成新的guid
        """
        while True:
            guid = generate_guid("wechat")
            if guid not in self.__client_map:
                return guid

    # 创建实例
    def create_client(self, create_time):
        guid = self.new_guid()
        wechat = ClientWeChat()
        wechat.create_time = create_time
        wechat.guid = guid
        self.__client_map[guid] = wechat

        # 注册回调
        wechat.on(ntchat.MT_ALL, self.__on_callback)
        wechat.on(ntchat.MT_RECV_WECHAT_QUIT_MSG, self.__on_quit_callback)
        return guid

    # 返回实例
    def get_client(self, guid: str) -> Union[None, ClientWeChat]:
        client = self.__client_map.get(guid, None)
        if client is None:
            raise ClientNotExists(guid)
        return client

    # 删除实例
    def remove_client(self, guid):
        if guid in self.__client_map:
            client = self.get_client(guid)
            remove_file(client.qrcode_path)
            client.on_close()
            del self.__client_map[guid]
            return True
        return False

    def __on_callback(self, wechat: ClientWeChat, message: dict):

        # 通知二维码显示
        msg_type = message['type']
        if msg_type == ntchat.MT_RECV_LOGIN_QRCODE_MSG and wechat.qrcode_event:
            wechat.qrcode = message["data"]["code"]
            wechat.qrcode_event.set()

        if not self.__callback_url:
            return

        client_message = {
            "guid": wechat.guid,
            "message": message
        }
        requests.post(self.__callback_url, json=client_message)

    def __on_quit_callback(self, wechat):
        self.__on_callback(wechat, {"type": ntchat.MT_RECV_WECHAT_QUIT_MSG, "data": {}})

    # 返回实例字典
    def get_guid_dict(self):
        return self.__client_map
