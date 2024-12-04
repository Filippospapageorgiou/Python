import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        # Dimensions and position for a slimmer beam
        beam_width = self.settings.bullet_width
        beam_height = self.settings.bullet_height
        
        # Make surface larger to accommodate glow effect
        self.image = pygame.Surface((beam_width + 10, beam_height + 10), pygame.SRCALPHA)
        
        # Define neon green colors for core and glow
        core_color = (255, 20, 20)  # Bright neon red core
        glow_color = (128, 0, 0)    # Darker red for glow
        
        # Draw the neon green beam with core and glow effect
        # Core beam
        pygame.draw.rect(self.image, core_color, (5, 5, beam_width, beam_height))
        
        # Glow effect - layered with diminishing opacity for a smooth glow
        for i in range(3):
            alpha = 100 - (i * 30)  # Decrease alpha for outer glow
            glow_surf = pygame.Surface((beam_width + i * 4, beam_height + i * 4), pygame.SRCALPHA)
            glow_color_with_alpha = (*glow_color, alpha)
            pygame.draw.rect(glow_surf, glow_color_with_alpha, 
                             (0, 0, beam_width + i * 4, beam_height + i * 4))
            # Position the glow around the core
            self.image.blit(glow_surf, (5 - i * 2, 5 - i * 2))
        
        self.rect = self.image.get_rect()
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)
    
    def update(self):
        # Move the bullet up the screen
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
    
    def draw_bullet(self):
        # Draw bullet to the screen
        self.screen.blit(self.image, self.rect)
