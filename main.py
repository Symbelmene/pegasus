import pygame
import physics
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
while run:
    t += cfg.SIM.TIMESTEP
    pygame.time.delay(int(cfg.SIM.TIMESTEP * 1000))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Decide thruster values
    tx, ty = physics.resolveThrust(x, y, xTarget, yTarget)
 
    # Resolve Forces
    fxd, fyd = physics.calculateDrag(vxTot, vyTot) #, debug=True)
    fxg, fyg = physics.calculateGravity() #debug=True)
    fxt, fyt = physics.calculateThrust(tx, ty) #, debug=True)
    vxTot += cfg.SIM.TIMESTEP * (fxd + fxg + fxt) / cfg.DRONE.MASS
    vyTot += cfg.SIM.TIMESTEP * (fyd + fyg + fyt) / cfg.DRONE.MASS
    x += int(round(cfg.SIM.TIMESTEP * vxTot * 10))
    y += int(round(cfg.SIM.TIMESTEP * vyTot * 10))

    # Reality Checks
    # Set wall bounce
    if y > cfg.ENV.GROUND - 20 and vyTot > 0:
        vyTot = -0.9 * vyTot
    if x < 20 and vxTot < 0:
        vxTot = -0.9 * vxTot
    if x > 580 and vxTot > 0:
        vxTot = -0.9 * vxTot
    if vxTot > 200 or vyTot > 200:
        print('Velocity continuum breached! Exiting...')
        run = False
        
    keys = pygame.key.get_pressed()

    win.fill((0,0,0))
    
    # Draw ground
    pygame.draw.rect(win, (50,155,50), (
        0, cfg.ENV.GROUND, cfg.SIM.WINDOWX, cfg.SIM.WINDOWY - cfg.ENV.GROUND))
    print(ty)
    # Draw thrusters
    if ty < 0:
        pygame.draw.polygon(win, (240, 150, 0), ((x-5,y+(cfg.DRONE.RADIUS)), 
                                             (x+5,y+(cfg.DRONE.RADIUS)), (x, y+(cfg.DRONE.RADIUS + (-40*ty)))))
    if tx > 0:
        pygame.draw.polygon(win, (240, 150, 0), ((x-(cfg.DRONE.RADIUS), y-5), 
                                             (x-(cfg.DRONE.RADIUS), y+5), (x-(cfg.DRONE.RADIUS + 20*tx), y)))
    
    if tx < 0:
        pygame.draw.polygon(win, (240, 150, 0), ((x+(cfg.DRONE.RADIUS), y-5), 
                                             (x+(cfg.DRONE.RADIUS), y+5), (x+(cfg.DRONE.RADIUS + -20*tx), y)))
    
    pygame.draw.circle(win, (100, 100, 100), (x, y), cfg.DRONE.RADIUS)
    pygame.draw.rect(win, (255,255,255), (xTarget, yTarget, 10, 10))
    pygame.display.update()

pygame.quit()