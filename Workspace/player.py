# player.py
import pygame

leafblower = pygame.image.load("leafblower.png")
leafblower = pygame.transform.scale(leafblower, (150, 150))


class player:
    def __init__(self, image, xpos=0, ypos=0):
        self.xpos = xpos
        self.ypos = ypos
        self.image = image
        self.leafblower = leafblower

    def drawPlayer(self, screen):
        screen.blit(self.image, (self.xpos, self.ypos))
        screen.blit(self.leafblower, (self.xpos - 90, self.ypos))

    def updatePostion(self, x, y):
        self.xpos = x
        self.ypos = y
