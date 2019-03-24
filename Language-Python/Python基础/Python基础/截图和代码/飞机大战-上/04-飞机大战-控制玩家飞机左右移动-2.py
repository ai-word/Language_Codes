# -*- coding:utf-8 -*-

import pygame
from pygame.locals import *
import time

def main():
    #1. 创建窗口
    screen = pygame.display.set_mode((480,852),0,32)

    #2. 创建一个背景图片
    background = pygame.image.load("./feiji/background.png")

    #3. 创建一个飞机图片
    hero = pygame.image.load("./feiji/hero1.png")

    x = 210
    y = 700

    while True:
        screen.blit(background, (0,0))

        screen.blit(hero, (x, y))

        pygame.display.update()

 	#获取事件，比如按键等
        for event in pygame.event.get():

            #判断是否是点击了退出按钮
            if event.type == QUIT:
                print("exit")
                exit()
            #判断是否是按下了键
            elif event.type == KEYDOWN:
                #检测按键是否是a或者left
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                    x-=5
                #检测按键是否是d或者right
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    x+=5
                #检测按键是否是空格键
                elif event.key == K_SPACE:
                    print('space')


        time.sleep(0.01)

if __name__ == "__main__":
    main()
