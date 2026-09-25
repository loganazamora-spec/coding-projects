import pygame

clock = pygame.time.Clock()

pygame.init()

screen = pygame.display.set_mode((640, 640))

running = True
while running:
    # Make sure the window is able to close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)

pygame.quit()