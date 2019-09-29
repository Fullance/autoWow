import cv2
import numpy
import aircv as ac
import win32gui as wg
import pyautogui as ag
from PIL import ImageGrab

wowh = 0
bnh = 0

def game_init():
    global wowh, bnh
    if (wowh == 0) | (bnh == 0):
        wowh = wg.FindWindow(None, '魔兽世界')
        bnh = wg.FindWindow(None, '暴雪战网')
    print('魔兽和战网的句柄分别为：', wowh, ',', bnh)
    wg.MoveWindow(wowh, 0, 0, 800, 600)
    wg.MoveWindow(bnh, 0, 0, 800, 600)


def game_state():
    pass


def auto_login():
    pass


def anti_afk():
    pass


def in_queue():
    pass


game_init()
