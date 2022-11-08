# -*- coding: utf-8 -*-
# @Time    : 2022/11/5 17:13
# @Author  : zhu
# @File    : down.py
# @Software: PyCharm

from flask import Blueprint, request, send_file

from core import client_mgr
from utils.Logger import Logger
from utils.Response import response_json
from utils.exception import CatchException

download_blue = Blueprint('download', __name__, url_prefix="/download")
log = Logger(loggername=__name__)


@download_blue.route('/qrcode', methods=['GET'])
@CatchException()
async def qrcode():
    uid = request.args.get('guid')
    wechat = client_mgr.get_client(uid)
    if wechat.is_open and wechat.login_status:
        return response_json(200, {'guid': uid, 'msg': 'download img failed: client is open or client is login'})

    qrcode_path = wechat.qrcode_path
    return send_file(qrcode_path)
