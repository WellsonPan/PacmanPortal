import pygame
from pygame.sprite import Sprite

class Node(Sprite):
    def __init__(self, screen, imagename, height, width, x, y, key):
        super(Node, self).__init__()
        self.screen = screen
        self.key = key
        name = "images/" + imagename + ".png"

        img = pygame.image.load(name)
        img = pygame.transform.scale(img, (height, width))
        self.rect = img.get_rect()
        self.rect.left -= self.rect.width
        self.rect.top -= self.rect.height
        self.image = img
        self.rect.x = x
        self.rect.y = y

    def blit(self):
        self.screen.blit(self.image, self.rect)