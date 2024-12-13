import pygame
import random
from pygame import mixer
from player import player
from leaf import leaf
from menu import Menu
from hyperspeed import ParticleSystem
from cockpit import Cockpit
from window import Window

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

particleSystem = ParticleSystem(screen)
window = Window(screen)
cockpit = Cockpit(screen)

hyperSpeed = False

# Constants
FPS = 60
playerImage = pygame.image.load("player.png")
playerImage = pygame.transform.scale(playerImage, (150, 150))

leafImage = pygame.image.load("leaf.png")
leafImage = pygame.transform.scale(leafImage, (30, 30))

leafImage2 = pygame.image.load("leaf2.png")
leafImage2 = pygame.transform.scale(leafImage2, (30, 30))

menu = Menu(screen)
p1 = player(playerImage, xpos=0, ypos=0)

leafMultiplier = 1
spawnMuliplier = 1

leafslist = [
    leaf(random.randint(0, 1280), random.randint(-100, 720), leafImage)
    for _ in range(12 * spawnMuliplier)
]

leafslist2 = [
    leaf(random.randint(0, 1280), random.randint(-100, 720), leafImage2)
    for _ in range(6 * spawnMuliplier)
]

leafs = 0
leafs2 = 0
gamePaused = False

points = [  # resume
    (587, 233),
    (587, 200),
    (722, 197),
    (727, 233),
]

points2 = [  # upgradescrene
    (587, 295),
    (730, 294),
    (735, 338),
    (588, 344),
]

upgrade1 = [  # upgrade1
    (45, 80),
    (396, 77),
    (400, 112),
    (45, 118),
]

upgrade2 = [  # upgrade2
    (47, 151),
    (500, 147),
    (509, 187),
    (46, 187),
]

running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # For testing purposes
            x, y = pygame.mouse.get_pos()
            print(x, y)
            if gamePaused:
                if pygame.draw.polygon(screen, (0, 0, 0), points, 1).collidepoint(x, y):
                    gamePaused = False
                elif pygame.draw.polygon(screen, (0, 0, 0), points2, 1).collidepoint(
                    x, y
                ):
                    menu.upgradeActive = True

                if menu.upgradeActive:
                    if menu.upgrade1stat == False:
                        if pygame.draw.polygon(
                            screen, (0, 0, 0), upgrade1, 1
                        ).collidepoint(x, y):
                            if leafs >= 50:
                                leafMultiplier = 2
                                leafs -= 50
                                menu.upgrade1stat = True

                if menu.upgradeActive:
                    if menu.upgrade2stat == False:
                        if pygame.draw.polygon(
                            screen, (0, 0, 0), upgrade2, 1
                        ).collidepoint(x, y):
                            if leafs >= 50:
                                spawnMuliplier = 1.5
                                leafs -= 50
                                menu.upgrade2stat = True

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
                leafs += 1 * leafMultiplier
                leaf.xpos = random.randint(0, 1280 - leaf.width)
                leaf.ypos = random.randint(-100, -10)

        for leaf2 in leafslist2:
            leaf2.update(1280, 720)
            leaf2.draw(screen)

            if leaf2.colliding(p1.xpos, p1.ypos, 150, 150):
                leafs2 += 2 * leafMultiplier
                leaf2.xpos = random.randint(0, 1280 - leaf.width)
                leaf2.ypos = random.randint(-100, -10)

        font = pygame.font.Font(None, 35)
        leaf_text = font.render(str(leafs), 1, (255, 255, 255))
        leaf_text2 = font.render(str(leafs2), 1, (255, 255, 255))
        screen.blit(leaf_text, (1225, 75))
        screen.blit(leafImage, (1175, 70))
        screen.blit(leaf_text2, (1225, 105))
        screen.blit(leafImage2, (1175, 100))

        x, y = pygame.mouse.get_pos()
        p1.updatePostion(x - 75, y - 75)
        p1.drawPlayer(screen)

    if hyperSpeed == True:
        window.draw_windows()
        particleSystem.update_particles()
        particleSystem.draw_particles()
        cockpit.draw_cockpit()
    else:
        pygame.display.flip()

    if gamePaused:
        if menu.upgradeActive:
            menu.drawUpgrade()
        else:
            menu.drawMenu()

    pygame.display.flip()

pygame.quit()
