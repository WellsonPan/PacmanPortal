import pygame
from ImageRect import ImageRect

class Maze():
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    BRICK_SIZE = 16
    POINT_SIZE = 5
    PILL_SIZE = 9
    def __init__(self, pacSettings, screen, mazefile, brickfile, portalfile, shieldfile, pointfile, mazeBound):#, pillfile):
        self.pacSettings = pacSettings
        self.screen = screen
        self.filename = mazefile
        with open(self.filename, "r") as f:
            self.rows = f.readlines()
        self.brickfile = brickfile

        self.bricks = []
        self.shields = []
        self.hportals = []
        self.vportals = []
        self.pill = []
        self.points = []

        self.bsz = Maze.BRICK_SIZE
        self.psz = Maze.POINT_SIZE

        self.brick = ImageRect(screen, self.brickfile, self.bsz, self.bsz, 0, 0)
        self.deltax = self.deltay = Maze.BRICK_SIZE

        self.portal = ImageRect(screen, portalfile, self.bsz, self.bsz, 0, 0)
        self.sheld = ImageRect(screen, shieldfile, self.bsz, self.bsz, 0, 0)
        self.pts = ImageRect(screen, pointfile, self.psz, self.psz, 0, 0)

        self.build(mazeBound)

    def build(self, mazeBound):
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
                    self.brick2 = ImageRect(self.screen, self.brickfile, self.bsz, self.bsz, ncol * dx, nrow * dy)
                    mazeBound.add(self.brick2)
                elif col == "h":
                    self.hportals.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == "o":
                    self.shields.append(pygame.Rect(ncol * dx, nrow * dy, sw, sh))
                elif col == ",":
                    self.points.append(pygame.Rect(ncol * dx, nrow * dy, pw, ph))
                elif col == "v":
                    self.vportals.append(pygame.Rect(ncol * dx, nrow * dy, w, h))

    def blitme(self):
        for pt in self.points:
            self.screen.blit(self.pts.image, pt)
        for rect in self.bricks:
            self.screen.blit(self.brick.image, rect)
        for hport in self.hportals:
            self.screen.blit(self.portal.image, hport)
        for shild in self.shields:
            self.screen.blit(self.sheld.image, shild)
        for vport in self.vportals:
            self.screen.blit(self.portal.image, vport)