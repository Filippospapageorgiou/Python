import sys
from time import sleep
from game_stats import Game_stats
import random
import pygame
from settings import Settings
from bullet import Bullet
from alien import Alien
from explosion import Explosion
from explosion import AlienExplosion
from ship import Ship
from background import Background
from sound import SoundFader
from button import Button
from scoreboard import Scoreboard


class AlienInvasion:
    def __init__(self): 
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        self.background = Background(self)
        
        
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.alien_explosions = pygame.sprite.Group()
        self.stats = Game_stats(self)
        self.sb = Scoreboard(self)
        
        self._create_flee()
        
        self.play_button = Button(self,"Play")
        
        # Load sound
        self.shoot_sound = pygame.mixer.Sound('assets/laser1.wav')
        self.shoot_sound.set_volume(0.2)
        self.explosion_sound = pygame.mixer.Sound('assets/retro-explosion.wav')
        pygame.mixer.music.load('assets/bg_music.mp3')
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

        self.alien_explosion_sound = pygame.mixer.Sound('assets/retro-explosion.wav')
        self.lost_round_sound = pygame.mixer.Sound('assets/lost.wav')
        self.level_win = pygame.mixer.Sound('assets/level_win.ogg')
    
    
    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()     
            self._update_screen()
    
    def _check_events(self):  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event): 
        if event.key == pygame.K_ESCAPE:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
        if event.key == pygame.K_RIGHT:  
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT: 
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()     
    
    def _check_keyup_events(self, event): 
        if event.key == pygame.K_RIGHT:  
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:  
            self.ship.moving_left = False
    
    def _check_play_button(self,mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.stats.game_active = True
            pygame.mouse.set_visible(False)
        
        self.aliens.empty()
        self.bullets.empty()
        
        self._create_flee()
        self.ship.center_ship()
    
    def _fire_bullet(self): 
        if len(self.bullets) < self.settings.bullets_allowed: 
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.shoot_sound.play()  # Play sound when firing
    
    def _update_bullets(self): 
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                explosion = Explosion(self, bullet.rect.centerx, 0)
                self.explosions.add(explosion)
                self.bullets.remove(bullet)
                self.explosion_sound.play()  # Play sound when explosion occurs
        
        self._check_bullet_alien_colision()
        self._update_explosions()
    
    def _check_bullet_alien_colision(self):
        #check for any bullets that have hit aliens
        #if so get rid of the bullet and alien
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
            for aliens in collisions.values():
               for alien in aliens:
                   alien_explosion = AlienExplosion(self, alien.rect.centerx, alien.rect.centery)
                   self.alien_explosions.add(alien_explosion)
                   self.explosion_sound.play()  # Play sound when explosion occurs
        
        if not self.aliens:
            if not hasattr(self, 'sound_fader'):
                self.sound_fader = SoundFader(self.level_win)
            self.bullets.empty()
            self._create_flee()
            self.settings.increase_settings()
            self.stats.level += 1
            self.sb.prep_level()

        if hasattr(self, 'sound_fader'):
            self.sound_fader.update()
            # Remove sound_fader when it's done fading
            if not self.sound_fader.is_fading:
                delattr(self, 'sound_fader')
    
    def _update_explosions(self):
        for explosion in self.explosions.copy():
            if explosion.update():
                self.explosions.remove(explosion)
        
        for alien_explosion in self.alien_explosions.copy():
            if alien_explosion.update():
                self.alien_explosions.remove(alien_explosion)
        
        
        
    
    def _update_screen(self):  
        self.screen.fill(self.settings.bg_color)
        
        self.background.update()
        self.background.draw()
        
        self.sb.draw_score()
        
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for explosion in self.explosions:
            explosion.draw_explosion()
        for alien_explosion in self.alien_explosions:
            alien_explosion.draw_explosion()
        self.aliens.draw(self.screen)
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()
        
        
    
    def _create_flee(self):
        alien = Alien(self)
        alien_width , alien_height = alien.rect.size
        
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        
        
        #create full fleet of aliens
        for row_number in range(number_rows-self.settings.rows_diff):
            for alien_number in range(number_aliens_x-self.settings.collum_diff):
                flag = random.randint(0,1)
                if flag:
                    self._create_alien(alien_number, row_number)
            
    def _create_alien(self,alien_number, row_number):
        alien = Alien(self)
        alien_width , alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)
    
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()
    
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    
    def _ship_hit(self):
        self.lost_round_sound.play()
        if self.stats.ship_left > 0:
            self.pause_music()
            self.stats.ship_left -= 1
            self.aliens.empty()
            self.bullets.empty()
            
            self._create_flee()
            self.ship.center_ship()
            #pause
            sleep(1.2)
            self.unpause_music()
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
    
    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break
    
    def pause_music(self):
        pygame.mixer.music.pause()

    def unpause_music(self):
        pygame.mixer.music.unpause()

    def stop_music(self):
        pygame.mixer.music.stop()
        

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
    
    
    
    
    
    
    
    
    
    
    
    
    
    