# -*- coding: utf-8 -*-
# @Time    : 2022/11/6 15:39
# @Author  : zhu
# @File    : common.py
# @Software: PyCharm
import os
import subprocess
import uuid
import time
import sys
from PyQt5.QtWidgets import QApplication
import win32gui


def screenshot(save_path, window_name='微信'):
    hwnd_title = dict()

    def _get_all_hwnd(hwnd, mouse):
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})

    win32gui.EnumWindows(_get_all_hwnd, 0)
    for id, title_name in hwnd_title.items():
        if title_name == window_name:
            app = QApplication(sys.argv)
            screen = QApplication.primaryScreen()
            img = screen.grabWindow(id).toImage()
            img_size = img.size()
            lr_size = img_size.width()
            ud_size = img_size.height()
            if lr_size < 400 and ud_size < 500:
                return img.save(save_path)
    return False


def generate_guid(prefix=''):
    return str(uuid.uuid3(uuid.NAMESPACE_URL, prefix + str(time.time()))).replace('-', '')


class ClientNotExists(Exception):
    guid = ""

    def __init__(self, guid):
        self.guid = guid


class MediaNotExistsError(Exception):
    pass


def close_process(pid):
    os.kill(pid, 9)
