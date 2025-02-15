import pygame
from config import *

class UI:
    def __init__(self, font_path="voice-platformer/assets/font.otf"):
        self.font = pygame.font.Font(font_path, 40)
        self.font2 = pygame.font.Font(font_path, 25)

    def draw_text(self, screen, text, color, y_offset=0):
        lines = self.split_text(text, screen.get_width() - 40)  # Ajuste la largeur max
        y = HEIGHT * 0.4 + y_offset - (len(lines) * self.font.get_height()) // 2
        for line in lines:
            rendered_text = self.font.render(line, True, color)
            screen.blit(rendered_text, (WIDTH // 2 - rendered_text.get_width() // 2, y))
            y += self.font.get_height()
    
    def draw_score(self, screen, score, color=WHITE):
        text = f"Score: {score}"
        lines = self.split_text(text, screen.get_width() - 40)  # Ajuste la largeur max
        y = HEIGHT * 0.02 - (len(lines) * self.font2.get_height()) // 2
        for line in lines:
            rendered_text = self.font2.render(line, True, color)
            screen.blit(rendered_text, (WIDTH*0.02, y))
            y += self.font2.get_height()

    def split_text(self, text, max_width):
        words = text.split(" ")
        lines = []
        current_line = ""
        
        for word in words:
            test_line = f"{current_line} {word}".strip()
            if self.font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word
        
        if current_line:
            lines.append(current_line)
        
        return lines
    
    def draw_start_menu(self, screen):
        self.draw_text(screen, "SHOUT 2 PLAY", WHITE)
    
    def draw_pause_menu(self, screen):
        self.draw_text(screen, "PAUSE - Criez pour reprendre", WHITE)
    
    def draw_game_over(self, screen, score):
        self.draw_text(screen, f"GAME OVER - Score: {score}", RED)
    
    def loading_bar(self, screen, loading):
        #pygame.draw.rect(screen, WHITE, (WIDTH*0.1, HEIGHT*0.9, WIDTH*0.8, 20))
        #pygame.draw.rect(screen, GREEN, (WIDTH*0.1, HEIGHT*0.9, WIDTH*0.8 * loading / max_loading, 20))
        bar_width = WIDTH/10 # Largeur totale de la barre
        bar_height = HEIGHT/20   # Hauteur de la barre
        x, y = WIDTH*0.02, HEIGHT*0.04   # Position de la barre
        
        # Dessiner le fond de la barre
        pygame.draw.rect(screen, (200, 200, 200), (x, y, bar_width, bar_height))
        
        # Dessiner la progression
        fill_width = (loading%100)/100 * bar_width
        pygame.draw.rect(screen, (0, 150, 255), (x, y, fill_width, bar_height))

        text = self.font2.render(f"Munitions : {int(loading/100)}", True, (255, 255, 255))
        screen.blit(text, (x + bar_width + 10, y))