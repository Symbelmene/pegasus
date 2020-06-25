from easydict import EasyDict as edict


__C                           = edict()
# Get config by: from config import cfg

cfg                           = __C

# Simulator Options
__C.SIM.WINDOWX             = 600
__C.SIM.WINDOWY             = 600

# Environment Options
__C.ENV                     = edict()
__C.ENV.GRAVITY             = "./NoteDir"
__C.ENV.AIRDENSITY          = "./Features"
__C.ENV.ORIGINX             = 300
__C.ENV.ORIGINY             = 590

# Drone Options
__C.DRONE                   = edict()
__C.DRONE.MASS              = 2             # kg
__C.DRONE.THRUST            = 20            # kN
__C.DRONE.RADIUS            = 0.1           # m

# Initialisation Options
__C.INIT                    = edict()
__C.INIT.XPOS               = 0
__C.INIT.YPOS               = 0
__C.INIT.VELOCITY           = 0