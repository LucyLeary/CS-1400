import pygame


def display_loss_screen():
    pygame.init()

    sad_taylor = pygame.image.load("sad_taylor.png")  # photo credit: https://www.rollingstone.com
    # Store window width and height in a tuple.
    sad_taylor_size = sad_taylor.get_size()
    sad_taylor_rect = sad_taylor.get_rect()

    # create the window based on the happy_taylor size
    screen = pygame.display.set_mode(sad_taylor_size)
    losing = True
    while losing:
        screen.blit(sad_taylor, sad_taylor_rect)
        message_font = pygame.font.SysFont('monospace', 200)
        label = message_font.render("NO!", True, (255, 255, 255))
        screen.blit(label, (50, 50))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                losing = False


def display_win_screen():
    pygame.init()

    happy_taylor = pygame.image.load("happy_taylor.png")  # photo credit: https://www.rollingstone.com
    # Store window width and height in a tuple.
    happy_taylor_size = happy_taylor.get_size()
    happy_taylor_rect = happy_taylor.get_rect()

    # create the window based on the happy_taylor size
    screen = pygame.display.set_mode(happy_taylor_size)
    winning = True
    while winning:
        screen.blit(happy_taylor, happy_taylor_rect)
        message_font = pygame.font.SysFont('monospace', 200)
        label = message_font.render("YES!", True, (255, 255, 255))
        screen.blit(label, (50, 50))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                winning = False
