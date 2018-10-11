import pygame
from ImageRect import ImageRect
from Pacman import Pacman

class Maze():
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    BRICK_SIZE = 16
    POINT_SIZE = 5
    PILL_SIZE = 9
    def __init__(self, pacSettings, screen, mazefile, brickfile, portalfile, shieldfile, pointfile):#, pillfile):
        self.pacSettings = pacSettings
        self.screen = screen
        self.filename = mazefile
        with open(self.filename, "r") as f:
            self.rows = f.readlines()

        self.bricks = []
        self.shields = []
        self.hportals = []
        self.vportals = []
        self.pill = []
        self.points = []

        bsz = Maze.BRICK_SIZE
        psz = Maze.POINT_SIZE

        self.brick = ImageRect(screen, brickfile, bsz, bsz)
        self.deltax = self.deltay = Maze.BRICK_SIZE

        self.portal = ImageRect(screen, portalfile, bsz, bsz)
        self.sheld = ImageRect(screen, shieldfile, bsz, bsz)
        self.pts = ImageRect(screen, pointfile, psz, psz)

        self.pacman = Pacman(self.pacSettings, self.screen)

        self.build()

    def build(self):
        r = self.brick.rect
        w, h = r.width, r.height
        dx, dy = self.deltax, self.deltay

        shield = self.sheld.rect
        sw, sh = shield.width, shield.height

        point = self.pts.rect
        pw, ph = point.width, point.height

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == "X":
                    self.bricks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == "h":
                    self.hportals.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == "o":
                    self.shields.append(pygame.Rect(ncol * dx, nrow * dy, sw, sh))
                elif col == ",":
                    self.points.append(pygame.Rect(ncol * dx, nrow * dy, pw, ph))

    def blitme(self):
        for pt in self.points:
            self.screen.blit(self.pts.image, pt)
        self.pacman.drawPacman()
        for rect in self.bricks:
            self.screen.blit(self.brick.image, rect)
        for port in self.hportals:
            self.screen.blit(self.portal.image, port)