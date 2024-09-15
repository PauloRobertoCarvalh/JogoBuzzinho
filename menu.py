import pygame
import sys

class Menu:
    def __init__(self):
        # Inicializa o pygame
        pygame.init()

        # Atributos privados para a tela e fontes
        self._screen = pygame.display.set_mode((800, 600))
        self._background = pygame.image.load('Imagem/FUNDOMENU.jpg')

        # Atributos para fontes
        self._title_font = pygame.font.Font('fonte/SuperCaramel.ttf', 75)  # Fonte maior para o título
        self._option_font = pygame.font.Font('fonte/SuperCaramel.ttf', 40)  # Fonte maior para as opções

        # Atributos para imagens de personagens
        self._buzz_image = pygame.image.load('Imagem/buzzcerto.png')
        self._woody_image = pygame.image.load('Imagem/woodycerto.png')

    # Getters e setters para o fundo
    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, path):
        self._background = pygame.image.load(path)

    # Getters e setters para o título
    @property
    def title_font(self):
        return self._title_font

    @title_font.setter
    def title_font(self, font_path, size):
        self._title_font = pygame.font.Font(font_path, size)

    # Getters e setters para as opções
    @property
    def option_font(self):
        return self._option_font

    @option_font.setter
    def option_font(self, font_path, size):
        self._option_font = pygame.font.Font(font_path, size)

    # Getters e setters para as imagens dos personagens
    @property
    def buzz_image(self):
        return self._buzz_image

    @buzz_image.setter
    def buzz_image(self, path):
        self._buzz_image = pygame.image.load(path)

    @property
    def woody_image(self):
        return self._woody_image

    @woody_image.setter
    def woody_image(self, path):
        self._woody_image = pygame.image.load(path)

    def show_menu(self):
        selected_character = None

        while selected_character is None:
            
            self._screen.blit(self._background, (0, 0))

            
            title_text = self._title_font.render("B U Z Z I N H O", True, (0, 0, 0))
            title_rect = title_text.get_rect(center=(self._screen.get_width() // 2, self._screen.get_height() // 2 - 200))
            self._screen.blit(title_text, title_rect)

            
            choose_text = self._option_font.render("Escolha seu personagem:", True, (0, 0, 0))
            choose_rect = choose_text.get_rect(center=(self._screen.get_width() // 2, self._screen.get_height() // 2 - 80))
            self._screen.blit(choose_text, choose_rect)

            #imagem dos personagens
            buzz_rect = self._buzz_image.get_rect(center=(self._screen.get_width() // 2 - 100, self._screen.get_height() // 2 + 40))
            woody_rect = self._woody_image.get_rect(center=(self._screen.get_width() // 2 + 100, self._screen.get_height() // 2 + 40))
            self._screen.blit(self._buzz_image, buzz_rect)
            self._screen.blit(self._woody_image, woody_rect)

            
            scores_text = self._option_font.render("Ver Scores", True, (0, 0, 0))
            scores_rect = scores_text.get_rect(center=(self._screen.get_width() // 2, self._screen.get_height() // 2 + 150))
            self._screen.blit(scores_text, scores_rect)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if buzz_rect.collidepoint(event.pos):
                        selected_character = 'buzz'
                    elif woody_rect.collidepoint(event.pos):
                        selected_character = 'woody'
                    elif scores_rect.collidepoint(event.pos):
                        self.view_scores_screen()  

        return selected_character

    def view_scores_screen(self):
        with open("log.txt", "r") as file:
            scores = file.readlines()

        viewing_scores = True
        while viewing_scores:
            self._screen.fill((0, 0, 0))
            y_offset = 80

            title_text = self._title_font.render("S C O R E S", True, (255, 255, 255))
            title_rect = title_text.get_rect(center=(self._screen.get_width() // 2, 50))
            self._screen.blit(title_text, title_rect)

            for line in scores:
                score_text = self._option_font.render(line.strip(), True, (255, 255, 255))
                self._screen.blit(score_text, (50, y_offset))
                y_offset += 40

            back_text = self._option_font.render("Pressione B para voltar", True, (255, 255, 255))
            self._screen.blit(back_text, (50, y_offset + 40))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_b:
                        viewing_scores = False  


if __name__ == "__main__":
    menu = Menu()
    selected_character = menu.show_menu()