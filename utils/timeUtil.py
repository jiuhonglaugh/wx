# -*- coding: utf-8 -*-
# @Time    : 2022/11/5 19:11
# @Author  : zhu
# @File    : timeUtil.py
# @Software: PyCharm
import time
import datetime


def format_time(format='%Y-%m-%d %H:%M:%S', timestamp=time.time(), reduce=0):
    return time.strftime(format, time.localtime(timestamp - reduce))


def get_time(format='%Y-%m-%d %H:%M:%S', reduce=0):
    return time.strftime(format, time.localtime(time.time() - reduce))


def sleep(mm):
    time.sleep(mm)


def session_time_out(minutes):
    return datetime.timedelta(minutes=minutes)


if __name__ == '__main__':
    print(get_time(reduce=10) < get_time())
