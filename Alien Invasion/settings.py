

class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        #ship settings
        self.ship_limit = 2
        #Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 4
        #Explosion settings
        self.explosion_start_size = 20
        self.explosion_color = (255, 165, 0)  # Orange
        self.explosion_duration = 30
        #alines settings
        self.fleet_drop_speed = 10
        #How quickly the game chnages
        self.speedip_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        
        
    
    
    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 1.3
        self.alien_speed = 1
        self.rows_diff = 10
        self.collum_diff = 10
        self.fleet_direction = 1
        #scoreboard
        self.alien_points = 50
    
    def increase_settings(self):
        self.alien_points = int(self.alien_points * self.score_scale)
        self.ship_speed *= self.speedip_scale
        self.bullet_speed *= self.speedip_scale
        self.alien_speed *= self.speedip_scale
        if not ((self.rows_diff - 2) == 0):
            self.rows_diff -= 1
        if not ((self.collum_diff - 2) == 0):
            self.collum_diff -= 1    
        self.fleet_drop_speed += 1
        
        
        
        