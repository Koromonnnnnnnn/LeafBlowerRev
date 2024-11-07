import pygame
import random
from player import player

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Leaf blower")
clock = pygame.time.Clock()

FPS = 60
gameOver = False

playerImage = pygame.image.load("player.png")
playerImage = pygame.transform.scale(playerImage, (150, 150))

p1 = player(playerImage, xpos=0, ypos = 0)
playerWidth, playerHeight = playerImage.get_size()

while not gameOver:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    x, y = pygame.mouse.get_pos()

    x -= playerWidth // 2
    y -= playerHeight // 2

    screen.fill((0,0,0))

    p1.updatePostion(x,y)
    p1.drawPlayer(screen)

    pygame.display.flip()

pygame.quit()



