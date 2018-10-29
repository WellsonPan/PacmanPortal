import pygame
from Portal import nodeDetector

class DetectionController():
    def __init__(self, game):
        self.game = game

        self.detect = False

    def update(self, nodeDetectors):
        if self.detect:
            nod = nodeDetector(self.game.pacSettings, self.game.screen, self.game.pacman)
            nodeDetectors.add(nod)