# -*- coding: utf-8 -*-
# @Time    : 2022/11/5 17:13
# @Author  : zhu
# @File    : ClientService.py
# @Software: PyCharm
from flask import Blueprint, request, json
from core import client_mgr
from service.RoomService import RoomService
from utils.Logger import Logger
from utils.Response import response_json
from utils.exception import CatchException
from service import RoomServiceImp

room_blue = Blueprint('rooms', __name__, url_prefix="/rooms")
log = Logger(loggername=__name__)
room_service: RoomServiceImp = RoomService()


@room_blue.route('/getAll', methods=['POST'])
@CatchException()
async def get_all_rooms():
    guid = request.get_json().get('guid')
    code, data, msg = room_service.get_all_rooms(guid)
    return response_json(code, data, msg)


@room_blue.route('/create', methods=['POST'])
@CatchException()
async def create_room():
    create_data = request.get_json()
    guid = create_data.get('guid')
    member_list: list = create_data.get('member_list')
    code, data, msg = room_service.create_room(guid, member_list)
    return response_json(code, data, msg)


@room_blue.route('/getRoomDetail', methods=['POST'])
@CatchException()
async def get_room_detail():
    detail_data = request.get_json()
    guid = detail_data.get('guid')
    room_wxid = detail_data.get('room_wxid')
    code, data, msg = room_service.get_room_detail(guid, room_wxid)
    return response_json(code, data, msg)


@room_blue.route('/get_publics', methods=['POST'])
@CatchException()
async def get_publics():
    uid = request.get_json().get('uid')
    wechat = client_mgr.get_client(uid)
    return response_json(200, {'publics': wechat.get_publics()})
