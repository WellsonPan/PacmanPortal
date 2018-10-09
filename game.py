import pygame
from Maze import Maze
from Settings import Settings
from EventLoop import EventLoop

class Game():
    def __init__(self, pacSettings):
        pygame.init()

        self.screen = pygame.display.set_mode((pacSettings.screenWidth, pacSettings.screenHeight))
        pygame.display.set_caption("Pacman Portal")

        self.maze = Maze(self.screen,"images/pacmanportalmaze.txt", "square")

    def play(self):
        eloop = EventLoop(finished=False)

        while not eloop.finished:
            eloop.checkEvents()
            self.updateScreen()

    def updateScreen(self):
        self.screen.fill((0, 0, 0))
        self.maze.blitme()
        pygame.display.flip()

pacSettings = Settings()
game = Game(pacSettings)
game.play()