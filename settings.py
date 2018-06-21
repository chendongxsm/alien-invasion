class Settings:
    """存储所有设置的类"""

    def __init__(self):
        self.screen_width = 640
        self.screen_height = 480
        self.bg_color = (230, 230, 230)


        # 子弹设置
        self.bullet_speed_factor = 0.1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # 外星人设置
        self.alien_speed_factor = 0.2
        self.alien_drop_speed = 10
        self.fleet_direction = 1

        # 飞船设置
        self.ship_speed_factor = 0.5
        self.ship_limit = 3
