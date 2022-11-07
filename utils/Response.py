# -*- coding: utf-8 -*-
# @Time    : 2022/11/6 21:38
# @Author  : zhu
# @File    : Response.py
# @Software: PyCharm
from flask import make_response


def response_json(status=500, data=None, msg=""):
    return {
        "status": status,
        "data": {} if data is None else data,
        "msg": msg}

