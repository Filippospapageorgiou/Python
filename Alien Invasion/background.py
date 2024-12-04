import pygame
import random
import math

class Background:
    def __init__(self, ai_game):
        """Initialize the background"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()
        
        # Star colors (slightly different white/blue tints)
        self.star_colors = [
            (255, 255, 255),  # Pure white
            (200, 200, 255),  # Bluish white
            (255, 255, 200),  # Yellowish white
            (200, 255, 255),  # Cyan tint
        ]
        
        # Create stars
        self.stars = []
        for _ in range(200):
            x = random.randint(0, self.settings.screen_width)
            y = random.randint(0, self.settings.screen_height)
            size = random.randint(1, 3)
            color = random.choice(self.star_colors)
            self.stars.append({
                'x': x,
                'y': y,
                'size': size,
                'base_color': color,
                'brightness': random.randint(150, 255),
                'twinkle_speed': random.uniform(0.02, 0.05)
            })
    
    def update(self):
        """Update star animation"""
        for star in self.stars:
            # Update star brightness using sine wave for smooth twinkling
            time = pygame.time.get_ticks() * star['twinkle_speed']
            star['brightness'] = int(200 + 55 * abs(math.sin(time)))
    
    def draw(self):
        """Draw the background"""
        # Fill with very dark blue (almost black) for space effect
        self.screen.fill((0, 0, 15))
        
        # Draw stars
        for star in self.stars:
            # Calculate current color based on brightness
            base_r, base_g, base_b = star['base_color']
            brightness_factor = star['brightness'] / 255.0
            color = (
                int(base_r * brightness_factor),
                int(base_g * brightness_factor),
                int(base_b * brightness_factor)
            )
            pygame.draw.circle(self.screen, color,
                             (star['x'], star['y']),
                             star['size'])