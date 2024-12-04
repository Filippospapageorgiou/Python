import pygame.font
import math

class Button:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        # Set the dimensions and properties of the button
        self.width, self.height = 220, 60
        # Neon blue color scheme
        self.button_color = (0, 0, 0)  # Black background
        self.border_color = (0, 255, 255)  # Cyan border
        self.glow_color = (0, 128, 255)  # Lighter blue for glow
        self.text_color = (0, 255, 255)  # Cyan text
        
        # Try to use a more retro font, fallback to default if not available
        try:
            self.font = pygame.font.Font('freesansbold.ttf', 40)
        except:
            self.font = pygame.font.SysFont(None, 40)
        
        # Build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # Animation properties
        self.glow_alpha = 0  # For pulsing effect
        self.glow_direction = 1
        self.glow_speed = 4
        self.time_passed = 0
        
        self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        # Create the base text
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
        # Create a glow effect for text
        self.glow_image = self.font.render(msg, True, self.glow_color)
        self.glow_image_rect = self.glow_image.get_rect()
        self.glow_image_rect.center = self.rect.center

    def draw_button(self):
        # Update glow effect
        self.time_passed += 1
        self.glow_alpha += self.glow_speed * self.glow_direction
        if self.glow_alpha >= 100:
            self.glow_direction = -1
        elif self.glow_alpha <= 0:
            self.glow_direction = 1

        # Create a surface for the button with alpha for glow
        glow_surface = pygame.Surface((self.width + 20, self.height + 20), pygame.SRCALPHA)
        button_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        
        # Draw main button (black background)
        pygame.draw.rect(button_surface, self.button_color, 
                        pygame.Rect(0, 0, self.width, self.height), border_radius=3)
        
        # Draw border with glow
        for i in range(3):  # Multiple borders for glow effect
            glow_color = (*self.border_color[:3], 100 - i * 30)
            pygame.draw.rect(button_surface, glow_color,
                           pygame.Rect(i, i, self.width - i * 2, self.height - i * 2),
                           2, border_radius=3)

        # Add scanline effect (retro CRT look)
        for y in range(0, self.height, 2):
            pygame.draw.line(button_surface, (0, 0, 0, 50), 
                           (0, y), (self.width, y))

        # Draw the surfaces
        self.screen.blit(glow_surface, 
                        (self.rect.x - 10, self.rect.y - 10))
        self.screen.blit(button_surface, self.rect)

        # Draw text with glow
        glow_text = self.font.render(self.msg_image.get_rect().width * " ", True, self.glow_color)
        glow_text_rect = glow_text.get_rect(center=self.msg_image_rect.center)
        
        # Add slight hover effect using sine wave
        hover_offset = math.sin(self.time_passed / 20) * 2
        
        # Draw text glow
        glow_surface = pygame.Surface(self.msg_image.get_size(), pygame.SRCALPHA)
        glow_surface.blit(self.glow_image, (0, 0))
        glow_surface.set_alpha(abs(self.glow_alpha))
        self.screen.blit(glow_surface, 
                        (self.msg_image_rect.x, 
                         self.msg_image_rect.y + hover_offset))
        
        # Draw main text
        self.screen.blit(self.msg_image, 
                        (self.msg_image_rect.x, 
                         self.msg_image_rect.y + hover_offset))
        