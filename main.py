import pygame
import random
import gameobject
from pygame import mixer
from player import Player
from enemy import Enemy
from enemy2 import EnemyType2
from bullet import Bullet
from menu import Menu  


class Buzzinho(gameobject.GameObject):
    def __init__(self):
        pygame.init()

        self._screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Buzzinho")
        self._background = pygame.image.load('Imagem/fundojogo.png')
        self._game_over_background = pygame.image.load('Imagem/fundogameover.png')

        self._font = pygame.font.Font('fonte/SuperCaramel.ttf', 32)
        self._over_font = pygame.font.Font('fonte/pixel.ttf', 64)
        mixer.music.load("Audio/spacesound.mp3")

        self._selected_character = None
        self._score_value = 0

        self._menu = Menu()

    
        self.bullets = []  # Lista de balas Woody

    @property
    def selected_character(self):
        return self._selected_character

    @selected_character.setter
    def selected_character(self, character):
        self._selected_character = character

    @property
    def score_value(self):
        return self._score_value

    @score_value.setter
    def score_value(self, value):
        if value >= 0:
            self._score_value = value
        else:
            raise ValueError("O valor da pontuação não pode ser negativo")

    # Salva pontuação, da primeira jogada -> ultima
    def save_score(self):
        try:
            with open("log.txt", "a") as file:
                if self._score_value > 0:
                    file.write(f"Score: {self._score_value}, {self._selected_character}\n")
        except IOError as e:
            print(f"Erro ao salvar o score: {e}")

    def show_score(self, x, y):
        score = self._font.render("Score : " + str(self._score_value), True, (255, 255, 255))
        self._screen.blit(score, (x, y))

    def view_scores_screen(self):
        try:
            with open("log.txt", "r") as file:
                scores = file.readlines()

            viewing_scores = True
            while viewing_scores:
                self._screen.fill((0, 0, 0))
                y_offset = 50

                for line in scores:
                    score_text = self._font.render(line.strip(), True, (255, 255, 255))
                    self._screen.blit(score_text, (50, y_offset))
                    y_offset += 40

                back_text = self._font.render("Pressione B para voltar", True, (255, 255, 255))
                self._screen.blit(back_text, (50, y_offset + 40))

                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_b:
                            viewing_scores = False  
        except IOError as e:
            print(f"Erro ao ler o arquivo de scores: {e}")

    
    def game_over_screen(self):
        mixer.music.pause()  
        self.save_score()  
        while True:
            self._screen.blit(self._game_over_background, (0, 0)) 

            over_text = self._over_font.render("GAME OVER", True, (219, 2, 2))
            restart_text = self._font.render("Pressione R para voltar ao menu", True, (255, 255, 255))

            
            over_text_rect = over_text.get_rect(center=(self._screen.get_width() // 2, self._screen.get_height() // 2 - 100))
            self._screen.blit(over_text, over_text_rect)

            
            restart_text_rect = restart_text.get_rect(center=(self._screen.get_width() // 2, self._screen.get_height() // 2 + 150))
            self._screen.blit(restart_text, restart_text_rect)

            #Verificamos se o jogador pontuou ou não
            if self._score_value == 0:
                no_score_text = self._font.render("Você não pontuou,seu score foi: 0", True, (219, 2, 2))
                no_score_text_rect = no_score_text.get_rect(center=(self._screen.get_width() // 2, self._screen.get_height() // 2 + 100))
                self._screen.blit(no_score_text, no_score_text_rect)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        mixer.music.stop() 
                        return  
                          

    # Lógica do jogo
    def game(self):
        self._score_value = 0
        try:
            mixer.music.play(-1)

           #Seleção dos personagens
            if self._selected_character == 'buzz':
                player_image = 'Imagem/buzzcerto.png'
            else:
                player_image = 'Imagem/woodycerto.png'

            player = Player(370, 480, player_image)

            
            enemies = [Enemy(random.randint(0, 736), random.randint(50, 150), 5.0, 15) for _ in range(5)]
            enemy_size = enemies[0].image.get_size()
            enemies2 = [EnemyType2(random.randint(0, 736), random.randint(50, 150), 3.0, 15, enemy_size) for _ in range(6)]

            
            if self._selected_character == 'buzz':
                bullet = Bullet(0, 480, 20) 
            else:
                self.bullets = [Bullet(0, 480, 13), Bullet(0, 480, 13)]

            running = True
            while running:
                self._screen.fill((0, 0, 0))
                self._screen.blit(self._background, (0, 0))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            player.set_x_change(-8)
                        if event.key == pygame.K_RIGHT:
                            player.set_x_change(8)
                        if event.key == pygame.K_SPACE:
                            if self._selected_character == 'buzz' and bullet.state == "ready":
                                bulletSound = mixer.Sound("Audio/laser.wav")
                                bulletSound.play()
                                bullet.fire(player.x)
                            elif self._selected_character == 'woody' and self.bullets[0].state == "ready":
                                bulletSound = mixer.Sound("Audio/laser.wav")
                                bulletSound.play()
                                self.bullets[0].fire(player.x - 10)  
                                self.bullets[1].fire(player.x + 10)  

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                            player.set_x_change(0)

                player.move()
                player.draw(self._screen)

                
                for enemy in enemies:
                    enemy.move()
                    if self._selected_character == 'buzz' and bullet.is_collision(enemy):
                        explosionSound = mixer.Sound("Audio/explosion1.mp3")
                        explosionSound.play()
                        bullet.y = 480
                        bullet.state = "ready"
                        self._score_value += 1
                        enemy.reset_position()

                    enemy.draw(self._screen)

                for enemy2 in enemies2:
                    enemy2.move()
                    if self._selected_character == 'buzz' and bullet.is_collision(enemy2):
                        explosionSound = mixer.Sound("Audio/explosion1.mp3")
                        explosionSound.play()
                        bullet.y = 480
                        bullet.state = "ready"
                        self._score_value += 2
                        enemy2.reset_position()

                    enemy2.draw(self._screen)


                if self._selected_character == 'woody':
                    for bullet in self.bullets:
                        bullet.move()
                        bullet.draw(self._screen)

                        for enemy in enemies + enemies2:
                            if bullet.is_collision(enemy,):
                                explosionSound = mixer.Sound("Audio/explosion1.mp3")
                                explosionSound.play()
                                bullet.y = 480
                                bullet.state = "ready"
                                self._score_value += 1 if isinstance(enemy, Enemy) else 2
                                enemy.reset_position()

                #colisão poder
                for enemy in enemies + enemies2:
                    if enemy.power.is_collision(player): 
                        running = False 
                        break

                if not running:
                    self.game_over_screen()
                    return

        
                else:
                    bullet.move()
                    bullet.draw(self._screen)

                self.show_score(10, 10)
                pygame.display.update()

        except pygame.error as e:
            print(f"Erro durante o jogo: {e}")
            exit()


        clock = pygame.time.Clock()
        clock.tick(60)     

    def run(self):
        while True:
            try:
                self.selected_character = self._menu.show_menu()
                if self.selected_character == 'view_scores':
                    self.view_scores_screen() 
                else:
                    self.game()  #Iniciação jogo personagem escolhido
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")
                exit()


if __name__ == "__main__":
    try:
        game_instance = Buzzinho()
        game_instance.run()
    except Exception as e:
        print(f"Erro ao iniciar o jogo: {e}")
        exit()