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

'''
#2.2.1打印文本(pygame.fout.Fout())
pygame.display.set_caption("2.2.1打印文本pygame.fout.Fout()")

white=255,255,255
blue=0,0,255
myfont=pygame.font.Font(None,60)
textimage=myfont.render("Hello Pygame",True,white)
while True:
    Ty()
    # 填充主窗口的背景颜色，参数值RGB（颜色元组）
    screen.fill(blue)
    #textimage表示要粘贴的对象，（100,100）表示在主窗口一个标识的位置
    screen.blit(textimage,(180,230))
    #更新屏幕内容
    pygame.display.update()
'''

'''
#2.2.3绘制圆(pygame.draw.circle())
pygame.display.set_caption("2.2.3绘制圆pygame.draw.circle()")
while True:
    Ty()
    screen.fill((0,0,200))

    #draw a circle
    color=255,255,0  #该参数用于该图形着色
    position=300,250 #该参数用来指定的圆心位置
    radius=100 #圆的半径
    width=10   #可选参数，指定边框的宽度，默认为 0，表示填充该矩形区域，当 width > 0 时，表示线框的宽度；而 width < 0 时，此时不会绘制任何图形。
    pygame.draw.circle(screen,color,position,radius,width)
    pygame.display.update()
'''

'''
#2.2.4绘制矩形(pygame.draw.rect())
pygame.display.set_caption("2.2.4绘制矩形pygame.draw.rect()")
pos_x=300
pos_y=250
vel_x=2
vel_y=1
while True:
    Ty()
    screen.fill((0,0,200))
    #move the rectangle
    pos_x+=vel_x
    pos_y+=vel_y

    #keep rectangle on the screen
    if pos_x > 500 or pos_x < 0:
        vel_x = -vel_x
    if pos_y > 400 or pos_y < 0:
        vel_y = -vel_y

    rand1 = randint(0, 255)
    rand2 = randint(0, 255)
    rand3 = randint(0, 255)
    color = rand1, rand2, rand3

    # color=255,255,0
    width = 0
    pos = pos_x, pos_y, 100, 100
    pygame.draw.rect(screen, color, pos, width)
    pygame.display.update()
'''

'''
#2.2.5绘制线条pygame.draw.line()
pygame.display.set_caption("2.2.5绘制线条pygame.draw.line()")
while True:
    Ty()
    screen.fill((0,80,0))

    #draw the line
    origin=100,100  #线的起点
    destination=500,400 #线的终点
    color=100,255,200  #线的颜色
    width=10  #线条的宽度
    pygame.draw.line(screen,color,origin,destination,width)

    pygame.display.update()
'''


'''
#2.2.6绘制弧形pygame.draw.arc()
pygame.display.set_caption("2.2.6绘制弧形pygame.draw.arc()")

while True:
    Ty()
    screen.fill((0,0,200))

    #draw the arc
    color=100,255,200 #圆弧的颜色
    position=200,150,200,200 #圆弧的起点坐标，终点坐标
    start_angle=math.radians(0) #圆弧的起点角度
    eng_angle=math.radians(180) #圆弧的终点角度
    width=8  #圆弧的线宽
    pygame.draw.arc(screen,color,position,start_angle,eng_angle,width)

    pygame.display.update()
'''