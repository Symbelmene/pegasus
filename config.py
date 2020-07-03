from easydict import EasyDict as edict


__C                           = edict()
# Get config by: from config import cfg

cfg                           = __C

# Simulator Options
__C.SIM                     = edict()
__C.SIM.WINDOWX             = 600
__C.SIM.WINDOWY             = 600
__C.SIM.TIMESTEP            = 0.025
__C.SIM.SCALE               = 100          # Pixels / m

# Environment Options
__C.ENV                     = edict()
__C.ENV.GRAVITY             = 9.81
__C.ENV.AIRDENSITY          = 1.225
__C.ENV.ORIGINX             = 300
__C.ENV.ORIGINY             = 590
__C.ENV.GROUND              = 590

# Drone Options
__C.DRONE                   = edict()
__C.DRONE.MASS              = 2            # kg
__C.DRONE.THRUST            = 20           # kN
__C.DRONE.RADIUS            = 20           # m

# Initialisation Options
__C.INIT                    = edict()
__C.INIT.XPOS               = 0
__C.INIT.YPOS               = 450
__C.INIT.VELOCITYX          = 20
__C.INIT.VELOCITYY          = -10

# Target Options
__C.TARGET                  = edict()
__C.TARGET.XPOS             = 0
__C.TARGET.YPOS             = 400