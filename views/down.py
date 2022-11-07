# -*- coding: utf-8 -*-
# @Time    : 2022/11/5 17:13
# @Author  : zhu
# @File    : down.py
# @Software: PyCharm
import os

from flask import Blueprint, request
from utils.Logger import Logger
from utils.Response import response_img

download_blue = Blueprint('download', __name__, url_prefix="/download")
log = Logger(loggername=__name__)
from views.client import client_mgr


@download_blue.route('/qrcode', methods=['GET'])
def qrcode():
    uid = request.args.get('guid')
    wechat = client_mgr.get_client(uid)
    qrcode_path = wechat.qrcode_path
    return response_img(qrcode_path)
