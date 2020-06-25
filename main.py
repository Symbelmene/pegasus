import math
import pygame

pygame.init()

win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("First Game")

# Initialisation parameters
t = 0               # Start time
xInit = 50          # X Start point
yInit = 530         # Y Start point

run = True
while run:
    t += 0.1
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if t < 1:
        velx = 0
        vely = -10
    elif t < 5:
        velx = 10
        vely = 0
    elif t < 6:
        vely = 10
        velx = 0

    if y > 530:
        vely = 0
    keys = pygame.key.get_pressed()
    x += velx
    y += vely

    win.fill((0,0,0))
    pygame.draw.rect(win, (100, 100, 100), (x, y, width, height))
    pygame.draw.rect(win, (255,255,255), (295, 295, 10, 10))
    pygame.draw.rect(win, (50,155,50), (0, 560, 600, 20))
    pygame.display.update()

pygame.quit()