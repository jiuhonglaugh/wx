# -*- coding: utf-8 -*-
# @Time    : 2022/11/26 11:49
# @Author  : zhu
# @File    : CleanUpInvalidClients.py
# @Software: PyCharm
from flask_apscheduler import APScheduler

from core import APP_CONF, CLIENT_MGR
from utils.Logger import Logger
from utils.common import close_process
from utils.timeUtil import get_time_stamp_ms

log = Logger(loggername=__name__, log_file_name='scheduler')


def clean_clients():
    log.info('start long time not login the client')
    for guid, client in CLIENT_MGR.get_all_clients().items():
        current_time = get_time_stamp_ms()
        create_time = int(APP_CONF.get('client_expiration_time_mm') * 60 + client.create_time)
        if create_time < current_time and not client.login_status:
            log.warn(f'{guid} Long time not login del client')
            CLIENT_MGR.remove_client(guid)


def add_clean_client_scheduler(scheduler):
    seconds = int(APP_CONF.get('clean_client_mm')) * 60
    scheduler.add_job(func=clean_clients, trigger='interval', seconds=seconds, id="clean_clients")
