class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self, plain_settings):
        """初始化统计信息"""
        self.plain_settings = plain_settings
        self.reset_stats()

        # 游戏刚启动时处于活动状态
        self.game_active = False
    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.plain_settings.ship_limit
        self.score = 0
