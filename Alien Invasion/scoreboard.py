import pygame.font
import math


class Scoreboard:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        
        # Retro arcade colors
        self.text_color = (0, 255, 255)  # Bright cyan
        self.glow_color = (0, 150, 255)  # Deeper blue for glow
        
        # Try to use a more retro-looking font
        try:
            # You might want to add your own retro font file to your game
            self.font = pygame.font.Font('freesansbold.ttf', 28)
        except:
            self.font = pygame.font.SysFont('arial', 28)
            
        self.small_font = pygame.font.SysFont('arial', 20)  # For the scanlines effect
        
        self.time_passed = 0
        self.high_score_flash = 0  # For flashing effect when new high score
        self.is_new_high_score = False
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        
    def prep_score(self):
        rounded_score = round(self.stats.score)
        # Format score with classic arcade style
        score_str = f"SCORE:{str(rounded_score)}"
        
        self.score_image = self.font.render(score_str, True, self.text_color)
        self.glow_image = self.font.render(score_str, True, self.glow_color)
        
        # Position it in the top right with some padding
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 15
        
    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        # Format high score with classic arcade style
        high_score_str = f"BEST:{str(high_score)}"
        
        # Create both normal and glow versions
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)
        self.high_score_glow = self.font.render(high_score_str, True, self.glow_color)
        
        # Position in center top
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
        
    def draw_high_score(self):
        # Create background surface for high score
        padding = 20
        bg_width = self.high_score_rect.width + padding
        bg_height = self.high_score_rect.height + padding
        bg_surface = pygame.Surface((bg_width, bg_height), pygame.SRCALPHA)
        
        # Add gradient background
        gradient = self.create_gradient_surface(bg_width, bg_height)
        bg_surface.blit(gradient, (0, 0))
        
        # Add scanlines with same effect as score
        for y in range(0, bg_height, 2):
            alpha = int(20 + math.sin(self.time_passed/10 + y/5) * 10)
            pygame.draw.line(bg_surface, (255, 255, 255, alpha),
                           (0, y), (bg_width, y), 1)
        
        # Position and draw high score background
        bg_rect = bg_surface.get_rect()
        bg_rect.centerx = self.screen_rect.centerx
        bg_rect.top = 5
        self.screen.blit(bg_surface, bg_rect)
        
        # Enhanced glow effect for new high score
        if self.is_new_high_score:
            self.high_score_flash += 1
            flash_intensity = abs(math.sin(self.high_score_flash / 10))
            glow_color = (
                int(self.glow_color[0] * flash_intensity),
                int(self.glow_color[1] * flash_intensity),
                int(self.glow_color[2])
            )
            self.high_score_glow = self.font.render(
                self.high_score_image.get_rect().width * " ", 
                True, glow_color
            )
        
        # Glowing text effect
        glow_offset = math.sin(self.time_passed / 20) * 1.5
        glow_alpha = int(abs(math.sin(self.time_passed / 30)) * 255)
        
        # Draw glowing high score
        glow_surface = self.high_score_glow.copy()
        glow_surface.set_alpha(glow_alpha // 2)
        self.screen.blit(glow_surface, 
                        (self.high_score_rect.x, 
                         self.high_score_rect.y + glow_offset))
        
        # Draw main high score text with float effect
        self.screen.blit(self.high_score_image, 
                        (self.high_score_rect.x, 
                         self.high_score_rect.y + math.sin(self.time_passed/20)))
        
        # Add vertical light beam effect
        beam_pos = (self.time_passed % (bg_width * 2)) - bg_width
        if beam_pos < bg_width:
            beam_surface = pygame.Surface((2, bg_height), pygame.SRCALPHA)
            for y in range(bg_height):
                alpha = int(50 * (1 - abs(y - bg_height/2)/(bg_height/2)))
                pygame.draw.line(beam_surface, (*self.text_color, alpha),
                               (0, y), (2, y))
            self.screen.blit(beam_surface, 
                           (self.high_score_rect.centerx + beam_pos - bg_width//2, 
                            self.high_score_rect.top))
        
    def draw_level(self):
        glow_alpha = int(abs(math.sin(self.time_passed / 25)) * 128)  # Subtle pulse
        glow_surface = self.level_glow.copy()
        glow_surface.set_alpha(glow_alpha)
    
        # Draw level glow and main text
        self.screen.blit(glow_surface, 
                    (self.level_rect.x, 
                     self.level_rect.y + 1))  # Slight offset for glow
        self.screen.blit(self.level_image, self.level_rect)
    
        # Optional: Flash effect when level increases
        if hasattr(self, 'level_changed') and self.level_changed:
            flash_alpha = int(abs(math.sin(self.time_passed / 10)) * 255)
            flash_surface = self.level_image.copy()
            flash_surface.set_alpha(flash_alpha)
            self.screen.blit(flash_surface, self.level_rect)
            # Reset level changed after a short time
            if self.time_passed % 60 == 0:  # Reset after about 1 second
                self.level_changed = False
            
    
    def draw_score(self):
        self.time_passed += 1
        
        # Create background surface
        padding = 20
        bg_width = self.score_rect.width + padding
        bg_height = self.score_rect.height + padding
        bg_surface = pygame.Surface((bg_width, bg_height), pygame.SRCALPHA)
        
        # Add gradient background
        gradient = self.create_gradient_surface(bg_width, bg_height)
        bg_surface.blit(gradient, (0, 0))
        
        # Add scanlines
        for y in range(0, bg_height, 2):
            alpha = int(20 + math.sin(self.time_passed/10 + y/5) * 10)
            pygame.draw.line(bg_surface, (255, 255, 255, alpha),
                           (0, y), (bg_width, y), 1)
        
        # Position and draw background
        bg_rect = bg_surface.get_rect()
        bg_rect.right = self.screen_rect.right - 10
        bg_rect.top = 5
        self.screen.blit(bg_surface, bg_rect)
        
        # Glowing text effect
        glow_offset = math.sin(self.time_passed / 20) * 1.5
        glow_alpha = int(abs(math.sin(self.time_passed / 30)) * 255)
        
        # Draw glowing text
        glow_surface = self.glow_image.copy()
        glow_surface.set_alpha(glow_alpha // 2)
        self.screen.blit(glow_surface, 
                        (self.score_rect.x, 
                         self.score_rect.y + glow_offset))
        
        # Draw main text with slight float effect
        self.screen.blit(self.score_image, 
                        (self.score_rect.x, 
                         self.score_rect.y + math.sin(self.time_passed/20)))
        
        # Add vertical light beam effect
        beam_pos = (self.time_passed % (bg_width * 2)) - bg_width
        if beam_pos < bg_width:
            beam_surface = pygame.Surface((2, bg_height), pygame.SRCALPHA)
            for y in range(bg_height):
                alpha = int(50 * (1 - abs(y - bg_height/2)/(bg_height/2)))
                pygame.draw.line(beam_surface, (*self.text_color, alpha),
                               (0, y), (2, y))
            self.screen.blit(beam_surface, 
                           (self.score_rect.right - beam_pos, self.score_rect.top))
        
        # Draw high score with all effects
        self.draw_high_score()
        self.draw_level()
    
    def create_gradient_surface(self, width, height):
        gradient = pygame.Surface((width, height), pygame.SRCALPHA)
        for y in range(height):
            alpha = int(128 * (1 - y/height))  # Fade from semi-transparent to transparent
            pygame.draw.line(gradient, (0, 0, 0, alpha), (0, y), (width, y))
        return gradient
    
    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.is_new_high_score = True
            self.high_score_flash = 0
            self.prep_high_score()
    
    def prep_level(self):
        """Prepare the level display with retro styling"""
        # Format level with leading zeros for retro feel
        level_str = f"{self.stats.level:2d}"  # Pad with zeros (e.g., "01", "02", etc.)
    
        # Using orange/amber color common in classic arcades
        self.text_color_level = (255, 160, 0)  # Bright orange
        self.glow_color_level = (200, 120, 0)  # Darker orange for glow
    
        # Create main level and glow effect
        self.level_image = self.font.render(level_str, True, self.text_color_level)
        self.level_glow = self.font.render(level_str, True, self.glow_color_level)
    
        # Position below score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10