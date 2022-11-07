# -*- coding: utf-8 -*-
# @Time    : 2022/11/5 17:13
# @Author  : zhu
# @File    : client.py
# @Software: PyCharm
import threading
from functools import wraps

from flask import Blueprint, json, request
from core import wechat_client_list
from manager.mgr import ClientManager
from utils.Logger import Logger
from utils.Response import response_json
from utils.exception import CatchException

client_blue = Blueprint('client', __name__, url_prefix="/client")
log = Logger(loggername=__name__)
client_mgr = ClientManager()

client_mgr.callback_url = "http://127.0.0.1:8000/client/callback"


@client_blue.route('/callback', methods=['GET', 'POST'])
def on_callback():
    data = request.stream.read()
    data = json.loads(data.decode('utf-8'))
    print(data)
    return ''


@client_blue.route('/create', methods=['GET'])
@CatchException()
def client_create():
    guid = client_mgr.create_client()
    return response_json(status=200, data={"guid": guid})


@client_blue.route("/open", methods=["GET", "POST"])
@CatchException()
def client_open():
    datax = request.get_json()
    client = client_mgr.get_client(datax["guid"])
    ret = client.open(datax["smart"], datax["show_login_qrcode"])

    if datax["show_login_qrcode"]:
        client.c = threading.Event()
        client.qrcode_event.wait(timeout=10)

    return response_json(200 if ret else 500, {"guid": datax["guid"], 'qrcode': client.qrcode})


@client_blue.route('/get_rooms', methods=['GET'])
def get_rooms():
    uid = request.args.get('uid')
    wechat = wechat_client_list.get(uid, None)
    if wechat:
        rooms = wechat.get_rooms()
        return json.dumps({'code': 200, 'rooms': rooms, 'success': True, 'msg': ''})
    else:
        return json.dumps({'code': 200, 'rooms': [], 'success': False, 'msg': '无效的uid'})


@client_blue.route('/get_publics', methods=['POST'])
def get_publics():
    uid = request.get_json().get('uid')
    wechat = wechat_client_list.get(uid, None)
    if wechat:
        publics = wechat.get_publics()
        return json.dumps({'code': 200, 'publics': publics, 'success': True, 'msg': ''})
    else:
        return json.dumps({'code': 200, 'publics': [], 'success': False, 'msg': '无效的uid'})
