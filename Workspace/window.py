import pygame

class Window:
    def __init__(self, surface):
        self.surface = surface
        self.points = {
            'left': [(0, 12), (454, 181), (492, 369), (135, 439), (127, 433), (75, 454), (73, 451), (52, 447), (36, 447), (0, 461)],
            'middle': [(517, 153), (488, 186), (513, 366), (760, 366), (799, 183), (767, 149), (636, 148)],
            'right': [(812, 188), (1207, 1), (1276, 3), (1275, 420), (1275, 444), (1106, 394), (1056, 387), (787, 379), (775, 349), (817, 181), (1026, 90)]
        }

    def draw_windows(self):
        transparent_color = (0, 0, 0, 128)
        pygame.draw.polygon(self.surface, transparent_color, self.points['left'])
        pygame.draw.polygon(self.surface, transparent_color, self.points['middle'])
        pygame.draw.polygon(self.surface, transparent_color, self.points['right'])
