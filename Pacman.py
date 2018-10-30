import pygame
from pygame.sprite import Sprite
from timer import Timer

class Pacman(Sprite):
    def __init__(self, pacSettings, screen):
        super(Pacman, self).__init__()
        self.pacSettings = pacSettings
        self.screen = screen
        self.screenRect = screen.get_rect()
        #self.color = pacSettings.pacmanColor
        self.color = (0, 255, 0)
        self.rect = pygame.Rect(0, 0, int(self.pacSettings.pacmanRad / 3), int(self.pacSettings.pacmanRad / 3))
        self.rect.center = self.screenRect.center
        self.rect.centery += 183
        self.rect.centerx += 15

        self.movingLeft = False
        self.movingRight = False
        self.movingUp = False
        self.movingDown = False

        self.picListRight = ["images/PacmanClose.png", "images/PacmanHalfRight.png", "images/PacmanOpenRight.png",
                             "images/PacmanHalfRight.png"]
        self.picListLeft = ["images/PacmanClose.png", "images/PacmanHalfLeft.png", "images/PacmanOpenLeft.png",
                            "images/PacmanHalfLeft.png"]
        self.picListUp = ["images/PacmanClose.png", "images/PacmanHalfUp.png", "images/PacmanOpenUp.png",
                          "images/PacmanHalfUp.png"]
        self.picListDown = ["images/PacmanClose.png", "images/PacmanHalfDown.png", "images/PacmanOpenDown.png",
                            "images/PacmanHalfDown.png"]
        self.picListStill = ["images/PacmanClose.png"]

        self.image = pygame.image.load("images/PacmanOpenRight.png")
        self.time = Timer(self.picListRight)
        self.time2 = Timer(self.picListLeft)
        self.time3 = Timer(self.picListUp)
        self.time4 = Timer(self.picListDown)
        self.time5 = Timer(self.picListStill)

        self.currentNode = None
        self.nextNode = None

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def setCurrentNode(self, node):
        self.currentNode = node

    def setNextNode(self, node):
        self.nextNode = node

    def update(self):
        if self.movingLeft:
            self.centerx -= self.pacSettings.pacmanSpeed
        elif self.movingRight:
            self.centerx += self.pacSettings.pacmanSpeed
        elif self.movingUp:
            self.centery -= self.pacSettings.pacmanSpeed
        elif self.movingDown:
            self.centery += self.pacSettings.pacmanSpeed

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery


    def drawPacman(self):
        # pygame.draw.circle(self.screen, self.color, self.rect.center, int(self.pacSettings.pacmanRad / 1.8))
        if self.movingRight:
            self.image2 = pygame.image.load(self.time.imagerect())
        elif self.movingLeft:
            self.image2 = pygame.image.load(self.time2.imagerect())
        elif self.movingUp:
            self.image2 = pygame.image.load(self.time3.imagerect())
        elif self.movingDown:
            self.image2 = pygame.image.load(self.time4.imagerect())
        else:
            self.image2 = pygame.image.load(self.time5.imagerect())

        self.image2 = pygame.transform.scale(self.image2, (46, 46))
        self.newRect = self.image2.get_rect()
        self.newRect.center = self.rect.center
        self.screen.blit(self.image2, self.newRect)

    def resetPos(self):
        self.centerx = self.screenRect.centerx + 15
        self.centery = self.screenRect.centery + 183


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


    def resetPos(self):
        self.centery = self.pacman.centery
        self.centerx = self.pacman.centerx
        self.centerx += int(self.pacSettings.pacmanRad / 3)


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

    def resetPos(self):
        self.centery = self.pacman.centery
        self.centerx = self.pacman.centerx
        self.centerx -= int(self.pacSettings.pacmanRad / 3)


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

    def resetPos(self):
        self.centery = self.pacman.centery
        self.centerx = self.pacman.centerx
        self.centery -= int(self.pacSettings.pacmanRad / 3)


class PacmanDown(Sprite):
    def __init__(self, pacSettings, screen, Pacman):
        super(PacmanDown, self).__init__()
        self.pacSettings = pacSettings
        self.screen = screen
        self.screenRect = screen.get_rect()
        self.pacman = Pacman
        self.rect = pygame.Rect(0, 0, int(self.pacSettings.pacmanRad / 3), int(self.pacSettings.pacmanRad / 3))
        self.rect.center = self.pacman.rect.center
        self.rect.centery += int(self.pacSettings.pacmanRad / 3)

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

    def resetPos(self):
        self.centery = self.pacman.centery
        self.centerx = self.pacman.centerx
        self.centery += int(self.pacSettings.pacmanRad / 3)