import pygame
from pygame.sprite import Sprite
from Node import Node

class Ghost(Sprite):
    def __init__(self, pacSettings, screen):
        super(Ghost, self).__init__()
        self.pacSettings = pacSettings
        self.screen = screen
        self.screenRect = screen.get_rect()
        self.image = pygame.image.load("images/blinkyBody.png")
        self.image = pygame.transform.scale(self.image, (24, 24))
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (36, 36))

        self.currentNode = None

        self.rect.centerx = self.screenRect.centerx
        self.rect.centery = self.screenRect.centery - 20

        self.direction = None

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.graph = {'aA': {'aC': "right", 'bA': "down"},
                 'aC': {'aA': "left", 'aE': "right", 'bC': "down"},
                 'aE': {'aC': "left", 'bE': "down"},
                 'aG': {'aI': "right", 'bG': "down"},
                 'aI': {'aG': "left", 'aK': "right", 'bI': "down"},
                 'aK': {'aI': "left", 'bK': "down"},

                 'bA': {'aA': "up", 'bC': "right", 'cA': "down"},
                 'bC': {'bA': "left", 'aC': "up", 'bD': "right", 'cC': "down"},
                 'bD': {'bC': "left", 'bE': "right", 'cD': "down"},
                 'bE': {'bD': "left", 'aE': "up", 'bG': "right"},
                 'bG': {'bE': "left", 'aG': "up", 'bH': "right"},
                 'bH': {'bG': "left", 'bI': "right", 'cH': "down"},
                 'bI': {'bH': "left", 'aI': "up", 'bK': "right", 'cI': "down"},
                 'bK': {'aK': "up", 'bI': "left", 'cK': "down"},

                 'cA': {'bA': "up", 'cC': "right"},
                 'cC': {'cA': "left", 'bC': "up", 'fC': "down"},
                 'cD': {'bD': "up", 'cE': "right"},
                 'cE': {'cD': "left", 'dE': "down"},
                 'cG': {'cH': "right", 'dG': "down"},
                 'cH': {'cG': "left", 'bH': "up"},
                 'cI': {'bH': "up", 'cK': "right", 'fI': "down"},
                 'cK': {'cI': "left", 'bK': "up"},

                 'dD': {'dE': "right", 'fD': "down"},
                 'dE': {'dD': "left", 'cE': "up", 'dF': "right"},
                 'dF': {'dE': "left", 'dG': "right", 'gF': "down"},
                 'dG': {'dF': "left", 'cG': "up", 'dH': "right"},
                 'dH': {'dG': "left", 'fH': "down"},

                 'eE': {'fE': "down"},
                 'eG': {'fG': "down"},

                 'fA': {'fC': "right"},
                 'fC': {'fA': "left", 'cC': "up", 'fD': "right", 'iC': "down"},
                 'fD': {'fC': "left", 'dD': "up", 'hD': "down"},
                 'fE': {'eE': "up", 'gE': "down"},
                 'fG': {'eG': "left", 'gG': "right"},
                 'fH': {'dH': "up", 'fI': "right", 'hH': "down"},
                 'fI': {'fH': "left", 'cI': "up", 'fK': "right", 'iI': "down"},
                 'fK': {'fI': "left"},

                 'gE': {'fE': "up", 'gF': "right"},
                 'gF': {'gE': "left", 'dF': "up", 'gG': "right"},
                 'gG': {'gF': "left", 'fG': "up"},

                 'hD': {'fD': "up", 'hH': "right", 'iD': "down"},
                 'hH': {'hD': "left", 'fH': "up", 'iH': "down"},

                 'iA': {'iC': "right", 'jA': "down"},
                 'iC': {'iA': "left", 'fC': "up", 'iD': "right", 'jC': "down"},
                 'iD': {'iC': "left", 'hD': "up", 'iE': "right"},
                 'iE': {'iD': "left", 'jE': "down"},
                 'iG': {'iH': "right", 'jG': "down"},
                 'iH': {'iG': "left", 'iI': "right", 'hH': "up"},
                 'iI': {'iH': "left", 'fI': "up", 'iK': "right", 'jI': "down"},
                 'iK': {'iI': "left", 'jK': "down"},

                 'jA': {'iA': "up", 'jB': "right"},
                 'jB': {'jA': "left", 'kB': "down"},
                 'jC': {'iC': "up", 'jD': "right", 'kC': "down"},
                 'jD': {'jC': "left", 'jE': "right", 'kD': "down"},
                 'jE': {'jD': "left", 'iE': "up", 'jF': "right"},
                 'jF': {'jE': "left", 'jG': "right"},
                 'jG': {'jF': "left", 'iG': "up", 'jH': "right"},
                 'jH': {'jG': "left", 'kH': "down", 'jI': "right"},
                 'jI': {'jH': "left", 'iI': "up", 'kI': "down"},
                 'jJ': {'jK': "right", 'kJ': "down"},
                 'jK': {'jJ': "left", 'iK': "up"},

                 'kA': {'kB': "right", 'iA': "up"},
                 'kB': {'kA': "left", 'jB': "up", 'kC': "right"},
                 'kC': {'kB': "left", 'jC': "up"},
                 'kD': {'jD': "up", 'kE': "right"},
                 'kE': {'kD': "left", 'lE': "down"},
                 'kG': {'kH': "right", 'lG': "down"},
                 'kH': {'kG': "left", 'jH': "up"},
                 'kI': {'jI': "up", 'kJ': "right"},
                 'kJ': {'kI': "left", 'jJ': "up", 'kK': "right"},
                 'kK': {'kJ': "left", 'lK': "down"},

                 'lA': {'kA': "up", 'lE': "right"},
                 'lE': {'lA': "left", 'kE': "up", 'lG': "right"},
                 'lG': {'lE': "left", 'kG': "up", 'lK': "right"},
                 'lK': {'lG': "left", 'kK': "up"},
                 }

    def setCurrentNode(self, node):
        self.currentNode = node

    def setDirection(self, nextNode):
        self.direction = self.graph[self.currentNode.key][nextNode]

    def setDirection2(self, direct):
        self.direction = direct

    def update(self):
        if self.direction == "right":
            self.centerx += self.pacSettings.ghostSpeed
        elif self.direction == "left":
            self.centerx -= self.pacSettings.ghostSpeed
        elif self.direction == "up":
            self.centery -= self.pacSettings.ghostSpeed
        elif self.direction == "down":
            self.centery += self.pacSettings.ghostSpeed
        else:
            self.centerx += 0
            self.centery += 0

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def reverse(self, direct):
        if direct == "right":
            self.direction = "left"
        if direct == "left":
            self.direction = "right"
        if direct == "up":
            self.direction = "down"
        if direct == "down":
            self.direction = "up"

    def resetPos(self):
        self.currentNode = None
        self.direction = None
        self.rect.centerx = self.screenRect.centerx
        self.rect.centery = self.screenRect.centery - 20

    def blit(self):
        self.screen.blit(self.image, self.rect)