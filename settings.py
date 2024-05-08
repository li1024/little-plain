class Settings():
    """存储《外星人入侵》 的所有设置的类"""
    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕大小设置
        self.screen_width = 1200
        self.screen_height = 800
        
        # 屏幕背景颜色设置
        self.bg_color = (230, 230, 230)

        # 飞机的数量限制
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3    # 允许同时发射的子弹数量
        
        # 外星人设置
        self.fleet_drop_speed = 10
        
        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        #self.score_scale = 1.5
        self.initialize_dynamic_settings()
        #self.increase_speed()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        # 飞船的移动速度设置，默认为1像素
        self.ship_speed_factor = 1.5
        # 子弹的移动速度设置
        self.bullet_speed_factor = 3
        # 外星人的移动速度设置
        self.alien_speed_factor = 1
        # fleet_direction为1表示向右； 为-1表示向左
        self.fleet_direction = 1
        # 得分
        self.alien_points = 50
    
    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

    