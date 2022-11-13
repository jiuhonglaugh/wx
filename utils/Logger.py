# -*- coding: utf-8 -*-
# @Time    : 2022/11/5 17:14
# @Author  : zhu
# @File    : Logger.py
# @Software: PyCharm

import logging

import core
from utils import timeUtil

'''
loggername 参数最好指定，如果不指定可能会导致日志重复输出
'''


class Logger:
    def __init__(self, loggername='default'):
        self.logger = logging.getLogger(name=loggername)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter(core.LOG_CONF.get('format'))
        # 设置Console日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(get_level(core.LOG_CONF.get('clevel')))
        # 设置文件日志

        fh = logging.FileHandler(filename=sp(core.LOG_CONF.get('log_file')), encoding='utf-8')
        fh.setFormatter(fmt)
        fh.setLevel(get_level(core.LOG_CONF.get('flevel')))
        self.logger.addHandler(sh)
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


def sp(old_path, symbol='/'):
    args = old_path.split(symbol)
    file_name = args[-1]
    file_len = len(args[-1])
    filepath = old_path[:-file_len] + timeUtil.get_time('%Y-%m-%d') + '-' + file_name
    return filepath
