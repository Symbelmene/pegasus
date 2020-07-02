import math
import pygame
import physics
from config import cfg

pygame.init()

win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("First Game")

# Initialisation parameters
t = 0                   # Start time
x = cfg.ENV.ORIGINX - cfg.INIT.XPOS   # X Start point
y = cfg.ENV.ORIGINY - (cfg.INIT.YPOS + cfg.DRONE.RADIUS)   # Y Start point
velx = cfg.INIT.VELOCITYX
vely = cfg.INIT.VELOCITYY

run = True
while run:
    t += cfg.SIM.TIMESTEP
    pygame.time.delay(int(cfg.SIM.TIMESTEP * 1000))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if y > cfg.ENV.GROUND:
        vely = 0
    keys = pygame.key.get_pressed()
    
    # Resolve Forces
    vxd, vyd = physics.calculateDrag
    vxg, vyg = physics.calculateGravity
    vxt, vyt = physics.calculateThrust
    
    x += cfg.SIM.TIMESTEP * (vxd + vxg + vxt)
    y += cfg.SIM.TIMESTEP * (vyd + vyg + vyt)

    win.fill((0,0,0))
    
    # Draw ground
    pygame.draw.rect(win, (50,155,50), (
        0, cfg.ENV.GROUND, cfg.SIM.WINDOWX, cfg.SIM.WINDOWY - cfg.ENV.GROUND))
    
    
    pygame.draw.circle(win, (100, 100, 100), (x, y), cfg.DRONE.RADIUS)
    pygame.draw.rect(win, (255,255,255), (295, 295, 10, 10))
    pygame.display.update()

pygame.quit()