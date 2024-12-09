while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if gamePaused:
                # Check if the click is inside the "resume" button area
                if pygame.draw.polygon(screen, (0, 0, 0), points, 1).collidepoint(x, y):
                    gamePaused = False
                # Check if the click is inside the "upgrade" button area
                elif pygame.draw.polygon(screen, (0, 0, 0), points2, 1).collidepoint(x, y):
                    menu.upgradeActive = True

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

        for leaf2 in leafslist2:
            leaf2.update(1280, 720)
            leaf2.draw(screen)

            if leaf2.colliding(p1.xpos, p1.ypos, 150, 150):
                leafs2 += 2
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

    if gamePaused:
        if menu.upgradeActive:
            menu.drawUpgrade()
        else:
            menu.drawMenu()

    pygame.display.flip()

pygame.quit()
