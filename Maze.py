import pygame
from ImageRect import ImageRect

class Maze():
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    BRICK_SIZE = 16
    POINT_SIZE = 9
    PILL_SIZE = 12
    def __init__(self, pacSettings, screen, mazefile, brickfile, portalfile, shieldfile, pointfile, mazeBound, barrierBound, points):#, pillfile):
        self.pacSettings = pacSettings
        self.screen = screen
        self.filename = mazefile
        with open(self.filename, "r") as f:
            self.rows = f.readlines()
        self.brickfile = brickfile
        self.shieldfile = shieldfile
        self.pointfile = pointfile

        self.hportals = []
        self.vportals = []
        self.pill = []

        self.bsz = Maze.BRICK_SIZE
        self.psz = Maze.POINT_SIZE

        self.brick = ImageRect(screen, self.brickfile, self.bsz, self.bsz, 0, 0)
        self.deltax = self.deltay = Maze.BRICK_SIZE

        self.portal = ImageRect(screen, portalfile, self.bsz, self.bsz, 0, 0)
        self.sheld = ImageRect(screen, shieldfile, self.bsz, self.bsz, 0, 0)
        self.pts = ImageRect(screen, pointfile, self.psz, self.psz, 0, 0)

        self.build(mazeBound, barrierBound, points)

    def build(self, mazeBound, barrierBound, points):
        r = self.brick.rect
        w, h = r.width, r.height
        self.dx, self.dy = self.deltax, self.deltay

        shield = self.sheld.rect
        sw, sh = shield.width, shield.height

        point = self.pts.rect
        pw, ph = point.width, point.height

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == "X":
                    # self.bricks.append(pygame.Rect(ncol * self.dx, nrow * self.dy, w, h))
                    self.brick2 = ImageRect(self.screen, self.brickfile, self.bsz, self.bsz, ncol * self.dx, nrow * self.dy)
                    mazeBound.add(self.brick2)
                elif col == "h":
                    self.hportals.append(pygame.Rect(ncol * self.dx, nrow * self.dy, w, h))
                elif col == "o":
                    # self.shields.append(pygame.Rect(ncol * self.dx, nrow * self.dy, sw, sh))
                    self.shield2 = ImageRect(self.screen, self.shieldfile, self.bsz, self.bsz, ncol * self.dx, nrow * self.dy)
                    barrierBound.add(self.shield2)
                elif col == ",":
                    # self.points.append(pygame.Rect(ncol * self.dx, nrow * self.dy, pw, ph))
                    self.point = ImageRect(self.screen, self.pointfile, self.psz, self.psz, ncol * self.dx, nrow * self.dy)
                    points.add(self.point)
                elif col == "v":
                    self.vportals.append(pygame.Rect(ncol * self.dx, nrow * self.dy, w, h))

    def blitme(self, mazeBound, barrierBound, points):
        for pt in points.sprites():
            self.screen.blit(self.pts.image, pt)
        for rect in mazeBound.sprites():
            self.screen.blit(self.brick.image, rect)
        for hport in self.hportals:
            self.screen.blit(self.portal.image, hport)
        for shild in barrierBound.sprites():
            self.screen.blit(self.sheld.image, shild)
        for vport in self.vportals:
            self.screen.blit(self.portal.image, vport)
            
    def resetMaze(self, points):
        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == ",":
                    # self.points.append(pygame.Rect(ncol * self.dx, nrow * self.dy, pw, ph))
                    self.point = ImageRect(self.screen, self.pointfile, self.psz, self.psz, ncol * self.dx, nrow * self.dy)
                    points.add(self.point)