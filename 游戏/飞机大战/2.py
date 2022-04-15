import random

import pygame
from pygame import *
import time
class HeroPlane:
    def __init__(self,screen):
        #创建一个飞机图片，当做真正的飞机
        self.player = pygame.image.load(r'E:\图片\python\游戏\3.jpg')
        #定义飞机的坐标
        self.x = 500
        self.y = 500
        #飞机速度
        self.speed=10
        #记录当前的窗口对象
        self.screen=screen
        #装子弹的列表
        self.bullets=[]
    def key_control(self):
        #监听键盘事件
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_w] or key_pressed[K_UP]:
            self.y -= self.speed
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            self.y += self.speed
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            self.x -= self.speed
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            self.x += self.speed
        if key_pressed[K_SPACE]:
            #按下空格键发射子弹
            bullet=Bullet(self.screen,self.x,self.y)
            #把子弹放到列表里
            self.bullets.append(bullet)
    def display(self):
        self.screen.blit(self.player,(self.x, self.y))
        # 遍历所有子弹
        for bullet in self.bullets:
            #让子弹飞
            bullet.auto_move()
            '''子弹显示在窗口'''
            bullet.display()

class EnemyPlane:
    def __init__(self,screen):
        #创建一个飞机图片，当做真正的飞机
        self.player = pygame.image.load(r'E:\图片\python\游戏\3.jpg')
        #定义飞机的坐标
        self.x = 0
        self.y = 0
        #飞机速度
        self.speed=10
        #记录当前的窗口对象
        self.screen=screen
        #装子弹的列表
        self.bullets=[]
        #敌机的方向
        self.direction='right'

    def display(self):
        self.screen.blit(self.player,(self.x, self.y))
        #遍历所有子弹
        for bullet in self.bullets:
            #让子弹飞
            bullet.auto_move()
            '''子弹显示在窗口'''
            bullet.display()
    def auto_move(self):
        if self.direction=='right':
            self.x+=self.speed
        elif self.direction=='left':
            self.x -= self.speed
        if self.x>950:
            self.direction='left'
        elif self.x<0:
            self.direction='right'
    def auto_fire(self):
        '''自动开火，创建子弹对象，添加进列表'''
        random_num=random.randint(1,10)
        if random_num==8:
            bullet=EnemyBullet(self.screen,self.x,self.y)
            self.bullets.append(bullet)

class Bullet:
    def __init__(self,screen,x,y):
        self.x = x
        self.y = y-10
        self.speed=10
        #图片
        self.image = pygame.image.load(r'E:\图片\python\游戏\3.jpg')
        #窗口
        self.screen=screen
    def display(self):
        #显示子弹到窗口
        self.screen.blit(self.image, (self.x, self.y))
    def auto_move(self):
        '''让子弹飞'''
        self.y-=self.speed

class EnemyBullet:
    def __init__(self,screen,x,y):
        self.x = x
        self.y = y+10
        self.speed=10
        #图片
        self.image = pygame.image.load(r'E:\图片\python\游戏\3.jpg')
        #窗口
        self.screen=screen
    def display(self):
        #显示子弹到窗口
        self.screen.blit(self.image, (self.x, self.y))
    def auto_move(self):
        '''让子弹飞'''
        self.y+=self.speed

class GameSound():
    def __init__(self):
        pygame.mixer.init()#音乐模块初始化
        pygame.mixer.music.load('E:\音乐\吹梦到西洲.mp3')
        pygame.mixer.music.set_volume(0.5)
    def playBackgroundMusic(self):
        pygame.mixer.music.play(-1)#开始播放音乐

def main():
    sound=GameSound()
    sound.playBackgroundMusic()
    screen=pygame.display.set_mode((1000,600),0,32)
    background=pygame.image.load('E:/图片/壁纸/女生 女子 起床 晚上 都市 夜景 4k动漫壁纸_彼岸图网.jpg')
    #创建一个飞机对象
    player=HeroPlane(screen)
    # 创建一个敌方飞机对象
    enemy_player = EnemyPlane(screen)
    while True:
        screen.blit(background, (0, 0))
        #遍历所有的事件
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
        #执行飞机的按键监听
        player.key_control()
        #飞机的显示
        player.display()
        # 敌方飞机的显示
        enemy_player.display()
        #敌机自动移动
        enemy_player.auto_move()
        # 敌机自动开火
        enemy_player.auto_fire()
        pygame.display.update()
        time.sleep(0.1)
if __name__ == '__main__':
    main()