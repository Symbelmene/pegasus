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

def calculateThrust(px, py, debug=False):
    fx = cfg.DRONE.THRUST * px
    fy = cfg.DRONE.THRUST * py
    if debug:
        print('Thrust Force X = {}'.format(round(fx, 2)))
        print('Thrust Force Y = {}'.format(round(fy, 2)))
    return fx, fy

def resolveThrust(x, y, xTarget, yTarget):
    tx = 2 * (xTarget - x) / cfg.SIM.WINDOWX
    ty = 2 * (yTarget - y) / cfg.SIM.WINDOWY
    ty = 0 if ty > 0 else ty
    return tx, ty