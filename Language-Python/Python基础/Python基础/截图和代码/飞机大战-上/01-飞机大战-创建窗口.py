# -*- coding:utf-8 -*-

import pygame
import time

def main():
    #1. 创建窗口
    screen = pygame.display.set_mode((480,852),0,32)

    #2. 创建一个背景图片
    background = pygame.image.load("./feiji/background.png")

    while True:
        screen.blit(background, (0,0))

        pygame.display.update()

        time.sleep(0.01)

if __name__ == "__main__":
    main()
