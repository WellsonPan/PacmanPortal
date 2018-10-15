import pygame
import sys

class EventLoop():
    def __init__(self, finished):
        self.finished = finished

    @staticmethod
    def checkEvents(game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    game.pacman.movingRight = True
                    game.pacmanRight.movingRight = True
                    game.pacmanLeft.movingRight = True
                if event.key == pygame.K_LEFT:
                    game.pacman.movingLeft = True
                    game.pacmanRight.movingLeft = True
                    game.pacmanLeft.movingLeft = True
                if event.key == pygame.K_DOWN:
                    game.pacman.movingDown = True
                    game.pacmanRight.movingDown = True
                    game.pacmanLeft.movingDown = True
                if event.key == pygame.K_UP:
                    game.pacman.movingUp = True
                    game.pacmanRight.movingUp = True
                    game.pacmanLeft.movingUp = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    game.pacman.movingRight = False
                    game.pacmanRight.movingRight = False
                    game.pacmanLeft.movingRight = False
                if event.key == pygame.K_LEFT:
                    game.pacman.movingLeft = False
                    game.pacmanRight.movingLeft = False
                    game.pacmanLeft.movingLeft = False
                if event.key == pygame.K_DOWN:
                    game.pacman.movingDown = False
                    game.pacmanRight.movingDown = False
                    game.pacmanLeft.movingDown = False
                if event.key == pygame.K_UP:
                    game.pacman.movingUp = False
                    game.pacmanRight.movingUp = False
                    game.pacmanLeft.movingUp = False

    @staticmethod
    def checkWallCollision(game, pacman, pacmanRight, pacmanLeft, mazeBound):
        collisionRight = pygame.sprite.spritecollideany(pacmanRight, mazeBound)
        collisionLeft = pygame.sprite.spritecollideany(pacmanLeft, mazeBound)

        if collisionRight:
            game.pacman.movingRight = False
            game.pacmanRight.movingRight = False
            game.pacmanLeft.movingRight = False
        if collisionLeft:
            game.pacman.movingLeft = False
            game.pacmanRight.movingLeft = False
            game.pacmanLeft.movingLeft = False
