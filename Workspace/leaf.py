import random
import pygame

img = pygame.image.load("leaf.png")


class leaf:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.color = (
            random.randrange(100, 250),
            random.randrange(100, 250),
            random.randrange(100, 250),
        )

    def draw(self, screen, xpos, ypos, amount):
        xpos = (random.randrange(100, 250), random.randrange(100, 250))
        ypos = (random.randrange(100, 250), random.randrange(100, 250))

        for i in range(amount):
            screen.blit(img, xpos, ypos)
