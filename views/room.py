# -*- coding: utf-8 -*-
# @Time    : 2022/11/5 17:13
# @Author  : zhu
# @File    : ClientServiceImp.py
# @Software: PyCharm
from flask import Blueprint, request
from core import CLIENT_MGR
from service.imp.RoomServiceImp import RoomService, RoomServiceImp
from utils.Logger import Logger
from utils.Response import response_json
from utils.exception import CatchException

room_blue = Blueprint('rooms', __name__, url_prefix="/rooms")
log = Logger(loggername=__name__)
room_service: RoomService = RoomServiceImp()


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
    code, data = room_service.get_room_detail(guid, room_wxid)
    return response_json(code, data)


@room_blue.route('/toSendRoomAtWxid', methods=['POST'])
@CatchException()
async def to_send_room_at_wxid():
    request_data = request.get_json()
    guid = request_data.get('guid')
    room_wxid = request_data.get('room_wxid')
    content = request_data.get('content')
    at_list = request_data.get('at_list', [])
    return response_json(room_service.send_room_at_msg(guid, room_wxid, content, at_list))


@room_blue.route('/delRoomMember', methods=['POST'])
@CatchException()
async def del_room_member():
    request_data = request.get_json()
    guid = request_data.get('guid')
    room_wxid = request_data.get('room_wxid')
    member_list: list = request_data.get('member_list')
    return response_json(room_service.del_room_member(guid, room_wxid, member_list))


@room_blue.route('/addRoomMember', methods=['POST'])
@CatchException()
async def add_room_member():
    request_data = request.get_json()
    guid = request_data.get('guid')
    room_wxid = request_data.get('room_wxid')
    member_list: list = request_data.get('member_list')
    return response_json(room_service.add_room_member(guid, room_wxid, member_list))


@room_blue.route('/quitRoom', methods=['POST'])
@CatchException()
async def quit_room():
    request_data = request.get_json()
    guid = request_data.get('guid')
    room_wxid = request_data.get('room_wxid')
    return response_json(room_service.quit_room(guid, room_wxid))


@room_blue.route('/getRoomMembers', methods=['POST'])
@CatchException()
async def get_room_members():
    request_data = request.get_json()
    guid = request_data.get('guid')
    room_wxid = request_data.get('room_wxid')
    code, data = room_service.get_room_members(guid, room_wxid)
    return response_json(code, data)


@room_blue.route('/getRoomName', methods=['POST'])
@CatchException()
async def get_room_name():
    request_data = request.get_json()
    guid = request_data.get('guid')
    room_wxid = request_data.get('room_wxid')
    code, data = room_service.get_room_name(guid, room_wxid)
    return response_json(code, data)


@room_blue.route('/get_publics', methods=['POST'])
@CatchException()
async def get_publics():
    uid = request.get_json().get('uid')
    wechat = CLIENT_MGR.get_client(uid)
    return response_json(200, {'publics': wechat.get_publics()})
