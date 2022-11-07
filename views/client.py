# -*- coding: utf-8 -*-
# @Time    : 2022/11/5 17:13
# @Author  : zhu
# @File    : client.py
# @Software: PyCharm
import threading
from flask import Blueprint, json, request

from core import ntchat_conf
from core import wechat_client_list
from manager.mgr import ClientManager
from utils.Logger import Logger
from utils.Response import response_json
from utils.common import screenshot
from utils.exception import CatchException
from utils.fileUtil import repair_path

client_blue = Blueprint('client', __name__, url_prefix="/client")
log = Logger(loggername=__name__)
client_mgr = ClientManager()

client_mgr.callback_url = ntchat_conf.get("callback_url")


@client_blue.route('/callback', methods=['GET', 'POST'])
def on_callback():
    data = request.stream.read()
    data = json.loads(data.decode('utf-8'))
    if data['type'] == 11026:
        client_mgr.remove_client(data['guid'])
    return ''


@client_blue.route('/create', methods=['GET'])
@CatchException()
async def create():
    guid = client_mgr.create_client()
    return response_json(status=200, data={"guid": guid, 'client_is_open': False})


@client_blue.route("/open", methods=["GET", "POST"])
@CatchException()
async def open():
    datax = request.get_json()
    guid = datax.get('guid', None)
    client = client_mgr.get_client(guid)
    if client.is_open:
        return response_json(200, {"guid": guid, 'client_is_opent': True})
    ret = client.open(False, True)
    client.qrcode_event = threading.Event()
    client.qrcode_event.wait(timeout=10)
    client.qrcode_path = f"{repair_path(ntchat_conf.get('qrcode_img_path', './qrcodes'))}{guid}.jpg"
    screenshot(client.qrcode_path)
    return response_json(status=200 if ret else 500, data={"guid": guid, 'client_is_open': ret})


@client_blue.route("/logout", methods=["GET", "POST"])
@CatchException()
async def logout():
    datax = request.get_json()
    guid = datax.get('guid', None)
    client = client_mgr.get_client(guid)
    if client.login_status or client.is_open:
        return response_json(200, {"guid": guid, 'client_is_open': True})
    ret = client.open(False, True)
    client.qrcode_event = threading.Event()
    client.qrcode_event.wait(timeout=10)
    client.qrcode_path = f"{repair_path(ntchat_conf.get('qrcode_img_path', './qrcodes'))}{guid}.jpg"
    screenshot(client.qrcode_path)
    return response_json(status=200 if ret else 500, data={"guid": guid, 'client_is_open': ret})


@client_blue.route('/getRooms', methods=['GET'])
async def get_rooms():
    uid = request.args.get('uid')
    client = client_mgr.get_client(uid)
    if client:
        rooms = client.get_rooms()
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
