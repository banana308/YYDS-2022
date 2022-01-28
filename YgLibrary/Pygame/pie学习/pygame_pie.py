import math
import sys
import time
import pygame
from random import randint
from pygame.locals import *


#使用pygame之前必须初始化
pygame.init()
#设置主屏窗口
screen=pygame.display.set_mode((600,500))

def Ty():
    # 循环获取事件，监听事件
    for event in pygame.event.get():
        # 判断用户是否点了关闭按钮或任意键的按钮
        if event.type in (QUIT,KEYDOWN):
            # 卸载所有模块
            pygame.quit()
            # 终止程序
            sys.exit()