import pygame
from pygame import *
import time

def main():
    screen=pygame.display.set_mode((480,480),0,32)
    background=pygame.image.load('E:/图片/壁纸/女生 女子 起床 晚上 都市 夜景 4k动漫壁纸_彼岸图网.jpg')
    lianhua=pygame.image.load('E:/图片/CAD/logodao.comBSSC00000054.png')
    screen.blit(background,(0,0))
    x=90
    y=100

    while True:
        screen.blit(lianhua, (x, y))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
        key_pressed=pygame.key.get_pressed()
        if key_pressed[K_w] or key_pressed[K_UP]:
            print('上')
            y-=1
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            print('下')
            y+=1
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            print('左')
            x-=1
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            print('右')
            x+=1
        if key_pressed[K_SPACE]:
            print('空格')

        pygame.display.update()
        time.sleep(0.1)
if __name__ == '__main__':
    main()