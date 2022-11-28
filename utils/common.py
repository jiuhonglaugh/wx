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

from PIL import Image
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
                if img.save(save_path):
                    image_cut_save(save_path, 60, 95, 220, 260, save_path)
                    return os.path.exists(save_path), ''
    return False, '二维码截图或者存储失败，请稍后再试'


def image_cut_save(path, left, upper, right, lower, save_path):
    """
        所截区域图片保存
    :param path: 图片路径
    :param left: 区块左上角位置的像素点离图片左边界的距离
    :param upper：区块左上角位置的像素点离图片上边界的距离
    :param right：区块右下角位置的像素点离图片左边界的距离
    :param lower：区块右下角位置的像素点离图片上边界的距离
     故需满足：lower > upper、right > left
    :param save_path: 所截图片保存位置
    """
    img = Image.open(path)  # 打开图像
    box = (left, upper, right, lower)
    roi = img.crop(box)

    # 保存截取的图片
    roi.save(save_path)


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
