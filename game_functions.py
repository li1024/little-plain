import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
def check_events(plain_settings, screen, stats, play_button, ship, aliens, bullets):
    """响应按键和鼠标事件"""
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(plain_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)
        
        ## 按下右键只移动一个像素
        #elif event.type == pygame.KEYDOWN:
        #    if event.key == pygame.K_RIGHT:
        #        #向右移动飞船
        #        ship.rect.centerx += 1
        
        # 实现一次或连续向右移动
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, plain_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(plain_settings, screen, ship, aliens, bullets, play_button, stats, sb):
    """更新屏幕上的图像， 并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(plain_settings.bg_color)

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    
    # 显示得分
    sb.show_score()

    # 如果游戏处于非活动状态， 就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def check_keydown_events(event, plain_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(plain_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_bullets(plain_settings, screen, stats, sb, ship, bullets, aliens):
    """更新子弹的位置， 并删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # 检查是否有子弹击中了外星人
    # 如果是这样， 就删除相应的子弹和外星人
    check_bullet_alien_collisions(plain_settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(plain_settings, screen, stats, sb, ship, aliens, bullets):
    """响应子弹和外星人的碰撞"""
    # 删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        stats.score += plain_settings.alien_points
        sb.prep_score()
    if len(aliens) == 0:
        # 删除现有的所有子弹， 并创建一个新的外星人群
        bullets.empty()
        plain_settings.increase_speed()
        create_fleet(plain_settings, screen, ship, aliens)

def fire_bullet(plain_settings, screen, ship, bullets):
    """如果还没有到达限制， 就发射一颗子弹"""
    #创建新子弹， 并将其加入到编组bullets中
    if len(bullets) < plain_settings.bullets_allowed:  # 在限制的子弹数量内，才创建新子弹
        new_bullet = Bullet(plain_settings, screen, ship)
        bullets.add(new_bullet)

#def update_ship(ship):
#    """根据移动标志调整飞船的位置"""
#    # 更新飞船的center值，而不是rect
#    if ship.moving_right and ship.rect.right < ship.screen_rect.right:
#        ship.center += ship.ai_settings.ship_speed_factor
#    if ship.moving_left and ship.rect.left > 0:
#        ship.center -= ship.ai_settings.ship_speed_factor
#
def get_number_rows(plain_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (plain_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def get_number_aliens_x(plain_settings, alien_width):
    """计算每行可容纳多少个外星人"""
    available_space_x = plain_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(plain_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(plain_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.x = alien.x
    aliens.add(alien)

def create_fleet(plain_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人， 并计算每行可容纳多少个外星人
    alien = Alien(plain_settings, screen)
    number_aliens_x = get_number_aliens_x(plain_settings, alien.rect.width)
    number_rows = get_number_rows(plain_settings, ship.rect.height, alien.rect.height)
    # 创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(plain_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(plain_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(plain_settings, aliens)
            break
def change_fleet_direction(plain_settings, aliens):
    """将整群外星人下移， 并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += plain_settings.fleet_drop_speed
    plain_settings.fleet_direction *= -1

def update_aliens(plain_settings, stats, screen, ship, aliens, bullets):
    """
    检查是否有外星人位于屏幕边缘， 并更新整群外星人的位置
    """
    check_fleet_edges(plain_settings, aliens)
    aliens.update()
    
    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(plain_settings, stats, screen, ship, aliens, bullets)
    
    # 检测是否有外星人到达屏幕底端
    check_aliens_bottom(plain_settings, stats, screen, ship, aliens, bullets)

def ship_hit(plain_settings, stats, screen, ship, aliens, bullets):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        # 将ships_left减1
        stats.ships_left -= 1
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        # 创建一群新的外星人， 并将飞船放到屏幕底端中央
        create_fleet(plain_settings, screen, ship, aliens)
        ship.center_ship()
        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(plain_settings, stats, screen, ship, aliens, bullets):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样进行处理
            ship_hit(plain_settings, stats, screen, ship, aliens, bullets)
            break

def check_play_button(plain_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """在玩家单击Play按钮时开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 重置游戏设置
        plain_settings.initialize_dynamic_settings()
        # 隐藏光标
        pygame.mouse.set_visible(False)
        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        # 创建一群新的外星人， 并让飞船居中
        create_fleet(plain_settings, screen, ship, aliens)
        ship.center_ship()
