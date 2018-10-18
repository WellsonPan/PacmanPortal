import pygame
from pygame.sprite import Sprite

class oPortal(Sprite):
    def __init__(self, pacSettings, screen, pacman):
        super(oPortal, self).__init__()
        self.pacSettings = pacSettings
        self.screen = screen
        self.pacman = pacman

        self.image = pygame.image.load("images/hPortal.png")
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.screenRect = self.screen.get_rect()

        self.rect.center = self.pacman.rect.center
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        self.left = self.pacman.movingLeft
        self.right = self.pacman.movingRight
        self.up = self.pacman.movingUp
        self.down = self.pacman.movingDown

    def update(self):
        if self.left:
            self.x -= self.pacSettings.portalSpeed
            self.rect.x = self.x
        if self.right:
            self.x += self.pacSettings.portalSpeed
            self.rect.x = self.x
        if self.up:
            self.y -= self.pacSettings.portalSpeed
            self.rect.y = self.y
        if self.down:
            self.y += self.pacSettings.portalSpeed
            self.rect.y = self.y

    def drawPortal(self):
        self.screen.blit(self.image, self.rect)

    def stop(self):
        if self.left:
            self.x += self.pacSettings.portalSpeed
            self.rect.x = self.x
        if self.right:
            self.x -= self.pacSettings.portalSpeed
            self.rect.x = self.x
        if self.up:
            self.y += self.pacSettings.portalSpeed
            self.rect.y = self.y
        if self.down:
            self.y -= self.pacSettings.portalSpeed
            self.rect.y = self.y


class iPortal(Sprite):
    def __init__(self, pacSettings, screen, pacman):
        super(iPortal, self).__init__()
        self.pacSettings = pacSettings
        self.screen = screen
        self.pacman = pacman

        self.image = pygame.image.load("images/vPortal.png")
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.screenRect = self.screen.get_rect()

        self.rect.center = self.pacman.rect.center
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        self.left = self.pacman.movingLeft
        self.right = self.pacman.movingRight
        self.up = self.pacman.movingUp
        self.down = self.pacman.movingDown

    def update(self):
        if self.left:
            self.x -= self.pacSettings.portalSpeed
            self.rect.x = self.x
        if self.right:
            self.x += self.pacSettings.portalSpeed
            self.rect.x = self.x
        if self.up:
            self.y -= self.pacSettings.portalSpeed
            self.rect.y = self.y
        if self.down:
            self.y += self.pacSettings.portalSpeed
            self.rect.y = self.y

    def drawPortal(self):
        self.screen.blit(self.image, self.rect)

    def stop(self):
        if self.left:
            self.x += self.pacSettings.portalSpeed
            self.rect.x = self.x
        if self.right:
            self.x -= self.pacSettings.portalSpeed
            self.rect.x = self.x
        if self.up:
            self.y += self.pacSettings.portalSpeed
            self.rect.y = self.y
        if self.down:
            self.y -= self.pacSettings.portalSpeed
            self.rect.y = self.y