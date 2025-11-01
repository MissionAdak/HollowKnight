import pygame
from settings import *
from os.path import join
import sys
import math

class Menu:
    def __init__(self, switch_to_game):
        # Setup
        self.display_surface = pygame.display.get_surface()
        self.switch_to_game = switch_to_game
        
        # Font
        self.font = pygame.font.Font(join('..', 'graphics', 'ui', 'runescape_uf.ttf'), 40)
        self.title_font = pygame.font.Font(join('..', 'graphics', 'ui', 'runescape_uf.ttf'), 80)
        self.small_font = pygame.font.Font(join('..', 'graphics', 'ui', 'runescape_uf.ttf'), 20)
        
        # Audio
        self.menu_music = pygame.mixer.Sound(join('..', 'audio', 'menumusic.mp3'))
        self.menu_music.set_volume(0.5)
        self.menu_music.play(-1)
        
        # Menu options
        self.options = ['Start', 'Continue', 'Settings', 'Quit']
        self.selected_option = 0
        
        # Colors
        self.title_color = '#FFFFFF'
        self.option_color = '#AAAAAA'
        self.selected_color = '#FFFFFF'
        self.studio_color = '#888888'
        
        # Animation
        self.animation_speed = 2
        self.animation_counter = 0
        
    def draw_text(self, text, font, color, x, y, centered=True):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if centered:
            text_rect.center = (x, y)
        else:
            text_rect.topleft = (x, y)
        self.display_surface.blit(text_surface, text_rect)
        return text_rect
    
    def input(self):
        keys = pygame.key.get_pressed()
        
        # Menu navigation
        if keys[pygame.K_UP] and not self.prev_key_up:
            self.selected_option = (self.selected_option - 1) % len(self.options)
        if keys[pygame.K_DOWN] and not self.prev_key_down:
            self.selected_option = (self.selected_option + 1) % len(self.options)
            
        # Selection
        if keys[pygame.K_RETURN] and not self.prev_key_enter:
            self.select_option()
            
        # Check for mouse clicks
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()[0]  # Left mouse button
        
        # Check if mouse is hovering over any option
        option_start_y = 300
        option_spacing = 70
        
        for i, option in enumerate(self.options):
            option_rect = pygame.Rect(0, 0, 200, 50)
            option_rect.center = (WINDOW_WIDTH // 2, option_start_y + i * option_spacing)
            
            # Highlight option on hover
            if option_rect.collidepoint(mouse_pos):
                self.selected_option = i
                
                # Select on click
                if mouse_click and not self.prev_mouse_click:
                    self.select_option()
            
        # Update previous input states
        self.prev_key_up = keys[pygame.K_UP]
        self.prev_key_down = keys[pygame.K_DOWN]
        self.prev_key_enter = keys[pygame.K_RETURN]
        self.prev_mouse_click = mouse_click
    
    def select_option(self):
        if self.options[self.selected_option] == 'Start':
            self.menu_music.stop()
            self.switch_to_game('level')
        elif self.options[self.selected_option] == 'Continue':
            self.menu_music.stop()
            self.switch_to_game('level')
        elif self.options[self.selected_option] == 'Settings':
            # Settings functionality would go here
            pass
        elif self.options[self.selected_option] == 'Quit':
            pygame.quit()
            sys.exit()
    
    def update_animation(self, dt):
        self.animation_counter += self.animation_speed * dt
        
    def display(self):
        # Clear screen with a dark background
        self.display_surface.fill('#0A0A10')
        
        # Draw title
        title_y = 100 + math.sin(self.animation_counter) * 10
        self.draw_text('Hollow Knight', self.title_font, self.title_color, WINDOW_WIDTH // 2, title_y)
        
        # Draw menu options
        option_start_y = 300
        option_spacing = 70
        
        for i, option in enumerate(self.options):
            color = self.selected_color if i == self.selected_option else self.option_color
            option_y = option_start_y + i * option_spacing
            
            # Add animation to selected option
            if i == self.selected_option:
                option_x = WINDOW_WIDTH // 2 + math.sin(self.animation_counter * 2) * 10
            else:
                option_x = WINDOW_WIDTH // 2
                
            self.draw_text(option, self.font, color, option_x, option_y)
        
        # Draw studio name
        self.draw_text('MD Game Studio', self.small_font, self.studio_color, 100, WINDOW_HEIGHT - 30, False)
    
    def run(self, dt):
        # Store previous key states
        if not hasattr(self, 'prev_key_up'):
            self.prev_key_up = False
            self.prev_key_down = False
            self.prev_key_enter = False
            self.prev_mouse_click = False
            
        self.input()
        self.update_animation(dt)
        self.display()