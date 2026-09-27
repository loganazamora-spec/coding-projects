import pygame

pygame.init()

clock = pygame.time.Clock()

# Variables
size = width, height = 640, 640
intro_ball_gif = "/mnt/chromeos/MyFiles/Downloads/intro_ball.gif"
black = 0, 0, 0

screen = pygame.display.set_mode((size))
ball = pygame.image.load(intro_ball_gif)
ballrect = ball.get_rect()  
speed = [2,2]

running = True
while running:
    clock.tick(60)

    # Make sure the window is able to close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or  ballrect.right > height:
        speed[1] = -speed[1]
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()

    

pygame.quit()