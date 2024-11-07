import random
import pygame 

img = pygame.image.load("leaf")

class leaf:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.color = (random.randrange(100,250), random.randrange(100,250), random.randrange(100,250))
    def draw(self, screen):
        img = self.color(random.randrange(100,250), random.randrange(100,250), random.randrange(100,250))
        screen.blit(img, (random.randrange(-100, 800),random.randrange(-100, 800)))

