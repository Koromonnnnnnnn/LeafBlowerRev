import pygame
from menu import Menu

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Menu Example")
clock = pygame.time.Clock()

# Initialize menu
menu = Menu(screen)
running = True
game_paused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Toggle main menu
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m and not menu.upgrade_screen_active:
                game_paused = not game_paused
                menu.menu_active = not menu.menu_active

            # Handle Upgrade screen toggle
            if menu.upgrade_screen_active and event.key == pygame.K_ESCAPE:
                menu.upgrade_screen_active = False

            # Menu actions
            if menu.menu_active:
                if event.key == pygame.K_DOWN:  # Select Upgrade
                    menu.upgrade_screen_active = True
                    menu.menu_active = False
                elif event.key == pygame.K_UP:  # Select Resume
                    menu.menu_active = False
                    game_paused = False

    # Game rendering logic
    if not game_paused:
        screen.fill((0, 100, 200))  # Game screen color
    elif menu.upgrade_screen_active:
        menu.draw_upgrade_screen()
    else:
        menu.draw_menu()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
