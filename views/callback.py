# -*- coding: utf-8 -*-
# @Time    : 2022/11/5 17:13
# @Author  : zhu
# @File    : ClientService.py
# @Software: PyCharm
from flask import Blueprint, json, request
from utils.Logger import Logger
from utils.exception import CatchException
from service.CallbackService import callback

callback_blue = Blueprint('callback', __name__, url_prefix="/callback")
log = Logger(loggername=__name__)


@callback_blue.route('/', methods=['POST'])
@CatchException()
def on_callback():
    callback_data = request.stream.read()
    callback(json.loads(callback_data.decode('utf-8')))
    return ''
