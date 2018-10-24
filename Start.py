import pygame
import pygame.font
from pygame import movie

class Start():
    def __init__(self, pacSettings, screen):
        self.pacSettings = pacSettings
        self.screen = screen

        self.rect = pygame.Rect(0, 0, pacSettings.screenWidth, pacSettings.screenHeight)
        self.screenRect = screen.get_rect()
        self.text_color = (255, 255, 255)
        self.text_color_2 = (0, 255, 0)

        self.color = pacSettings.backgroundColor

        self.prep_msg("Pacman", "Portal")

    def prep_msg(self, msg, msg2):
        self.font = pygame.font.SysFont(None, 150)
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        self.msg_image_rect.centery = self.rect.centery - 300

        self.font = pygame.font.SysFont(None, 100)
        self.msg2_image = self.font.render(msg2, True, self.text_color_2)
        self.msg2_image_rect = self.msg2_image.get_rect()
        self.msg2_image_rect.center = self.rect.center
        self.msg2_image_rect.centery = self.rect.centery - 200

    def printStart(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        self.screen.blit(self.msg2_image, self.msg2_image_rect)
