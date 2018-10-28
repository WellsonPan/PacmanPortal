import pygame
from Maze import Maze
from Settings import Settings
import EventLoop as eloop
from Pacman import Pacman
from Pacman import PacmanRight
from Pacman import PacmanLeft
from Pacman import PacmanUp
from Pacman import PacmanDown
from pygame.sprite import Group
from pygame.sprite import GroupSingle
from Ghost import Ghost
from Button import Button, highScore
from Start import Start
from Node import Node

class Game():
    def __init__(self, pacSettings):
        pygame.init()

        self.pacSettings = pacSettings
        self.screen = pygame.display.set_mode((self.pacSettings.screenWidth, self.pacSettings.screenHeight))
        pygame.display.set_caption("Pacman Portal")
        self.playButton = Button(self.pacSettings, self.screen, "Play Game")
        self.highScoreButton = highScore(self.pacSettings, self.screen, "High Scores")
        self.startScreen = Start(self.pacSettings, self.screen)

        self.pacman = Pacman(self.pacSettings, self.screen)
        self.pacmanRight = PacmanRight(self.pacSettings, self.screen, self.pacman)
        self.pacmanLeft = PacmanLeft(self.pacSettings, self.screen, self.pacman)
        self.pacmanUp = PacmanUp(self.pacSettings, self.screen, self.pacman)
        self.pacmanDown = PacmanDown(self.pacSettings, self.screen, self.pacman)

        self.mazeBound = Group()
        self.barrierBound = Group()
        self.points = Group()
        self.portals = GroupSingle()
        self.portals2 = GroupSingle()
        self.laser = GroupSingle()
        self.laser2 = GroupSingle()
        self.nodes = Group()
        self.nodeDetectors = Group()

        self.ghost = Ghost(self.pacSettings, self.screen)

        self.maze = Maze(self.pacSettings, self.screen, "images/pacmanportalmaze.txt", "Block", "hPortal", "shield", "Point", "Node", self.mazeBound, self.barrierBound, self.points, self.nodes)

    def play(self):
        while True:
            eloop.checkEvents(self, self.pacSettings, self.laser, self.laser2, self.playButton, self.highScoreButton, self.nodeDetectors)
            if self.pacSettings.gameActive and not self.pacSettings.highScores:
                eloop.checkWallCollision(self, self.pacmanRight, self.pacmanLeft, self.pacmanUp, self.pacmanDown, self.mazeBound, self.barrierBound)
                eloop.scoring(self.pacSettings, self.pacman, self.pacmanLeft, self.pacmanRight, self.pacmanUp, self.pacmanDown, self.points)
                eloop.levelComplete(self.pacman, self.pacmanLeft, self.pacmanRight, self.pacmanUp, self.pacmanDown, self.maze, self.points)
                eloop.portalWallCollision(self, self.laser, self.laser2, self.portals, self.portals2, self.mazeBound)
                eloop.pacmanPortalCollision(self.pacSettings, self.pacman, self.pacmanLeft, self.pacmanRight, self.pacmanUp, self.pacmanDown, self.portals, self.portals2)
                eloop.nextNodeDetection(self.pacman, self.mazeBound, self.nodes, self.nodeDetectors)
                eloop.checkGhostNodeCollision(self.ghost, self.nodes)
                # eloop.checkPacmanNodeCollision(self.pacman, self.ghost, self.nodes)
                eloop.ghostRouting(self.pacman, self.pacmanLeft, self.pacmanRight, self.pacmanUp, self.pacmanDown, self.ghost, self.nodes)
                self.updateScreen()
                self.pacman.update()
                self.pacmanRight.update()
                self.pacmanLeft.update()
                self.pacmanUp.update()
                self.pacmanDown.update()
                self.laser.update()
                self.laser2.update()
                self.ghost.update()
                self.nodeDetectors.update()
            elif not self.pacSettings.highScores and not self.pacSettings.gameActive:
                self.screen.fill((0, 0, 0))
                self.startScreen.printStart()
                self.playButton.draw_button()
                self.highScoreButton.draw_button()
                pygame.display.flip()
            elif self.pacSettings.highScores and not self.pacSettings.gameActive:
                eloop.printHighScores(self.screen)



    def updateScreen(self):
        self.screen.fill((0, 0, 0))
        self.maze.blitme(self.mazeBound, self.barrierBound, self.points, self.nodes)
        for lase in self.laser.sprites():
            lase.drawLaser()
        for lase in self.laser2.sprites():
            lase.drawLaser()
        for portal in self.portals.sprites():
            portal.drawPortal()
        for portal in self.portals2.sprites():
            portal.drawPortal()
        for nod in self.nodeDetectors.sprites():
            nod.drawNode()
        self.pacman.drawPacman()
        self.ghost.blit()
        # self.pacmanRight.drawRight()
        pygame.display.flip()

pacSettings = Settings()
game = Game(pacSettings)
game.play()