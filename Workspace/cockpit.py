import pygame


class Cockpit:
    def __init__(self, surface):
        self.surface = surface
        self.image = pygame.image.load("cockpit.png")
        self.image = pygame.transform.scale(self.image, (1280, 720))

    def draw_cockpit(self):
        self.surface.blit(self.image, (0, 0))
