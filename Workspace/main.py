import pygame
import random
from pygame import mixer
from player import player
from leaf import leaf
from menu import Menu

# Initialize pygame and mixer
pygame.init()
mixer.init()

# Music setup
mixer.music.load("music.mp3")
mixer.music.play(-1)
mixer.music.set_volume(1)

# Screen setup
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Leaf Blower")
clock = pygame.time.Clock()

# Constants
FPS = 60
playerImage = pygame.image.load("player.png")
playerImage = pygame.transform.scale(playerImage, (150, 150))

leafImage = pygame.image.load("leaf.png")
leafImage = pygame.transform.scale(leafImage, (30, 30))

menu = Menu(screen)
p1 = player(playerImage, xpos=0, ypos=0)
leafslist = [
    leaf(random.randint(0, 1280), random.randint(-100, 720), leafImage)
    for _ in range(10)
]

leafs = 0
gamePaused = False
running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m and not menu.upgradeActive:
                gamePaused = not gamePaused
                menu.menuActive = not menu.menuActive

            if menu.upgradeActive and event.key == pygame.K_ESCAPE:
                menu.upgradeActive = False

            if menu.menuActive:
                if event.key == pygame.K_DOWN:
                    menu.upgradeActive = True
                    menu.menuActive = False
                elif event.key == pygame.K_UP:
                    menu.menuActive = False
                    gamePaused = False

    if not gamePaused:
        screen.fill((0, 0, 0))

        for leaf in leafslist:
            leaf.update(1280, 720)
            leaf.draw(screen)

            if leaf.colliding(p1.xpos, p1.ypos, 150, 150):
                leafs += 1
                leaf.xpos = random.randint(0, 1280 - leaf.width)
                leaf.ypos = random.randint(-100, -10)

        font = pygame.font.Font(None, 35)
        leaf_text = font.render(str(leafs), 1, (255, 255, 255))
        screen.blit(leaf_text, (1225, 75))
        screen.blit(leafImage, (1175, 70))

        x, y = pygame.mouse.get_pos()
        p1.updatePostion(x - 75, y - 75)
        p1.drawPlayer(screen)

    if gamePaused:
        if menu.upgradeActive:
            menu.drawUpgrade()
        else:
            menu.drawMenu()

    pygame.display.flip()

pygame.quit()
