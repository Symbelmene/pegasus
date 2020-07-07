from config import cfg

def calculateDrag(vx, vy, debug=False):
    # Returns air resistance as force (in kN)
    density = cfg.ENV.AIRDENSITY
    area = (cfg.DRONE.RADIUS / 4)**2
    cDrag = 0.2
    fx = -0.5*cDrag*density*(vx**2)*area
    fy = -0.5*cDrag*density*(vy**2)*area
    if debug:
        print('Drag Force X = {}'.format(round(fx, 2)))
        print('Drag Force Y = {}'.format(round(fy, 2)))
    return 0, 0

def calculateGravity(debug=False):
    # Returns force due to gravity
    fx = 0
    fy = cfg.DRONE.MASS * cfg.ENV.GRAVITY
    if debug:
        print('Gravity Force X = {}'.format(round(fx, 2)))
        print('Gravity Force Y = {}'.format(round(fy, 2)))
    return fx, fy

def resolveThrust(x, y, xTarget, yTarget, vx, vy, c, k):
    # Distance to target
    dx = xTarget - x
    dy = yTarget - y
    # Current Speed Differential
    dvx = 0 - vx
    dvy = 0 - vy
    tx = dx*k + dvx*c
    ty = max(-50, dy*k + dvy*c)
    # Apply lateral thrust caps
    if tx > 30:
        tx = 30
    elif tx < -30:
        tx = -30
        
    ty = 0 if ty > 0 else ty
    return tx, ty

def proximitySensor(x,y, redZones):
    # redZones = List of polygons
    t = 1