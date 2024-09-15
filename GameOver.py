import pygame
from pygame import mixer

class GameOverScreen:
    def __init__(self, screen, font, over_font, background):
        self._screen = screen
        self._font = font
        self._over_font = over_font
        self._background = background

    #GT pra screen
    @property
    def screen(self):
        return self._screen

    @screen.setter
    def screen(self, value):
        self._screen = value

    #GT pro atributo de font
    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, value):
        self._font = value

    
    @property
    def over_font(self):
        return self._over_font

    @over_font.setter
    def over_font(self, value):
        self._over_font = value

    
    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, value):
        self._background = value

    #Mostra tela de game over
    def display(self, score_value, save_score_callback):
        mixer.music.pause() 
        save_score_callback()
        while True:
            self._screen.blit(self._background, (0, 0))  

            over_text = self._over_font.render("GAME OVER", True, (219, 2, 2))
            restart_text = self._font.render("Pressione R para voltar ao menu", True, (255, 255, 255))

            
            over_text_rect = over_text.get_rect(center=(self._screen.get_width() // 2, self._screen.get_height() // 2 - 50))
            self._screen.blit(over_text, over_text_rect)

            
            restart_text_rect = restart_text.get_rect(center=(self._screen.get_width() // 2, self._screen.get_height() // 2 + 50))
            self._screen.blit(restart_text, restart_text_rect)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        mixer.music.stop()  
                        return  