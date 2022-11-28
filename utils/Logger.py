# -*- coding: utf-8 -*-
# @Time    : 2022/11/5 17:14
# @Author  : zhu
# @File    : Logger.py
# @Software: PyCharm

import logging
from logging.handlers import RotatingFileHandler
from core import LOG_CONF

'''
loggername 参数最好指定，如果不指定可能会导致日志重复输出
'''


class Logger:
    def __init__(self, loggername='default', log_file_name='app'):
        self.logger = logging.getLogger(name=loggername)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter(LOG_CONF.get('format'))
        # 设置Console日志
        if LOG_CONF.get('c_open'):
            sh = logging.StreamHandler()
            sh.setFormatter(fmt)
            sh.setLevel(get_level(LOG_CONF.get('clevel')))
            self.logger.addHandler(sh)

        # 设置文件日志
        if LOG_CONF.get('f_open', True):
            log_file_path = f"{LOG_CONF.get('log_dir').format(log_file_name)}.log"
            file_max_bytes = LOG_CONF.get('file_max', 512) * 1024
            file_count = LOG_CONF.get('file_count', 3)
            fh = RotatingFileHandler(filename=log_file_path,
                                     encoding='utf-8',
                                     maxBytes=file_max_bytes,
                                     backupCount=file_count)
            fh.setFormatter(fmt)
            fh.setLevel(get_level(LOG_CONF.get('flevel')))
            self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def cri(self, message):
        self.logger.critical(message)


def get_level(level):
    if level.lower() == 'error':
        return logging.ERROR
    elif level.lower() == 'warn':
        return logging.WARN
    elif level.lower() == 'debug':
        return logging.DEBUG
    else:
        return logging.INFO
