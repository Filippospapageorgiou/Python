import pygame
from pygame.sprite import Sprite
import math

class Explosion(Sprite):
    def __init__(self, ai_game, x, y):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        # Create explosion rectangle
        self.width = self.settings.explosion_start_size
        self.height = self.settings.explosion_start_size
        self.color = self.settings.explosion_color
        
        # Create the explosion's rect
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = x
        self.rect.centery = y
        
        # Timer for explosion duration
        self.timer = 30
    
    def update(self):
        # Make explosion expand
        self.width += 1
        self.height += 1
        self.rect = pygame.Rect(
            self.rect.centerx - self.width//2,
            self.rect.centery - self.height//2,
            self.width,
            self.height
        )
        
        self.timer -= 1
        return self.timer <= 0
    
    def draw_explosion(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

class AlienExplosion(Sprite):
    def __init__(self, ai_game, x, y):
        super().__init__()
        self.screen = ai_game.screen
        self.center_x = x
        self.center_y = y
        
        # Diagonal lines for X shape
        self.lines = [
            {'angle': 45, 'length': 5},   # Top-right
            {'angle': 135, 'length': 5},  # Top-left
            {'angle': 225, 'length': 5},  # Bottom-left
            {'angle': 315, 'length': 5},  # Bottom-right
        ]
        
        self.timer = 25
        self.expansion_speed = 4
        self.color = (255, 200, 0)  # Yellow
    
    def update(self):
        for line in self.lines:
            line['length'] += self.expansion_speed
        
        self.timer -= 1
        return self.timer <= 0
    
    def draw_explosion(self):
        fade = self.timer / 25
        current_color = (
            int(255 * fade),
            int(200 * fade),
            0
        )
        
        for line in self.lines:
            angle_rad = math.radians(line['angle'])
            end_x = self.center_x + math.cos(angle_rad) * line['length']
            end_y = self.center_y + math.sin(angle_rad) * line['length']
            
            pygame.draw.line(
                self.screen,
                current_color,
                (self.center_x, self.center_y),
                (end_x, end_y),
                2
            )