# -*- coding: utf-8 -*-
# @Time    : 2022/11/5 16:43
# @Author  : zhu
# @File    : confUtil.py
# @Software: PyCharm

import yaml

from utils.fileUtil import get_home, get_config_path, repair_path


def get_conf(o) -> dict:
    if isinstance(o, str):
        return __get_conf_by_file(o)
    else:
        return __get_conf_by_stream(o)


def __get_conf_by_file(file):
    with open(file, 'r') as r:
        return yaml.load(r, Loader=yaml.SafeLoader)


def __get_conf_by_stream(stream):
    return yaml.load(stream, Loader=yaml.SafeLoader)


def get_conf_by_name(file_name):
    return __get_conf_by_file(repair_path(get_config_path()) + file_name)
