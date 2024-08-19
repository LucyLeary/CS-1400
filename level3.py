import pygame

# Finished game authors:
# Lucy Leary
# Lyndsey Schindler


def pixel_collision(mask1, rect1, mask2, rect2):
    """
    Check if the non-transparent pixels of one mask contacts the non-transparent pixels of another.
    :param: image masks and rectangles for two objects
    :return: True or False depending on whether the objects overlap
    """
    offset_x = rect2[0] - rect1[0]
    offset_y = rect2[1] - rect1[1]
    # See if the two masks at the offset are overlapping.
    overlap = mask1.overlap(mask2, (offset_x, offset_y))
    return overlap is not None


def level3():
    """
    First level of an adventure game where Travis Kelce has to collect water drops to water a rose.
    :return: Returns either True (if the level is completed) or False (if the level isn't completed)
    """

    # Initialize pygame
    pygame.init()

    lover = pygame.image.load("swift_album.png")  # Image Source: pinimg.com
    # Store window width and height in a tuple.
    lover_size = lover.get_size()
    lover_rect = lover.get_rect()

    # create the window based on the lover size
    screen = pygame.display.set_mode(lover_size)
    lover = lover.convert_alpha()
    lover_mask = pygame.mask.from_surface(lover)

    # Create the player data
    player = pygame.image.load("Travis Kelce.png").convert_alpha()  # Image Source: www.thesportsdb.com
    player = pygame.transform.smoothscale(player, (70, 70))
    player_rect = player.get_rect()
    player_mask = pygame.mask.from_surface(player)

    # Create the start button
    start = pygame.image.load("start.png").convert_alpha()  # Image Source: www.pngall.com
    start = pygame.transform.smoothscale(start, (40, 40))
    start_rect = start.get_rect()
    start_rect.center = (600, 700)
    start_mask = pygame.mask.from_surface(start)

    # Create the four Swifts from behind
    swift_1 = pygame.image.load("taylor_back.png").convert_alpha()  # Image Source: hollieblog.com
    swift_1 = pygame.transform.smoothscale(swift_1, (60, 60))
    swift_1_rect = swift_1.get_rect()
    swift_1_rect.center = (600, 280)
    swift_1_mask = pygame.mask.from_surface(swift_1)

    swift_2 = pygame.image.load("taylor_back.png").convert_alpha()  # Image Source: hollieblog.com
    swift_2 = pygame.transform.smoothscale(swift_2, (60, 60))
    swift_2_rect = swift_2.get_rect()
    swift_2_rect.center = (600, 380)
    swift_2_mask = pygame.mask.from_surface(swift_2)

    swift_3 = pygame.image.load("taylor_back.png").convert_alpha()  # Image Source: hollieblog.com
    swift_3 = pygame.transform.smoothscale(swift_3, (60, 60))
    swift_3_rect = swift_3.get_rect()
    swift_3_rect.center = (600, 480)
    swift_3_mask = pygame.mask.from_surface(swift_3)

    swift_4 = pygame.image.load("taylor_back.png").convert_alpha()  # Image Source: hollieblog.com
    swift_4 = pygame.transform.smoothscale(swift_4, (60, 60))
    swift_4_rect = swift_4.get_rect()
    swift_4_rect.center = (600, 580)
    swift_4_mask = pygame.mask.from_surface(swift_4)

    # Create Scarlett
    scarlett = pygame.image.load("scarlett.png").convert_alpha()  # Image Source: www.fashiongonerogue.com
    scarlett = pygame.transform.smoothscale(scarlett, (60, 60))
    scarlett_rect = scarlett.get_rect()
    scarlett_rect.center = (600, 480)

    # Create Gwyneth
    gwyneth = pygame.image.load("gwyneth.png").convert_alpha()  # Image Source: www.hawtcelebs.com
    gwyneth = pygame.transform.smoothscale(gwyneth, (60, 60))
    gwyneth_rect = gwyneth.get_rect()
    gwyneth_rect.center = (600, 580)

    # Create Margot
    margot = pygame.image.load("margot.png").convert_alpha()  # Image Source: www.fashiongonerogue.com
    margot = pygame.transform.smoothscale(margot, (60, 60))
    margot_rect = margot.get_rect()
    margot_rect.center = (600, 280)

    # Create Taylor
    taylor_face = pygame.image.load("taylor_face.png").convert_alpha()  # Image Source: hollieblog.com
    taylor_face = pygame.transform.smoothscale(taylor_face, (60, 60))
    taylor_face_rect = taylor_face.get_rect()
    taylor_face_rect.center = (600, 380)

    # The frame tells which sprite frame to draw
    frame_count = 0

    # The clock helps us manage the frames per second of the animation
    clock = pygame.time.Clock()

    # Set font for writing displayed on the screen.
    message_font = pygame.font.SysFont('monospace', 24)

    # The started variable records if the start button has been clicked and the level started
    started = False

    # Shows that the 4 ladies have not been found yet
    swift_1_found = False
    swift_2_found = False
    swift_3_found = False
    swift_4_found = False

    # The is_alive variable records if anything bad has happened
    is_alive = True

    # Hide the arrow cursor and replace it with a sprite.
    pygame.mouse.set_visible(False)

    # This is the main game loop
    while is_alive:
        # Check events by looping over the list of events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_alive = False
            if (event.type == pygame.MOUSEBUTTONDOWN and
                    pixel_collision(player_mask, player_rect, start_mask, start_rect)):
                started = True  # Starts the level when player clicks the start button

        # Position the player to the mouse location
        pos = pygame.mouse.get_pos()
        player_rect.center = pos

        if started:
            # See if we touch the album cover boundaries
            if pixel_collision(player_mask, player_rect, lover_mask, lover_rect):
                is_alive = False

            # Check for collision between player and swift 1
            if not swift_1_found and pixel_collision(player_mask, player_rect, swift_1_mask, swift_1_rect):
                swift_1_found = True

            # Check for collision between player and swift 2
            if not swift_2_found and pixel_collision(player_mask, player_rect, swift_2_mask, swift_2_rect):
                swift_2_found = True

            # Check for collision between player and swift 3
            if not swift_3_found and pixel_collision(player_mask, player_rect, swift_3_mask, swift_3_rect):
                swift_3_found = True

            # Check for collision between player and swift 4
            if not swift_4_found and pixel_collision(player_mask, player_rect, swift_4_mask, swift_4_rect):
                swift_4_found = True

        # Draw the lover album background
        screen.fill((150, 150, 150))  # This helps check if the image path is transparent
        screen.blit(lover, lover_rect)

        # Draw the player character Travis Kelce
        screen.blit(player, player_rect)

        # Draw the start button if it has not been clicked.
        if not started:
            screen.blit(start, start_rect)

        # Draw swift 1 if swift 1 has not been found.
        if not swift_1_found:
            screen.blit(swift_1, swift_1_rect)

        # Draw swift 2 if swift 2 has not been found.
        if not swift_2_found:
            screen.blit(swift_2, swift_2_rect)

        # Draw swift 3 if swift 3 has not been found.
        if not swift_3_found:
            screen.blit(swift_3, swift_3_rect)

        # Draw swift 4 if swift 4 has not been found.
        if not swift_4_found:
            screen.blit(swift_4, swift_4_rect)

        # Draw Margot where swift 1 was if swift 1 was found
        if swift_1_found:
            screen.blit(margot, margot_rect)
            pygame.display.update()
            for count in range(50000000):  # Delay loss so Margot is seen on the screen longer
                pass
            is_alive = False

        # Draw Taylor where swift 2 was if swift 2 was found
        if swift_2_found:
            screen.blit(taylor_face, taylor_face_rect)
            pygame.display.update()
            for count in range(50000000):  # Delay win so Taylor is seen on the screen longer
                pass
            return True  # Return true if player correctly finds swift 2

        # Draw Scarlett where swift 3 was if swift 3 was found
        if swift_3_found:
            screen.blit(scarlett, scarlett_rect)
            pygame.display.update()
            for count in range(50000000):  # Delay loss so Scarlett is seen on the screen longer
                pass
            is_alive = False

        # Draw Gwyneth where swift 4 was if swift 4 was found
        if swift_4_found:
            screen.blit(gwyneth, gwyneth_rect)
            pygame.display.update()
            for count in range(50000000):  # Delay loss so Gwyneth is seen on the screen longer
                pass
            is_alive = False

        # Write text instructions to the screen.
        label = message_font.render("Which one is your girl?", True, (255, 255, 255))
        screen.blit(label, (20, 10))

        # Every time through the loop, increase the frame count.
        frame_count += 1

        # Bring drawn changes to the front
        pygame.display.update()

        # This tries to force the loop to run at 30 fps
        clock.tick(30)
