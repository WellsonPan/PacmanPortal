import pygame

class Pacman():
    def __init__(self, pacSettings, screen):
        self.pacSettings = pacSettings
        self.screen = screen
        self.screenRect = screen.get_rect()
        self.color = pacSettings.pacmanColor
        self.rect = pygame.Rect(0, 0, self.pacSettings.pacmanRad, self.pacSettings.pacmanRad)
        self.rect.center = self.screenRect.center
        self.rect.centery -= 115

        self.movingLeft = False
        self.movingRight = False
        self.movingUp = False
        self.movingDown = False

    # def update(self):
    #     if self.movingLeft == True:


    def drawPacman(self):
        pygame.draw.circle(self.screen, self.color, self.rect.center, self.pacSettings.pacmanRad)