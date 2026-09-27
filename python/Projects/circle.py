import pygame

pygame.init()

clock = pygame.time.Clock
size = (460, 460)
screen = pygame.display.set_mode(size)


white = 255, 255, 255
black = 0, 0 ,0

running = True 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.circle(screen, color=white, center=[0,0], radius=250, width=0)


