# -*- coding: utf-8 -*-
# @Time    : 2022/11/5 16:45
# @Author  : zhu
# @File    : fileUtil.py
# @Software: PyCharm
import os
from os.path import dirname, abspath


def get_file_as_stream(file):
    if os.path.exists(file):
        with open(file, 'r') as r:
            return r


def repair_path(path):
    if str(path).endswith(os.sep):
        return path
    return path + os.sep


def get_file_as_lines(file) -> list:
    return get_file_as_stream(file).readlines()


def get_home():
    return dirname(dirname(abspath(__file__)))


def get_config_path():
    return repair_path(get_home()) + 'conf'
