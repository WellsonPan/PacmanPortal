import pygame
from pygame.sprite import Sprite

class Ghost(Sprite):
    def __init__(self, pacSettings, screen):
        super(Ghost, self).__init__()
        self.pacSettings = pacSettings
        self.screen = screen
        self.screenRect = screen.get_rect()
