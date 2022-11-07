# -*- coding: utf-8 -*-
# @Time    : 2022/11/6 15:39
# @Author  : zhu
# @File    : common.py
# @Software: PyCharm
import uuid
import time


def generate_guid(prefix=''):
    return str(uuid.uuid3(uuid.NAMESPACE_URL, prefix + str(time.time())))


class ClientNotExists(Exception):
    guid = ""

    def __init__(self, guid):
        self.guid = guid


class MediaNotExistsError(Exception):
    pass


if __name__ == '__main__':

    from PyQt5.QtWidgets import QApplication
    import win32gui, sys

    hwnd = win32gui.FindWindow(None, '微信')
    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(hwnd).toImage()
    img.save("screenshot.jpg")

    # hwnd_title = dict()  # 创建字典保存窗口的句柄与名称映射关系
    #
    #
    # def get_all_hwnd(hwnd, mouse):
    #     if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
    #         hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
    #
    #
    # win32gui.EnumWindows(get_all_hwnd, 0)
    #
    # for h, t in hwnd_title.items():
    #     if t == "微信":
    #         win32gui.FindWindow(t)
    #         print(h, t)
    # import cv2
    # import numpy as np
    #
    # img = pyautogui.screenshot(region=[300, 50, 200, 100])  # 分别代表：左上角坐标，宽高
    # # 对获取的图片转换成二维矩阵形式，后再将RGB转成BGR
    # # 因为imshow,默认通道顺序是BGR，而pyautogui默认是RGB所以要转换一下，不然会有点问题
    # img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
    #
    # cv2.imshow("截屏", img)
    # cv2.waitKey(0)
