import pygame


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 50)
        self.menuActive = False
        self.upgradeActive = False
        self.upgrade1stat = False
        self.upgrade2stat = False
        self.upgrade3stat = False

    def drawMenu(self):
        self.screen.fill((0, 0, 0))
        resumeTxt = self.font.render("Resume", True, (255, 255, 255))
        upgradeTxt = self.font.render("Upgrade", True, (255, 255, 255))
        self.screen.blit(resumeTxt, (self.screen.get_width() // 2 - 50, 200))
        self.screen.blit(upgradeTxt, (self.screen.get_width() // 2 - 50, 300))

    def drawUpgrade(self):
        self.screen.fill((50, 50, 150))
        upgradeTxt = self.font.render(
            "Upgrade Screen - ESC to go back", True, (255, 255, 255)
        )
        upgrade1 = self.font.render("x2 Leafs - 1,000 leafs", True, (255, 255, 255))
        upgrade2 = self.font.render(
            "x1.5 spawnrate - 1,500 leafs", True, (255, 255, 255)
        )
        self.screen.blit(upgradeTxt, (50, 10))
        if self.upgrade1stat == False:
            self.screen.blit(upgrade1, (50, 80))
        else:
            pygame.display.flip()
            
        if self.upgrade2stat == False:
            self.screen.blit(upgrade2, (50, 150))
        else:
            pygame.display.flip()
