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


def level1():
    """
    First level of an adventure game where Travis Kelce has to collect water drops to water a rose.
    :return: Returns either True (if the level is completed) or False (if the level isn't completed)
    """

    # Initialize pygame
    pygame.init()

    garden = pygame.image.load("Garden Background.png")
    # Store window width and height in a tuple.
    garden_size = garden.get_size()
    garden_rect = garden.get_rect()

    # create the window based on the garden size
    screen = pygame.display.set_mode(garden_size)
    garden = garden.convert_alpha()

    # Change white pixels in the garden to transparent.
    garden.set_colorkey((255, 255, 255))
    garden_mask = pygame.mask.from_surface(garden)

    # Create the player data
    player = pygame.image.load("Travis Kelce.png").convert_alpha()  # Image Source: thesportsdb.com
    player = pygame.transform.smoothscale(player, (70, 70))
    player_rect = player.get_rect()
    player_mask = pygame.mask.from_surface(player)

    # Create the start button
    start = pygame.image.load("start.png").convert_alpha()  # Image Source: www.pngall.com
    start = pygame.transform.smoothscale(start, (40, 40))
    start_rect = start.get_rect()
    start_rect.center = (50, 400)
    start_mask = pygame.mask.from_surface(start)

    # Create the drops
    drop_1 = pygame.image.load("drop.png").convert_alpha()  # Image Source: www.transparentpng.com
    drop_1 = pygame.transform.smoothscale(drop_1, (40, 40))
    drop_1_rect = drop_1.get_rect()
    drop_1_rect.center = (110, 90)
    drop_1_mask = pygame.mask.from_surface(drop_1)

    drop_2 = pygame.image.load("drop.png").convert_alpha()  # Image Source: www.transparentpng.com
    drop_2 = pygame.transform.smoothscale(drop_2, (40, 40))
    drop_2_rect = drop_2.get_rect()
    drop_2_rect.center = (600, 700)
    drop_2_mask = pygame.mask.from_surface(drop_2)

    drop_3 = pygame.image.load("drop.png").convert_alpha()  # Image Source: www.transparentpng.com
    drop_3 = pygame.transform.smoothscale(drop_3, (40, 40))
    drop_3_rect = drop_3.get_rect()
    drop_3_rect.center = (900, 710)
    drop_3_mask = pygame.mask.from_surface(drop_3)

    drop_4 = pygame.image.load("drop.png").convert_alpha()  # Image Source: www.transparentpng.com
    drop_4 = pygame.transform.smoothscale(drop_4, (40, 40))
    drop_4_rect = drop_4.get_rect()
    drop_4_rect.center = (420, 50)
    drop_4_mask = pygame.mask.from_surface(drop_4)

    # Create the seeds
    seeds = pygame.image.load("Seeds.png").convert_alpha()  # Image Source: cdn-icons-png.flaticon.com
    seeds = pygame.transform.smoothscale(seeds, (100, 100))
    seeds_rect = seeds.get_rect()
    seeds_rect.center = (1150, 500)
    seeds_mask = pygame.mask.from_surface(seeds)

    # Create the rose
    rose = pygame.image.load("rose.png").convert_alpha()  # Image Source: pngimg.com
    rose = pygame.transform.smoothscale(rose, (100, 100))
    rose_rect = rose.get_rect()
    rose_rect.center = (1180, 600)
    rose_mask = pygame.mask.from_surface(rose)

    # The frame tells which sprite frame to draw
    frame_count = 0

    # The clock helps us manage the frames per second of the animation
    clock = pygame.time.Clock()

    # Set font for writing displayed on screen
    message_font = pygame.font.SysFont('monospace', 24)

    # The started variable records if the start color has been clicked and the level started
    started = False

    # Shows that the drops and seeds have not been found yet
    drop_1_found = False
    drop_2_found = False
    drop_3_found = False
    drop_4_found = False
    seeds_found = False

    # The is_alive variable records if anything bad has happened
    is_alive = True

    # Hide the arrow cursor and replace it with a sprite.
    pygame.mouse.set_visible(False)

    # This is the main game loop.
    while is_alive:
        # Check events by looping over the list of events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_alive = False
            if event.type == pygame.MOUSEBUTTONDOWN and pixel_collision(player_mask, player_rect, start_mask,
                                                                        start_rect):
                started = True  # Starts the level when player clicks the start button

        # Position the player to the mouse location
        pos = pygame.mouse.get_pos()
        player_rect.center = pos
        if started:
            # See if we touch the garden walls
            if pixel_collision(player_mask, player_rect, garden_mask, garden_rect):
                is_alive = False

            # Check for collision with the seeds if it is not opened by the drop.
            if ((not drop_1_found or not drop_2_found or not drop_3_found or not drop_4_found) and
                    pixel_collision(player_mask, player_rect, seeds_mask, seeds_rect)):
                return False  # return False to show level fail

            # Pick up water drops if player collides with drop
            if not drop_1_found and pixel_collision(player_mask, player_rect, drop_1_mask, drop_1_rect):
                drop_1_found = True

            if not drop_2_found and pixel_collision(player_mask, player_rect, drop_2_mask, drop_2_rect):
                drop_2_found = True

            if not drop_3_found and pixel_collision(player_mask, player_rect, drop_3_mask, drop_3_rect):
                drop_3_found = True

            if not drop_4_found and pixel_collision(player_mask, player_rect, drop_4_mask, drop_4_rect):
                drop_4_found = True

            # Pick up the seeds if player collides with seeds after drops have been collected
            if not seeds_found and pixel_collision(player_mask, player_rect, seeds_mask, seeds_rect):
                seeds_found = True

        # Draw the background garden image
        screen.fill((150, 150, 150))  # This helps check if the image path is transparent
        screen.blit(garden, garden_rect)

        # Draw the player character Travis Kelce
        screen.blit(player, player_rect)

        # Draw the start button if it has not been clicked.
        if not started:
            screen.blit(start, start_rect)

        # Draw the drop and seeds only if the drop has not been found.
        if not drop_1_found:
            screen.blit(drop_1, drop_1_rect)

        if not drop_2_found:
            screen.blit(drop_2, drop_2_rect)
            screen.blit(seeds, seeds_rect)

        if not drop_3_found:
            screen.blit(drop_3, drop_3_rect)
            screen.blit(seeds, seeds_rect)

        if not drop_4_found:
            screen.blit(drop_4, drop_4_rect)
            screen.blit(seeds, seeds_rect)

        # Create seeds if the drops and seeds have not been collected
        if drop_1_found and drop_2_found and drop_3_found and drop_4_found and not seeds_found:
            screen.blit(seeds, seeds_rect)

        # Create the rose if seeds are collected
        if drop_1_found and drop_2_found and drop_3_found and drop_4_found and seeds_found:
            screen.blit(rose, rose_rect)

        # If player touches rose move to next level
        if pixel_collision(player_mask, player_rect, rose_mask, rose_rect) and seeds_found:
            return True

        # Write some text to the screen.
        label = message_font.render("Water the seeds and pick the rose.", True, (255, 255, 255))
        screen.blit(label, (760, 10))

        # Every time through the loop, increase the frame count.
        frame_count += 1

        # Bring drawn changes to the front
        pygame.display.update()

        # This tries to force the loop to run at 30 fps
        clock.tick(30)
