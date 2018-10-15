import pygame
from pygame.sprite import Sprite

class Pacman(Sprite):
    def __init__(self, pacSettings, screen):
        super(Pacman, self).__init__()
        self.pacSettings = pacSettings
        self.screen = screen
        self.screenRect = screen.get_rect()
        self.color = pacSettings.pacmanColor
        self.rect = pygame.Rect(0, 0, int(self.pacSettings.pacmanRad / 3), int(self.pacSettings.pacmanRad / 3))
        self.rect.center = self.screenRect.center
        self.rect.centery -= 115

        self.movingLeft = False
        self.movingRight = False
        self.movingUp = False
        self.movingDown = False

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def update(self):
        if self.movingLeft == True:
            self.centerx -= self.pacSettings.pacmanSpeed
        elif self.movingRight == True:
            self.centerx += self.pacSettings.pacmanSpeed
        elif self.movingUp == True:
            self.centery -= self.pacSettings.pacmanSpeed
        elif self.movingDown == True:
            self.centery += self.pacSettings.pacmanSpeed

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery


    def drawPacman(self):
        pygame.draw.circle(self.screen, self.color, self.rect.center, int(self.pacSettings.pacmanRad / 1.8))


class PacmanRight(Sprite):
    def __init__(self, pacSettings, screen, Pacman):
        super(PacmanRight, self).__init__()
        self.pacSettings = pacSettings
        self.screen = screen
        self.screenRect = screen.get_rect()
        self.pacman = Pacman
        self.rect = pygame.Rect(0, 0, int(self.pacSettings.pacmanRad / 3), int(self.pacSettings.pacmanRad / 3))
        self.rect.center = self.pacman.rect.center
        self.rect.centerx += int(self.pacSettings.pacmanRad / 3)

        self.movingLeft = False
        self.movingRight = False
        self.movingUp = False
        self.movingDown = False

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def update(self):
        if self.movingLeft == True:
            self.centerx -= self.pacSettings.pacmanSpeed
        elif self.movingRight == True:
            self.centerx += self.pacSettings.pacmanSpeed
        elif self.movingUp == True:
            self.centery -= self.pacSettings.pacmanSpeed
        elif self.movingDown == True:
            self.centery += self.pacSettings.pacmanSpeed

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    # def drawRight(self):
    #     pygame.draw.circle(self.screen, (255, 0, 0), self.rect.center, int(self.pacSettings.pacmanRad / 1.8))


class PacmanLeft(Sprite):
    def __init__(self, pacSettings, screen, Pacman):
        super(PacmanLeft, self).__init__()
        self.pacSettings = pacSettings
        self.screen = screen
        self.screenRect = screen.get_rect()
        self.pacman = Pacman
        self.rect = pygame.Rect(0, 0, int(self.pacSettings.pacmanRad / 3), int(self.pacSettings.pacmanRad / 3))
        self.rect.center = self.pacman.rect.center
        self.rect.centerx -= int(self.pacSettings.pacmanRad / 3)

        self.movingLeft = False
        self.movingRight = False
        self.movingUp = False
        self.movingDown = False

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def update(self):
        if self.movingLeft == True:
            self.centerx -= self.pacSettings.pacmanSpeed
        elif self.movingRight == True:
            self.centerx += self.pacSettings.pacmanSpeed
        elif self.movingUp == True:
            self.centery -= self.pacSettings.pacmanSpeed
        elif self.movingDown == True:
            self.centery += self.pacSettings.pacmanSpeed

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery


class PacmanUp(Sprite):
    def __init__(self, pacSettings, screen, Pacman):
        super(PacmanUp, self).__init__()
        self.pacSettings = pacSettings
        self.screen = screen
        self.screenRect = screen.get_rect()
        self.pacman = Pacman
        self.rect = pygame.Rect(0, 0, int(self.pacSettings.pacmanRad / 3), int(self.pacSettings.pacmanRad / 3))
        self.rect.center = self.pacman.rect.center
        self.rect.centery -= int(self.pacSettings.pacmanRad / 3)

        self.movingLeft = False
        self.movingRight = False
        self.movingUp = False
        self.movingDown = False

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def update(self):
        if self.movingLeft == True:
            self.centerx -= self.pacSettings.pacmanSpeed
        elif self.movingRight == True:
            self.centerx += self.pacSettings.pacmanSpeed
        elif self.movingUp == True:
            self.centery -= self.pacSettings.pacmanSpeed
        elif self.movingDown == True:
            self.centery += self.pacSettings.pacmanSpeed

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery