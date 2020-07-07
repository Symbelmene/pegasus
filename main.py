import math
import pygame
import physics
import random
import pandas as pd
from config import cfg

pygame.init()

win = pygame.display.set_mode((cfg.SIM.WINDOWX, cfg.SIM.WINDOWY))
pygame.display.set_caption("First Game")

# Initialisation parameters
t = 0                   # Start time
x = cfg.ENV.ORIGINX - cfg.INIT.XPOS   # X Start point
y = cfg.ENV.ORIGINY - (cfg.INIT.YPOS + cfg.DRONE.RADIUS)   # Y Start point
vxTot = cfg.INIT.VELOCITYX
vyTot = cfg.INIT.VELOCITYY

# Target parameters
xTarget = cfg.ENV.ORIGINX - cfg.TARGET.XPOS
yTarget = cfg.ENV.ORIGINY - cfg.TARGET.YPOS
run = True

# Feedback sensitivity
k = 1.5
c = 10

dfPath = pd.DataFrame(columns=['Time', 'XPos', 'YPos', 'Vx', 'Vy', 'Fx', 'Fy'])

idx = 0
while run:
    t += cfg.SIM.TIMESTEP
    pygame.time.delay(int(cfg.SIM.TIMESTEP * 1000))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Decide thruster values
    fxt, fyt = physics.resolveThrust(x, y, xTarget, yTarget, vxTot, vyTot, c, k)

    # Resolve Forces
    fxd, fyd = physics.calculateDrag(vxTot, vyTot) #, debug=True)
    fxg, fyg = physics.calculateGravity() #debug=True)
    
    vxTot += cfg.SIM.TIMESTEP * (fxd + fxg + fxt) / cfg.DRONE.MASS
    vyTot += cfg.SIM.TIMESTEP * (fyd + fyg + fyt) / cfg.DRONE.MASS
    x += cfg.SIM.TIMESTEP * vxTot * 10
    y += cfg.SIM.TIMESTEP * vyTot * 10
    
    xDisp = int(x)
    yDisp = int(y)

    # Reality Checks
    # Set wall bounce
    if y > cfg.ENV.GROUND - 20 and vyTot > 0:
        vyTot = -0.9 * vyTot
    if x < 20 and vxTot < 0:
        vxTot = -0.9 * vxTot
    if x > cfg.SIM.WINDOWX - 20 and vxTot > 0:
        vxTot = -0.9 * vxTot
    if vxTot > 200 or vyTot > 200:
        print('Velocity continuum breached! Exiting...')
        run = False
    
    dfPath.loc[idx] = [t, x, y, vxTot, vyTot, fxt, fyt]
    keys = pygame.key.get_pressed()
    win.fill((0,0,0))
    
    # Draw ground
    pygame.draw.rect(win, (50,155,50), (
        0, cfg.ENV.GROUND, cfg.SIM.WINDOWX, cfg.SIM.WINDOWY - cfg.ENV.GROUND))
    
    # Draw thrusters
    if fyt < 0:
        pygame.draw.polygon(win, (240, 150, 0), 
                            ((xDisp-5,yDisp+(cfg.DRONE.RADIUS)), 
                             (xDisp+5,yDisp+(cfg.DRONE.RADIUS)), 
                             (xDisp, yDisp+(cfg.DRONE.RADIUS + (-2*fyt)))))
    if fxt > 0:
        pygame.draw.polygon(win, (240, 150, 0), 
                            ((xDisp-(cfg.DRONE.RADIUS), yDisp-5), 
                             (xDisp-(cfg.DRONE.RADIUS), yDisp+5), 
                             (xDisp-(cfg.DRONE.RADIUS + 1*fxt), yDisp)))
    if fxt < 0:
        pygame.draw.polygon(win, (240, 150, 0), 
                            ((xDisp+(cfg.DRONE.RADIUS), yDisp-5), 
                             (xDisp+(cfg.DRONE.RADIUS), yDisp+5), 
                             (xDisp+(cfg.DRONE.RADIUS + -1*fxt), yDisp)))
    
    pygame.draw.circle(win, (100, 100, 100), (xDisp, yDisp), cfg.DRONE.RADIUS)
    pygame.draw.circle(win, (255,50,50), (xTarget, yTarget), 5)
    #for ix, row in dfPath.iterrows():
    #    pygame.draw.rect(win, (255,255,255), (row[1], row[2], 2, 2))
    pygame.display.update()
    
    # Check goals
    posFlag = (abs(x - xTarget) < 20) and (abs(y - yTarget) < 20)
    velFlag = (vxTot < 1) and (vyTot < 1)
    if posFlag and velFlag:
        xTarget = random.randint(50, cfg.SIM.WINDOWX - 50)
        yTarget = random.randint(50, cfg.SIM.WINDOWY - 50)
    
    idx += 1

pygame.quit()