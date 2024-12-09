import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 50)
        self.menuActive = False
        self.upgradeActive = False

    def drawMenu(self):
        self.screen.fill((0, 0, 0))
        resumeTxt = self.font.render("Resume", True, (255, 255, 255))
        upgradeTxt = self.font.render("Upgrade", True, (255, 255, 255))
        self.screen.blit(resumeTxt, (self.screen.get_width() // 2 - 50, 200))
        self.screen.blit(upgradeTxt, (self.screen.get_width() // 2 - 50, 300))

    def drawUpgrade(self):
        self.screen.fill((50, 50, 150))
        upgradeTxt = self.font.render("Upgrade Screen - ESC to go back", True, (255, 255, 255))
        self.screen.blit(upgradeTxt, (50, 250))
