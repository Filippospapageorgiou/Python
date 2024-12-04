import math
import pygame

class SoundFader:
    def __init__(self, sound, fade_duration=4000):
        self.channel = sound.play()
        self.start_time = pygame.time.get_ticks()
        self.fade_duration = fade_duration
        self.is_fading = True
        if self.channel is not None:
            self.channel.set_volume(1.0)
    
    def update(self):
        if self.is_fading and self.channel is not None:
            current_time = pygame.time.get_ticks()
            elapsed = current_time - self.start_time
            if elapsed < self.fade_duration:
                # Using a cosine function for smoother fade
                progress = elapsed / self.fade_duration
                volume = math.cos(progress * math.pi / 2)
                self.channel.set_volume(max(0.0, volume))
            else:
                self.channel.stop()
                self.is_fading = False