# -*- coding: utf-8 -*-
# @Time    : 2022/11/6 15:39
# @Author  : zhu
# @File    : common.py
# @Software: PyCharm
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
        print(id, title_name)
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
    return str(uuid.uuid3(uuid.NAMESPACE_URL, prefix + str(time.time())))


class ClientNotExists(Exception):
    guid = ""

    def __init__(self, guid):
        self.guid = guid


class MediaNotExistsError(Exception):
    pass


if __name__ == '__main__':

    hwnd_title = dict()


    def _get_all_hwnd(hwnd, mouse):
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


    win32gui.EnumWindows(_get_all_hwnd, 0)
    for wnd, v in hwnd_title.items():
        print(wnd, v)
        if v == '微信':
            app = QApplication(sys.argv)
            screen = QApplication.primaryScreen()
            img = screen.grabWindow(wnd).toImage()
            img_size = img.size()
            lr_size = img_size.width()
            ud_size = img_size.height()
            if lr_size < 400 and ud_size < 500:
                img.save(f"{wnd}.jpg")

    # from PIL import Image
    #
    # filename = r'./2426224.jpg'
    # img = Image.open(filename)
    # lr_size, ud_size = img.size  # 图片的长和宽
    #
    # print(lr_size, ud_size)

    # 这个是截取全屏的
    # hwnd = win32gui.FindWindow()
    # app = QApplication(sys.argv)
    # screen = QApplication.primaryScreen()
    # img = screen.grabWindow(hwnd).toImage()
    # img.save("screenshot.jpg")
