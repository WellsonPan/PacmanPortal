import pygame
from pygame.sprite import Sprite

class Ghost(Sprite):
    def __init__(self, pacSettings, screen):
        super(Ghost, self).__init__()
        self.pacSettings = pacSettings
        self.screen = screen
        self.screenRect = screen.get_rect()
        self.image = pygame.image.load("images/blinkyBody.png")
        self.image = pygame.transform.scale(self.image, (36, 36))
        self.rect = self.image.get_rect()

        self.rect.center = self.screenRect.center
        self.rect.centery -= 20

    def blit(self):
        self.screen.blit(self.image, self.rect)