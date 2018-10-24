import pygame
import sys
from Portal import oPortal, iPortal, Laser, Laser2


def levelComplete(pacman, pacmanLeft, pacmanRight, pacmanUp, pacmanDown, maze, points):
        if len(points) == 0:
            pacman.resetPos()
            pacmanLeft.resetPos()
            pacmanRight.resetPos()
            pacmanUp.resetPos()
            pacmanDown.resetPos()
            maze.resetMaze(points)

def checkEvents(game, pacSettings, laser, laser2, playButton, highScoreButton):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                buttonClicked = playButton.rect.collidepoint(mouseX, mouseY)
                highClicked = highScoreButton.rect.collidepoint(mouseX, mouseY)
                if buttonClicked and not pacSettings.gameActive:
                    pacSettings.highScores = False
                    pacSettings.gameActive = True
                elif highClicked and not pacSettings.gameActive and not pacSettings.highScores:
                    pacSettings.highScores = True
                elif highClicked and not pacSettings.gameActive and pacSettings.highScores:
                    pacSettings.highScores = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    game.pacman.movingRight = True
                    game.pacmanRight.movingRight = True
                    game.pacmanLeft.movingRight = True
                    game.pacmanUp.movingRight = True
                    game.pacmanDown.movingRight = True
                if event.key == pygame.K_LEFT:
                    game.pacman.movingLeft = True
                    game.pacmanRight.movingLeft = True
                    game.pacmanLeft.movingLeft = True
                    game.pacmanUp.movingLeft = True
                    game.pacmanDown.movingLeft = True
                if event.key == pygame.K_DOWN:
                    game.pacman.movingDown = True
                    game.pacmanRight.movingDown = True
                    game.pacmanLeft.movingDown = True
                    game.pacmanUp.movingDown = True
                    game.pacmanDown.movingDown = True
                if event.key == pygame.K_UP:
                    game.pacman.movingUp = True
                    game.pacmanRight.movingUp = True
                    game.pacmanLeft.movingUp = True
                    game.pacmanUp.movingUp = True
                    game.pacmanDown.movingUp = True
                if event.key == pygame.K_q:
                    lase = Laser(game.pacSettings, game.screen, game.pacman)
                    laser.add(lase)
                if event.key == pygame.K_e:
                    lase2 = Laser2(game.pacSettings, game.screen, game.pacman)
                    laser2.add(lase2)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    game.pacman.movingRight = False
                    game.pacmanRight.movingRight = False
                    game.pacmanLeft.movingRight = False
                    game.pacmanUp.movingRight = False
                    game.pacmanDown.movingRight = False
                if event.key == pygame.K_LEFT:
                    game.pacman.movingLeft = False
                    game.pacmanRight.movingLeft = False
                    game.pacmanLeft.movingLeft = False
                    game.pacmanUp.movingLeft = False
                    game.pacmanDown.movingLeft = False
                if event.key == pygame.K_DOWN:
                    game.pacman.movingDown = False
                    game.pacmanRight.movingDown = False
                    game.pacmanLeft.movingDown = False
                    game.pacmanUp.movingDown = False
                    game.pacmanDown.movingDown = False
                if event.key == pygame.K_UP:
                    game.pacman.movingUp = False
                    game.pacmanRight.movingUp = False
                    game.pacmanLeft.movingUp = False
                    game.pacmanUp.movingUp = False
                    game.pacmanDown.movingUp = False


def checkWallCollision(game, pacmanRight, pacmanLeft, pacmanUp, pacmanDown, mazeBound, barrierBound):
        collisionRight = pygame.sprite.spritecollideany(pacmanRight, mazeBound)
        collisionLeft = pygame.sprite.spritecollideany(pacmanLeft, mazeBound)
        collisionUp = pygame.sprite.spritecollideany(pacmanUp, mazeBound)
        collisionDown = pygame.sprite.spritecollideany(pacmanDown, mazeBound)
        collisionBarrier = pygame.sprite.spritecollideany(pacmanDown, barrierBound)

        if collisionRight:
            game.pacman.movingRight = False
            game.pacmanRight.movingRight = False
            game.pacmanLeft.movingRight = False
            game.pacmanUp.movingRight = False
            game.pacmanDown.movingRight = False
        if collisionLeft:
            game.pacman.movingLeft = False
            game.pacmanRight.movingLeft = False
            game.pacmanLeft.movingLeft = False
            game.pacmanUp.movingLeft = False
            game.pacmanDown.movingLeft = False
        if collisionUp:
            game.pacman.movingUp = False
            game.pacmanRight.movingUp = False
            game.pacmanLeft.movingUp = False
            game.pacmanUp.movingUp = False
            game.pacmanDown.movingUp = False
        if collisionDown or collisionBarrier:
            game.pacman.movingDown = False
            game.pacmanRight.movingDown = False
            game.pacmanLeft.movingDown = False
            game.pacmanUp.movingDown = False
            game.pacmanDown.movingDown = False


