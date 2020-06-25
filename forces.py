from config import cfg

def calculateDrag(vx, vy):
    # Returns air resistance as force (in kN)
    velocity = (vx*vx + vy*vy)**0.5
    density = cfg.ENV.AIRDENSITY
    area = (cfg.DRONE.RADIUS / 4)**2
    cDrag = 0.2
    return 0.5*cDrag*density*(velocity**2)*area
