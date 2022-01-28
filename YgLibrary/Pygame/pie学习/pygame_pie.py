import math
import sys
import time
import pygame
import random
from random import randint
from pygame.locals import *


#使用pygame之前必须初始化
pygame.init()
#设置主屏窗口
screen=pygame.display.set_mode((600,500))
pygame.display.set_caption("The Pie Game - Press 1,2,3,4")


white = 255, 255, 255
blue = 0, 0, 255
myfont = pygame.font.Font(None, 60)
x=300
y=250
radius=200
position=x-radius,y-radius,radius*2,radius*2

piece1=False
piece2=False
piece3=False
piece4=False

while True:
    # 循环获取事件，监听事件
    for event in pygame.event.get():  # pygame.event.get 从队列中获取事件
        # 判断用户是否点了关闭按钮或任意键的按钮
        if event.type == pygame.QUIT:
            # 终止程序
            sys.exit()
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == (pygame.K_1 or pygame.K_KP1):
                    print("1")
                    piece1 = True
                if event.key == (pygame.K_2 or pygame.K_KP2):
                    print("2")
                    piece2 = True
                if event.key == (pygame.K_3 or pygame.K_KP3):
                    print("3")
                    piece3 = True
                if event.key == (pygame.K_4 or pygame.K_KP5):
                    print("4")
                    piece4 = True
    screen.fill((0, 0, 200))

    # draw the arc
    color = 100, 255, 200  # 圆弧的颜色
    width = 8  # 圆弧的线宽


    rand1=(x + radius / 2 - 20, y - radius / 2 - 20)
    rand2=(x - radius / 2, y - radius / 2 - 20)
    rand3=(x - radius / 2, y + radius / 2)
    rand4=(x + radius / 2-20, y + radius/ 2)

    textimage = myfont.render("Press Enter to start again", True, (255,0,0))
    screen.blit(textimage,(50,0))
    textimage01 = myfont.render("1", True, white)
    screen.blit(textimage01, rand1)
    textimage02 = myfont.render("2", True, white)
    screen.blit(textimage02, rand2)
    textimage03 = myfont.render("3", True, white)
    screen.blit(textimage03, rand3)
    textimage04 = myfont.render("4", True, white)
    screen.blit(textimage04, rand4)



    if piece1 == True:
        start_angle = math.radians(0)  # 圆弧的起点角度
        eng_angle = math.radians(90)  # 圆弧的终点角度
        pygame.draw.arc(screen, color, position, start_angle, eng_angle, width)

        pygame.draw.line(screen, color, (x,y), (x,y-radius), width)
        pygame.draw.line(screen, color, (x,y), (x+radius,y), width)
    if piece2 == True:
        start_angle = math.radians(90)  # 圆弧的起点角度
        eng_angle = math.radians(180)  # 圆弧的终点角度
        width = 8  # 圆弧的线宽
        pygame.draw.arc(screen, color, position, start_angle, eng_angle, width)

        pygame.draw.line(screen, color, (x,y), (x,y-radius), width)
        pygame.draw.line(screen, color, (x,y), (x-radius,y), width)
    if piece3 == True:
        start_angle = math.radians(180)  # 圆弧的起点角度
        eng_angle = math.radians(270)  # 圆弧的终点角度
        width = 8  # 圆弧的线宽
        pygame.draw.arc(screen, color, position, start_angle, eng_angle, width)

        pygame.draw.line(screen, color, (x, y), (x, y + radius), width)
        pygame.draw.line(screen, color, (x, y), (x - radius, y), width)
    if piece4 == True:
        start_angle = math.radians(270)  # 圆弧的起点角度
        eng_angle = math.radians(360)  # 圆弧的终点角度
        width = 8  # 圆弧的线宽
        pygame.draw.arc(screen, color, position, start_angle, eng_angle, width)

        pygame.draw.line(screen, color, (x, y), (x, y + radius), width)
        pygame.draw.line(screen, color, (x, y), (x+ radius, y), width)

    if piece1 == True and piece2 == True and piece3 == True and piece4 == True:
        color = 0, 255, 0  # 圆弧的颜色

    pygame.display.update()