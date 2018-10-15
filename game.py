import pygame
from Maze import Maze
from Settings import Settings
from EventLoop import EventLoop
from Pacman import Pacman
from Pacman import PacmanRight
from Pacman import PacmanLeft
from pygame.sprite import Group

class Game():
    def __init__(self, pacSettings):
        pygame.init()

        self.screen = pygame.display.set_mode((pacSettings.screenWidth, pacSettings.screenHeight))
        pygame.display.set_caption("Pacman Portal")

        self.pacman = Pacman(pacSettings, self.screen)
        self.pacmanRight = PacmanRight(pacSettings, self.screen, self.pacman)
        self.pacmanLeft = PacmanLeft(pacSettings, self.screen, self.pacman)

        self.mazeBound = Group()

        self.maze = Maze(pacSettings, self.screen, "images/pacmanportalmaze.txt", "Block", "hPortal", "shield", "pill", self.mazeBound)

    def play(self):
        eloop = EventLoop(finished=False)

        while not eloop.finished:
            eloop.checkEvents(self)
            eloop.checkWallCollision(self, self.pacman, self.pacmanRight, self.pacmanLeft, self.mazeBound)
            self.updateScreen()
            self.pacman.update()
            self.pacmanRight.update()
            self.pacmanLeft.update()

    def updateScreen(self):
        self.screen.fill((0, 0, 0))
        self.maze.blitme()
        self.pacman.drawPacman()
        # self.pacmanRight.drawRight()
        pygame.display.flip()

pacSettings = Settings()
game = Game(pacSettings)
game.play()