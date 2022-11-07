# -*- coding: utf-8 -*-
# @Time    : 2022/11/6 16:31
# @Author  : zhu
# @File    : exception.py
# @Software: PyCharm
from functools import wraps

import ntchat

from utils.Response import response_json


class ClientNotExists(Exception):
    guid = ""

    def __init__(self, guid):
        self.guid = guid


class MediaNotExistsError(Exception):
    pass


class CatchException:
    def __call__(self, f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                return f(*args, **kwargs)
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