def scoring(pacSettings, pacman, pacmanLeft, pacmanRight, pacmanUp, pacmanDown, points):
        collisionPoint = pygame.sprite.spritecollide(pacman, points, True)
        collisionLeft = pygame.sprite.spritecollide(pacmanLeft, points, True)
        collisionRight = pygame.sprite.spritecollide(pacmanRight, points, True)
        collisionUp = pygame.sprite.spritecollide(pacmanUp, points, True)
        collisionDown = pygame.sprite.spritecollide(pacmanDown, points, True)

        if collisionPoint or collisionLeft or collisionRight or collisionUp or collisionDown:
            pacSettings.score += pacSettings.pointVal


def portalWallCollision(game, laser, laser2, portal, portal2, mazeBound):
        collisions = pygame.sprite.groupcollide(laser, mazeBound, False, False)
        collisions2 = pygame.sprite.groupcollide(laser2, mazeBound, False, False)
        collisions3 = pygame.sprite.groupcollide(laser, laser2, True, True)
        collisions4 = pygame.sprite.groupcollide(portal, portal2, True, True)

        for lase in collisions.copy():
            lase.stop()
            oportal = oPortal(game.pacSettings, game.screen, lase.x, lase.y)
            oportal.rect.center = lase.rect.center
            portal.add(oportal)
            laser.remove(lase)

        for lase in collisions2.copy():
            lase.stop()
            iportal = iPortal(game.pacSettings, game.screen, lase.x, lase.y)
            iportal.rect.center = lase.rect.center
            portal2.add(iportal)
            laser2.remove(lase)


def pacmanPortalCollision(pacSettings, pacman, pacmanLeft, pacmanRight, pacmanUp, pacmanDown, portals, portals2):
        collisions = pygame.sprite.spritecollide(pacman, portals, False)
        collisions2 = pygame.sprite.spritecollide(pacman, portals2, False)

        if collisions:
            for port in portals2.sprites():
                pacman.centerx = port.x
                pacman.centery = port.y
                pacmanLeft.centerx = port.x - int(pacSettings.pacmanRad / 3)
                pacmanLeft.centery = port.y
                pacmanRight.centerx = port.x + int(pacSettings.pacmanRad / 3)
                pacmanRight.centery = port.y
                pacmanUp.centerx = port.x
                pacmanUp.centery = port.y - int(pacSettings.pacmanRad / 3)
                pacmanDown.centerx = port.x
                pacmanDown.centery = port.y + int(pacSettings.pacmanRad / 3)
                portals2.remove(port)
        if collisions2:
            for port in portals.sprites():
                pacman.centerx = port.x
                pacman.centery = port.y
                pacmanLeft.centerx = pacman.centerx - int(pacSettings.pacmanRad / 3)
                pacmanLeft.centery = pacman.centery
                pacmanRight.centerx = pacman.centerx + int(pacSettings.pacmanRad / 3)
                pacmanRight.centery = pacman.centery
                pacmanUp.centerx = pacman.centerx
                pacmanUp.centery = pacman.centery - int(pacSettings.pacmanRad / 3)
                pacmanDown.centerx = pacman.centerx
                pacmanDown.centery = pacman.centery + int(pacSettings.pacmanRad / 3)
                portals.remove(port)


def readHighScore():
    file = open("files/highScores.txt", "r")
    high = int(file.read())
    file.close()
    return high


def printHighScores(screen):
    font = pygame.font.SysFont(None, 48)
    high_score = int(round(readHighScore(), -1))
    high_score_str = "{:,} Pts".format(high_score)
    high_score_image = font.render(high_score_str, True, (255, 255, 255), (0, 0, 0))
    screen_rect = screen.get_rect()

    high_score_rect = high_score_image.get_rect()
    high_score_rect.centerx = screen_rect.centerx
    high_score_rect.centery = screen_rect.centery

    exitHighString = "Exit"
    exitImage = font.render(exitHighString, True, (255, 255, 255), (0, 0, 0))
    exitRect = exitImage.get_rect()
    exitRect.centerx = screen_rect.centerx
    exitRect.centery = screen_rect.centery + 350

    font = pygame.font.SysFont(None, 72)
    highScore = "High Score"
    scoreImage = font.render(highScore, True, (255, 255, 255), (0, 0, 0))
    scoreRect = scoreImage.get_rect()
    scoreRect.centerx = screen_rect.centerx
    scoreRect.top = screen_rect.top + 50

    screen.fill((0, 0, 0))
    screen.blit(scoreImage, scoreRect)
    screen.blit(high_score_image, high_score_rect)
    screen.blit(exitImage, exitRect)
    pygame.display.flip()