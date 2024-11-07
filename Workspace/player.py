# player.py
import pygame

class player:
    def __init__(self, image, xpos=0, ypos=0):
        self.xpos = xpos
        self.ypos = ypos
        self.image = image

    def drawPlayer(self, screen):
        screen.blit(self.image, (self.xpos, self.ypos))

    def updatePostion(self, x, y):
        self.xpos = x
        self.ypos = y
