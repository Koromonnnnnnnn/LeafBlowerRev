import random
import pygame

img = pygame.image.load("leaf.png")


class leaf:
    def __init__(self, xpos, ypos, image):
        self.xpos = xpos
        self.ypos = ypos
        self.xvel = random.uniform(-2, 2)
        self.yvel = random.uniform(1, 3)
        self.image = pygame.transform.scale(image, (30, 30))  
        self.width, self.height = self.image.get_size()

    def update(self, w, h):
        self.xpos += self.xvel
        self.ypos += self.yvel

        if self.ypos > h or self.xpos < -self.width or self.xpos > w:
            self.xpos = random.randint(0, w - self.width)
            self.ypos = random.randint(-100, -10) 

    def draw(self, screen):
        screen.blit(self.image, (int(self.xpos), int(self.ypos)))

    def colliding(self, px, py, pw, ph):
        return (
            self.xpos < px + pw
            and self.xpos + self.width > px
            and self.ypos < py + ph
            and self.ypos + self.height > py
        )
