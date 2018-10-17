import pygame
from Maze import Maze
from Settings import Settings
from EventLoop import EventLoop
from Pacman import Pacman
from Pacman import PacmanRight
from Pacman import PacmanLeft
from Pacman import PacmanUp
from Pacman import PacmanDown
from pygame.sprite import Group

class Game():
    def __init__(self, pacSettings):
        pygame.init()

        self.screen = pygame.display.set_mode((pacSettings.screenWidth, pacSettings.screenHeight))
        pygame.display.set_caption("Pacman Portal")

        self.pacman = Pacman(pacSettings, self.screen)
        self.pacmanRight = PacmanRight(pacSettings, self.screen, self.pacman)
        self.pacmanLeft = PacmanLeft(pacSettings, self.screen, self.pacman)
        self.pacmanUp = PacmanUp(pacSettings, self.screen, self.pacman)
        self.pacmanDown = PacmanDown(pacSettings, self.screen, self.pacman)

        self.mazeBound = Group()
        self.barrierBound = Group()
        self.points = Group()

        self.maze = Maze(pacSettings, self.screen, "images/pacmanportalmaze.txt", "Block", "hPortal", "shield", "pill", self.mazeBound, self.barrierBound, self.points)

    def play(self):
        eloop = EventLoop(finished=False)

        while not eloop.finished:
            eloop.checkEvents(self)
            eloop.checkWallCollision(self, self.pacmanRight, self.pacmanLeft, self.pacmanUp, self.pacmanDown, self.mazeBound, self.barrierBound)
            eloop.scoring(pacSettings, self.pacman, self.pacmanLeft, self.pacmanRight, self.pacmanUp, self.pacmanDown, self.points)
            eloop.levelComplete(self.pacman, self.pacmanLeft, self.pacmanRight, self.pacmanUp, self.pacmanDown, self.maze, self.points)
            self.updateScreen()
            self.pacman.update()
            self.pacmanRight.update()
            self.pacmanLeft.update()
            self.pacmanUp.update()
            self.pacmanDown.update()

    def updateScreen(self):
        self.screen.fill((0, 0, 0))
        self.maze.blitme(self.mazeBound, self.barrierBound, self.points)
        self.pacman.drawPacman()
        # self.pacmanRight.drawRight()
        pygame.display.flip()

pacSettings = Settings()
game = Game(pacSettings)
game.play()