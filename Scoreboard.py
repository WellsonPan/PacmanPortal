import pygame
from pygame.sprite import Group
from Pacman import Pacman

class Scoreboard():
    def __init__(self, pacSettings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.pacSettings = pacSettings

        self.text_color = (230, 230, 230)
        self.font = pygame.font.SysFont(None, 48)

        self.file = open("files/highScores.txt", "r")
        self.high = int(self.file.read())
        self.file.close()

        self.prep_score()
        self.prep_high_score(self.high)
        self.prep_ships()

    def prep_score(self):
        rounded_score = int(self.pacSettings.score)
        score_str = "Score: {:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.pacSettings.backgroundColor)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.bottom = self.screen_rect.bottom

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        # self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def prep_high_score(self, highScore):
        high_score = int(highScore)
        high_score_str = "High Score: {:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.pacSettings.backgroundColor)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.bottom = self.score_rect.bottom
        
    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.pacSettings.livesLeft):
            ship = Pacman(self.pacSettings, self.screen)
            ship.rect.x = 10 + ship_number * (ship.rect.width * 3)
            ship.rect.y = self.screen_rect.bottom - 50
            self.ships.add(ship)