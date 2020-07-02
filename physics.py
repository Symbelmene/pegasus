from config import cfg

def calculateDrag(vx, vy):
    # Returns air resistance as force (in kN)
    density = cfg.ENV.AIRDENSITY
    area = (cfg.DRONE.RADIUS / 4)**2
    cDrag = 0.2
    fx = 0.5*cDrag*density*(vx**2)*area
    fy = 0.5*cDrag*density*(vy**2)*area
    return fx, fy

def calculateGravity(mass):
    # Returns force due to gravity
    fx = 0
    fy = mass * cfg.ENV.GRAVITY
    return fx, fy

def calculateThrust(px, py):
    fx = cfg.DRONE.THRUST * px
    fy = cfg.DRONE.THRUST * py
    return fx, fy