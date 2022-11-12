# -*- coding: utf-8 -*-
# @Time    : 2022/11/5 17:13
# @Author  : zhu
# @File    : ClientServiceImp.py
# @Software: PyCharm
from flask import Blueprint, request

from service.ClientService import ClientService
from service.imp.ClientServiceImp import ClientServiceImp
from utils.Logger import Logger
from utils.Response import response_json
from utils.exception import CatchException

client_blue = Blueprint('client', __name__, url_prefix="/client")
log = Logger(loggername=__name__)
client_service: ClientService = ClientServiceImp()


@client_blue.route('/create', methods=['GET'])
@CatchException()
async def create():
    result = client_service.create_client()
    return response_json(result)


@client_blue.route("/open", methods=["POST"])
@CatchException()
async def open():
    open_data = request.get_json()
    return response_json(client_service.open_client(open_data.get('guid')))


@client_blue.route("/logout", methods=["POST"])
@CatchException()
async def logout():
    logout_data = request.get_json()
    return response_json(client_service.logout_client(logout_data.get('guid')))


@client_blue.route("/status", methods=["POST"])
@CatchException()
async def status():
    info_data = request.get_json()
    return response_json(client_service.status_client(info_data.get('guid')))
