import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""
    def __init__(self, plain_settings, screen):
        """初始化外星人并设置其起始位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.plain_settings = plain_settings
        
        # 加载外星人图像， 并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

#        self.y = float(self.rect.y)
#        self.speed_factor = plain_settings.alien_speed_factor
#        self.direction = 1
#        self.direction_y = 1
#
#        self.rect.x = self.x
#        self.rect.y = self.y
#        self.screen_rect = screen.get_rect()
#        self.check_edges()
#        self.check_edges_y()
            
    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """如果外星人位于屏幕边缘， 就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """向左或向右移动外星人"""
        self.x += (self.plain_settings.alien_speed_factor * self.plain_settings.fleet_direction)
        self.rect.x = self.x
#        self.x += (self.speed_factor * self.direction)
#        self.y += (self.speed_factor * self.direction_y)
#        self.rect.x = self.x
#        self.rect.y = self.y
#        self.check_edges()
#        self.check_edges_y()
#        self.update_bullets()
#        self.update_bullets_y()
        
