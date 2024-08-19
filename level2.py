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


def level2():
    """
    Second level of an adventure game where Travis Kelce has to dodge other male celebrities to get to Taylor.
    :return: Returns either True (if the level is completed) or False (if the level isn't completed)
    """

    # Initialize pygame
    pygame.init()

    red_carpet = pygame.image.load("red_carpet.png")  # Image Source: www.freepik.com
    # Store window width and height in a tuple.
    red_carpet_size = red_carpet.get_size()
    red_carpet_rect = red_carpet.get_rect()

    # create the window based on the red_carpet size
    screen = pygame.display.set_mode(red_carpet_size)
    red_carpet = red_carpet.convert_alpha()
    red_carpet_mask = pygame.mask.from_surface(red_carpet)

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

    # Create the boy obstacles
    bieber = pygame.image.load("boy1.png").convert_alpha()  # Image Source: purepng.com
    bieber = pygame.transform.smoothscale(bieber, (60, 60))
    bieber_rect = bieber.get_rect()
    bieber_rect.center = (600, 600)
    bieber_mask = pygame.mask.from_surface(bieber)
    bieber_x_value = 600
    bieber_left = False

    sandler = pygame.image.load("boy2.png").convert_alpha()  # Image Source: clipartcraft.com
    sandler = pygame.transform.smoothscale(sandler, (60, 60))
    sandler_rect = sandler.get_rect()
    sandler_rect.center = (600, 550)
    sandler_mask = pygame.mask.from_surface(sandler)
    sandler_x_value = 600
    sandler_left = True

    kanye = pygame.image.load("boy3.png").convert_alpha()  # Image Source: pluspng.com
    kanye = pygame.transform.smoothscale(kanye, (60, 60))
    kanye_rect = kanye.get_rect()
    kanye_rect.center = (600, 500)
    kanye_mask = pygame.mask.from_surface(kanye)
    kanye_x_value = 600
    kanye_left = False

    # Create the level exit
    level_exit = pygame.image.load("exit.png").convert_alpha()  # Image Source: SafetySign.com
    level_exit = pygame.transform.smoothscale(level_exit, (90, 90))
    level_exit_rect = level_exit.get_rect()
    level_exit_rect.center = (600, 400)
    level_exit_mask = pygame.mask.from_surface(level_exit)

    # The frame tells which sprite frame to draw
    frame_count = 0

    # The clock helps us manage the frames per second of the animation
    clock = pygame.time.Clock()

    # Set font for writing displayed on screen
    message_font = pygame.font.SysFont('monospace', 24)

    # The started variable records if the start button has been clicked and the level started
    started = False

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
            if (event.type == pygame.MOUSEBUTTONDOWN and
                    pixel_collision(player_mask, player_rect, start_mask, start_rect)):
                started = True  # Starts the level when player clicks the start button

        # Position the player to the mouse location
        pos = pygame.mouse.get_pos()
        player_rect.center = pos

        # Move bieber across the red carpet
        if bieber_x_value > 900:
            bieber_left = True
        if bieber_x_value < 300:
            bieber_left = False
        if bieber_left:
            bieber_x_value -= 8
        if not bieber_left:
            bieber_x_value += 8
        bieber_rect.center = (bieber_x_value, 600)

        # Move sandler across the red carpet
        if sandler_x_value > 800:
            sandler_left = True
        if sandler_x_value < 400:
            sandler_left = False
        if sandler_left:
            sandler_x_value -= 8
        if not sandler_left:
            sandler_x_value += 8
        sandler_rect.center = (sandler_x_value, 550)

        # Move kanye across the red carpet
        if kanye_x_value > 700:
            kanye_left = True
        if kanye_x_value < 500:
            kanye_left = False
        if kanye_left:
            kanye_x_value -= 8
        if not kanye_left:
            kanye_x_value += 8
        kanye_rect.center = (kanye_x_value, 500)

        if started:
            # See if player is off of the carpet
            if pixel_collision(player_mask, player_rect, red_carpet_mask, red_carpet_rect):
                is_alive = False

            # Checks for player collision with bieber
            if pixel_collision(player_mask, player_rect, bieber_mask, bieber_rect):
                is_alive = False

            # Checks for player collision with sandler
            if pixel_collision(player_mask, player_rect, sandler_mask, sandler_rect):
                is_alive = False

            # Checks for player collision with kanye
            if pixel_collision(player_mask, player_rect, kanye_mask, kanye_rect):
                is_alive = False

            # Checks for player collision with the exit of the level
            if pixel_collision(player_mask, player_rect, level_exit_mask, level_exit_rect):
                return True

        # Draw the background red carpet image
        screen.fill((150, 150, 150))  # This helps check if the image path is transparent
        screen.blit(red_carpet, red_carpet_rect)

        # Draw the player character Travis Kelce
        screen.blit(player, player_rect)

        # Draw the exit sign
        screen.blit(level_exit, level_exit_rect)

        # Draw the start button if it has not been clicked.
        if not started:
            screen.blit(start, start_rect)

        # Draw the boy obstacles
        screen.blit(bieber, bieber_rect)  # Draws bieber

        screen.blit(sandler, sandler_rect)  # Draws sandler

        screen.blit(kanye, kanye_rect)  # Draws Kanye

        # Write text instructions to the screen
        label = message_font.render("Dodge the men to reach the exit.", True, (255, 255, 255))
        screen.blit(label, (20, 10))

        # Every time through the loop, increase the frame count.
        frame_count += 1

        # Bring drawn changes to the front
        pygame.display.update()

        # This tries to force the loop to run at 30 fps
        clock.tick(30)
