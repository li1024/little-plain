import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""
    def __init__(self, plain_settings, screen, ship):
        """在飞船所处的位置创建一个子弹对象"""
        # 调用了父类（即Bullet类的直接基类）的 __init__ 方法,。这样做是为了执行父类的初始化逻辑，确保子弹对象继承自父类的所有基本属性和行为得到正确设置。
        # 如果没有特殊的父类初始化需求，或者父类的 __init__ 方法不需要传递任何参数，这段代码也可以省略
        super(Bullet, self).__init__()  # 代码super(Bullet, self).__init__() 使用了Python 2.7语法。这种语法也适用于Python 3，但你也可以将这行代码简写为super().__init__()
        self.screen = screen
        
        # 在(0,0)处创建一个表示子弹的矩形， 再设置正确的位置
        self.rect = pygame.Rect(0, 0, plain_settings.bullet_width, plain_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        #存储用小数表示的子弹位置
        self.y = float(self.rect.y)
        self.color = plain_settings.bullet_color
        self.speed_factor = plain_settings.bullet_speed_factor
        #self.screen_rect = screen.get_rect()
        #self.height = ai_settings.bullet_height
        #self.width = ai_settings.bullet_width
        #self.rect.width = self.width
        #self.rect.height = self.height
        #self.rect.bottom = ship.rect.bottom
        #self.rect.centerx = ship.rect.centerx
        #self.y = float(self.rect.y)
        #self.color = ai_settings.bullet_color
        #self.speed_factor = ai_settings.bullet_speed_factor
        #self.screen_rect = screen.get_rect()
        #self.height = ai_settings.bullet_height
        #self.width = ai_settings.bullet_width
        #self.rect.width = self.width
        #self.rect.height = self.height
        #self.rect.bottom = ship.rect.bottom
        #self.rect.centerx = ship.rect.centerx
        #self.y = float(self.rect.y)
        #self.color = ai_settings.bullet_color
        #self.speed_factor = ai_settings.bullet_speed_factor
        #self.screen_rect = screen.get_rect()
        #self.height = ai_settings.bullet_height
        #self.width = ai_settings.bullet_width
        #self.rect.width = self.width
        #self.rect.height = self.height
        #self.rect.bottom = ship.rect.bottom
        #self.rect.centerx = ship.rect.centerx
        #self.y = float(self.rect.y)
        #self.color = ai_settings.bullet_color
        #self.speed_factor = ai_settings.bullet_speed_factor
        #self.screen_rect = screen.get_rect()
        #self.height = ai_settings.bullet_height
        #self.width = ai_settings.bullet_width
        #self.rect.width = self.width
        #self.rect.height = self.height
        #self.rect.bottom = ship.rect.bottom
        #self.rect.centerx = ship.rect.centerx
        #self.y = float(self.rect.y)
        #self.color = ai_settings.bullet_color
        #self.speed_factor = ai_settings.bullet_speed_factor
        #self.screen_rect = screen.get_rect()
        #self.height = ai_settings.bullet_height
        #self.width = ai_settings.bullet_width
        #self.rect.width = self.width
        #self.rect.height = self.height
        #self.rect.bottom = ship.rect.bottom
        #self.rect.centerx = ship.rect.centerx
        #self.y = float(self.rect.y)
        #self.color = ai_settings.bullet_color
        #self.speed_factor = ai_settings.bullet_speed_factor
        #self.screen_rect = screen.get_rect()
        #self.height = ai_settings.bullet_height

    def update(self):
        """向上移动子弹"""
        #更新表示子弹位置的小数值
        self.y -= self.speed_factor
        
        #更新表示子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
