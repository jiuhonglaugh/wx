# -*- coding: utf-8 -*-
# @Time    : 2022/11/6 16:31
# @Author  : zhu
# @File    : exception.py
# @Software: PyCharm
from functools import wraps
import ntchat
from utils.Response import response_json
from flask import request


class ClientNotExists(Exception):
    guid = ""

    def __init__(self, guid):
        self.guid = guid


class MediaNotExistsError(Exception):
    pass


class CatchException:
    def __call__(self, f):
        @wraps(f)
        async def wrapper(*args, **kwargs):
            try:
                return await f(*args, **kwargs)
            except ntchat.WeChatNotLoginError:
                return response_json(msg="wechat instance not login")
            except ntchat.WeChatBindError:
                return response_json(msg="wechat bind error")
            except ntchat.WeChatVersionNotMatchError:
                return response_json(msg="wechat version not match, install require wechat version")
            except MediaNotExistsError:
                return response_json(msg="file_path or url error")
            except ClientNotExists as e:
                return response_json(msg="client not exists, guid: %s" % e.guid)
            except Exception as e:
                return response_json(msg=str(e))

        return wrapper


class ClientLoginAuth:
    def __call__(self, f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            from core import CLIENT_MGR
            guid = request.get_json()['guid']
            client = CLIENT_MGR.get_client(guid)
            if client.is_open and client.login_status:
                return f(*args, **kwargs)
            return 500, {"guid": guid, 'client_is_open': client.is_open, 'login_status': client.login_status}, ''

        return wrapper
