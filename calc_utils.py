import math

DISTANCE_CONST = 0.00000014264
ARM = 0.31
def calc_distance(prx):
    return DISTANCE_CONST/prx

def dbm_to_potency(dbm):
    return 0.001*math.pow(10, float(float(dbm)/10))

def calc_distance_from_dbm(dbm):
    return calc_distance(dbm_to_potency(dbm))

def get_x(d1, d2):
    return float((d1 - d2)/(4*ARM))

def get_y(d1, d2 ,d3):
    return float((0.5*ARM)*(d3-(0.5*d2)-(0.5*d1)))
    
