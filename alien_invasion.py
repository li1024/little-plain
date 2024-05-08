
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    plain_settings = Settings()
    screen = pygame.display.set_mode((plain_settings.screen_width, plain_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(plain_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(plain_settings)
    
    # # 创建存储游戏统计信息的实例， 并创建记分牌
    sb = Scoreboard(plain_settings, screen, stats)

    # 创建一艘飞船
    ship = Ship(plain_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建一个外星人编组
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(plain_settings, screen, ship, aliens)

    # 设置背景色
    # bg_color = (144, 238, 144)
    bg_color = plain_settings.bg_color
    
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件,通过game_functions.py中的check_events()函数来监视
        gf.check_events(plain_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
        
            # 更新子弹的位置，并删除已消失的子弹
            gf.update_bullets(plain_settings, screen, stats, sb, ship, bullets, aliens)

            # 更新外星人位置
            gf.update_aliens(plain_settings, stats, screen, ship, aliens, bullets)

        """更新屏幕上的图像， 并切换到新屏幕"""
        # 每次循环时都重绘屏幕
        gf.update_screen(plain_settings, screen, ship, aliens, bullets, play_button, stats, sb)

run_game()
