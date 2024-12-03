import pygame
import random
import math
from pygame import mixer
from player import player
from leaf import leaf

pygame.init()
mixer.init()

music = pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)  # Loop the music
pygame.mixer.music.set_volume(1)

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Leaf blower")
clock = pygame.time.Clock()

FPS = 60
gameOver = False

playerImage = pygame.image.load("player.png")
playerImage = pygame.transform.scale(playerImage, (150, 150))

leafImage = pygame.image.load("leaf.png")
leafImage = pygame.transform.scale(leafImage, (30, 30))

p1 = player(playerImage, xpos=0, ypos=0)
playerWidth, playerHeight = playerImage.get_size()

leafslist = [
    leaf(random.randint(0, 1280), random.randint(-100, 720), leafImage)
    for _ in range(10)
]

leafs = 0

while not gameOver:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    x, y = pygame.mouse.get_pos()

    x -= playerWidth // 2
    y -= playerHeight // 2

    screen.fill((0, 0, 0))

    for leaf in leafslist:
        leaf.update(1280, 720)
        leaf.draw(screen)

        if leaf.colliding(x, y, playerWidth, playerHeight):
            leafs += 1

            leaf.xpos = random.randint(0, 1280 - leaf.width)
            leaf.ypos = random.randint(-100, -10)

    font = pygame.font.Font(None, 35)

    leaftext = font.render(str(leafs), 1, (255, 255, 255))
    screen.blit(leaftext, (1225, 75))
    screen.blit(leafImage, (1175, 70))

    p1.updatePostion(x, y)
    p1.drawPlayer(screen)

    screen.blit(leafImage, (1175, 70))

    pygame.display.flip()

pygame.quit()
