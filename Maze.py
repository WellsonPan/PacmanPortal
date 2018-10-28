import pygame
from ImageRect import ImageRect
from Node import Node

class Maze():
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    BRICK_SIZE = 16
    POINT_SIZE = 9
    PILL_SIZE = 12
    NODE_SIZE = 12

    graph = {'aA': {'aC': 8, 'bA': 6},
             'aC': {'aA': 8, 'aE': 10, 'bC': 6},
             'aE': {'aC': 10, 'bE': 6},
             'aG': {'aI': 10, 'bG': 6},
             'aI': {'aG': 10, 'aK': 8, 'bI': 6},
             'aK': {'aI': 8, 'bK': 6},

             'bA': {'aA': 6, 'bC': 8, 'cA': 5},
             'bC': {'bA': 8, 'aC': 6, 'bD': 5, 'cC': 5},
             'bD': {'bC': 5, 'bE': 5, 'cD': 5},
             'bE': {'bD': 5, 'aE': 6, 'bG': 5},
             'bG': {'bE': 5, 'aG': 6, 'bH': 5},
             'bH': {'bG': 5, 'bI': 5, 'cH': 5},
             'bI': {'bH': 5, 'aI': 6, 'bK': 8, 'cI': 5},
             'bK': {'aK': 6, 'bI': 8, 'cK': 5},

             'cA': {'bA': 5, 'cC': 8},
             'cC': {'cA': 8, 'bC': 5, 'fC': 10},
             'cD': {'bD': 5, 'cE': 5},
             'cE': {'cD': 5, 'dE': 5},
             'cG': {'cH': 5, 'dG': 5},
             'cH': {'cG': 5, 'bH': 5},
             'cI': {'bH': 5, 'cK': 8, 'fI': 10},
             'cK': {'cI': 8, 'bK': 5},

             'dD': {'dE': 5, 'fD': 5},
             'dE': {'dD': 5, 'cE': 5, 'dF': 3},
             'dF': {'dE': 3, 'dG': 2, 'gF': 7},
             'dG': {'dF': 2, 'cG': 5, 'dH': 5},
             'dH': {'dG': 5, 'fH': 5},

             'eE': {'fE': 2},
             'eG': {'fG': 2},

             'fA': {'fC': 8},
             'fC': {'fA': 8, 'cC': 10, 'fD': 5, 'iC': 10},
             'fD': {'fC': 5, 'dD': 5, 'hD': 5},
             'fE': {'eE': 2, 'gE': 2},
             'fG': {'eG': 2, 'gG': 2},
             'fH': {'dH': 5, 'fI': 5, 'hH': 5},
             'fI': {'fH': 5, 'cI': 10, 'fK': 8, 'iI': 10},
             'fK': {'fI': 8},

             'gE': {'fE': 2, 'gF': 3},
             'gF': {'gE': 3, 'dF': 7, 'gG': 2},
             'gG': {'gF': 2, 'fG': 2},

             'hD': {'fD': 5, 'hH': 15, 'iD': 5},
             'hH': {'hD': 15, 'fH': 5, 'iH': 5},

             'iA': {'iC': 8, 'jA': 5},
             'iC': {'iA': 8, 'fC': 10, 'iD': 5, 'jC': 5},
             'iD': {'iC': 5, 'hD': 5, 'iE': 5},
             'iE': {'iD': 5, 'jE': 5},
             'iG': {'iH': 5, 'jG': 5},
             'iH': {'iG': 5, 'iI': 5, 'hH': 5},
             'iI': {'iH': 5, 'fI': 10, 'iK': 8, 'jI': 5},
             'iK': {'iI': 8, 'jK': 5},

             'jA': {'iA': 5, 'jB': 3},
             'jB': {'jA': 3, 'kB': 5},
             'jC': {'iC': 5, 'jD': 5, 'kC': 5},
             'jD': {'jC': 5, 'jE': 5, 'kD': 5},
             'jE': {'jD': 5, 'iE': 5, 'jF': 3},
             'jF': {'jE': 3, 'jG': 2},
             'jG': {'jF': 2, 'iG': 5, 'jH': 5},
             'jH': {'jG': 5, 'kH': 5, 'jI': 5},
             'jI': {'jH': 5, 'iI': 5, 'kI': 5},
             'jJ': {'jK': 3, 'kJ': 5},
             'jK': {'jJ': 3, 'iK': 5},

             'kA': {'kB': 3, 'iA': 5},
             'kB': {'kA': 3, 'jB': 5, 'kC': 5},
             'kC': {'kB': 5, 'jC': 5},
             'kD': {'jD': 5, 'kE': 5},
             'kE': {'kD': 5, 'lE': 5},
             'kG': {'kH': 5, 'lG': 5},
             'kH': {'kG': 5, 'jH': 5},
             'kI': {'jI': 5, 'kJ': 5},
             'kJ': {'kI': 5, 'jJ': 5, 'kK': 3},
             'kK': {'kJ': 3, 'lK': 5},

             'lA': {'kA': 5, 'lE': 19},
             'lE': {'lA': 19, 'kE': 5, 'lG': 5},
             'lG': {'lE': 5, 'kG': 5, 'lK': 19},
             'lK': {'lG': 19, 'kK': 5},
             }

    def __init__(self, pacSettings, screen, mazefile, brickfile, portalfile, shieldfile, pointfile, nodefile, mazeBound, barrierBound, points, nodes):#, pillfile):
        self.pacSettings = pacSettings
        self.screen = screen
        self.filename = mazefile
        self.nodefile = nodefile
        with open(self.filename, "r") as f:
            self.rows = f.readlines()
        self.brickfile = brickfile
        self.shieldfile = shieldfile
        self.pointfile = pointfile

        self.keyList = list(Maze.graph.keys())

        self.hportals = []
        self.vportals = []
        self.pill = []

        self.bsz = Maze.BRICK_SIZE
        self.psz = Maze.POINT_SIZE
        self.nsz = Maze.NODE_SIZE

        self.brick = ImageRect(screen, self.brickfile, self.bsz, self.bsz, 0, 0)
        self.deltax = self.deltay = Maze.BRICK_SIZE

        self.portal = ImageRect(screen, portalfile, self.bsz, self.bsz, 0, 0)
        self.sheld = ImageRect(screen, shieldfile, self.bsz, self.bsz, 0, 0)
        self.pts = ImageRect(screen, pointfile, self.psz, self.psz, 0, 0)
        self.nod = ImageRect(screen, nodefile, self.psz, self.psz, 0, 0)

        self.build(mazeBound, barrierBound, points, nodes)

    def build(self, mazeBound, barrierBound, points, nodes):
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
                elif col == "," or col == "N":
                    # self.points.append(pygame.Rect(ncol * self.dx, nrow * self.dy, pw, ph))
                    self.point = ImageRect(self.screen, self.pointfile, self.psz, self.psz, ncol * self.dx, nrow * self.dy)
                    points.add(self.point)
                elif col == "v":
                    self.vportals.append(pygame.Rect(ncol * self.dx, nrow * self.dy, w, h))

        counter = 0
        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == "N" or col == "n":
                    self.node = Node(self.screen, self.nodefile, self.nsz, self.nsz, ncol * self.dx, nrow * self.dy, self.keyList[counter])
                    nodes.add(self.node)
                    counter += 1

    def blitme(self, mazeBound, barrierBound, points, nodes):
        for node in nodes.sprites():
            self.screen.blit(self.nod.image, node)
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
                if col == "," or col == "N":
                    self.point = ImageRect(self.screen, self.pointfile, self.psz, self.psz, ncol * self.dx, nrow * self.dy)
                    points.add(self.point)